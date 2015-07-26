::Test name: CSV_DirsSkip1
	::Description:	Read each CSV file from a directory "C:\Python27\data_migrator_1239_mongo\test\v101\data\mongo_data_dir".Skip 1 rows and load CSV file into MongoDBCollection Upsert.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-I[--input_dirs] is "Input CSV directory."
::	-k[--skip_rows] is "Header size. Number of rows to skip in input file."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target MongoDB db user."
::	-p[--to_passwd] is "MongoDB user password."
::	-d[--to_db_name] is "MongoDB database."
::	-s[--to_db_server] is "Target MongoDB instance name."
::	-T[--to_db_port] is "Target MongoDB port."
::	-a[--to_collection] is "To table."
::	-Z[--to_column_names] is "To column list for MongoDB."
::	-G[--upsert] is "Upsert rows into MongoDB."
::	-numIW[--numInsertionWorkers] is "Upsert rows into MongoDB."	
	
echo y|C:\Python27\qc_dist_32\20150614_220157\qc32\qc32.exe ^
-w csv-mongo ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150614_220206_111000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-I C:\Python27\data_migrator_1239_mongo\test\v101\data\mongo_data_dir ^
-k 1 ^
-y 1000 ^
-u test_user ^
-p tast_pwd ^
-d test ^
-s localhost ^
-T 27017 ^
-a test ^
-Z "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-G 1 ^
-numIW 1