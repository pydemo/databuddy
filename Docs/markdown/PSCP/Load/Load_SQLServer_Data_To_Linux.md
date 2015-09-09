# Extract scalar data from SQL Server to Linux.
In this example we are going to extract data from SQL Server table to CSV file and then copy it to Linux (in single session).
Migration steps:
- Extract scalar data from SQLServer table to CSV file.
- Copy CSV file to Linux usinf pscp.exe
##Open Databuddy
[Download](https://github.com/data-buddy/DataBuddy/releases/tag/0.3.5), [configure](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/Configure_Databuddy0.3.3.md#configuration-for-mongdb), and [start](https://github.com/data-buddy/DataBuddy/blob/master/Docs/markdown/How_to_start_Databuddy.md) Databuddy. 
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
  From SQL Server Express-
						|
						To PSCP
```  

![Define copy vector for SQL Server-to-Linux copy pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/PSCP/Copy_data_from_SQLServer_to_Linux.png "Define copy vector for SQL Server-to-Linux copy pipeline.")

## Select Source and Target templates
Next and last step is template selection. Pick one from the source list on the left (`ORA11G_TimestampTable`) and one from the target list on the right (`ORA11G_Table`):

![Source and target template selection](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/PSCP/Copy_data_from_SQLServer_to_Linux_Templates.png "Source and target template selection.")

## Define arguments.
After you click `Create` button new session is created and right panel is populated with default values.
Please, ignore __Common__ argument section for now. Go through __Source__ and __Target__ arguments and set each argument to appropriate value. 

![Define arguments](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/PSCP/Copy_data_from_SQLServer_to_Linux_Arguments.png  "Define arguments.")

## Run Session.
After you click __Run__ button black CLI window will pop-up executing QueryCopy (`qc32\qc.exe`).

![Session executed](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/PSCP/Copy_data_from_SQLServer_to_Linux_CLI_Window.png "Session executed.")


##Checking the results
Check job results at the bottom of the black CLI window:
```
############################################################
2015-06-01 11:30:09,022 - SSEXP-PSCP - INFO - Done.
2015-06-01 11:30:09,022 - SSEXP-PSCP - INFO - Elapsed: 00:00:03
Press any key to continue . . .
```
	