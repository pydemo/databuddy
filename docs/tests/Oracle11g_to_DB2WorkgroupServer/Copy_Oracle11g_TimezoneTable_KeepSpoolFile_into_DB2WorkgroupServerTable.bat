::Test name: Oracle11g_TimezoneTable KeepSpoolFile
	::Description:	Copy Oracle11g table into DB2WorkgroupServerTable.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "Oracle 11g source user."
::	-x[--from_passwd] is "Oracle 11g source user password."
::	-b[--from_db_name] is "Oracle 11g source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-a[--to_table] is "Target DB2 Workgroup Server table."
::	-u[--to_user] is "Target DB2 Workgroup Server db user."
::	-p[--to_passwd] is "Target DB2 Workgroup Server db user password."
::	-d[--to_db_name] is "Target DB2 Workgroup Server database."
::	-s[--to_db_server] is "Target DB2 Workgroup Server db instance name."
::	-Z[--target_client_home] is "Path to DB2 Workgroup Server client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w ora11g-dbtws ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074311_505000 ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-c SCOTT.Timezone_test_from ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "YYYY-MM-DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-a ALEX_BUZ.Timezone_test_to ^
-u "ALEX_BUZ" ^
-p "198Morgan" ^
-d "SAMPLE" ^
-s "DB2" ^
-Z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN"