::Test name: Oracle11g_SubpartitionList
	::Description:	Copy Oracle11g sub-partition into SybaseSQLAnywhereTable.
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
::	-Sl[--from_sub_partition_list] is "(From) Coma separated sub-partition list."
::	-j[--from_user] is "Oracle 11g source user."
::	-x[--from_passwd] is "Oracle 11g source user password."
::	-b[--from_db_name] is "Oracle 11g source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-u[--to_user] is "Target Sybase SQL Anywhere db user."
::	-p[--to_passwd] is "Target Sybase SQL Anywhere db user password."
::	-d[--to_db_name] is "Target Sybase SQL Anywhere database."
::	-s[--to_db_server] is "Target Sybase SQL Anywhere db instance name."
::	-a[--to_table] is "Target Sybase SQL Anywhere table."
::	-Z[--target_client_home] is "Path to Sybase SQL Anywhere client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w ora11g-syany ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074310_895000 ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-c SCOTT.Sub_Partitioned_test_from ^
-Sl part_15_sp1,part_15_sp2,part_14_sp1,part_14_sp2 ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-u "dba" ^
-p "sql" ^
-d "demo" ^
-s "demo16" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\SQL Anywhere 16\Bin64"