aa={'DBTDE_Partition.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ShardedQueryFile.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Developer Edition query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_QueryFile_Limit10.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Developer Edition query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_QueryDir_Limit10.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Developer Edition query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_Partition_Limit30.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 30, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with DB2 Developer Edition query sql.'), 'from_db_name': ('-b', '--from_db_name', 'DB2 Developer Edition source database.'), 'from_partition': ('-P', '--from_partition', 'From partition.'), 'from_table': ('-c', '--from_table', 'From table.'), 'source_client_home': ('-z', '--source_client_home', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', 'DB2 Developer Edition source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with DB2 Developer Edition query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target database.'), 'to_table': ('-a', '--to_table', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to mysql client home.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.')}], 'DBTDE_Table_Limit20.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 20, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ParallelQueryDir.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Developer Edition query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ShardedTable_Limit65.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 65, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_QueryDir.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_db2', 'Input dir with DB2 Developer Edition query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ShardedPartition_Limit50.SLITE_Table': [{'lame_duck': ('-l', '--lame_duck', 50, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_Table_KeepSpoolFile.SLITE_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_QueryFile.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\db2_query.sql', 'Input file with DB2 Developer Edition query sql.'), 'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_Table.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ShardedPartition.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_partition': ('-P', '--from_partition', '0', 'From partition.'), 'from_table': ('-c', '--from_table', 'Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}], 'DBTDE_ShardedTable.SLITE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbtde2slite', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Developer Edition source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Developer Edition source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Developer Edition source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Developer Edition source instance name.')}, {'to_db_name': ('-d', '--to_db_name', 'C:\\Temp\\SqlLite\\database2.db', 'Target database.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\SqlLite"', 'Path to mysql client home.')}]}