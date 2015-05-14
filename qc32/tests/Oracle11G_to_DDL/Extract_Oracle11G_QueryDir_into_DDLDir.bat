::Test name: Oracle11G_QueryDir
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ora".Extract Oracle11G query results into DDLDir.
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
::	-Q[--query_sql_dir] is "Input dir with Oracle 11G query files sql."
::	-j[--from_user] is "Oracle 11G source user."
::	-x[--from_passwd] is "Oracle 11G source user password."
::	-b[--from_db_name] is "Oracle 11G source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Python27\qc_dist_32\20150513_194648\qc32\qc32.exe ^
-w ora11g2ddl ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150513_194654_016000 ^
-5 ".\config\host_map_v2.py" ^
-Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ora ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-D C:\Python27\data_migrator_1239_ddl\DDL_OUT