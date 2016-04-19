aa={'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with SQL Lite query sql.'), 'from_db_name': ('-b', '--from_db_name', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', 'Path to SQL Lite client home.'), 'header': ('-H', '--header', 'Include header to SQL Lite extract.'), 'from_table': ('-c', '--from_table', 'From table.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with SQL Lite query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_Table.DBTAES_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_ShardedQueryFile.DBTAES_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\sqllite_query.sql', 'Input file with SQL Lite query sql.'), 'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_Table_KeepSpoolFile.DBTAES_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_QueryDir.DBTAES_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_slite', 'Input dir with SQL Lite query files sql.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_ParallelQueryDir.DBTAES_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_slite', 'Input dir with SQL Lite query files sql.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}], 'SLITE_ShardedTable.DBTAES_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtaes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Advanced Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Advanced Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Advanced Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Advanced Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Advanced Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Advanced Enterprise Server table.')}]}