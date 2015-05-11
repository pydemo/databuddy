# DataBuddy
##Version

data-buddy (GUI) | QueryCopy (command line)
---- | -------------
0.3.3 beta | 1.23.9 beta

##Purpose

Ad-hoc data migration between databases and file formats (CSV)

##Audience

Database developers, ETL developers, Data Integrators.

##Designated Environment
Pre-Prod (UAT/QA/DEV)

##Databases supported

Database | GUI (data-buddy) | Command line (QueryCopy)
---------|---- | -------------
DB2      |  | yes
Informix |  | yes
MariaDB    |  | yes
MySQL    |  | yes
**Oracle**   |[yes](https://github.com/data-buddy/DataBuddy/releases/tag/v0.2.9)   | [yes](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9)
PostgreSQL|  | yes
SQLite|  | yes
SQLServer|   | yes
Sybase   |  | yes
TimesTen|  | yes


##File formats

Database | DDL extract | CSV extract | CSV load
---------|---- | ------------- | -------
DB2      |  | yes  | yes
Informix |  | yes  | yes
MariaDB    |  | yes  | yes
MySQL    |  | yes  | yes
**Oracle**   | Table | yes  | yes
PostgreSQL|  | yes  | yes
SQLite|  | yes  | yes
SQLServer|   | yes  | yes
Sybase   |  | yes  | yes
TimesTen|  | yes  | yes




##Contents
- Front end - data-buddy GUI (wxPython, PyInstaller).
- Back end -[QueryCopy](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9) (Python, PyInstaller).
  
##Features:

###Front end (data-buddy).

- Session management.

###Command line (QueryCopy):
- Multi-query load.
- Partition/sub-partition copy
- Sharded copy (turbo mode)
- Custom spool location (config/user_conf.py)
- config/include/oracle.py - configurable SQL*Loader args.
- 3 generic arguments (use them to pass job_id or timestamp and process in config/user_config.py)
- added all usecases
- lame_duck/limit fix for trial runs
- keep_data_file param (set it to 1 if you want to keep data dump)
- White-space control.
- Header line control.
- Truncate target table/partition/subpartition
- Ask to truncate.
- No client (url) connect.
- Supports CSV file load from multiple dirs.
- --exit_on_key - let's you keep exec window open after load job is done

##Implementation

- Written using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller
 
##Execution

* python data-buddy.py
* data-buddy.exe

#Templates v.s. free argument entry
##Pros
- all templates are tested with presets

##Cons
- user has to create new session if new argument has to be added/removed

#SQL*Loader config
- Change SQL*Loader arguments and control file in ```qc32\config\include\oracle.py```

#Exec host config
- Change host where physical copy is done in host_map.py ```qc32\include\v101\host_map.py```

#TODO
- argument values reuse from existing session. **DONE**
- clean uargs.db. **DONE**
- nls_format* duplication. **DONE**
- test UI.
- add --log_dir to backend. **DONE**
- add "source" and "target" datasources to "New Session". **DONE**
- Copy/Paste of argument values between sessions.
- generic "New Session" so user not limited by source and target templates. **DONE**
- history of values for each argument.
- cleanup all other databases but Oracle.
- more templates and better templates hierarchy.
- init templates to open session for "New Session". **DONE**
- validate args on Run. **DONE**.
- smaller test_api files (get default args from test routines, not canned files).
- fix template filters. **DONE**
- create "Menu" button and hide "About".
- create templates tab **DONE**
- create sessions tab **DONE**
- validate session name for chars not usable in file name. **DONE**
- allow user to create multiple session libraries. **DONE**
- fix mailformed path from MDD.MultiDirDialog. **DONE**
- make sure all paths are windows friendly.**DONE**
- open dir and open file use stale values.**DONE**
- filter control keys from ones affecting field value. **DONE**
- close all existing shells/shell groups upon exit.
- highlight running sessions.**DONE**
- beep on failing sessions.
- detect DONE/FAILED from cmd window. **DONE**
- let user disable post-etl email (Common: email_to). **DONE**
- change copy_vector format from db2db to db->db or db_2_db
- fix flicker on frame freeze **DONE**
- save on close **DONE**
- Table DDL export for Oracle **DONE**
- validate all path arguments before run
- add create template menu **DONE**
- add "--host_map" arg to set hosts for each thread **DONE**
- let user change host mapping **DONE**
- save as template **DONE**
- save as **DONE**
- test ezconnect
- add "Output" tab
- add '--compress_spool' arg for zipped output
- add sqlloader.py
- fix session sort
- fix favorites
- fix session refresh
- add scp/ftp/sftp as data source/target
- make all paths relative to transport_home
- create wizard for "New Session" template selection
- distinguish A-Templates from B-Templates
- let data copy to be executed on Linux (bash via ssh)**DONE**
- let data spool/load to be executed on Linux (bash via ssh)
- add SQLServer
- add MySQL
- add PostgreSQL
- add SQLite
- add Informix
- add Sybase
- add DB2
- add dBase
- add Access DB
- add MariaDB
- add Infobright
- add TimesTen
- add MongoDB
- add Hadoop
- add Hive
- add Terradata
- add Redshift
- add Apache Hive
- add Vertica
- add Netezza
- add Parstream
- add ParAccel
- add Twitter (extract)
- add GA
- add Facebook (extract)
- add Taleo HR (extract) 
- add Salesforce
- add Greenplum
- add Actian
- add McObject
- add NuiDB
- add Clustrix
- add Orient
- add Scribe
- add KDB+
- add Volt DB
- add Arango DB
- add Foundation DB
- add Enterprise DB
- add Altibase HDB
- add Couchbase
- add Aerospike
- add InterSystems
- add QV (QlikView file format)
- add MDX (file format)




#Does it work?
- yes, with some quirks and only for Oracle. 

##References
* [QueryCopy for Oracle](https://github.com/QueryCopy/QueryCopy-for-Oracle) -- `qc32\qc32.exe`
