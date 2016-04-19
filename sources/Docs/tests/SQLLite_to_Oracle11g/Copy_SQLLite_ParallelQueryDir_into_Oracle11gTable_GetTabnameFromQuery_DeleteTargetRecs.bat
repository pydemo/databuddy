::Test name: SQLLite_ParallelQueryDir
	::Description:	Read each SQL query file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_slite".Copy SQLLite query results into Oracle11gTable GetTabnameFromQuery DeleteTargetRecs.
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
::	-1[--job_pre_etl] is "Path to job level pre-ETL Python script."
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-Q[--query_sql_dir] is "Input dir with SQL Lite query files sql."
::	-b[--from_db_name] is "SQL Lite source database."
::	-z[--source_client_home] is "Path to SQL Lite client home."
::	-u[--to_user] is "Target Oracle 11g db user."
::	-p[--to_passwd] is "Oracle 11g user password."
::	-d[--to_db_name] is "Oracle 11g database."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w slite-ora11g ^
-o 3 ^
-r 3 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074404_654000 ^
-1 ".\etl_templates\Oracle\delete_target_recs\job_pre_etl.py" ^
-C ".\config\sqlloader.py" ^
-5 ".\config\host_map_v2.py" ^
-6 csv ^
-Q C:\Python27\data_migrator_1239_mongo\test\v101\query\query_dir_slite ^
-b C:\Temp\SqlLite\database.db ^
-z "C:\Temp\SqlLite" ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"