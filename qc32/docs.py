#md docs
def get_page(db_from, db_to, k, k1):
	tmpl="""
# Migrating %s table data to %s.
In this example we are going to migrate %s table data to %s.
Migration steps:
- Extract %s table data to CSV.
- Load CSV file into %s.

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
  From %s-
				|
				From %s-
									  |
									  To %s
```  
(sample image)
![Define copy vector for %s-to-%s extract pipeline](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/MongoDB/Define_copy_vector_for_Oracle12c-to-MongoDB_copy_pipeline.png "Define copy vector for %s-to-%s copy pipeline.")

## Select Source and Target templates
Next and last step is template selection. Pick one from the source list on the left (`%s_TimestampTable`) and one from the target list on the right (`%s_Table`):
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
2015-06-01 11:30:09,022 - %s-%s - INFO - Done.
2015-06-01 11:30:09,022 - %s-%s - INFO - Elapsed: 00:00:00
Press any key to continue . . .
```
Status __"Done"__ means export job executed successfully. 
- [x] Temporary %s CSV spool data file will be at `C:\tmp\TEST_default_spool\qc_job\[timestamp]\[table_name].data` as defined by __Common__ section `default_spool_dir` argument.

	""" % (from_db, to_db,  from_db, to_db, from_db,to_db, from_db,from_db, to_db,from_db, to_db, from_db, to_db, k, k1,k, k1,k, k1, from_db)
	return tmpl	

import os
dbs={	'SYASE':'SAP Sybase ASE', 'SYANY':'Sybase SQL Anywhere','SYIQ':'Sybase IQ',
		'ORA12C':'Oracle 12c','ORA11G':'Oracle 11g', 'ORAXE':'Oracle XE', 'ORAEXA':'Exadata',
		'TTEN':'TimesTen', 
		'SLITE':'SQL Lite',
		'SSEXP':'SQL Server Express','SSENT':'SQL Server Enterprise',
		'MYSQL':'MySQL', 'MARIA':'MariaDB', 'INFOB':'Infobright',
		'CSV':'CSV',
		'DDL':'DDL',
		'PGRES':'PostgreSQL',		
		'DBTAES':'DB2 Advanced Enterprise Server','DBTES':'DB2 Enterprise Server',
		'DBTAWS':'DB2 Advanced Workgroup Server',
		'DBTWS':'DB2 Workgroup Server',
		'DBTE':'DB2 Express', 'DBTEC':'DB2 Express C', 'DBTDE':'DB2 Developer Edition',
		'INFOR':'Informix IDS', 'INFORC':'Informix Innovator C',
		'MONGO':'MongoDB',		
		}
save_to=r'C:\tmp\md_docs'
for  k,v in dbs.items():
	for  k1,v1 in dbs.items():
		if  k.startswith('CSV') or k1.startswith('CSV') or k.startswith('DDL') or k1.startswith('DDL'):
			pass
		else:
			from_db, to_db=dbs[k].replace(' ',''),dbs[k1].replace(' ','')
			fname= 'Copy_data_from_%s_to_%s.md' % (from_db, to_db)
			dirname= os.path.join(save_to,from_db,'Copy')
			if not os.path.isdir(dirname):
				os.makedirs(dirname)
			
			md_name= os.path.join(dirname,fname)
			print md_name
			
			f= open(md_name,'w')
			f.write(get_page(from_db, to_db, k,k1))
			f.close()

		
		
		
		
		