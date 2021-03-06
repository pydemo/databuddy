::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-ps[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-l[--lame_duck] is "Limit rows (lame duck run)."
::-K[--keep_data_file] is "Keep data dump."
::-M[--log_dir] is "Log destination."
::-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::-B[--job_name] is "Job name (log_dir/job_name)."
::-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::-5[--host_map] is "Host-to-shard map."
::-6[--spool_type] is "Spool file type (CSV or JSON)."
::-dbg[--debug_level] is "QC Debug level."
::-q[--query_sql_file] is "Input file with SQL Server 2016 query sql."
::-j[--from_user] is "SQL Server 2016 source user."
::-x[--from_passwd] is "SQL Server 2016 source user password."
::-b[--from_db_name] is "SQL Server 2016 source database."
::-n[--from_db_server] is "SQL Server 2016 source instance name."
::-z[--source_client_home] is "Path to SQL Server 2016 client home."
::-u[--to_user] is "Target SQL Server Express db user."
::-p[--to_passwd] is "SQL Server Express user password."
::-d[--to_db_name] is "SQL Server Express database."
::-s[--to_db_server] is "SQL Server Express instance name."
::-a[--to_table] is "To table."
::-Z[--target_client_home] is "Path to SQL Server Express client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160527_194131\qc32\qc32.exe ^
-w SS2016-SSEXP ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160527_194132_306000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\ss_query.sql ^
-j sa ^
-x ssent_pwd ^
-b test ^
-n ALEX_BUZ-PC\MSSQLSERVER_ENT ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-u sa ^
-p 198Morgan ^
-d master ^
-s ALEX_BUZ-PC\SQLEXPRESS ^
-a dbo.Timestamp_test_to ^
-Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"