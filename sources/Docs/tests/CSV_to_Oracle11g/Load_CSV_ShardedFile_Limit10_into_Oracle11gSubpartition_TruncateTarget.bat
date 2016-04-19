::Test name: CSV_ShardedFile Limit10
	::Description:	Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	::				and run loader process on each shard in thread pool (-o[--pool_size] 1).
	::				Load only 10 rows from CSV file into Oracle11gSubpartition TruncateTarget.
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
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target Oracle 11g db user."
::	-p[--to_passwd] is "Oracle 11g user password."
::	-d[--to_db_name] is "Oracle 11g database."
::	-a[--to_table] is "To Oracle table."
::	-N[--to_sub_partition] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
..\\python -c "print 'y\ny'" |C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w csv-ora11g ^
-o 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-U 1 ^
-E 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150616_074313_128000 ^
-C ".\config\sqlloader.py" ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-i C:\Python27\data_migrator_1239_mongo\test\v101\data\oracle_shard_0_ts.data ^
-y 10 ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-a SCOTT.Sub_Partitioned_test_to ^
-N part_15_sp1 ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"