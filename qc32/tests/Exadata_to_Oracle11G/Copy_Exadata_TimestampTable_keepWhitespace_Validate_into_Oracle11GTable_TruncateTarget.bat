::Test name: Exadata_TimestampTable keepWhitespace Validate
	::Description:	Copy Exadata table into Oracle11GTable TruncateTarget.
	::Arguments:
	::	-w[--copy_vector] is "Data copy direction."
::	-o[--pool_size] is "Pool size."
::	-r[--num_of_shards] is "Number of shards."
::	-t[--field_term] is "Field terminator."
::	-V[--validate] is "Check if source and target objects exist."
::	-U[--truncate_target] is "Truncate target table/partition/subpartition."
::	-L[--email_to] is "Email job status."
::	-M[--log_dir] is "Log destination."
::	-F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
::	-B[--job_name] is "Job name (log_dir/job_name)."
::	-Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
::	-c[--from_table] is "From table."
::	-j[--from_user] is "Exadata source user."
::	-x[--from_passwd] is "Exadata source user password."
::	-b[--from_db_name] is "Exadata source database."
::	-e[--nls_date_format] is "nls_date_format for source."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for source."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
::	-z[--source_client_home] is "Path to Exadata client home."
::	-W[--keep_whitespace] is "Keep whitespace from CHAR type in "Exadata" extract."
::	-u[--to_user] is "Target Oracle 11G db user."
::	-p[--to_passwd] is "Oracle 11G user password."
::	-d[--to_db_name] is "Oracle 11G database."
::	-a[--to_table] is "To Oracle table."
::	-e[--nls_date_format] is "nls_date_format for target."
::	-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::	-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::	-Z[--target_client_home] is "Path to Oracle 11G client home bin dir."	
	
python -c "print 'y\ny'" |C:\Python27\qc_dist_32\20150309_175212\qc32\qc32.exe ^
-w oraexa2ora11g ^
-o 1 ^
-r 1 ^
-t "|" ^
-V 1 ^
-U 1 ^
-L alex_buz@yahoo.com;alexbuzunov@gmail.com ^
-M C:\Temp\qc_log ^
-F C:\tmp\TEST_default_spool ^
-B qc_job ^
-Y 20150309_175212_835000 ^
-c SCOTT.Timestamp_test_from ^
-j SCOTT ^
-x tiger2 ^
-b orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-W 1 ^
-u SCOTT ^
-p tiger2 ^
-d orcl ^
-a SCOTT.Timestamp_test_to ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"