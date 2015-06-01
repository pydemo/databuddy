# Migrating Oracle 12c table data to MongoDB collection.
In this example we are going to migrate Oracle table data to MongoDB collection.
Migration steps:
- Extract Oracle table data to CSV file using SQL*Plus.
- Load CSV file into MongoDB collection using mongoimport.

##Open Databuddy
First [start](https://github.com/data-buddy/DataBuddy/blob/master/Docs/How_to_start_Databuddy.md) Databuddy. 
It opens to a state where no sessions are selected and all tabs are disabled:

![Starter view with no sessions defined](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/open_databuddy_no_sessions.png "Starter view with no sessions defined")

## Define "Copy Vector"
Click "New" button located in top right corner. It will open to "New session" dialog. 
Define data extraction `Copy Vector` by zooming through popup menu items:
```python
  Copy Vector
  --------------
  |     ->     |
  --------------
  From Oracle-
                |
                From Oracle 12c-
                                      |
                                      To MongoDB
```  

![Define copy vector for Oracle12c-to-MongoDb extract pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Define_copy_vector_for_Oracle12c-to-MongoDB_copy_pipeline.png "Define copy vector for Oracle12c-to-MongoDB copy pipeline.")

## Select Source and Target templates
Next and last step is template selection. Pick one from the source list on the left (`ORA12C_TimestampTable_withComaHeader`) and one from the target list on the right (`MONGO_Table`):
![Source and target template selection](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Copy_from_Oracle12c_to_MongoDB_Templates.png "Source and target template selection.")

## Define arguments.
After you click `Create` button new session is created and right panel is populated with default values.
Please, ignore __Common__ argument section for now. Go through __Source__ and __Target__ arguments and set each argument to appropriate value. 

![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Oracle12c_to_MongoDB_Define_Arguments.png "Define arguments.")

## Run Session.
After you click __Run__ button black CLI window will pop-up executing QueryCopy (`qc32\qc.exe`).

![Session executed](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Oracle12c_to_MongoDB_Copy_CLI_Window.png "Session executed.")

Command executed:
```powershell
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-t , ^
-r 1 ^
-o 1 ^
-w ora12c-mongo ^
-K 1 ^
-F C:\tmp\TEST_default_spool ^
-Y 20150601_113008_383000 ^
-5 C:\Users\alex_buz\sessions\My_Sessions\ORA12C_TimestampTable_withComaHeader_to_MONGO_Table\host_map_v2.py ^
-B qc_job ^
-M C:\Temp\qc_log ^
-b orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-j SCOTT ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-A 1 ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-c SCOTT.Timestamp_test_from ^
-d test ^
-T 27017 ^
-Z ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED ^
-a test ^
-u test_user ^
-s localhost 
```

##Checking the results
Check job results at the bottom of the black CLI window:
```
Copy stats (1 threads, 1 shards):
2015-06-01 11:30:09,020 - ora12c-mongo - INFO - Shard-0/0:          44 rows
2015-06-01 11:30:09,020 - ora12c-mongo - INFO - TOTAL Bytes:        5360 Bytes
2015-06-01 11:30:09,020 - ora12c-mongo - INFO - TOTAL Rows:           44 Rows
############################################################
2015-06-01 11:30:09,022 - ora12c-mongo - INFO - Done.
2015-06-01 11:30:09,022 - ora12c-mongo - INFO - Elapsed: 00:00:00
Press any key to continue . . .
```
Status __"Done"__ means export job executed successfully. 
- [x] Temporary Oracle CSV spool data file is at `C:\tmp\TEST_default_spool\qc_job\20150601_113008_383000\SCOTT.Timestamp_test_from.shard_0.data` as defined by __Common__ section `default_spool_dir` argument.










