::Test name: SQLServerExpress_ShardedTable Limit50
	::Description:	Copy only 50 rows from SQLServerExpress table into Oracle11gTable SkipHeader.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "SQL Server Express source user."
::	-x[--from_passwd] is "SQL Server Express source user password."
::	-b[--from_db_name] is "SQL Server Express source database."
::	-n[--from_db_server] is "SQL Server Express source instance name."
::	-z[--source_client_home] is "Path to SQL Server Express client home."
::	-u[--to_user] is "Target Oracle 11g db user."
::	-p[--to_passwd] is "Oracle 11g user password."
::	-d[--to_db_name] is "Oracle 11g database."
::	-a[--to_table] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::	-k[--skip_rows] is "Number of rows to skip in input file."	
	
echo y|C:\Python27\qc_dist_32\20150908_192607\qc32\qc32.exe ^
-w SSEXP-ORA11G ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 50 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150908_192617_686000 ^
-C ".\config\sqlloader.py" ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j sa ^
-x 198Morgan ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD" ^
-m "YYYY-MM-DD HH24:MI:SS.FF3" ^
-O "YYYY-MM-DD HH24:MI:SS.FF" ^
-k 1