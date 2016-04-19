::Test name: SQLServerExpress_QueryDir
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_ss".Copy SQLServerExpress query results into PscpDir.
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
::	-Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
::	-j[--from_user] is "SQL Server Express source user."
::	-x[--from_passwd] is "SQL Server Express source user password."
::	-b[--from_db_name] is "SQL Server Express source database."
::	-n[--from_db_server] is "SQL Server Express source instance name."
::	-z[--source_client_home] is "Path to SQL Server Express client home."
::	-pw[--to_passwd] is "Target server password."
::	-fusr[--to_user] is "To user."
::	-fsrv[--to_server] is "To server."
::	-trd[--to_remote_dir] is "Target remote dir."	
	
echo y|C:\Python27\qc_dist_32\20150908_192607\qc32\qc32.exe ^
-w SSEXP-PSCP ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150908_192621_746000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_ss ^
-j sa ^
-x 198Morgan ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-pw oracle ^
-fusr oracle ^
-fsrv 192.168.15.227 ^
-trd /tmp/qctest/