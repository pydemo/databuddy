#do not change
aa={'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'status_pipe_id': ['-spID', '--status_pipe_id', '', 'Status reporting pipe ID.'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-ps', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'from_remote_dirs': ['-frdl', '--from_remote_dirs', '', 'From remote dir list.  One or more coma separated dir names  (in command line).'], 'from_remote_file': ['-frm', '--from_remote_file', '', 'From remote file.'], 'from_remote_dir': ['-frd', '--from_remote_dir', '', 'From remote dir.'], 'from_server': ['-fsrv', '--from_server', '', 'From server.'], 'from_user': ['-fusr', '--from_user', '', 'From user.'], 'from_remote_files': ['-frfl', '--from_remote_files', '', 'From remote file list. One or more coma separated file names (in command line).'], 'from_passwd': ['-pw', '--from_passwd', '', 'Password.']}, {'to_db_name': ['-d', '--to_db_name', '', 'Target DB2 Express C database.'], 'target_client_home': ['-Z', '--target_client_home', '', 'Path to DB2 Express C client home bin dir.'], 'skip_rows': ['-k', '--skip_rows', '', 'Header size. Number of rows to skip in input file.'], 'to_user': ['-u', '--to_user', '', 'Target DB2 Express C db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Target DB2 Express C db user password.'], 'to_db_server': ['-s', '--to_db_server', '', 'Target DB2 Express C db instance name.'], 'to_table': ['-a', '--to_table', '', 'Target DB2 Express C table.']}], 'PSCP_File.DBTEC_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-DBTEC', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000316_820000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_remote_file': ('-frm', '--from_remote_file', '/tmp/qctest/pscp_test.zip', 'From remote file.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express C client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express C db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express C db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express C table.')}], 'PSCP_Dir.DBTEC_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-DBTEC', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000316_836000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_remote_dir': ('-frd', '--from_remote_dir', '/tmp/qctest', 'From remote dir.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express C client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express C db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express C db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express C table.')}], 'PSCP_FileList.DBTEC_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'csv', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'PSCP-DBTEC', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150908_000316_804000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_remote_files': ('-frfl', '--from_remote_files', '/tmp/qctest/pscp_test.zip,/tmp/qctest/ProcessExplorer.zip', 'From remote file list. One or more coma separated file names (in command line).'), 'from_passwd': ('-pw', '--from_passwd', 'oracle', 'Password.'), 'from_server': ('-fsrv', '--from_server', '192.168.15.227', 'From server.'), 'from_user': ('-fusr', '--from_user', 'oracle', 'From user.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express C client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express C db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express C db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express C table.')}]}