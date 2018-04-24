::Test name: DB2AdvancedEnterpriseServer_ShardedPartition Limit50
	::Description:	Copy only 50 rows from DB2AdvancedEnterpriseServer sharded partition into Oracle11gPartition TruncateTarget.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-U[--truncate_target] is "Truncate target table/partition/subpartition."
::	-E[--ask_to_truncate] is "Ask to truncate."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-c[--from_table] is "From table."
::	-P[--from_partition] is "From partition."
::	-j[--from_user] is "DB2 Advanced Enterprise Server source user."
::	-x[--from_passwd] is "DB2 Advanced Enterprise Server source user password."
::	-b[--from_db_name] is "DB2 Advanced Enterprise Server source database."
::	-n[--from_db_server] is "DB2 Advanced Enterprise Server source instance name."
::	-z[--source_client_home] is "Path to DB2 Advanced Enterprise Server client home."
::	-u[--to_user] is "Target Oracle 11g db user."
::	-p[--to_passwd] is "Oracle 11g user password."
::	-d[--to_db_name] is "Oracle 11g database."
::	-a[--to_table] is "To Oracle table."
::	-G[--to_partition] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
..\\python -c "print 'y\ny'" |C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w dbtaes-ora11g ^
-o 1 ^
-r 3 ^
-t "|" ^
-l 50 ^
-K 1 ^
-U 1 ^
-E 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074317_558000 ^
-C ".\config\sqlloader.py" ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-c Partitioned_test_from ^
-P 0 ^
-j "ALEX_BUZ" ^
-x "198Morgan" ^
-b "SAMPLE" ^
-n "DB2" ^
-z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN" ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-a SCOTT.Partitioned_test_to ^
-G part_15 ^
-e "YYYY-MM-DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF"