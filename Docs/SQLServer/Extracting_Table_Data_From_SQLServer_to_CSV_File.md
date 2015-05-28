# SQL Server: Table data extract to CSV file.
In this exersize we are going to define data extraction pipeline for SQLServer.

##Open Databuddy
First [start](https://github.com/data-buddy/DataBuddy/blob/master/Docs/How_to_start_Databuddy.md) Databuddy. 
It opens to a state where no sessions are selected and all tabs are disabled:

![Output view with no sessions defined](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/open_databuddy_no_sessions.png "Output view with no sessions defined")

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







