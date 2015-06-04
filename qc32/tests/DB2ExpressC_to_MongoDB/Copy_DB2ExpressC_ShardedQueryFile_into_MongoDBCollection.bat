::Test name: DB2ExpressC_ShardedQueryFile
	::Description:	Read SQL from a query file "C:\Python27\data_migrator_1239_mongo\test\v101\query\db2_query.sql".Copy DB2ExpressC query results into MongoDBCollection.
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
::	-q[--query_sql_file] is "Input file with DB2 Express C query sql."
::	-j[--from_user] is "DB2 Express C source user."
::	-x[--from_passwd] is "DB2 Express C source user password."
::	-b[--from_db_name] is "DB2 Express C source database."
::	-n[--from_db_server] is "DB2 Express C source instance name."
::	-z[--source_client_home] is "Path to DB2 Express C client home."
::	-u[--to_user] is "Target MongoDB db user."
::	-p[--to_passwd] is "MongoDB user password."
::	-d[--to_db_name] is "MongoDB database."
::	-s[--to_db_server] is "Target MongoDB instance name."
::	-T[--to_db_port] is "Target MongoDB port."
::	-a[--to_collection] is "To table."
::	-Z[--to_column_names] is "To column list for MongoDB."	
	
echo y|C:\Python27\qc_dist_32\20150604_155850\qc32\qc32.exe ^
-w dbtec-mongo ^
-o 3 ^
-r 3 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150604_155858_547000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-q C:\Python27\data_migrator_1239_mongo\test\v101\query\db2_query.sql ^
-j "ALEX_BUZ" ^
-x "198Morgan" ^
-b "SAMPLE" ^
-n "DB2" ^
-z "C:\Program Files (x86)\IBM\SQLLIB_01\BIN" ^
-u test_user ^
-p tast_pwd ^
-d test ^
-s localhost ^
-T 27017 ^
-a test ^
-Z "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"