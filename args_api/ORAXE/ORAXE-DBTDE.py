{'default': [{'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, {'query_sql_file': ('-q', '--query_sql_file', 'Input file with Oracle XE query sql.'), 'source_client_home': ('-z', '--source_client_home', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for source.'), 'trim_whitespace': ('-W', '--trim_whitespace', 'Trim whitespace from varchar2 in "Oracle XE" extract.'), 'from_db': ('-f', '--from_db', 'From database.'), 'from_table': ('-c', '--from_table', 'From table.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to DB2 Developer Edition client home bin dir.'), 'skip_rows': ('-k', '--skip_rows', 'Header size. Number of rows to skip in input file.'), 'to_user': ('-u', '--to_user', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'Target DB2 Developer Edition table.')}], 'ORAXE_ShardedTable.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_QueryFile.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\oracle_query.sql', 'Input file with Oracle XE query sql.'), 'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_TimestampTable.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_Table_KeepSpoolFile.DBTDE_Table': [{'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_TimezoneTable.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'from_table': ('-c', '--from_table', 'SCOTT.Timestamp_test_from', 'From table.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_ParallelQueryDir.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ora', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}], 'ORAXE_QueryDir.DBTDE_Table': [{'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'oraxe2dbtde', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, {'source_client_home': ('-z', '--source_client_home', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'Path to Oracle XE client home.'), 'header': ('-A', '--header', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Include header to Oracle XE extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_time_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY-MM-DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_ora', 'Input dir with Oracle XE query files sql.')}, {'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Developer Edition database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Developer Edition client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Developer Edition db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Developer Edition db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Developer Edition db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Developer Edition table.')}]}