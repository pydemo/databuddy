
	::Test vector: From PGRES_DateTable to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_487000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Date_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_DateTable to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_560000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Date_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_DateTable to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_637000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Date_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_DateTable.csv
	::Test vector: From PGRES_Table to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_721000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_Table to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_789000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Table to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_865000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_Table.csv
	::Test vector: From PGRES_QueryFile to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000207_949000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_QueryFile to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_021000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_QueryFile to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_098000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_QueryFile.csv
	::Test vector: From PGRES_Table_Limit15 to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_173000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_Table_Limit15 to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_250000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Table_Limit15 to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_323000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_Table_Limit15.csv
	::Test vector: From PGRES_QueryDir to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_399000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_QueryDir to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_487000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_QueryDir_Limit12 to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 12 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_562000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_QueryDir_Limit12 to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 12 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_677000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_QueryDir_Limit12 to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 12 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_766000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_QueryDir_Limit12.csv
	::Test vector: From PGRES_ShardedPartition to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_835000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_ShardedPartition to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_909000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_TimestampTable to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000208_997000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_TimestampTable to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_069000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_TimestampTable to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_144000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_TimestampTable.csv
	::Test vector: From PGRES_QueryFile_Limit11 to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 11 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_219000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_QueryFile_Limit11 to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 11 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_305000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_QueryFile_Limit11 to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 11 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_375000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_QueryFile_Limit11.csv
	::Test vector: From PGRES_ShardedQueryFile to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_452000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_ShardedQueryFile to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_554000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_ParallelQueryDir to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 3 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_637000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_ParallelQueryDir to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 3 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_708000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Partition_Limit33 to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_790000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_Partition_Limit33 to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_859000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Partition_Limit33 to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000209_939000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_Partition_Limit33.csv
	::Test vector: From PGRES_TimezoneTable to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_018000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timezone_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_TimezoneTable to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_092000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timezone_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_TimezoneTable to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_167000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timezone_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_TimezoneTable.csv
	::Test vector: From PGRES_ShardedTable to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_241000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_ShardedTable to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_317000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Partition to CSV_Dir
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-D[--to_dir] is "To directory."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_394000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-D C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT
	::Test vector: From PGRES_Partition to CSV_Default
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_477000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434
	::Test vector: From PGRES_Partition to CSV_File
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-CSV ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_551000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-g C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\CSV_OUT\testPGRES_Partition.csv
	::Test vector: From PGRES_DateTable to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_632000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Date_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_DateTable to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_719000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Date_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_Table_KeepSpoolFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_805000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_Table_KeepSpoolFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_892000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_Table to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000210_975000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_Table to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_066000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_QueryFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_148000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_QueryFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_234000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_Table_Limit15 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_323000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_Table_Limit15 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 15 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_407000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_QueryDir to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_490000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_QueryDir to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_574000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_QueryDir_Limit12 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 12 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_659000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_QueryDir_Limit12 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 12 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_756000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_ShardedPartition to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_839000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_ShardedPartition to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000211_923000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_TimestampTable to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_041000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_TimestampTable to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_126000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_QueryFile_Limit11 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 11 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_216000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_QueryFile_Limit11 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 11 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_302000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_ShardedQueryFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_398000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_ShardedQueryFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-q[--query_sql_file] is "Input file with PostgreSQL query sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_482000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\postgre_query.sql ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_ParallelQueryDir to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 3 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_565000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_ParallelQueryDir to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-Q[--query_sql_dir] is "Input dir with PostgreSQL query files sql."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 3 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_650000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-Q C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc32\test\v101\query\query_dir_pgres ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_Partition_Limit33 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_734000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_Partition_Limit33 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 33 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_820000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_TimezoneTable to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_907000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timezone_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timezone_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_TimezoneTable to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000212_990000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timezone_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timezone_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_ShardedTable to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000213_076000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_ShardedTable to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000213_161000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Timestamp_test_from ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From PGRES_Partition to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000213_244000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From PGRES_Partition to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-6[--spool_type] is "Spool file type (CSV or JSON)."
::	-dbg[--debug_level] is "QC Debug level."
::	-c[--from_table] is "From table."
::	-P[--from_any_partition] is "From partition."
::	-j[--from_user] is "PostgreSQL source user."
::	-x[--from_passwd] is "PostgreSQL source user password."
::	-b[--from_db_name] is "PostgreSQL source database."
::	-n[--from_db_server] is "PostgreSQL source instance name."
::	-z[--source_client_home] is "Path to PostgreSQL client home."
::	-R[--source_port] is "Connection port for source PostgreSQL."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w PGRES-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20160528_000213_332000 ^
-5 ".\config\host_map\host_map.py" ^
-6 csv ^
-dbg 1 ^
-c Partitioned_test_from ^
-P Partitioned_test_from_2014 ^
-j "postgres" ^
-x "postgre_pwd" ^
-b "postgres" ^
-n "localhost" ^
-z "C:\Program Files\PostgreSQL\9.4\bin" ^
-R 5434 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_Dirs to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_431000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_Dirs to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_499000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_580000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_651000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_Dirs_Limit10 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_722000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_Dirs_Limit10 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_794000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_File_TableNamedFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_869000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i ".\test\v101\data\SCOTT.Timestamp_test_to.data" ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_File_TableNamedFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000213_949000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i ".\test\v101\data\SCOTT.Timestamp_test_to.data" ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_File_Limit10 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_054000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_File_Limit10 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_130000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedFileSkip1 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_205000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedFileSkip1 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_284000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_DateFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_359000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_dt.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_DateFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_427000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_dt.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_TimestampFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_499000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_TimestampFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_582000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_TimezoneFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_654000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_tz.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timezone_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_TimezoneFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_726000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_tz.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timezone_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_Files_TableNamedFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_794000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i ".\test\v101\data\SCOTT.Timestamp_test_to.data",".\test\v101\data\SCOTT.Timestamp_test_to_2.data" ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_Files_TableNamedFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_869000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i ".\test\v101\data\SCOTT.Timestamp_test_to.data",".\test\v101\data\SCOTT.Timestamp_test_to_2.data" ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_Dir to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000214_945000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_Dir to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_012000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedDir_Limit10 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_084000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedDir_Limit10 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_167000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_FileSkip1 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_241000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_FileSkip1 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_314000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedDirSkip1 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_388000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedDirSkip1 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_463000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_File to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_541000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_File to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_615000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_DateFiles to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_700000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_dt.data,.\test\v101\data\pgres_shard_0_dt.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_DateFiles to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_770000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_dt.data,.\test\v101\data\pgres_shard_0_dt.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Date_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_MongoFile to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_840000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\oracle_shard_0_mongo.csv ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_MongoFile to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_915000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\oracle_shard_0_mongo.csv ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedFile_Limit10 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000215_988000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedFile_Limit10 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-i[--input_files] is "Input CSV file(s)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000216_075000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-i .\test\v101\data\pgres_shard_0_ts.data ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_ShardedDir to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000216_151000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_ShardedDir to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 3 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000216_225000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434
	::Test vector: From CSV_DirsSkip1 to PGRES_Table_SkipHeader
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."
::	-k[--skip_header] is "Skip header line."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000216_304000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434 ^
-k 1
	::Test vector: From CSV_DirsSkip1 to PGRES_Table
	::	Arguments:
	::		-w[--copy_vector] is "Data copy direction."
::	-ps[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-5[--host_map] is "Host-to-shard map."
::	-dbg[--debug_level] is "QC Debug level."
::	-I[--input_dirs] is "Input CSV directory."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target PostgreSQL db user."
::	-p[--to_passwd] is "Target PostgreSQL db user password."
::	-d[--to_db_name] is "Target PostgreSQL database."
::	-s[--to_db_server] is "Target PostgreSQL db instance name."
::	-a[--to_table] is "Target PostgreSQL table."
::	-Z[--target_client_home] is "Path to PostgreSQL client home bin dir."
::	-T[--target_port] is "Connection port for target PostgreSQL."	
	
echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources\qc_dist_32\20160528_000207\qc32\qc32.exe ^
-w CSV-PGRES ^
-ps 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20160528_000216_380000 ^
-5 ".\config\host_map\host_map.py" ^
-dbg 1 ^
-I .\test\v101\data\pgres_data_dir ^
-y 1 ^
-u "postgres" ^
-p "postgre_pwd" ^
-d "postgres" ^
-s "localhost" ^
-a "Timestamp_test_to" ^
-Z "C:\Program Files\PostgreSQL\9.4\bin" ^
-T 5434