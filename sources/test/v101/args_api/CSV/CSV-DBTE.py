aa={'CSV_DateFile.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_TimezoneFile.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'input_dir': ('-I', '--input_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Express table.')}], 'CSV_Dir_Limit10.DBTE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_ShardedDir.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_File_Limit10.DBTE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_Dir.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_TimestampFile.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_ShardedDir_Limit10.DBTE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_ShardedFile_Limit10.DBTE_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_FileSkip1.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 100, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_DirSkip1.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_ShardedFileSkip1.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}], 'CSV_ShardedDirSkip1.DBTE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2dbte', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\db2_data_dir', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Express database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Express db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Express db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Express db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Express table.')}]}