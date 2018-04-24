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
::-S[--from_sub_partition] is "From sub-partition."
::-j[--from_user] is "MySQL source user."
::-x[--from_passwd] is "MySQL source user password."
::-b[--from_db_name] is "MySQL source database."
::-n[--from_db_server] is "MySQL source instance name."
::-z[--source_client_home] is "Path to MySQL client home."
::-D[--to_dir] is "To directory."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160603_105945\qc32\qc32.exe ^
-w MYSQL-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160603_105948_984000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c TEST.Sub_Partitioned_test_from ^
-S subpart200 ^
-j "alex" ^
-x "mysql_pwd" ^
-b "test" ^
-n "localhost" ^
-z "C:\Temp\mysql\bin" ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT