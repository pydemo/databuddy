::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-I[--input_dir] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target SQL Server Enterprise db user."
::-p[--to_passwd] is "SQL Server Enterprise user password."
::-d[--to_db_name] is "SQL Server Enterprise database."
::-s[--to_db_server] is "SQL Server Enterprise instance name."
::-a[--to_table] is "To table."
::-Z[--target_client_home] is "Path to SQL Server Enterprise client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\csvloader_dist_32\20141128_132623\csvloader32\csvloader32.exe ^
-w csv2ssent ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-I c:\Python27\csvloader_1237\test\v101\data\ss_data_dir ^
-y 1000 ^
-u sa ^
-p ssent_pwd ^
-d test ^
-s ALEX_BUZ-PC\MSSQLSERVER_ENT ^
-a dbo.Persons_pipe_datetime_1 ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"