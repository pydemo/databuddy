aa={'CSV_ShardedFileSkip1.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_ShardedDirSkip1.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'input_dir': ('-I', '--input_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Target Informix IDS table.')}], 'CSV_Dir_Limit10.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_File_Limit10.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_ShardedFile_Limit10.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_ShardedDir.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_DirSkip1.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_DateFile.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_TimezoneFile.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_ShardedDir_Limit10.INFOR_Table': [{'lame_duck': ('-l', '--lame_duck', 10, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_FileSkip1.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 100, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_Dir.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\infor_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}], 'CSV_TimestampFile.INFOR_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2infor', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'shard_size_kb': ('-y', '--shard_size_kb', 1000, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\informix_shard_0.data', 'Input CSV file.')}, {'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix IDS database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix IDS client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix IDS db user.'), 'to_passwd': ('-p', '--to_passwd', '"test_pwd"', 'Target Informix IDS db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix IDS db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix IDS table.')}]}