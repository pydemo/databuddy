::Test name: Oracle11g_JSON Table
	::Description:	Copy Oracle11g table into InformixInnovatorCTable.
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
::	-j[--from_user] is "Oracle 11g source user."
::	-x[--from_passwd] is "Oracle 11g source user password."
::	-b[--from_db_name] is "Oracle 11g source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-a[--to_table] is "Target Informix Innovator C table."
::	-u[--to_user] is "Target Informix Innovator C db user."
::	-p[--to_passwd] is "Target Informix Innovator C db user password."
::	-d[--to_db_name] is "Target Informix Innovator C database."
::	-s[--to_db_server] is "Target Informix Innovator C db instance name."
::	-Z[--target_client_home] is "Path to Informix Innovator C client home bin dir."	
	
echo y|C:\Python27\qc_dist_32\20150616_074308\qc32\qc32.exe ^
-w ora11g-inforc ^
-o 1 ^
-r 1 ^
-t "," ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150616_074334_019000 ^
-5 ".\config\host_map_v2.py" ^
-6 json ^
-c SCOTT.Timestamp_test_from ^
-j SCOTT ^
-x tiger ^
-b orcl ^
-e "MM/DD/YYYY" ^
-m "YYYY-MM-DD HH24:MI:SS.FF2" ^
-O "YYYY-MM-DD HH24:MI:SS.FF2" ^
-a Timestamp_test_to ^
-u "informix" ^
-p "infor_pwd" ^
-d "test" ^
-s "ol_s_121414_204157" ^
-Z "C:\Program Files (x86)\IBM Informix Software Bundle\bin"