::Test name: Oracle11G_Table Limit10
	::Description:	Extract only 10 rows from Oracle11G table into CSVFile.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-l[--lame_duck] is "Limit rows (lame duck run)."
::	-L[--email_to] is "Email job status."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "Oracle 11G source user."
::	-x[--from_passwd] is "Oracle 11G source user password."
::	-b[--from_db_name] is "Oracle 11G source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-z[--source_client_home] is "Path to Oracle 11G client home."
::	-g[--to_file] is "To CSV file."	
	
echo y|C:\Python27\qc_dist_32\20150309_175212\qc32\qc32.exe ^
-w ora11g2csv ^
-o 1 ^
-r 1 ^
-t "|" ^
-l 10 ^
-L alex_buz@yahoo.com;alexbuzunov@gmail.com ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150309_175212_835000 ^
-c SCOTT.Timestamp_test_from ^
-j SCOTT ^
-x tiger2 ^
-b orcl ^
-e "YYYY/MM/DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-g C:\Python27\data_migrator_1239\CSV_OUT\testORA11G_Table_Limit10.data