::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-I[--input_dir] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-a[--to_table] is "Target DB2 Express table."
::-u[--to_user] is "Target DB2 Express db user."
::-p[--to_passwd] is "Target DB2 Express db user password."
::-d[--to_db_name] is "Target DB2 Express database."
::-s[--to_db_server] is "Target DB2 Express db instance name."
::-Z[--target_client_home] is "Path to DB2 Express client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_114827\qc32\qc32.exe ^
-w csv2dbte ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-I c:\Python27\data_migrator_1239\test\v101\data\db2_data_dir ^
-y 1000 ^
-a ALEX_BUZ.Timestamp_test_to ^
-u "ALEX_BUZ" ^
-p "198Morgan" ^
-d "SAMPLE" ^
-s "DB2" ^
-Z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN"