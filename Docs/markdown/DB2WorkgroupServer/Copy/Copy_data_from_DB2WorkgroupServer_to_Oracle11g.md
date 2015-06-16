
# Migrating DB2WorkgroupServer table data to Oracle11g.
In this example we are going to migrate DB2WorkgroupServer table data to Oracle11g.
Migration steps:
- Extract DB2WorkgroupServer table data to CSV.
- Load CSV file into Oracle11g.

##Open Databuddy
[Download](https://github.com/data-buddy/DataBuddy/releases/tag/v0.3.3), [configure](https://github.com/data-buddy/DataBuddy/blob/master/Docs/Configure_Databuddy0.3.3.md#configuration-for-mongdb), and [start](https://github.com/data-buddy/DataBuddy/blob/master/Docs/How_to_start_Databuddy.md) Databuddy. 
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
  From DB2WorkgroupServer-
				|
				From DB2WorkgroupServer-
									  |
									  To Oracle11g
```  
(sample image)
![Define copy vector for DB2WorkgroupServer-to-Oracle11g extract pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Define_copy_vector_for_Oracle12c-to-MongoDB_copy_pipeline.png "Define copy vector for DB2WorkgroupServer-to-Oracle11g copy pipeline.")

## Select Source and Target templates
Next and last step is template selection. Pick one from the source list on the left (`DBTWS_TimestampTable`) and one from the target list on the right (`ORA11G_Table`):
(sample image)
![Source and target template selection](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Copy_from_Oracle12c_to_MongoDB_Templates.png "Source and target template selection.")

## Define arguments.
After you click `Create` button new session is created and right panel is populated with default values.
Please, ignore __Common__ argument section for now. Go through __Source__ and __Target__ arguments and set each argument to appropriate value. 
(sample image)
![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Oracle12c_to_MongoDB_Define_Arguments.png "Define arguments.")

## Run Session.
After you click __Run__ button black CLI window will pop-up executing QueryCopy (`qc32\qc.exe`).
(sample image)
![Session executed](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Oracle12c_to_MongoDB_Copy_CLI_Window.png "Session executed.")


##Checking the results
Check job results at the bottom of the black CLI window:
```
############################################################
2015-06-01 11:30:09,022 - DBTWS-ORA11G - INFO - Done.
2015-06-01 11:30:09,022 - DBTWS-ORA11G - INFO - Elapsed: 00:00:00
Press any key to continue . . .
```
Status __"Done"__ means export job executed successfully. 
- [x] Temporary DB2WorkgroupServer CSV spool data file will be at `C:	mp\TEST_default_spool\qc_job\[timestamp]\[table_name].data` as defined by __Common__ section `default_spool_dir` argument.

	