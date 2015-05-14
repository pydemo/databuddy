##
##qc32.exe -h ALL 

Press any key to continue . . . 
----------------------------------------------------------------------
QueryCopy for SQL Server Express (v0.3.3, beta, 2015/05/13 19:24:38) [32bit]
Copyright (c): 2014 Alex Buzunov, All rights reserved.
Agreement: Use this tool at your own risk. Author is not liable for any damages or losses related to the use of this software.
----------------------------------------------------------------------
Databases supported (1):
1. SQL Server Express

Data formats supported (2):
1. CSV
2. DDL

For detailed help use one of the options:

From SQL Server Express:

	To SQL Server Express  : qc32.exe -h ssexp2ssexp
	To CSV                 : qc32.exe -h ssexp2csv
	To DDL                 : qc32.exe -h ssexp2ddl

To SQL Server Express:

	From CSV               : qc32.exe -h csv2ssexp
	From DDL               : qc32.exe -h ddl2ssexp


--USE CASES--

1. CSV_to_SQLServerExpress. 15 use cases.
2. SQLServerExpress_to_CSV. 23 use cases.
3. SQLServerExpress_to_DDL. 29 use cases.
4. SQLServerExpress_to_SQLServerExpress. 10 use cases.


CSV_to_SQLServerExpress: 15 use case(s) available:

1. CSV_DateFile_to_SSEXP_Table - Load CSV file into SQLServerExpress Table table.
2. CSV_DateFiles_to_SSEXP_Table - Load CSV file into SQLServerExpress Table table.
3. CSV_DirsSkip1_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
4. CSV_Dirs_Limit10_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
5. CSV_Dirs_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Load CSV file into SQLServerExpress Table table.
6. CSV_FileSkip1_to_SSEXP_Table - Skip 1 rows and load CSV file into SQLServerExpress Table table.
7. CSV_File_Limit10_to_SSEXP_Table - Load only 10 rows from CSV file into SQLServerExpress Table table.
8. CSV_ShardedDirSkip1_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
9. CSV_ShardedDir_Limit10_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
10. CSV_ShardedDir_to_SSEXP_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into SQLServerExpress Table table.
11. CSV_ShardedFileSkip1_to_SSEXP_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
12. CSV_ShardedFile_Limit10_to_SSEXP_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
13. CSV_ShardedFile_to_SSEXP_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into SQLServerExpress Table table.
14. CSV_TimestampFile_to_SSEXP_Table - Load CSV file into SQLServerExpress Table table.
15. CSV_TimezoneFile_to_SSEXP_Table - Load CSV file into SQLServerExpress Table table.
SQLServerExpress_to_CSV: 23 use case(s) available:

16. SSEXP_QueryDir_Limit25_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV Default location.
17. SSEXP_QueryDir_Limit25_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV Dir location.
18. SSEXP_QueryDir_Limit25_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV File location.
19. SSEXP_QueryDir_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into CSV Default location.
20. SSEXP_QueryDir_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into CSV Dir location.
21. SSEXP_QueryFile_Limit15_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV Default location.
22. SSEXP_QueryFile_Limit15_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV Dir location.
23. SSEXP_QueryFile_Limit15_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV File location.
24. SSEXP_QueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV Default location.
25. SSEXP_QueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV Dir location.
26. SSEXP_QueryFile_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV File location.
27. SSEXP_ShardedQueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into CSV Default location.
28. SSEXP_ShardedQueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into CSV Dir location.
29. SSEXP_ShardedTable_Limit50_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into CSV Default location.
30. SSEXP_ShardedTable_Limit50_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into CSV Dir location.
31. SSEXP_ShardedTable_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into CSV Default location.
32. SSEXP_ShardedTable_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into CSV Dir location.
33. SSEXP_Table_Limit10_to_CSV_Default - Extract only 10 rows from SQLServerExpress table into CSV Default location.
34. SSEXP_Table_Limit10_to_CSV_Dir - Extract only 10 rows from SQLServerExpress table into CSV Dir location.
35. SSEXP_Table_Limit10_to_CSV_File - Extract only 10 rows from SQLServerExpress table into CSV File location.
36. SSEXP_Table_to_CSV_Default - Extract SQLServerExpress table into CSV Default location.
37. SSEXP_Table_to_CSV_Dir - Extract SQLServerExpress table into CSV Dir location.
38. SSEXP_Table_to_CSV_File - Extract SQLServerExpress table into CSV File location.
SQLServerExpress_to_DDL: 29 use case(s) available:

39. SSEXP_QueryDir_Limit25_to_DDL_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL Default table.
40. SSEXP_QueryDir_Limit25_to_DDL_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL Dir table.
41. SSEXP_QueryDir_Limit25_to_DDL_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL File table.
42. SSEXP_QueryDir_to_DDL_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into DDL Default table.
43. SSEXP_QueryDir_to_DDL_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into DDL Dir table.
44. SSEXP_QueryFile_Limit15_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL Default table.
45. SSEXP_QueryFile_Limit15_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL Dir table.
46. SSEXP_QueryFile_Limit15_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL File table.
47. SSEXP_QueryFile_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL Default table.
48. SSEXP_QueryFile_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL Dir table.
49. SSEXP_QueryFile_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL File table.
50. SSEXP_ShardedQueryFile_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL Default table.
51. SSEXP_ShardedQueryFile_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL Dir table.
52. SSEXP_ShardedQueryFile_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL File table.
53. SSEXP_ShardedTable_Limit50_to_DDL_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL Default table.
54. SSEXP_ShardedTable_Limit50_to_DDL_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL Dir table.
55. SSEXP_ShardedTable_Limit50_to_DDL_File - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL File table.
56. SSEXP_ShardedTable_to_DDL_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL Default table.
57. SSEXP_ShardedTable_to_DDL_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL Dir table.
58. SSEXP_ShardedTable_to_DDL_File - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL File table.
59. SSEXP_Table_KeepSpoolFile_to_DDL_Default - Extract SQLServerExpress table into DDL Default table.
60. SSEXP_Table_KeepSpoolFile_to_DDL_Dir - Extract SQLServerExpress table into DDL Dir table.
61. SSEXP_Table_KeepSpoolFile_to_DDL_File - Extract SQLServerExpress table into DDL File table.
62. SSEXP_Table_Limit10_to_DDL_Default - Extract only 10 rows from SQLServerExpress table into DDL Default table.
63. SSEXP_Table_Limit10_to_DDL_Dir - Extract only 10 rows from SQLServerExpress table into DDL Dir table.
64. SSEXP_Table_Limit10_to_DDL_File - Extract only 10 rows from SQLServerExpress table into DDL File table.
65. SSEXP_Table_to_DDL_Default - Extract SQLServerExpress table into DDL Default table.
66. SSEXP_Table_to_DDL_Dir - Extract SQLServerExpress table into DDL Dir table.
67. SSEXP_Table_to_DDL_File - Extract SQLServerExpress table into DDL File table.
SQLServerExpress_to_SQLServerExpress: 10 use case(s) available:

68. SSEXP_QueryDir_Limit25_to_SSEXP_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Copy only 25 rows from SQLServerExpress query results into SQLServerExpress Table table.
69. SSEXP_QueryDir_to_SSEXP_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
70. SSEXP_QueryFile_Limit15_to_SSEXP_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Copy only 15 rows from SQLServerExpress query results into SQLServerExpress Table table.
71. SSEXP_QueryFile_to_SSEXP_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
72. SSEXP_ShardedQueryFile_to_SSEXP_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
73. SSEXP_ShardedTable_Limit50_to_SSEXP_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 50 rows from SQLServerExpress table into SQLServerExpress Table table.
74. SSEXP_ShardedTable_to_SSEXP_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy SQLServerExpress table into SQLServerExpress Table table.
75. SSEXP_Table_KeepSpoolFile_to_SSEXP_Table - Copy SQLServerExpress table into SQLServerExpress Table table.
76. SSEXP_Table_Limit10_to_SSEXP_Table - Copy only 10 rows from SQLServerExpress table into SQLServerExpress Table table.
77. SSEXP_Table_to_SSEXP_Table - Copy SQLServerExpress table into SQLServerExpress Table table.

--DETAILS--

-USE-CASE # 1
Use case name: CSV_DateFile_to_SSEXP_Table
Description:  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_603000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 2
Use case name: CSV_DateFiles_to_SSEXP_Table
Description:  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_665000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data;C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 3
Use case name: CSV_DirsSkip1_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_712000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -k 1 ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 4
Use case name: CSV_Dirs_Limit10_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_571000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 5
Use case name: CSV_Dirs_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_540000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 6
Use case name: CSV_FileSkip1_to_SSEXP_Table
Description:  Skip 1 rows and load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_634000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -k 1 ^
  -y 100 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 7
Use case name: CSV_File_Limit10_to_SSEXP_Table
Description:  Load only 10 rows from CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_571000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 8
Use case name: CSV_ShardedDirSkip1_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_649000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -k 1 ^
  -y 50 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 9
Use case name: CSV_ShardedDir_Limit10_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_618000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -y 50 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 10
Use case name: CSV_ShardedDir_to_SSEXP_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -I[--input_dirs] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_696000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_data_dir ^
  -y 50 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 11
Use case name: CSV_ShardedFileSkip1_to_SSEXP_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_587000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -k 1 ^
  -y 10 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 12
Use case name: CSV_ShardedFile_Limit10_to_SSEXP_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_681000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 10 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 13
Use case name: CSV_ShardedFile_to_SSEXP_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_556000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 10 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 14
Use case name: CSV_TimestampFile_to_SSEXP_Table
Description:  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_696000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 15
Use case name: CSV_TimezoneFile_to_SSEXP_Table
Description:  Load CSV file into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -i[--input_files] is "Input CSV file(s)."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w csv2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150513_192439_618000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_ddl\test\v101\data\ss_shard_0.data ^
  -y 1000 ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 16
Use case name: SSEXP_QueryDir_Limit25_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_738000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 17
Use case name: SSEXP_QueryDir_Limit25_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_707000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 18
Use case name: SSEXP_QueryDir_Limit25_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_769000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\CSV_OUT\testSSEXP_QueryDir_Limit25.data

-USE-CASE # 19
Use case name: SSEXP_QueryDir_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_816000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 20
Use case name: SSEXP_QueryDir_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_800000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 21
Use case name: SSEXP_QueryFile_Limit15_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_007000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 22
Use case name: SSEXP_QueryFile_Limit15_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_995000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 23
Use case name: SSEXP_QueryFile_Limit15_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_019000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\CSV_OUT\testSSEXP_QueryFile_Limit15.data

-USE-CASE # 24
Use case name: SSEXP_QueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_831000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 25
Use case name: SSEXP_QueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_816000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 26
Use case name: SSEXP_QueryFile_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_847000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\CSV_OUT\testSSEXP_QueryFile.data

-USE-CASE # 27
Use case name: SSEXP_ShardedQueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_660000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 28
Use case name: SSEXP_ShardedQueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_644000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 29
Use case name: SSEXP_ShardedTable_Limit50_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_972000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 30
Use case name: SSEXP_ShardedTable_Limit50_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_956000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 31
Use case name: SSEXP_ShardedTable_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_909000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 32
Use case name: SSEXP_ShardedTable_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_894000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 33
Use case name: SSEXP_Table_Limit10_to_CSV_Default
Description:  Extract only 10 rows from SQLServerExpress table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_941000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 34
Use case name: SSEXP_Table_Limit10_to_CSV_Dir
Description:  Extract only 10 rows from SQLServerExpress table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_925000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 35
Use case name: SSEXP_Table_Limit10_to_CSV_File
Description:  Extract only 10 rows from SQLServerExpress table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_956000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\CSV_OUT\testSSEXP_Table_Limit10.data

-USE-CASE # 36
Use case name: SSEXP_Table_to_CSV_Default
Description:  Extract SQLServerExpress table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_878000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 37
Use case name: SSEXP_Table_to_CSV_Dir
Description:  Extract SQLServerExpress table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_863000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\CSV_OUT

-USE-CASE # 38
Use case name: SSEXP_Table_to_CSV_File
Description:  Extract SQLServerExpress table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192438_878000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\CSV_OUT\testSSEXP_Table.data

-USE-CASE # 39
Use case name: SSEXP_QueryDir_Limit25_to_DDL_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_071000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 40
Use case name: SSEXP_QueryDir_Limit25_to_DDL_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_087000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 41
Use case name: SSEXP_QueryDir_Limit25_to_DDL_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract only 25 rows from SQLServerExpress query results into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_071000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_QueryDir_Limit25.ddl

-USE-CASE # 42
Use case name: SSEXP_QueryDir_to_DDL_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_102000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 43
Use case name: SSEXP_QueryDir_to_DDL_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Extract SQLServerExpress query results into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_118000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 44
Use case name: SSEXP_QueryFile_Limit15_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_368000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 45
Use case name: SSEXP_QueryFile_Limit15_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_383000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 46
Use case name: SSEXP_QueryFile_Limit15_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract only 15 rows from SQLServerExpress query results into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_352000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_QueryFile_Limit15.ddl

-USE-CASE # 47
Use case name: SSEXP_QueryFile_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_149000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 48
Use case name: SSEXP_QueryFile_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_149000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 49
Use case name: SSEXP_QueryFile_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Extract SQLServerExpress query results into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_134000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_QueryFile.ddl

-USE-CASE # 50
Use case name: SSEXP_ShardedQueryFile_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_040000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 51
Use case name: SSEXP_ShardedQueryFile_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_056000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 52
Use case name: SSEXP_ShardedQueryFile_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress query results into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_024000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_ShardedQueryFile.ddl

-USE-CASE # 53
Use case name: SSEXP_ShardedTable_Limit50_to_DDL_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_336000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 54
Use case name: SSEXP_ShardedTable_Limit50_to_DDL_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_336000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 55
Use case name: SSEXP_ShardedTable_Limit50_to_DDL_File
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 50 rows from SQLServerExpress table into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_321000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_ShardedTable_Limit50.ddl

-USE-CASE # 56
Use case name: SSEXP_ShardedTable_to_DDL_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_212000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 57
Use case name: SSEXP_ShardedTable_to_DDL_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_227000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 58
Use case name: SSEXP_ShardedTable_to_DDL_File
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract SQLServerExpress table into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_196000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_ShardedTable.ddl

-USE-CASE # 59
Use case name: SSEXP_Table_KeepSpoolFile_to_DDL_Default
Description:  Extract SQLServerExpress table into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_258000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 60
Use case name: SSEXP_Table_KeepSpoolFile_to_DDL_Dir
Description:  Extract SQLServerExpress table into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_274000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 61
Use case name: SSEXP_Table_KeepSpoolFile_to_DDL_File
Description:  Extract SQLServerExpress table into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_243000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_Table_KeepSpoolFile.ddl

-USE-CASE # 62
Use case name: SSEXP_Table_Limit10_to_DDL_Default
Description:  Extract only 10 rows from SQLServerExpress table into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_290000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 63
Use case name: SSEXP_Table_Limit10_to_DDL_Dir
Description:  Extract only 10 rows from SQLServerExpress table into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_305000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 64
Use case name: SSEXP_Table_Limit10_to_DDL_File
Description:  Extract only 10 rows from SQLServerExpress table into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_274000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_Table_Limit10.ddl

-USE-CASE # 65
Use case name: SSEXP_Table_to_DDL_Default
Description:  Extract SQLServerExpress table into DDL Default table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_180000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 66
Use case name: SSEXP_Table_to_DDL_Dir
Description:  Extract SQLServerExpress table into DDL Dir table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_196000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -D C:\Python27\data_migrator_1239_ddl\DDL_OUT

-USE-CASE # 67
Use case name: SSEXP_Table_to_DDL_File
Description:  Extract SQLServerExpress table into DDL File table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_165000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -g C:\Python27\data_migrator_1239_ddl\DDL_OUT\testSSEXP_Table.ddl

-USE-CASE # 68
Use case name: SSEXP_QueryDir_Limit25_to_SSEXP_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Copy only 25 rows from SQLServerExpress query results into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 25 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_414000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 69
Use case name: SSEXP_QueryDir_to_SSEXP_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss".
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -Q[--query_sql_dir] is "Input dir with SQL Server Express query sqls."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_430000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_ddl\test\v101\query\query_dir_ss ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 70
Use case name: SSEXP_QueryFile_Limit15_to_SSEXP_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Copy only 15 rows from SQLServerExpress query results into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 15 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_524000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 71
Use case name: SSEXP_QueryFile_to_SSEXP_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_446000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 72
Use case name: SSEXP_ShardedQueryFile_to_SSEXP_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql".
	  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy SQLServerExpress query results into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -q[--query_sql_file] is "Input file with SQL Server Express query sql."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_399000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_ddl\test\v101\query\ss_query.sql ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 73
Use case name: SSEXP_ShardedTable_Limit50_to_SSEXP_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 50 rows from SQLServerExpress table into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 50 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_508000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 74
Use case name: SSEXP_ShardedTable_to_SSEXP_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy SQLServerExpress table into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_461000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 75
Use case name: SSEXP_Table_KeepSpoolFile_to_SSEXP_Table
Description:  Copy SQLServerExpress table into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_477000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 76
Use case name: SSEXP_Table_Limit10_to_SSEXP_Table
Description:  Copy only 10 rows from SQLServerExpress table into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_492000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"

-USE-CASE # 77
Use case name: SSEXP_Table_to_SSEXP_Table
Description:  Copy SQLServerExpress table into SQLServerExpress Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -M[--log_dir] is "Log destination."
  -F[--default_spool_dir] is "Default data dump dir (default_spool_dir/job_name/timestamp)."
  -B[--job_name] is "Job name (log_dir/job_name)."
  -Y[--time_stamp] is "Timestamp (log_dir/job_name/timestamp)."
  -5[--host_map] is "Host-to-shard map."
  -c[--from_table] is "From table."
  -j[--from_user] is "SQL Server Express source user."
  -x[--from_passwd] is "SQL Server Express source user password."
  -b[--from_db_name] is "SQL Server Express source database."
  -n[--from_db_server] is "SQL Server Express source instance name."
  -z[--source_client_home] is "Path to SQL Server Express client home."
  -u[--to_user] is "Target SQL Server Express db user."
  -p[--to_passwd] is "SQL Server Express user password."
  -d[--to_db_name] is "SQL Server Express database."
  -s[--to_db_server] is "SQL Server Express instance name."
  -a[--to_table] is "To table."
  -Z[--target_client_home] is "Path to SQL Server Express client home bin dir."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150513_192438\qc32\qc32.exe ^
  -w ssexp2ssexp ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150513_192439_461000 ^
  -5 ".\config\host_map_v2.py" ^
  -c Timestamp_test_from ^
  -j sa ^
  -x test_pwd ^
  -b master ^
  -n ALEX_BUZ-PC\SQLEXPRESS ^
  -z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn" ^
  -u sa ^
  -p test_pwd ^
  -d master ^
  -s ALEX_BUZ-PC\SQLEXPRESS ^
  -a dbo.Timestamp_test_to ^
  -Z "C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn"