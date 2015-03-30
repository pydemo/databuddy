::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-i[--input_file] is "Input CSV file."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target SQL Server Enterprise db user."
::-p[--to_passwd] is "SQL Server Enterprise user password."
::-d[--to_db_name] is "SQL Server Enterprise database."
::-s[--to_db_server] is "SQL Server Enterprise instance name."
::-a[--to_table] is "To table."
::-Z[--target_client_home] is "Path to SQL Server Enterprise client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_115651\qc32\qc32.exe ^
-w csv2ssent ^
-o 1 ^
-r 1 ^
-t "|" ^
-i c:\Python27\data_migrator_1239\test\v101\data\ss_shard_0.data ^
-y 1000 ^
-u sa ^
-p ssent_pwd ^
-d test ^
-s ALEX_BUZ-PC\MSSQLSERVER_ENT ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"