::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-I[--input_dir] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target Sybase IQ db user."
::-p[--to_passwd] is "Target Sybase IQ db user password."
::-d[--to_db_name] is "Target Sybase IQ database."
::-s[--to_db_server] is "Target Sybase IQ db instance name."
::-a[--to_table] is "Target Sybase IQ table."
::-Z[--target_client_home] is "Path to Sybase IQ client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\csvloader_dist_32\20141128_132623\csvloader32\csvloader32.exe ^
-w csv2syiq ^
-o 1 ^
-r 1 ^
-t "|" ^
-I c:\Python27\csvloader_1237\test\v101\data\sybase_data_dir ^
-y 1000 ^
-u "dba" ^
-p "sql" ^
-d "demo" ^
-s "demo16" ^
-a "Persons_pipe_datetime_1" ^
-Z "C:\Program Files\SQL Anywhere 16\Bin64"