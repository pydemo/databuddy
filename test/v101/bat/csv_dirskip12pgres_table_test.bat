::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-I[--input_dir] is "Input CSV directory."
::-k[--skip_rows] is "Header size. Number of rows to skip in input file."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target PostgreSQL db user."
::-p[--to_passwd] is "Target PostgreSQL db user password."
::-d[--to_db_name] is "Target PostgreSQL database."
::-s[--to_db_server] is "Target PostgreSQL db instance name."
::-a[--to_table] is "Target PostgreSQL table."
::-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::-T[--target_port] is "Connection port for target PostgreSQL."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_115609\qc32\qc32.exe ^
-w csv2pgres ^
-o 1 ^
-r 1 ^
-t "|" ^
-I c:\Python27\data_migrator_1239\test\v101\data\pgres_data_dir ^
-k 1 ^
-y 1000 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434