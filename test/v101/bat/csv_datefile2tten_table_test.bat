::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::-w[--copy_vector] is "Data copy direction."
::-o[--pool_size] is "Pool size."
::-r[--num_of_shards] is "Number of shards."
::-t[--field_term] is "Field terminator."
::-i[--input_file] is "Input CSV file."
::-y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
::-a[--to_table] is "Target TimesTen table."
::-u[--to_user] is "Target TimesTen db user."
::-p[--to_passwd] is "Target TimesTen db user password."
::-d[--to_DSN_name] is "Target TimesTen database."
::-e[--nls_date_format] is "nls_date_format for target."
::-m[--nls_timestamp_format] is "nls_timestamp_format for target."
::-O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
::-Z[--target_client_home] is "Path to TimesTen client home bin dir."
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
echo y|c:\Python27\qc_dist_32\20150207_115904\qc32\qc32.exe ^
-w csv2tten ^
-o 1 ^
-r 1 ^
-t "|" ^
-i c:\Python27\data_migrator_1239\test\v101\data\tt_shard_0.data ^
-y 1000 ^
-a TERRY.Timestamp_test_to ^
-u TERRY ^
-p secret ^
-d my_ttdb ^
-e "YYYY-MM-DD" ^
-m "YYYY-MM-DD-HH24.MI.SS.FF" ^
-O "YYYY-MM-DD-HH24:MI:SS.FF" ^
-Z "C:\Program Files (x86)\TimesTen\tt1122_64\bin"