# DataBuddy
##Version

GUI (data-buddy) | Command line (QueryCopy)
---- | -------------
0.2.9 beta | 1.23.9 beta

##Purpose

Ad-hoc data migration between databases and file formats (CSV)

##Audience

Database developers, Data Integrators.

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

Format | GUI | Command line
---------|---- | -------------
CSV   | yes | yes


##Copy vectors

From | To/From | To
---------|---- | -------------
DB2      
Informix 
MariaDB    |  | yes



##Components
- Fron end - data-buddy GUI (wxPython, PyInstaller).
- Back end -[QueryCopy](https://github.com/QueryCopy/QueryCopy-for-Oracle) (Python, PyInstaller).
  
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

- Wriiten using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller
 
##Execution

* python data-buddy.py
* data-buddy.exe

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
- **validate args on Run**
- smaller test_api files (get default args from test routines, not canned files)
- fix template filters
- create "Menu" button and hide "About"
- create session library on first run
- validate session name for chars not usable in file name
- allow user to create multiple session libraries
- fix mailformed path from MDD.MultiDirDialog DONE
- make sure all paths are windows friendly
- open dir and open file use stale values
- filter control keys from ones affecting field value
- close all existing shells/shell groups upon exit
- highlight running sessions
- beep on failing sessions
- detect DONE/FAILED from cmd window

#Does it work?
yes, with some quirks and only for Oracle. 

##References
* [QueryCopy](https://github.com/QueryCopy/QueryCopy-for-Oracle) -- `qc32\qc32.exe`
