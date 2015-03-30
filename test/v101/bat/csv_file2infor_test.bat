::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-i[--input_file] is "Input CSV file."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-a[--to_table] is "Target Informix IDS table."
::-u[--to_user] is "Target Informix IDS db user."
::-p[--to_passwd] is "Target Informix IDS db user password."
::-d[--to_db_name] is "Target Informix IDS database."
::-s[--to_db_server] is "Target Informix IDS db instance name."
::-Z[--target_client_home] is "Path to Informix IDS client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\csvloader_dist_32\20141128_132623\csvloader32\csvloader32.exe ^
-w csv2infor ^
-o 1 ^
-r 1 ^
-t "|" ^
-i c:\Python27\csvloader_1237\test\v101\data\informix_shard_0.data ^
-y 1000 ^
-a Persons_pipe_datetime_1 ^
-u "informix" ^
-p "test_pwd" ^
-d "test" ^
-s "ol_s_112614_175026" ^
-Z "C:\Program Files (x86)\IBM Informix Software Bundle\bin"