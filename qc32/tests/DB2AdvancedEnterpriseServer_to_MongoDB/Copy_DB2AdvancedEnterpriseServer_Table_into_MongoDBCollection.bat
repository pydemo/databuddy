::Test name: DB2AdvancedEnterpriseServer_Table
	::Description:	Copy DB2AdvancedEnterpriseServer table into MongoDBCollection.
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
::	-j[--from_user] is "DB2 Advanced Enterprise Server source user."
::	-x[--from_passwd] is "DB2 Advanced Enterprise Server source user password."
::	-b[--from_db_name] is "DB2 Advanced Enterprise Server source database."
::	-n[--from_db_server] is "DB2 Advanced Enterprise Server source instance name."
::	-z[--source_client_home] is "Path to DB2 Advanced Enterprise Server client home."
::	-u[--to_user] is "Target MongoDB db user."
::	-p[--to_passwd] is "MongoDB user password."
::	-d[--to_db_name] is "MongoDB database."
::	-s[--to_db_server] is "Target MongoDB instance name."
::	-T[--to_db_port] is "Target MongoDB port."
::	-a[--to_collection] is "To table."
::	-Z[--to_column_names] is "To column list for MongoDB."
::	-numIW[--numInsertionWorkers] is "Upsert rows into MongoDB."	
	
echo y|C:\Python27\qc_dist_32\20150614_220157\qc32\qc32.exe ^
-w dbtaes-mongo ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150614_220243_709000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-c Timestamp_test_from ^
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
-Z "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-numIW 1