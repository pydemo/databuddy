::Test name: TimesTen_ShardedQueryFile
	::Description:	Read SQL from a query file "C:\Python27\data_migrator_1239_mongo\test\v101\query\timesten_query.sql".Copy TimesTen query results into Oracle11gTable NoClient.
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
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-q[--query_sql_file] is "Input file with TimesTen query sql."
::	-j[--from_user] is "TimesTen source user."
::	-x[--from_passwd] is "TimesTen source user password."
::	-b[--from_DSN_name] is "Source server DSN for TimesTen."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-z[--source_client_home] is "Path to TimesTen client home."
::	-u[--to_user] is "Target Oracle 11g db user."
::	-p[--to_passwd] is "Oracle 11g user password."
::	-d[--to_db_name] is "Oracle 11g database."
::	-a[--to_table] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w tten-ora11g ^
-o 1 ^
-r 3 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074311_155000 ^
-C ".\config\sqlloader.py" ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-q C:\Python27\data_migrator_1239_mongo\test\v101\query\timesten_query.sql ^
-j TERRY ^
-x secret ^
-b my_ttdb ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-z "C:\Program Files (x86)\TimesTen\tt1122_64\bin" ^
-u SCOTT ^
-p tiger ^
-d '(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"