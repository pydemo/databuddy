::Test name: MongoDB_Collection Skip10
	::Description:	Skip 10 rows and copy MongoDB table into DB2ExpressCTable.
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
::	-c[--from_collection] is "From collection."
::	-P[--from_column_names] is "From column list."
::	-j[--from_user] is "MongoDB source user."
::	-x[--from_passwd] is "MongoDB source user password."
::	-b[--from_db_name] is "MongoDB source database."
::	-n[--from_db_server] is "MongoDB source instance name."
::	-z[--from_db_port] is "MongoDB source database port."
::	-O[--from_skip_rows] is "Number of rows tto skip in source MongoDBtream."
::	-a[--to_table] is "Target DB2 Express C table."
::	-u[--to_user] is "Target DB2 Express C db user."
::	-p[--to_passwd] is "Target DB2 Express C db user password."
::	-d[--to_db_name] is "Target DB2 Express C database."
::	-s[--to_db_server] is "Target DB2 Express C db instance name."
::	-Z[--target_client_home] is "Path to DB2 Express C client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150604_155850\qc32\qc32.exe ^
-w mongo-dbtec ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150604_155858_073000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-c test ^
-P "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-j test_user ^
-x tast_pwd ^
-b test ^
-n localhost ^
-z 27017 ^
-O 1 ^
-a ALEX_BUZ.Timestamp_test_to ^
-u "ALEX_BUZ" ^
-p "198Morgan" ^
-d "SAMPLE" ^
-s "DB2" ^
-Z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN"