::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-U[--truncate_target] is "Truncate target table/partition/subpartition."
::-I[--input_dirs] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target Exadata db user."
::-p[--to_passwd] is "Exadata user password."
::-d[--to_db_name] is "Exadata database."
::-a[--to_table] is "To Oracle table."
::-e[--nls_date_format] is "nls_date_format for target."
::-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::-Z[--target_client_home] is "Path to Exadata client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
python -c "print 'y\ny'" |C:\Python27\qc_dist_32\20150222_111236\qc32\qc32.exe ^
-w csv2oraexa ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-U 1 ^
-I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_1;C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_2 ^
-y 1000 ^
-u SCOTT ^
-p tiger2 ^
-d orcl ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"