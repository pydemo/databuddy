# SQL Server: Table data extract to CSV file.
In this exersize we are going to define data extraction pipeline for SQLServer.

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
  From SQLServer-
                |
                From SQLServer Express-
                                      |
                                      To CSV
```  

![Define copy vetor for SQLServer-to-CSV extract pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Define_copy_vector_for_SQLServer-to-CSV_extract_pipeline.png "Define copy vector for SQLServer-to-CSV extract pipeline.")

## Select Source and Target templates
Next and last step is template selection. Why templates - I delve on this later. Right now pick one from the source list on the left (`SSEXP_Table`) and one from the target list on the right (`CSV_File`):
![Source and target template selection](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Export_from_SQLServer_CSV_file_Templates.png "Source and target template selection.")

## Define arguments.
After you click `Create` button new session is created and right panel is populated with default values.
Go through __Source__ and __Target__ arguments and set each agrument. 
- Export file location:
```python
  Target
  to_file: C:\Python27\data_migrator_1239_12c\CSV_OUT\testSSEXP_Table.data
```  
![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/SQLServer_to_CSV_arguments.png "Define arguments.")

## Run Session.
After you click __Run__ button black CLI window will popup executing QueryCopy (`qc32\qc.exe`).


![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/Session_Executed_for_SQLServer_to_CSV_file_extract.png "Define arguments.")

Command executed:
```powershell
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-t | ^
-r 1 ^
-o 1 ^
-w ssexp-csv ^
-K 1 ^
-F C:\tmp\TEST_default_spool ^
-Y 20150515_220006_944000 ^
-5 C:\Users\alex_buz\sessions\My_Sessions\SSEXP_Table_to_CSV_File\host_map_v2.py ^
-B qc_job ^
-M C:\Temp\qc_log ^
-b master ^
-c Timestamp_test_from ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-j sa ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-g C:\Python27\data_migrator_1239_12c\CSV_OUT\testSSEXP_Table.data 
```








