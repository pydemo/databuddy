#do not change
aa={'SSEXP_QueryFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_676000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server Express query sql.'), 'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_QueryFile_Limit15.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_864000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'query_sql_file': ('-q', '--query_sql_file', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server Express query sql.'), 'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'arg_6': ['-6', '--arg_6', '', 'Generic string argument 1.'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'arg_8': ['-8', '--arg_8', '', 'Generic string argument 3.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'arg_7': ['-7', '--arg_7', '', 'Generic string argument 2.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-o', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'query_sql_file': ['-q', '--query_sql_file', '', 'Input file with SQL Server Express query sql.'], 'from_db_name': ['-b', '--from_db_name', '', 'SQL Server Express source database.'], 'from_table': ['-c', '--from_table', '', 'From table.'], 'source_client_home': ['-z', '--source_client_home', '', 'Path to SQL Server Express client home.'], 'from_user': ['-j', '--from_user', '', 'SQL Server Express source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'SQL Server Express source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'SQL Server Express source instance name.'], 'query_sql_dir': ['-Q', '--query_sql_dir', '', 'Input dir with SQL Server Express query sqls.']}, {'to_db_name': ['-d', '--to_db_name', '', 'Oracle XE database.'], 'nls_date_format': ['-e', '--nls_date_format', '', 'nls_date_format for target.'], 'nls_timestamp_format': ['-m', '--nls_timestamp_format', '', 'nls_timestamp_format for target.'], 'to_user': ['-u', '--to_user', '', 'Target Oracle XE db user.'], 'to_passwd': ['-p', '--to_passwd', '', 'Oracle XE user password.'], 'nls_timestamp_tz_format': ['-O', '--nls_timestamp_tz_format', '', 'nls_timestamp_tz_format for target.'], 'to_table': ['-a', '--to_table', '', 'To Oracle table.']}], 'SSEXP_ShardedTable.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_737000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_Table.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_706000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_ShardedTable_Limit50.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_835000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_Table_Limit10.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_807000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_QueryDir_Limit25.ORAXE_Table': [{'lame_duck': ('-l', '--lame_duck', 25, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_610000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server Express query sqls.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_QueryDir.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_648000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'C:\\Python27\\data_migrator_1239_12c\\test\\v101\\query\\query_dir_ss', 'Input dir with SQL Server Express query sqls.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}], 'SSEXP_Table_KeepSpoolFile.ORAXE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ssexp-oraxe', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20150515_220005_776000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map_v2.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'loader_profile': ('-C', '--loader_profile', '"C:\\Python27\\data_migrator_1239\\config\\loader\\sqlloader.yaml"', 'SQL*Loader profile (user defined).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_db_name': ('-b', '--from_db_name', 'master', 'SQL Server Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Express client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Express source user.'), 'from_passwd': ('-x', '--from_passwd', '198Morgan', 'SQL Server Express source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\SQLEXPRESS', 'SQL Server Express source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'orcl', 'Oracle XE database.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD HH24:MI:SS.FF3"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'SCOTT', 'Target Oracle XE db user.'), 'to_passwd': ('-p', '--to_passwd', 'tiger', 'Oracle XE user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'SCOTT.Timestamp_test_to', 'To Oracle table.')}]}