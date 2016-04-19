aa={'DBTES_ParallelQueryDir.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Enterprise Server query files sql.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_Partition.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with DB2 Enterprise Server query sql.'), 'from_db_name': ('-b', '--from_db_name', 'DB2 Enterprise Server source database.'), 'from_partition': ('-P', '--from_partition', 'From partition.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', 'DB2 Enterprise Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with DB2 Enterprise Server query files sql.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to TimesTen client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'Target TimesTen table.')}], 'DBTES_ShardedPartition.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_QueryDir_Limit10.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Enterprise Server query files sql.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_ShardedQueryFile.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Enterprise Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_ParallelQueryDir_Limit10.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Enterprise Server query files sql.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_Table_KeepSpoolFile.TTEN_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_ShardedTable.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_ShardedPartition_Limit50.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_Table.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_QueryDir.TTEN_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Enterprise Server query files sql.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_Partition_Limit30.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 30, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_QueryFile_Limit10.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Enterprise Server query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_Table_Limit20.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}], 'DBTES_ShardedTable_Limit65.TTEN_Table': [{'lame_duck': ('-l', '--lame_duck', 65, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtes2tten', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Enterprise Server source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Enterprise Server source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Enterprise Server source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Enterprise Server source instance name.')}, {'to_DSN_name': ('-d', '--to_DSN_name', 'my_ttdb', 'Target TimesTen database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\TimesTen\\tt1122_64\\bin"', 'Path to TimesTen client home bin dir.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for target.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for target.'), 'to_user': ('-u', '--to_user', 'TERRY', 'Target TimesTen db user.'), 'to_passwd': ('-p', '--to_passwd', 'secret', 'Target TimesTen db user password.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for target.'), 'to_table': ('-a', '--to_table', 'TERRY.Timestamp_test_to', 'Target TimesTen table.')}]}