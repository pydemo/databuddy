#do not change
aa={'SS2000_ShardedQueryFile.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_289000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_pscp\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server 2000 query sql.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_Partition_Limit20.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_282000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_partition': ('-P', '--from_partition', 'DateRange(Created)=3', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_ShardedPartition.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_285000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_partition': ('-P', '--from_partition', 'DateRange(Created)=3', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'status_pipe_id': ['-spID', '--status_pipe_id', '', 'Status reporting pipe ID.'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-ps', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'query_sql_file': ['-q', '--query_sql_file', '', 'Input file with SQL Server 2000 query sql.'], 'from_db_name': ['-b', '--from_db_name', '', 'SQL Server 2000 source database.'], 'from_partition': ['-P', '--from_partition', '', 'From partition.'], 'from_table': ['-c', '--from_table', '', 'From table.'], 'source_client_home': ['-z', '--source_client_home', '', 'Path to SQL Server 2000 client home.'], 'from_user': ['-j', '--from_user', '', 'SQL Server 2000 source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'SQL Server 2000 source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'SQL Server 2000 source instance name.'], 'query_sql_dir': ['-Q', '--query_sql_dir', '', 'Input dir with SQL Server 2000 query sqls.']}, {'to_db_name': ['-d', '--to_db_name', '', 'Target SAP Sybase ASE database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to SAP Sybase ASE client home bin dir.'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'to_user': ['-u', '--to_user', '', 'Target SAP Sybase ASE db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Target SAP Sybase ASE db user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target SAP Sybase ASE db instance name.'], 'to_table': ['-a', '--to_table', '', 'Target SAP Sybase ASE table.']}], 'SS2000_QueryDir.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_300000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_pscp\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server 2000 query sqls.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_ShardedTable_Limit50.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_278000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_table': ('-c', '--from_table', 'Date_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_Table_KeepSpoolFile.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_274000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_table': ('-c', '--from_table', 'Date_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_QueryFile_Limit15.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_304000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_pscp\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server 2000 query sql.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_ShardedTable.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_311000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_table': ('-c', '--from_table', 'Date_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_Table.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_307000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_table': ('-c', '--from_table', 'Date_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_QueryDir_Limit25.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 25, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_315000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_pscp\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server 2000 query sqls.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_Partition.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_296000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'from_partition': ('-P', '--from_partition', 'DateRange(Created)=3', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}], 'SS2000_QueryFile.SYASE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'SS2000-SYASE', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20160418_001124_293000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_pscp\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server 2000 query sql.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server 2000 source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server 2000 client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server 2000 source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server 2000 source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server 2000 source instance name.')}, {'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Date_test_to"', 'Target SAP Sybase ASE table.')}]}