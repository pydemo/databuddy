# DataBuddy
Do it yourself data integration starter kit.

##Version

data-buddy (GUI) | QueryCopy (command line)
---- | -------------
0.3.3 beta | 1.23.9 beta
>There are 2 components. Upon "Run" data-buddy (UI) will kick off QueryCopy (`qc32\qc.exe`) out of process.

##Purpose

- It is data integration software used to define technical processes to combine data from different sources. Data is moved across RDBMS borders using CSV files.
- __DataBuddy__ facilitates data delivery from multiple relational data sources including Oracle, SQLServer, DB2, SAP Sybase, Informix, MySQL, Infobright, MariaDB, PostgreSQL, TimesTen, and SQLite.
- It requires minimal initial configuration and lets you manage data integration process using GUI or command line.
- Your data integration processes are stored as session files and can be scripted into your ETL pipelines or used in ad-hoc manner.
- Lets you develop Extract-Copy-Load processes to scrub and ingest large, distinct data sets from multiple sources into a unified data warehouse.
- Provides structured and ad-hoc access to large datasets.

##Audience

Database developers, ETL developers, Data Integrators.

##Designated Environment
Pre-Prod (UAT/QA/DEV)


##Databases supported

Database | GUI (data-buddy) | Command line (QueryCopy)
---------|---- | -------------
DB2      | yes | yes
Informix | yes  | yes
MariaDB    | yes | yes
MySQL    | yes | yes
Infobright    | yes | yes
**Oracle**   | yes | [yes](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9)
PostgreSQL| yes | yes
SQLite| yes | yes
SQLServer| yes | yes
Sybase   | yes  | yes
TimesTen| yes  | yes


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
> DDL extract works only for Oracle tables.

##Components
- GUI - data-buddy (wxPython, PyInstaller).
- Command line -[QueryCopy](https://github.com/QueryCopy/QueryCopy-for-Oracle/releases/tag/v1.23.9) (Python, PyInstaller).

##Features:

###Front end, GUI (data-buddy).

- Session management.

###Command line (QueryCopy):
- [x] Multi-query load.
- [x] Partition/sub-partition copy
- [x] Sharded copy (turbo mode)
- [x] Custom spool location (config/user_conf.py)
- [x] config/include/oracle.py - configurable SQL*Loader args.
- [x] 3 generic arguments (use them to pass job_id or timestamp and process in config/user_config.py)
- [x] added all usecases
- [x] lame_duck/limit fix for trial runs
- [x] keep_data_file param (set it to 1 if you want to keep data dump)
- [x] White-space control.
- [x] Header line control.
- [x] Truncate target table/partition/subpartition
- [x] Ask to truncate.
- [x] No client (url) connect.
- [x] Supports CSV file load from multiple dirs.
- [x] --exit_on_key - let's you keep exec window open after load job is done

##How it works.

1. "DbShell" - queries target and source for table metadata.
2. "Spooler"  - extracts data to temp file from source.
3. "Loader" - loads temp file to target using bulk loader.

###Tools used to extract, load, and query data
DB family|Database | Spooler | Loader | DbShell
---------|----------|-------- | -------| -------
DB2 | DB2 Advanced Enterprise Server | db2.exe | db2.exe | db2.exe
 | DB2 Advanced Workgroup Server | db2.exe | db2.exe | db2.exe
 | DB2 Developer Edition | db2.exe | db2.exe | db2.exe
 | DB2 Express | db2.exe | db2.exe | db2.exe
 | DB2 Express C | db2.exe | db2.exe | db2.exe
 | DB2 Enterprise Server | db2.exe | db2.exe | db2.exe
 | DB2 Workgroup Server | db2.exe | db2.exe | db2.exe
MySQL | MySQL | mysql.exe | mysql.exe | mysql.exe 
 | Infobright | mysql.exe | mysql.exe | mysql.exe
 | MariaDB | mysql.exe | mysql.exe | mysql.exe 
Informix | Informix IDS | dbaccess.exe | dbaccess.exe | dbaccess.exe
 | Informix Innovator C | dbaccess.exe | dbaccess.exe | dbaccess.exe
Oracle | Oracle 12c | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Oracle 11g | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Exadata | sqlplus.exe | sqlldr.exe | sqlplus.exe
 | Oracle XE | sqlplus.exe | sqlldr.exe | sqlplus.exe
PostgreSQL | PostgreSQL | psql.exe | psql.exe | psql.exe
SQL Server | SQL Server Enterprise | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
 | SQL Server Express | sqlcmd.exe | sqlcmd.exe | sqlcmd.exe
SAP Sybase | Sybase SQL Anywhere | dbisql.com | dbisql.com | dbisql.com
 | SAP Sybase ASE | dbisql.com | dbisql.com | dbisql.com
 | Sybase IQ | dbisql.com | dbisql.com | dbisql.com
TimesTen | TimesTen | ttBulkCp.exe | ttBulkCp.exe | ttIsql.exe
SQLite | SQLite | sqlite3.exe | sqlite3.exe | sqlite3.exe



## What it doesn't do
- It does not create target table.
- It does not pipe data (it extracts into a file then loads).
- It should not be used in Prod. Trial/ad-hoc use only.


##Implementation

- Written using Python (command line) and wxPython (GUI).
- Compiled with PyInstaller

##Configuration
- modify default host_map.py: ![host_map.py](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/edit_hostmap.png "Edit host_map.py")
- set your 'source' and 'target' dirs for local clients for each database.
```python
 'host_list': {0: {'db_env': {'ORA11G': {'source': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN',
                                         'target': 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN'},
```
- you are good to go

##Execution
* data-buddy.exe

>from Windows command line or File Explorer

#Target object Truncate
- it will popup with warning window every time you try to run QueryCopy truncating you target object.
![truncate](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/truncate_target.png "Truncate target")

#Templates v.s. free argument entry
##Pros
- all templates are tested with presets

##Cons
- user has to create new session if new argument has to be added/removed

>There's no way to add/remove args to your choosing. Argument combos come as templates which you select in "Create new session window"

#TODO
- [x] argument values reuse from existing session. **DONE**
- [x] clean uargs.db. **DONE**
- [x] nls_format* duplication. **DONE**
- [x] test UI.
- [x] add --log_dir to backend. **DONE**
- [x] add "source" and "target" datasources to "New Session". **DONE**
- [x] Copy/Paste of argument values between sessions.
- [x] generic "New Session" so user not limited by source and target templates. **DONE**
- [x] history of values for each argument.
- [x] cleanup all other databases but Oracle.
- [x] more templates and better templates hierarchy.
- [x] init templates to open session for "New Session". **DONE**
- [x] validate args on Run. **DONE**.
- [x] smaller test_api files (get default args from test routines, not canned files).
- [x] fix template filters. **DONE**
- [x] create "Menu" button and hide "About".
- [x] create templates tab **DONE**
- [x] create sessions tab **DONE**
- [x] validate session name for chars not usable in file name. **DONE**
- [x] allow user to create multiple session libraries. **DONE**
- [x] fix mailformed path from MDD.MultiDirDialog. **DONE**
- [x] make sure all paths are windows friendly.**DONE**
- [x] open dir and open file use stale values.**DONE**
- [x] filter control keys from ones affecting field value. **DONE**
- [x] close all existing shells/shell groups upon exit.
- [x] highlight running sessions.**DONE**
- [x] beep on failing sessions.
- [x] detect DONE/FAILED from cmd window. **DONE**
- [x] let user disable post-etl email (Common: email_to). **DONE**
- [x] change copy_vector format from db2db to db->db or db_2_db
- [x] fix flicker on frame freeze **DONE**
- [x] save on close **DONE**
- [x] Table DDL export for Oracle **DONE**
- [x] validate all path arguments before run
- [x] add create template menu **DONE**
- [x] add "--host_map" arg to set hosts for each thread **DONE**
- [x] let user change host mapping **DONE**
- [x] save as template **DONE**
- [x] save as **DONE**
- [x] test ezconnect
- [x] add "Output" tab **DONE**
- [x] add '--compress_spool' arg for zipped output
- [x] add sqlloader.py
- [x] fix session sort **DONE**
- [x] fix session refresh **DONE**
- [x] let user set primary dbs, source/target dbs
- [x] add scp/ftp/sftp as data source/target
- [x] make all paths relative to transport_home 
- [x] create wizard for "New Session" template selection
- [x] distinguish A-Templates from B-Templates
- [x] let data copy to be executed on Linux (bash via ssh)**DONE**
- [x] let data spool/load to be executed on Linux (bash via ssh)
- [x] add [Oracle 12c Release 1](http://docs.oracle.com/database/121/index.htm) **DONE**
- [x] add [Oracle 11g Release 2](https://docs.oracle.com/cd/E11882_01/nav/portal_4.htm) **DONE**
- [x] add [SQLServer](https://msdn.microsoft.com/en-US/sqlserver)   **DONE**
- [x] add [MySQL](http://dev.mysql.com/doc/)    **DONE**
- [x] add [PostgreSQL](http://www.postgresql.org/docs/)   **DONE**
- [x] add [SQLite](https://www.sqlite.org/docs.html)   **DONE**
- [x] add [Informix](http://www-01.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.welcome.doc/welcome.htm?lang=en)   **DONE**
- [x] add [SAP ASE Sybase](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.help.ase.15.7/title.htm)   **DONE**
- [x] add [DB2](http://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.kc.doc/welcome.html)    **DONE**
- [] add [dBase](http://www.dbase.com/dbasesql/dbase-documentation-download/)   
- [] add [MS Access](https://msdn.microsoft.com/en-us/library/office/ff604965%28v=office.14%29.aspx)
- [] add [Pandas](http://pandas.pydata.org/pandas-docs/version/0.12.0/)   
- [] add [Apache Spark] (https://spark.apache.org/docs/latest/)  
- [] add [Apache Storm] (https://storm.apache.org/documentation/Home.html)  
- [] add [Hadoop](http://hadoop.apache.org/docs/r2.7.0/)    
- [x] add [MariaDB](https://mariadb.com/kb/en/mariadb/documentation/)  **DONE**
- [x] add [Infobright](https://www.infobright.com/index.php/community-2/)    **DONE**
- [x] add [TimesTen](http://www.oracle.com/technetwork/database/database-technologies/timesten/documentation/index.html)    **DONE**
- [] add [MongoDB] (http://docs.mongodb.org/manual/)  
- [] add [HBase] (http://hbase.apache.org/)  
- [] add [Cassandra] (http://cassandra.apache.org/)  
- [] add [Bigtable] (https://cloud.google.com/bigtable/docs/)  
- [] add [Teradata] (http://www.info.teradata.com/HTMLPubs/DB_TTU_14_00/index.html#page/Storage_Management/B035_2492_071A/2492ch01.084.17.html)  
- [] add [Apache Hive] (http://doc.mapr.com/display/MapR/Hive)    
- [] add [Vertica](http://www.vertica.com/hp-vertica-documentation/hp-vertica-7-1-x-documentation/)   
- [] add [Netezza](https://www-304.ibm.com/support/knowledgecenter/SSULQD_7.2.0/com.ibm.nz.welcome.doc/doc/welcome.html)   
- [] add Parstream
- [] add ParAccel
- [] add [Twitter Streaming API](https://dev.twitter.com/streaming/overview)  (extract)
- [] add [Google Analytics](https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py)  
- [] add [Crate Data](https://www.openhub.net/p/cratedata)
- [] add Facebook (extract)
- [] add Taleo HR (extract) 
- [] add [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/) (load, extract) 
- [] add [Greenplum](http://gpdb.docs.pivotal.io/gpdb-435.html)  
- [] add [Actian Ingres](http://esd.actian.com/product/docs)  
- [] add [McObject](http://www.mcobject.com/embedded-database-manuals)  
- [] add [NuiDB](http://doc.nuodb.com/display/doc/NuoDB+Online+Documentation)  
- [] add [Disco](https://www.openhub.net/p/disco)
- [] add [Clustrix](http://docs.clustrix.com/display/CLXDOC/Home)  
- [] add [OrientDB](http://orientdb.com/docs/last/)   
- [] add [KDB+](http://kx.com/resources.php)  
- [] add [Volt DB](http://docs.voltdb.com/)  
- [] add [Arango DB](https://www.arangodb.com/documentation/)   
- [] add [Foundation DB](https://foundationdb.com/key-value-store/documentation/index.html)  
- [] add [Enterprise DB](http://www.enterprisedb.com/products-services-training/products/documentation)   
- [] add Altibase HDB
- [] add [EXASOL](https://www.exasol.com/support/secure/attachment/30841/EXASolution_User_Manual-5.0.3-en.pdf)   
- [] add [Aster](http://www.teradata.com/Teradata-Aster/overview/)  
- [] add [Kinesis](http://aws.amazon.com/documentation/kinesis/) (extract)
- [] add [Redshift](http://aws.amazon.com/documentation/redshift/)   
- [] add [RDS](http://aws.amazon.com/documentation/rds/)   
- [] add [DynamoDB](http://aws.amazon.com/documentation/dynamodb/)  
- [] add [Couchbase](http://docs.couchbase.com/admin/admin/Couchbase-intro.html)  
- [] add [Aerospike](http://www.aerospike.com/docs/)    
- [] add [InterSystems Caché](http://www.intersystems.com/our-products/cache/managing-data/),  [export](http://docs.intersystems.com/ens20131/csp/docbook/DocBook.UI.Page.cls?KEY=GSQL_shell)   
- add QV (QlikView file format)
- add MDX (file format)

##Quirks
- tested to run only on Windows for now (even thou it's wxPython)
- CSV dump files are uncompressed (will add zip compression as option)
- physical copy is done on Windows. Only Oracle copy can be executed on Linux (bash via ssh)

##Performance
- data copy speed mostly depends on your NIC(Ethernet) speed and other factors like how _far_ you are from target and source servers (in terms of network topology and physically). 

>I've seen 10x performance improvement when I ran it on DEV Linux server (10Gb Ethernet) v.s. my office Windows Desktop (100Mb Ethernet).

##References
* [QueryCopy for Oracle](https://github.com/QueryCopy/QueryCopy-for-Oracle) -- `qc32\qc32.exe`


##Vendor Docs

Database |Version | Export | Import | Comments
---------|----------|-------- | -------| -------
[Oracle 12c](http://docs.oracle.com/database/121/index.htm)  |`Release 1` |[SQL*Plus ](https://docs.oracle.com/database/121/SQPUG/toc.htm)|[SQL*Loader ](https://docs.oracle.com/database/121/SUTIL/ldr_concepts.htm#SUTIL003) 
[Oracle 11g](https://docs.oracle.com/cd/E11882_01/nav/portal_4.htm) | `Release 2`| ||
[Disco](https://www.openhub.net/p/disco)||||
[Crate Data](https://www.openhub.net/p/cratedata)||||
[MongoDB](http://docs.mongodb.org/manual/)| `3.0` |||
[TimesTen](http://www.oracle.com/technetwork/database/database-technologies/timesten/documentation/index.html)|`Release 2`|||
[DynamoDB](http://aws.amazon.com/documentation/dynamodb/) ||||
[Hadoop](http://hadoop.apache.org/docs/r2.7.0/) |`r2.7.0` |||
[EXASOL](https://www.exasol.com/support/secure/attachment/30841/EXASolution_User_Manual-5.0.3-en.pdf) |`5.0.3`|||pdf
[Kinesis](http://aws.amazon.com/documentation/kinesis/)||||
[Netezza](https://www-304.ibm.com/support/knowledgecenter/SSULQD_7.2.0/com.ibm.nz.welcome.doc/doc/welcome.html) |`7.2.0` |||
[KDB+](http://kx.com/resources.php)||||
[Aster](http://www.teradata.com/Teradata-Aster/overview/) ||||
[Aerospike](http://www.aerospike.com/docs/) ||||
[Couchbase](http://docs.couchbase.com/admin/admin/Couchbase-intro.html) ||||
[Redshift](http://aws.amazon.com/documentation/redshift/) ||||
[RDS](http://aws.amazon.com/documentation/rds/) ||||
[Enterprise DB](http://www.enterprisedb.com/products-services-training/products/documentation)  ||||
[Foundation DB](https://foundationdb.com/key-value-store/documentation/index.html) ||||
[Arango DB](https://www.arangodb.com/documentation/) ||||
[Volt DB](http://docs.voltdb.com/)  ||||
[OrientDB](http://orientdb.com/docs/last/) ||||
[Clustrix](http://docs.clustrix.com/display/CLXDOC/Home)  ||||
[NuiDB](http://doc.nuodb.com/display/doc/NuoDB+Online+Documentation) ||||
[McObject](http://www.mcobject.com/embedded-database-manuals) ||||
[Actian Ingres](http://esd.actian.com/product/docs) ||||
[Greenplum](http://gpdb.docs.pivotal.io/gpdb-435.html)||||
[Salesforce](https://developer.salesforce.com/docs/atlas.en-us.dataLoader.meta/dataLoader/) |`DataLoader`|||
[Twitter Streaming API](https://dev.twitter.com/streaming/overview)||||
[Google Analytics](https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py)||||
[Vertica](http://www.vertica.com/hp-vertica-documentation/hp-vertica-7-1-x-documentation/)|`7-1-x`|||
[SQLServer](https://msdn.microsoft.com/en-US/sqlserver)||||
[MySQL](http://dev.mysql.com/doc/)||||
[PostgreSQL](http://www.postgresql.org/docs/)||||
[SQLite](https://www.sqlite.org/docs.html)||||
[Informix](http://www-01.ibm.com/support/knowledgecenter/SSGU8G_12.1.0/com.ibm.welcome.doc/welcome.htm?lang=en)| `12.1.0`|||
[SAP ASE Sybase](http://infocenter.sybase.com/help/index.jsp?topic=/com.sybase.infocenter.help.ase.15.7/title.htm)||||
[DB2](http://www-01.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.kc.doc/welcome.html)| `10.5.0`|||
[dBase](http://www.dbase.com/dbasesql/dbase-documentation-download/)||||
[MS Access](https://msdn.microsoft.com/en-us/library/office/ff604965%28v=office.14%29.aspx)| `10.0` |||
[Pandas](http://pandas.pydata.org/pandas-docs/version/0.12.0/)||||
[Apache Spark](https://spark.apache.org/docs/latest/)||||
[Apache Storm](https://storm.apache.org/documentation/Home.html)||||
[MariaDB](https://mariadb.com/kb/en/mariadb/documentation/)|||| 
[Infobright](https://www.infobright.com/index.php/community-2/)||||
[Cassandra] (http://cassandra.apache.org/)||||
[HBase] (http://hbase.apache.org/)||||
[Teradata] (http://www.info.teradata.com/HTMLPubs/DB_TTU_14_00/index.html#page/Storage_Management/B035_2492_071A/2492ch01.084.17.html)||||
[Bigtable] (https://cloud.google.com/bigtable/docs/)||||
[Apache Hive] (http://doc.mapr.com/display/MapR/Hive)||||
[InterSystems Caché](http://www.intersystems.com/our-products/cache/managing-data/)|| [export](http://docs.intersystems.com/ens20131/csp/docbook/DocBook.UI.Page.cls?KEY=GSQL_shell)||




## Screenshots

- New Session Menu: 

![New Session Menu](https://raw.githubusercontent.com/data-buddy/DataBuddy/master/screenshots/new_session_all_dbs.png "New Session Menu")


- Add New Session: 

![Add New Session](https://github.com/data-buddy/DataBuddy/blob/master/screenshots/new_session.png "Add New Session")

- Run Session: 

![Run Session](https://github.com/data-buddy/DataBuddy/blob/master/screenshots/Run_Session_for_SQLServer_to_CSV_file_extract.png "Run Session")

- Executed Session: 

![Executed Session](https://github.com/data-buddy/DataBuddy/blob/master/screenshots/Session_Executed_for_SQLServer_to_CSV_file_extract.png "Executed Session")

- Output Tab: 

![Output Tab](https://github.com/data-buddy/DataBuddy/blob/master/screenshots/ouput_tab.png "Output Tab")


##Endorse
* [My Linkedin](https://www.linkedin.com/in/alexbuz) `Alex Buzunov`

#Download
* [Data Buddy latest release](https://github.com/data-buddy/DataBuddy/releases/tag/v0.3.3) -- `data-buddy 0.3.3`



