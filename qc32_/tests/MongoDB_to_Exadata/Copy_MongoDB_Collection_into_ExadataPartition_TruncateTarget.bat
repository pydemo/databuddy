::Test name: MongoDB_Collection
	::Description:	Copy MongoDB table into ExadataPartition TruncateTarget.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
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
::	-c[--from_collection] is "From collection."
::	-P[--from_column_names] is "From column list."
::	-j[--from_user] is "MongoDB source user."
::	-x[--from_passwd] is "MongoDB source user password."
::	-b[--from_db_name] is "MongoDB source database."
::	-n[--from_db_server] is "MongoDB source instance name."
::	-z[--from_db_port] is "MongoDB source database port."
::	-u[--to_user] is "Target Exadata db user."
::	-p[--to_passwd] is "Exadata user password."
::	-d[--to_db_name] is "Exadata database."
::	-a[--to_table] is "To Oracle table."
::	-G[--to_partition] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
..\\python -c "print 'y\ny'" |C:\Python27\qc_dist_32\20150614_220157\qc32\qc32.exe ^
-w mongo-oraexa ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-U 1 ^
-E 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150614_220302_586000 ^
-C "C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml" ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-c test ^
-P "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-j test_user ^
-x tast_pwd ^
-b test ^
-n localhost ^
-z 27017 ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-a SCOTT.Partitioned_test_to ^
-G part_15 ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"