# DataBuddy
##Version

DataBuddy 0.23.9 beta

##Purpose

Ad-hoc data migration between databases and file formats (CSV)

##Audience

Database developers, Data Integrators.

##Designated Environment
Pre-Prod (UAT/QA/DEV)

##Databases supported

Database | GUI | Command line
---------|---- | -------------
DB2      |  | yes
Informix |  | yes
MariaDB    |  | yes
MySQL    |  | yes
**Oracle**   | yes | yes
PostgreSQL|  | yes
SQLite|  | yes
SQLServer|   | yes
Sybase   |  | yes
TimesTen|  | yes


##File formats

Format | GUI | Command line
---------|---- | -------------
CSV   | yes | yes


##Components
- Front end GUI (wxPython).
- Command line script (Python).
  
##Features:

###Front end.

- Session management.

###Command line:
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

- Wriiten using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller
 
##Execution

python data-buddy.py

#Templates v.s. free argument entry
##Pros
-it's tested
##Cons
-user has to create new session if new argument has to be added/removed

#SQL*Loader config
-Change SQL*Loader arguments and control file in ```qc32\config\include\oracle.py```

#TODO
- argument values reuse from existing session DONE
- clean uargs.db
- nls_format* duplication DONE
- test UI
- add --log_dir to backend
- add "source" and "target" datasources to "New Session"
- Copy/Paste of argument values between sessions
- generic "New Session" so user not limited by source and target templates
- history of values for each argument
- cleanup all other databases but Oracle
- more templates and better templates hierarchy
- init templates to open session for "New Session" DONE
- validate args on Run
- smaller test_api files (get default args from test routines, not canned files)
- fix template filters
- create "Menu" button and hide "About"

#Does it work?
yes, with some quirks and only for Oracle. 

