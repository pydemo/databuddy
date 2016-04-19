::Test name: TimesTen_ParallelQueryDir
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_tt".Copy TimesTen query results into SQLServerExpressTable.
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
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with TimesTen query files sql."
::	-j[--from_user] is "TimesTen source user."
::	-x[--from_passwd] is "TimesTen source user password."
::	-b[--from_DSN_name] is "Source server DSN for TimesTen."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-z[--source_client_home] is "Path to TimesTen client home."
::	-u[--to_user] is "Target SQL Server Express db user."
::	-p[--to_passwd] is "SQL Server Express user password."
::	-d[--to_db_name] is "SQL Server Express database."
::	-s[--to_db_server] is "SQL Server Express instance name."
::	-a[--to_table] is "To table."
::	-Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150908_192607\qc32\qc32.exe ^
-w TTEN-SSEXP ^
-ps 3 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150908_192637_958000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_tt ^
-j TERRY ^
-x secret ^
-b my_ttdb ^
-e "YYYY-MM-DD HH24:MI:SS" ^
-m "YYYY-MM-DD HH24:MI:SS.FF3" ^
-z "C:\Program Files (x86)\TimesTen\tt1122_64\bin" ^
-u sa ^
-p 198Morgan ^
-d master ^
-s ALEX_BUZ-PC\SQLEXPRESS ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"