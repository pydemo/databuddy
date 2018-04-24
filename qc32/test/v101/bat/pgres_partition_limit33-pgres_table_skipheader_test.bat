::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-ps[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-K[--keep_data_file] is "Keep data dump."
::-M[--log_dir] is "Log destination."
::-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-5[--host_map] is "Host-to-shard map."
::-6[--spool_type] is "Spool file type (CSV or JSON)."
::-dbg[--debug_level] is "QC Debug level."
::-c[--from_table] is "From table."
::-P[--from_any_partition] is "From partition."
::-j[--from_user] is "PostgreSQL source user."
::-x[--from_passwd] is "PostgreSQL source user password."
::-b[--from_db_name] is "PostgreSQL source database."
::-n[--from_db_server] is "PostgreSQL source instance name."
::-z[--source_client_home] is "Path to PostgreSQL client home."
::-R[--source_port] is "Connection port for source PostgreSQL."
::-u[--to_user] is "Target PostgreSQL db user."
::-p[--to_passwd] is "Target PostgreSQL db user password."
::-d[--to_db_name] is "Target PostgreSQL database."
::-s[--to_db_server] is "Target PostgreSQL db instance name."
::-a[--to_table] is "Target PostgreSQL table."
::-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::-T[--target_port] is "Connection port for target PostgreSQL."
::-k[--skip_header] is "Skip header line."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_734000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1