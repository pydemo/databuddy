::Test name: CSV_DirsSkip1
	::Description:	Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_1;C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_2".Skip 1 rows and load CSV file into Oracle11GTable.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-K[--keep_data_file] is "Keep data dump."
::	-M[--log_dir] is "Log destination."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-C[--loader_profile] is "SQL*Loader profile (user defined)."
::	-5[--host_map] is "Host-to-shard map."
::	-I[--input_dirs] is "Input CSV directory."
::	-k[--skip_rows] is "Header size. Number of rows to skip in input file."
::	-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::	-u[--to_user] is "Target Oracle 11G db user."
::	-p[--to_passwd] is "Oracle 11G user password."
::	-d[--to_db_name] is "Oracle 11G database."
::	-a[--to_table] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."	
	
echo y|C:\Python27\qc_dist_32\20150513_194648\qc32\qc32.exe ^
-w csv2ora11g ^
-o 1 ^
-r 1 ^
-t "|" ^
-K 1 ^
-M C:\Temp\qc_log ^
-B qc_job ^
-Y 20150513_194705_196000 ^
-C "C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml" ^
-5 ".\config\host_map_v2.py" ^
-I C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_1;C:\Python27\data_migrator_1239_ddl\test\v101\data\ora_data_dir_2 ^
-k 1 ^
-y 1000 ^
-u SCOTT ^
-p tiger ^
-d orcl ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"