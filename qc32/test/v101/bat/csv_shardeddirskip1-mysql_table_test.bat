::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-ps[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-K[--keep_data_file] is "Keep data dump."
::-M[--log_dir] is "Log destination."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-5[--host_map] is "Host-to-shard map."
::-dbg[--debug_level] is "QC Debug level."
::-I[--input_dirs] is "Input CSV directory."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-u[--to_user] is "Target MySQL db user."
::-p[--to_passwd] is "Target db user password."
::-d[--to_db_name] is "Target database."
::-s[--to_db_server] is "Target db instance name."
::-a[--to_table] is "Target table."
::-Z[--target_client_home] is "Path to mysql client home."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160603_105945\qc32\qc32.exe ^
-w CSV-MYSQL ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160603_105947_599000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\mysql_data_dir ^
-y 1 ^
-u alex ^
-p mysql_pwd ^
-d test ^
-s localhost ^
-a Timestamp_test_to ^
-Z "C:\Temp\mysql\bin"