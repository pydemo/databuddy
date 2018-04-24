::Test name: Oracle11g_ShardedQueryDir
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_ora".Copy Oracle11g query results into PostgreSQLTable SkipHeader.
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
::	-Q[--query_sql_dir] is "Input dir with Oracle 11g query files sql."
::	-j[--from_user] is "Oracle 11g source user."
::	-x[--from_passwd] is "Oracle 11g source user password."
::	-b[--from_db_name] is "Oracle 11g source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w ora11g-pgres ^
-o 1 ^
-r 3 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074319_525000 ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-Q C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_ora ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "YYYY-MM-DD HH24:MI:SS" ^
-m "YYYY-MM-DD HH24:MI:SS" ^
-O "YYYY-MM-DD HH24:MI:SS.FF3 TZH:TZM" ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1