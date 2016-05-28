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
::-i[--input_files] is "Input CSV file(s)."
::-u[--to_user] is "Target PostgreSQL db user."
::-p[--to_passwd] is "Target PostgreSQL db user password."
::-d[--to_db_name] is "Target PostgreSQL database."
::-s[--to_db_server] is "Target PostgreSQL db instance name."
::-a[--to_table] is "Target PostgreSQL table."
::-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::-T[--target_port] is "Connection port for target PostgreSQL."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_427000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_dt.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434