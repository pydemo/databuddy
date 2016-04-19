#do not change
aa={'MONGO_Collection_Skip10.JSON_File': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_079000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_skip_rows': ('-S', '--from_skip_rows', 1, 'Number of rows tto skip in source MongoDBtream.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT\\testMONGO_Collection_Skip10.js', 'To JSON file.')}], 'MONGO_Query.JSON_File': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_039000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'json_query': ('-jsonq', '--json_query', '"{\'COUNTRY\':\'United States\'}"', 'Inline MongoDB JSON qry.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT\\testMONGO_Query.js', 'To JSON file.')}], 'MONGO_Collection_withHeader.JSON_File': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_149000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'header': ('-A', '--header', 1, 'Include header to MongoDB extract.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT\\testMONGO_Collection_withHeader.js', 'To JSON file.')}], 'default': [{'ask_to_truncate': ['-E', '--ask_to_truncate', '', 'Ask to truncate.'], 'shard_pre_etl': ['-2', '--shard_pre_etl', '', 'Path to shard level pre-ETL Python script.'], 'debug_level': ['-dbg', '--debug_level', '', 'QC Debug level.'], 'spool_type': ['-6', '--spool_type', '', 'Spool file type (CSV or JSON).'], 'keep_data_file': ['-K', '--keep_data_file', '', 'Keep data dump.'], 'default_spool_dir': ['-F', '--default_spool_dir', '', 'Default data dump dir (default_spool_dir/job_name/timestamp).'], 'lame_duck': ['-l', '--lame_duck', '', 'Limit rows (lame duck run).'], 'copy_vector': ['-w', '--copy_vector', '', 'Data copy direction.'], 'log_dir': ['-M', '--log_dir', '', 'Log destination.'], 'time_stamp': ['-Y', '--time_stamp', '', 'Timestamp (log_dir/job_name/timestamp).'], 'job_name': ['-B', '--job_name', '', 'Job name (log_dir/job_name).'], 'status_pipe_id': ['-spID', '--status_pipe_id', '', 'Status reporting pipe ID.'], 'job_pre_etl': ['-1', '--job_pre_etl', '', 'Path to job level pre-ETL Python script.'], 'num_of_shards': ['-r', '--num_of_shards', '', 'Number of shards.'], 'loader_profile': ['-C', '--loader_profile', '', 'SQL*Loader profile (user defined).'], 'email_to': ['-L', '--email_to', '', 'Email job status.'], 'host_map': ['-5', '--host_map', '', 'Host-to-shard map.'], 'validate': ['-V', '--validate', '', 'Check if source and target objects exist.'], 'field_term': ['-t', '--field_term', '', 'Field terminator.'], 'pool_size': ['-ps', '--pool_size', '', 'Pool size.'], 'column_buckets': ['-0', '--column_buckets', '', 'Wide row support.'], 'job_post_etl': ['-3', '--job_post_etl', '', 'Jobs post-etl script.'], 'truncate_target': ['-U', '--truncate_target', '', 'Truncate target table/partition/subpartition.'], 'shard_post_etl': ['-4', '--shard_post_etl', '', 'Shards post-etl script.'], 'key_on_exit': ['-X', '--key_on_exit', '', 'Ask for an "Enter" key upon exit.']}, {'from_column_names': ['-P', '--from_column_names', '', 'From column list.'], 'from_db_name': ['-b', '--from_db_name', '', 'MongoDB source database.'], 'header': ['-A', '--header', '', 'Include header to MongoDB extract.'], 'from_db_port': ['-z', '--from_db_port', '', 'MongoDB source database port.'], 'json_query_file': ['-q', '--json_query_file', '', 'Input file with MongoDB JSON query file.'], 'from_skip_rows': ['-S', '--from_skip_rows', '', 'Number of rows tto skip in source MongoDBtream.'], 'json_query_dir': ['-Q', '--json_query_dir', '', 'Input dir with MongoDB JSON query files.'], 'json_query': ['-jsonq', '--json_query', '', 'Inline MongoDB JSON qry.'], 'from_user': ['-j', '--from_user', '', 'MongoDB source user.'], 'from_passwd': ['-x', '--from_passwd', '', 'MongoDB source user password.'], 'from_db_server': ['-n', '--from_db_server', '', 'MongoDB source instance name.'], 'from_collection': ['-c', '--from_collection', '', 'From collection.']}, {'to_file': ['-g', '--to_file', '', 'To JSON file.'], 'to_dir': ['-D', '--to_dir', '', 'To JSON directory.']}], 'MONGO_Collection_JSON.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_129000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Collection_withHeader.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_169000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'header': ('-A', '--header', 1, 'Include header to MongoDB extract.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Collection.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103853_949000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Collection_Limit10.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_029000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Collection_JSON.JSON_File': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_119000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT\\testMONGO_Collection_JSON.js', 'To JSON file.')}], 'MONGO_Collection_Skip10.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_099000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_skip_rows': ('-S', '--from_skip_rows', 1, 'Number of rows tto skip in source MongoDBtream.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Query.JSON_Dir': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_059000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'json_query': ('-jsonq', '--json_query', '"{\'COUNTRY\':\'United States\'}"', 'Inline MongoDB JSON qry.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_dir': ('-D', '--to_dir', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT', 'To JSON directory.')}], 'MONGO_Collection_Limit10.JSON_File': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '","', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-ps', '--pool_size', 1, 'Pool size.'), 'debug_level': ('-dbg', '--debug_level', 1, 'QC Debug level.'), 'spool_type': ('-6', '--spool_type', 'json', 'Spool file type (CSV or JSON).'), 'copy_vector': ('-w', '--copy_vector', 'MONGO-JSON', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'default_spool_dir': ('-F', '--default_spool_dir', 'C:\\tmp\\TEST_default_spool', 'Default data dump dir (default_spool_dir/job_name/timestamp).'), 'time_stamp': ('-Y', '--time_stamp', '20151105_103854_009000', 'Timestamp (log_dir/job_name/timestamp).'), 'host_map': ('-5', '--host_map', '".\\config\\host_map\\host_map.py"', 'Host-to-shard map.'), 'job_name': ('-B', '--job_name', 'qc_job', 'Job name (log_dir/job_name).'), 'log_dir': ('-M', '--log_dir', 'C:\\Temp\\qc_log', 'Log destination.')}, {'from_column_names': ('-P', '--from_column_names', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'From column list.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'MongoDB source database.'), 'from_db_port': ('-z', '--from_db_port', '27017', 'MongoDB source database port.'), 'from_user': ('-j', '--from_user', 'test_user', 'MongoDB source user.'), 'from_passwd': ('-x', '--from_passwd', 'tast_pwd', 'MongoDB source user password.'), 'from_db_server': ('-n', '--from_db_server', 'localhost', 'MongoDB source instance name.'), 'from_collection': ('-c', '--from_collection', 'test', 'From collection.')}, {'to_file': ('-g', '--to_file', 'C:\\Python27\\data_migrator_1239_mongo\\JSON_OUT\\testMONGO_Collection_Limit10.js', 'To JSON file.')}]}