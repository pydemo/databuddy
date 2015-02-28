# DataBuddy
##version

DataBuddy 1.23.9

##Purpose

Ad-hoc data migration between databases and file formats (CSV)

##Components

  1. Gront end UI.
  2. Command line executable.
  
##Features:

###Front end.

  1.session management.

###Command line:

  1.Multi-query load.
  2.Partition/sub-partition copy
  3.Sharded copy (turbo mode)
  4.Custom spool location (config/user_conf.py)
  5.config/include/oracle.py - configurable SQL*Loader args.
  6.3 generic arguments (use them to pass job_id or timestamp and process in config/user_config.py)
  7.added all usecases
  8.lame_duck/limit fix for trial runs
  9.keep_data_file param (set it to 1 if you want to keep data dump)
  10.White-space control.
  11.Header line control.
  12.Truncate target table/partition/subpartition
  13.Ask to truncate.
  14. No client (url) connect.
  15.Supports CSV file load from multiple dirs.

##Implementation

  Wriiten using Python and wxPython.
  Compiled with PyInstaller
