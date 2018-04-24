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
::-Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
::-j[--from_user] is "SQL Server Express source user."
::-x[--from_passwd] is "SQL Server Express source user password."
::-b[--from_db_name] is "SQL Server Express source database."
::-n[--from_db_server] is "SQL Server Express source instance name."
::-z[--source_client_home] is "Path to SQL Server Express client home."
::-u[--to_user] is "Target MySQL db user."
::-p[--to_passwd] is "Target db user password."
::-d[--to_db_name] is "Target database."
::-s[--to_db_server] is "Target db instance name."
::-a[--to_table] is "Target table."
::-Z[--target_client_home] is "Path to mysql client home."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160527_194131\qc32\qc32.exe ^
-w SSEXP-MYSQL ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 25 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160527_194141_218000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_ss ^
-j sa ^
-x 198Morgan ^
-b master ^
-n ALEX_BUZ-PC\SQLEXPRESS ^
-z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
-u alex ^
-p mysql_pwd ^
-d test ^
-s localhost ^
-a Timestamp_test_to ^
-Z "C:\Temp\mysql\bin"