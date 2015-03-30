::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-I[--input_dir] is "Input CSV directory."
::-k[--skip_rows] is "Header size. Number of rows to skip in input file."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target SQL Server Express db user."
::-p[--to_passwd] is "SQL Server Express user password."
::-d[--to_db_name] is "SQL Server Express database."
::-s[--to_db_server] is "SQL Server Express instance name."
::-a[--to_table] is "To table."
::-Z[--target_client_home] is "Path to SQL Server Express client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_115718\qc32\qc32.exe ^
-w csv2ssexp ^
-o 1 ^
-r 1 ^
-t "|" ^
-I c:\Python27\data_migrator_1239\test\v101\data\ss_data_dir ^
-k 1 ^
-y 1000 ^
-u sa ^
-p 198Morgan ^
-d master ^
-s ALEX_BUZ-PC\SQLEXPRESS ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"