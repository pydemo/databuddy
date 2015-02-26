C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe ^
-w "csv2ora11g" ^
-t "|" ^
-r "1" ^
-o "1" ^
-i "C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data" ^
-y "1000" ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-d "orcl" ^
-p "tiger2" ^
-a "SCOTT.Timestamp_test_to" ^
-u "SCOTT" ^

C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe -t "|" -w csv2ora11g -r 1 -o 1 -y 1000 -i C:\\Python27\\data_migrator_1239\\test\\v101\\data\\oracle_shard_0_ts.data -d orcl -Z C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -u SCOTT -p tiger2 -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -a SCOTT.Timestamp_test_to

['C:\\Users\\alex_buz\\Documents\\GitHub\\DataBuddy\\qc32\\qc32.exe',
 '-t', '|',
 '-w', 'csv2ora11g',
 '-r', '1',
 '-o', '1',
 '-y', '1000',
 '-i', 'C:\\Python27\\data_migrator_1239\\test\\v101\\data\\oracle_shard_0_ts.data',
 '-d', 'orcl',
 '-Z', 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN',
 '-e', '"YYYY-MM-DD HH24.MI.SS"',
 '-m', '"YYYY-MM-DD HH24.MI.SS.FF2"',
 '-u', 'SCOTT',
 '-p', 'tiger2',
 '-O', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"',
 '-a', 'SCOTT.Timestamp_test_to',
 '-X', '1']
 
 Namespace(arg_1='', arg_2='', arg_3='', ask_to_truncate=0, cmd=[], copy_vector='
csv2ora11g', field_term='|', input_dirs=None, input_files='C:\\Python27\\data_mi
grator_1239\\test\\v101\\data\\oracle_shard_0_ts.data', keep_data_file=0, key_on
_exit=1, lame_duck=0, nls_date_format='"YYYY-MM-DD HH24.MI.SS"', nls_timestamp_format='"YYYY-MM-DD HH24.MI.SS.FF2"', nls_timestamp_tz_format='"YYYY-MM-DD HH:MI:
SS.FF2 TZH:TZM"', num_of_shards=1, pool_size=1, shard_size_kb=1000, skip_rows=0,
 target_client_home='C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN', to_db_n
ame='orcl', to_partition=None, to_passwd='tiger2', to_sub_partition=None, to_tab
le='SCOTT.Timestamp_test_to', to_user='SCOTT', truncate_target=0, validate=0)

Namespace(arg_1='', arg_2='', arg_3='', ask_to_truncate=0, cmd=[], copy_vector='
csv2ora11g', field_term='|', input_dirs=None, input_files='C:\\Python27\\data_mi
grator_1239\\test\\v101\\data\\oracle_shard_0_ts.data', keep_data_file=0, key_on
_exit=0, lame_duck=0, nls_date_format='YYYY-MM-DD HH24.MI.SS', nls_timestamp_for
mat='YYYY-MM-DD HH24.MI.SS.FF2', nls_timestamp_tz_format='YYYY-MM-DD HH:MI:SS.FF
2 TZH:TZM', num_of_shards=1, pool_size=1, shard_size_kb=1000, skip_rows=0, targe
t_client_home='C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN', to_db_name='o
rcl', to_partition=None, to_passwd='tiger2', to_sub_partition=None, to_table='SC
OTT.Timestamp_test_to', to_user='SCOTT', truncate_target=0, validate=0)




