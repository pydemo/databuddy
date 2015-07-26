::Test name: SQLServerExpress_QueryFile Limit15
	::Description:	Read SQL from a query file "c:\Python27\data_migrator_1239_mongo\test\v101\query\ss_query.sql".Copy only 15 rows from SQLServerExpress query results into SQLServer2008Table.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
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
::	-q[--query_sql_file] is "Input file with SQL Server Express query sql."
::	-j[--from_user] is "SQL Server Express source user."
::	-x[--from_passwd] is "SQL Server Express source user password."
::	-b[--from_db_name] is "SQL Server Express source database."
::	-n[--from_db_server] is "SQL Server Express source instance name."
::	-z[--source_client_home] is "Path to SQL Server Express client home."
::	-u[--to_user] is "Target SQL Server 2008 db user."
::	-p[--to_passwd] is "SQL Server 2008 user password."
::	-d[--to_db_name] is "SQL Server 2008 database."
::	-s[--to_db_server] is "SQL Server 2008 instance name."
::	-a[--to_table] is "To table."
::	-Z[--target_client_home] is "Path to SQL Server 2008 client home bin dir."	
	
echo y|c:\Python27\qc_dist_32\20150723_234254\qc32\qc32.exe ^
-w SSEXP-SS2008 ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150723_234257_163000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q c:\Python27\data_migrator_1239_mongo\test\v101\query\ss_query.sql ^
-j sa ^
-x 198Morgan ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-u sa ^
-p ssent_pwd ^
-d test ^
-s ALEX_BUZ-PC\MSSQLSERVER_ENT ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"