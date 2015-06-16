::Test name: MongoDB_Query
	::Description:	Copy MongoDB query results into InformixIDSTable.
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
::	-jsonq[--json_query] is "Inline MongoDB JSON qry."
::	-c[--from_collection] is "From collection."
::	-P[--from_column_names] is "From column list."
::	-j[--from_user] is "MongoDB source user."
::	-x[--from_passwd] is "MongoDB source user password."
::	-b[--from_db_name] is "MongoDB source database."
::	-n[--from_db_server] is "MongoDB source instance name."
::	-z[--from_db_port] is "MongoDB source database port."
::	-a[--to_table] is "Target Informix IDS table."
::	-u[--to_user] is "Target Informix IDS db user."
::	-p[--to_passwd] is "Target Informix IDS db user password."
::	-d[--to_db_name] is "Target Informix IDS database."
::	-s[--to_db_server] is "Target Informix IDS db instance name."
::	-Z[--target_client_home] is "Path to Informix IDS client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150614_220157\qc32\qc32.exe ^
-w mongo-infor ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150614_220211_508000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-jsonq "{'COUNTRY':'United States'}" ^
-c test ^
-P "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" ^
-j test_user ^
-x tast_pwd ^
-b test ^
-n localhost ^
-z 27017 ^
-a Timestamp_test_to ^
-u "informix" ^
-p "test_pwd" ^
-d "test" ^
-s "ol_s_121414_204157" ^
-Z "C:\Program Files (x86)\IBM Informix Software Bundle\bin"