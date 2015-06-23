##
##qc32.exe -h ALL 

Press any key to continue . . . 
----------------------------------------------------------------------
QueryCopy for MySQL (v0.3.3, beta, 2015/05/14 12:46:22) [32bit]
Copyright (c): 2014 Alex Buzunov, All rights reserved.
Agreement: Use this tool at your own risk. Author is not liable for any damages or losses related to the use of this software.
----------------------------------------------------------------------
Databases supported (1):
1. MySQL

Data formats supported (2):
1. CSV
2. DDL

For detailed help use one of the options:

From MySQL:

	To MySQL               : qc32.exe -h mysql2mysql
	To CSV                 : qc32.exe -h mysql2csv
	To DDL                 : qc32.exe -h mysql2ddl

To MySQL:

	From CSV               : qc32.exe -h csv2mysql
	From DDL               : qc32.exe -h ddl2mysql


--USE CASES--

1. CSV_to_MySQL. 15 use cases.
2. MySQL_to_CSV. 40 use cases.
3. MySQL_to_DDL. 47 use cases.
4. MySQL_to_MySQL. 16 use cases.


CSV_to_MySQL: 15 use case(s) available:

1. CSV_DateFile_to_MYSQL_Table - Load CSV file into MySQL Table table.
2. CSV_DateFiles_to_MYSQL_Table - Load CSV file into MySQL Table table.
3. CSV_DirsSkip1_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Skip 1 rows and load CSV file into MySQL Table table.
4. CSV_Dirs_Limit10_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Load only 10 rows from CSV file into MySQL Table table.
5. CSV_Dirs_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Load CSV file into MySQL Table table.
6. CSV_FileSkip1_to_MYSQL_Table - Skip 1 rows and load CSV file into MySQL Table table.
7. CSV_File_Limit10_to_MYSQL_Table - Load only 10 rows from CSV file into MySQL Table table.
8. CSV_ShardedDirSkip1_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into MySQL Table table.
9. CSV_ShardedDir_Limit10_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into MySQL Table table.
10. CSV_ShardedDir_to_MYSQL_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into MySQL Table table.
11. CSV_ShardedFileSkip1_to_MYSQL_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into MySQL Table table.
12. CSV_ShardedFile_Limit10_to_MYSQL_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into MySQL Table table.
13. CSV_ShardedFile_to_MYSQL_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into MySQL Table table.
14. CSV_TimestampFile_to_MYSQL_Table - Load CSV file into MySQL Table table.
15. CSV_TimezoneFile_to_MYSQL_Table - Load CSV file into MySQL Table table.
MySQL_to_CSV: 40 use case(s) available:

16. MYSQL_Partition_Limit22_to_CSV_Default - Extract only 22 rows from MySQL partition into CSV Default location.
17. MYSQL_Partition_Limit22_to_CSV_Dir - Extract only 22 rows from MySQL partition into CSV Dir location.
18. MYSQL_Partition_Limit22_to_CSV_File - Extract only 22 rows from MySQL partition into CSV File location.
19. MYSQL_Partition_to_CSV_Default - Extract MySQL partition into CSV Default location.
20. MYSQL_Partition_to_CSV_Dir - Extract MySQL partition into CSV Dir location.
21. MYSQL_Partition_to_CSV_File - Extract MySQL partition into CSV File location.
22. MYSQL_QueryDir_Limit333_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV Default location.
23. MYSQL_QueryDir_Limit333_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV Dir location.
24. MYSQL_QueryDir_Limit333_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV File location.
25. MYSQL_QueryDir_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into CSV Default location.
26. MYSQL_QueryDir_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into CSV Dir location.
27. MYSQL_QueryFile_Limit100_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV Default location.
28. MYSQL_QueryFile_Limit100_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV Dir location.
29. MYSQL_QueryFile_Limit100_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV File location.
30. MYSQL_QueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Default location.
31. MYSQL_QueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Dir location.
32. MYSQL_QueryFile_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV File location.
33. MYSQL_ShardedPartition_to_CSV_Default - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into CSV Default location.
34. MYSQL_ShardedPartition_to_CSV_Dir - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into CSV Dir location.
35. MYSQL_ShardedQuery_to_CSV_Default - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into CSV Default location.
36. MYSQL_ShardedQuery_to_CSV_Dir - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into CSV Dir location.
37. MYSQL_ShardedSubpartition_to_CSV_Default - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into CSV Default location.
38. MYSQL_ShardedSubpartition_to_CSV_Dir - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into CSV Dir location.
39. MYSQL_ShardedTable_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into CSV Default location.
40. MYSQL_ShardedTable_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into CSV Dir location.
41. MYSQL_Subpartition_Limit33_to_CSV_Default - Extract only 33 rows from MySQL sub-partition into CSV Default location.
42. MYSQL_Subpartition_Limit33_to_CSV_Dir - Extract only 33 rows from MySQL sub-partition into CSV Dir location.
43. MYSQL_Subpartition_Limit33_to_CSV_File - Extract only 33 rows from MySQL sub-partition into CSV File location.
44. MYSQL_Subpartition_to_CSV_Default - Extract MySQL sub-partition into CSV Default location.
45. MYSQL_Subpartition_to_CSV_Dir - Extract MySQL sub-partition into CSV Dir location.
46. MYSQL_Subpartition_to_CSV_File - Extract MySQL sub-partition into CSV File location.
47. MYSQL_Table_Limit1000_to_CSV_Default - Extract only 1000 rows from MySQL table into CSV Default location.
48. MYSQL_Table_Limit1000_to_CSV_Dir - Extract only 1000 rows from MySQL table into CSV Dir location.
49. MYSQL_Table_Limit1000_to_CSV_File - Extract only 1000 rows from MySQL table into CSV File location.
50. MYSQL_Table_to_CSV_Default - Extract MySQL table into CSV Default location.
51. MYSQL_Table_to_CSV_Dir - Extract MySQL table into CSV Dir location.
52. MYSQL_Table_to_CSV_File - Extract MySQL table into CSV File location.
53. MYSQL_TimezoneQueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Default location.
54. MYSQL_TimezoneQueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Dir location.
55. MYSQL_TimezoneQueryFile_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV File location.
MySQL_to_DDL: 47 use case(s) available:

56. MYSQL_Partition_Limit22_to_DDL_Default - Extract only 22 rows from MySQL partition into DDL Default table.
57. MYSQL_Partition_Limit22_to_DDL_Dir - Extract only 22 rows from MySQL partition into DDL Dir table.
58. MYSQL_Partition_Limit22_to_DDL_File - Extract only 22 rows from MySQL partition into DDL File table.
59. MYSQL_Partition_to_DDL_Default - Extract MySQL partition into DDL Default table.
60. MYSQL_Partition_to_DDL_Dir - Extract MySQL partition into DDL Dir table.
61. MYSQL_Partition_to_DDL_File - Extract MySQL partition into DDL File table.
62. MYSQL_QueryDir_Limit333_to_DDL_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL Default table.
63. MYSQL_QueryDir_Limit333_to_DDL_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL Dir table.
64. MYSQL_QueryDir_Limit333_to_DDL_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL File table.
65. MYSQL_QueryDir_to_DDL_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into DDL Default table.
66. MYSQL_QueryDir_to_DDL_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into DDL Dir table.
67. MYSQL_QueryFile_Limit100_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL Default table.
68. MYSQL_QueryFile_Limit100_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL Dir table.
69. MYSQL_QueryFile_Limit100_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL File table.
70. MYSQL_QueryFile_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Default table.
71. MYSQL_QueryFile_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Dir table.
72. MYSQL_QueryFile_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL File table.
73. MYSQL_ShardedPartition_to_DDL_Default - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL Default table.
74. MYSQL_ShardedPartition_to_DDL_Dir - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL Dir table.
75. MYSQL_ShardedPartition_to_DDL_File - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL File table.
76. MYSQL_ShardedQuery_to_DDL_Default - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL Default table.
77. MYSQL_ShardedQuery_to_DDL_Dir - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL Dir table.
78. MYSQL_ShardedQuery_to_DDL_File - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL File table.
79. MYSQL_ShardedSubpartition_to_DDL_Default - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL Default table.
80. MYSQL_ShardedSubpartition_to_DDL_Dir - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL Dir table.
81. MYSQL_ShardedSubpartition_to_DDL_File - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL File table.
82. MYSQL_ShardedTable_to_DDL_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL Default table.
83. MYSQL_ShardedTable_to_DDL_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL Dir table.
84. MYSQL_ShardedTable_to_DDL_File - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL File table.
85. MYSQL_Subpartition_Limit33_to_DDL_Default - Extract only 33 rows from MySQL sub-partition into DDL Default table.
86. MYSQL_Subpartition_Limit33_to_DDL_Dir - Extract only 33 rows from MySQL sub-partition into DDL Dir table.
87. MYSQL_Subpartition_Limit33_to_DDL_File - Extract only 33 rows from MySQL sub-partition into DDL File table.
88. MYSQL_Subpartition_to_DDL_Default - Extract MySQL sub-partition into DDL Default table.
89. MYSQL_Subpartition_to_DDL_Dir - Extract MySQL sub-partition into DDL Dir table.
90. MYSQL_Subpartition_to_DDL_File - Extract MySQL sub-partition into DDL File table.
91. MYSQL_Table_KeepSpoolFile_to_DDL_Default - Extract MySQL table into DDL Default table.
92. MYSQL_Table_KeepSpoolFile_to_DDL_Dir - Extract MySQL table into DDL Dir table.
93. MYSQL_Table_KeepSpoolFile_to_DDL_File - Extract MySQL table into DDL File table.
94. MYSQL_Table_Limit1000_to_DDL_Default - Extract only 1000 rows from MySQL table into DDL Default table.
95. MYSQL_Table_Limit1000_to_DDL_Dir - Extract only 1000 rows from MySQL table into DDL Dir table.
96. MYSQL_Table_Limit1000_to_DDL_File - Extract only 1000 rows from MySQL table into DDL File table.
97. MYSQL_Table_to_DDL_Default - Extract MySQL table into DDL Default table.
98. MYSQL_Table_to_DDL_Dir - Extract MySQL table into DDL Dir table.
99. MYSQL_Table_to_DDL_File - Extract MySQL table into DDL File table.
100. MYSQL_TimezoneQueryFile_to_DDL_Default - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Default table.
101. MYSQL_TimezoneQueryFile_to_DDL_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Dir table.
102. MYSQL_TimezoneQueryFile_to_DDL_File - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL File table.
MySQL_to_MySQL: 16 use case(s) available:

103. MYSQL_Partition_Limit22_to_MYSQL_Table - Copy only 22 rows from MySQL partition into MySQL Table table.
104. MYSQL_Partition_to_MYSQL_Table - Copy MySQL partition into MySQL Table table.
105. MYSQL_QueryDir_Limit333_to_MYSQL_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Copy only 333 rows from MySQL query results into MySQL Table table.
106. MYSQL_QueryDir_to_MYSQL_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Copy MySQL query results into MySQL Table table.
107. MYSQL_QueryFile_Limit100_to_MYSQL_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy only 100 rows from MySQL query results into MySQL Table table.
108. MYSQL_QueryFile_to_MYSQL_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy MySQL query results into MySQL Table table.
109. MYSQL_ShardedPartition_to_MYSQL_Table - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL sharded partition into MySQL Table table.
110. MYSQL_ShardedQuery_to_MYSQL_Table - Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL query results into MySQL Table table.
111. MYSQL_ShardedSubpartition_to_MYSQL_Table - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL sharded sub-partition into MySQL Table table.
112. MYSQL_ShardedTable_to_MYSQL_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL table into MySQL Table table.
113. MYSQL_Subpartition_Limit33_to_MYSQL_Table - Copy only 33 rows from MySQL sub-partition into MySQL Table table.
114. MYSQL_Subpartition_to_MYSQL_Table - Copy MySQL sub-partition into MySQL Table table.
115. MYSQL_Table_KeepSpoolFile_to_MYSQL_Table - Copy MySQL table into MySQL Table table.
116. MYSQL_Table_Limit1000_to_MYSQL_Table - Copy only 1000 rows from MySQL table into MySQL Table table.
117. MYSQL_Table_to_MYSQL_Table - Copy MySQL table into MySQL Table table.
118. MYSQL_TimezoneQueryFile_to_MYSQL_Table - Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy MySQL query results into MySQL Table table.

--DETAILS--

-USE-CASE # 1
Use case name: CSV_DateFile_to_MYSQL_Table
Description:  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_622000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 2
Use case name: CSV_DateFiles_to_MYSQL_Table
Description:  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_731000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data;C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 3
Use case name: CSV_DirsSkip1_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Skip 1 rows and load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_824000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -k 1 ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 4
Use case name: CSV_Dirs_Limit10_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Load only 10 rows from CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_559000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 5
Use case name: CSV_Dirs_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_512000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 6
Use case name: CSV_FileSkip1_to_MYSQL_Table
Description:  Skip 1 rows and load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_684000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -k 1 ^
  -y 100 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 7
Use case name: CSV_File_Limit10_to_MYSQL_Table
Description:  Load only 10 rows from CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_575000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 8
Use case name: CSV_ShardedDirSkip1_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_715000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -k 1 ^
  -y 50 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 9
Use case name: CSV_ShardedDir_Limit10_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_668000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -y 50 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 10
Use case name: CSV_ShardedDir_to_MYSQL_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_793000 ^
  -5 ".\config\host_map_v2.py" ^
  -I C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_data_dir ^
  -y 50 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 11
Use case name: CSV_ShardedFileSkip1_to_MYSQL_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_606000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -k 1 ^
  -y 10 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 12
Use case name: CSV_ShardedFile_Limit10_to_MYSQL_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_746000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 10 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 13
Use case name: CSV_ShardedFile_to_MYSQL_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_528000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 10 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 14
Use case name: CSV_TimestampFile_to_MYSQL_Table
Description:  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_778000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 15
Use case name: CSV_TimezoneFile_to_MYSQL_Table
Description:  Load CSV file into MySQL Table table.
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
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w csv-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -B qc_job ^
  -Y 20150514_124624_637000 ^
  -5 ".\config\host_map_v2.py" ^
  -i C:\Python27\data_migrator_1239_12c\test\v101\data\mysql_shard_0.data ^
  -y 1000 ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 16
Use case name: MYSQL_Partition_Limit22_to_CSV_Default
Description:  Extract only 22 rows from MySQL partition into CSV Default location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_871000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 17
Use case name: MYSQL_Partition_Limit22_to_CSV_Dir
Description:  Extract only 22 rows from MySQL partition into CSV Dir location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_840000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 18
Use case name: MYSQL_Partition_Limit22_to_CSV_File
Description:  Extract only 22 rows from MySQL partition into CSV File location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_887000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Partition_Limit22.data

-USE-CASE # 19
Use case name: MYSQL_Partition_to_CSV_Default
Description:  Extract MySQL partition into CSV Default location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_324000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 20
Use case name: MYSQL_Partition_to_CSV_Dir
Description:  Extract MySQL partition into CSV Dir location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_308000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 21
Use case name: MYSQL_Partition_to_CSV_File
Description:  Extract MySQL partition into CSV File location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_355000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Partition.data

-USE-CASE # 22
Use case name: MYSQL_QueryDir_Limit333_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV Default location.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_261000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 23
Use case name: MYSQL_QueryDir_Limit333_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV Dir location.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_230000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 24
Use case name: MYSQL_QueryDir_Limit333_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into CSV File location.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_277000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_QueryDir_Limit333.data

-USE-CASE # 25
Use case name: MYSQL_QueryDir_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into CSV Default location.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_651000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 26
Use case name: MYSQL_QueryDir_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into CSV Dir location.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_636000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 27
Use case name: MYSQL_QueryFile_Limit100_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV Default location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_934000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 28
Use case name: MYSQL_QueryFile_Limit100_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV Dir location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_918000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 29
Use case name: MYSQL_QueryFile_Limit100_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into CSV File location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_965000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_QueryFile_Limit100.data

-USE-CASE # 30
Use case name: MYSQL_QueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Default location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_699000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 31
Use case name: MYSQL_QueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Dir location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_683000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 32
Use case name: MYSQL_QueryFile_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV File location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_730000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_QueryFile.data

-USE-CASE # 33
Use case name: MYSQL_ShardedPartition_to_CSV_Default
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into CSV Default location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_090000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 34
Use case name: MYSQL_ShardedPartition_to_CSV_Dir
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into CSV Dir location.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_058000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 35
Use case name: MYSQL_ShardedQuery_to_CSV_Default
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into CSV Default location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_464000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 36
Use case name: MYSQL_ShardedQuery_to_CSV_Dir
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into CSV Dir location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_448000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 37
Use case name: MYSQL_ShardedSubpartition_to_CSV_Default
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into CSV Default location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_214000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 38
Use case name: MYSQL_ShardedSubpartition_to_CSV_Dir
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into CSV Dir location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_183000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 39
Use case name: MYSQL_ShardedTable_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into CSV Default location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_777000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 40
Use case name: MYSQL_ShardedTable_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into CSV Dir location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_746000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 41
Use case name: MYSQL_Subpartition_Limit33_to_CSV_Default
Description:  Extract only 33 rows from MySQL sub-partition into CSV Default location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_589000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 42
Use case name: MYSQL_Subpartition_Limit33_to_CSV_Dir
Description:  Extract only 33 rows from MySQL sub-partition into CSV Dir location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_558000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 43
Use case name: MYSQL_Subpartition_Limit33_to_CSV_File
Description:  Extract only 33 rows from MySQL sub-partition into CSV File location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_604000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Subpartition_Limit33.data

-USE-CASE # 44
Use case name: MYSQL_Subpartition_to_CSV_Default
Description:  Extract MySQL sub-partition into CSV Default location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_136000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 45
Use case name: MYSQL_Subpartition_to_CSV_Dir
Description:  Extract MySQL sub-partition into CSV Dir location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_105000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 46
Use case name: MYSQL_Subpartition_to_CSV_File
Description:  Extract MySQL sub-partition into CSV File location.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_152000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Subpartition.data

-USE-CASE # 47
Use case name: MYSQL_Table_Limit1000_to_CSV_Default
Description:  Extract only 1000 rows from MySQL table into CSV Default location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_012000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 48
Use case name: MYSQL_Table_Limit1000_to_CSV_Dir
Description:  Extract only 1000 rows from MySQL table into CSV Dir location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_996000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 49
Use case name: MYSQL_Table_Limit1000_to_CSV_File
Description:  Extract only 1000 rows from MySQL table into CSV File location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_043000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Table_Limit1000.data

-USE-CASE # 50
Use case name: MYSQL_Table_to_CSV_Default
Description:  Extract MySQL table into CSV Default location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_402000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 51
Use case name: MYSQL_Table_to_CSV_Dir
Description:  Extract MySQL table into CSV Dir location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_370000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 52
Use case name: MYSQL_Table_to_CSV_File
Description:  Extract MySQL table into CSV File location.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_417000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_Table.data

-USE-CASE # 53
Use case name: MYSQL_TimezoneQueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Default location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_511000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 54
Use case name: MYSQL_TimezoneQueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV Dir location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_495000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\CSV_OUT

-USE-CASE # 55
Use case name: MYSQL_TimezoneQueryFile_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into CSV File location.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124625_542000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\CSV_OUT\testMYSQL_TimezoneQueryFile.data

-USE-CASE # 56
Use case name: MYSQL_Partition_Limit22_to_DDL_Default
Description:  Extract only 22 rows from MySQL partition into DDL Default table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_026000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 57
Use case name: MYSQL_Partition_Limit22_to_DDL_Dir
Description:  Extract only 22 rows from MySQL partition into DDL Dir table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_058000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 58
Use case name: MYSQL_Partition_Limit22_to_DDL_File
Description:  Extract only 22 rows from MySQL partition into DDL File table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_011000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Partition_Limit22.ddl

-USE-CASE # 59
Use case name: MYSQL_Partition_to_DDL_Default
Description:  Extract MySQL partition into DDL Default table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_589000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 60
Use case name: MYSQL_Partition_to_DDL_Dir
Description:  Extract MySQL partition into DDL Dir table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_620000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 61
Use case name: MYSQL_Partition_to_DDL_File
Description:  Extract MySQL partition into DDL File table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_573000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Partition.ddl

-USE-CASE # 62
Use case name: MYSQL_QueryDir_Limit333_to_DDL_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL Default table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_449000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 63
Use case name: MYSQL_QueryDir_Limit333_to_DDL_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL Dir table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_480000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 64
Use case name: MYSQL_QueryDir_Limit333_to_DDL_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract only 333 rows from MySQL query results into DDL File table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_433000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_QueryDir_Limit333.ddl

-USE-CASE # 65
Use case name: MYSQL_QueryDir_to_DDL_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into DDL Default table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_919000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 66
Use case name: MYSQL_QueryDir_to_DDL_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Extract MySQL query results into DDL Dir table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_934000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 67
Use case name: MYSQL_QueryFile_Limit100_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL Default table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_104000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 68
Use case name: MYSQL_QueryFile_Limit100_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL Dir table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_120000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 69
Use case name: MYSQL_QueryFile_Limit100_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract only 100 rows from MySQL query results into DDL File table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_073000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_QueryFile_Limit100.ddl

-USE-CASE # 70
Use case name: MYSQL_QueryFile_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Default table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_997000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 71
Use case name: MYSQL_QueryFile_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Dir table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_012000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 72
Use case name: MYSQL_QueryFile_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL File table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_965000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_QueryFile.ddl

-USE-CASE # 73
Use case name: MYSQL_ShardedPartition_to_DDL_Default
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL Default table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_246000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 74
Use case name: MYSQL_ShardedPartition_to_DDL_Dir
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL Dir table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_277000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 75
Use case name: MYSQL_ShardedPartition_to_DDL_File
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded partition into DDL File table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_230000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_ShardedPartition.ddl

-USE-CASE # 76
Use case name: MYSQL_ShardedQuery_to_DDL_Default
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL Default table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_729000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 77
Use case name: MYSQL_ShardedQuery_to_DDL_Dir
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL Dir table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_761000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 78
Use case name: MYSQL_ShardedQuery_to_DDL_File
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL query results into DDL File table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_714000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_ShardedQuery.ddl

-USE-CASE # 79
Use case name: MYSQL_ShardedSubpartition_to_DDL_Default
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL Default table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_386000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 80
Use case name: MYSQL_ShardedSubpartition_to_DDL_Dir
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL Dir table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_402000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 81
Use case name: MYSQL_ShardedSubpartition_to_DDL_File
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL sharded sub-partition into DDL File table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_355000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_ShardedSubpartition.ddl

-USE-CASE # 82
Use case name: MYSQL_ShardedTable_to_DDL_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL Default table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_059000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 83
Use case name: MYSQL_ShardedTable_to_DDL_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL Dir table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_090000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 84
Use case name: MYSQL_ShardedTable_to_DDL_File
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Extract MySQL table into DDL File table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_043000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_ShardedTable.ddl

-USE-CASE # 85
Use case name: MYSQL_Subpartition_Limit33_to_DDL_Default
Description:  Extract only 33 rows from MySQL sub-partition into DDL Default table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_870000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 86
Use case name: MYSQL_Subpartition_Limit33_to_DDL_Dir
Description:  Extract only 33 rows from MySQL sub-partition into DDL Dir table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_885000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 87
Use case name: MYSQL_Subpartition_Limit33_to_DDL_File
Description:  Extract only 33 rows from MySQL sub-partition into DDL File table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_839000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Subpartition_Limit33.ddl

-USE-CASE # 88
Use case name: MYSQL_Subpartition_to_DDL_Default
Description:  Extract MySQL sub-partition into DDL Default table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_308000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 89
Use case name: MYSQL_Subpartition_to_DDL_Dir
Description:  Extract MySQL sub-partition into DDL Dir table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_339000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 90
Use case name: MYSQL_Subpartition_to_DDL_File
Description:  Extract MySQL sub-partition into DDL File table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_293000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Subpartition.ddl

-USE-CASE # 91
Use case name: MYSQL_Table_KeepSpoolFile_to_DDL_Default
Description:  Extract MySQL table into DDL Default table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_527000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 92
Use case name: MYSQL_Table_KeepSpoolFile_to_DDL_Dir
Description:  Extract MySQL table into DDL Dir table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_542000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 93
Use case name: MYSQL_Table_KeepSpoolFile_to_DDL_File
Description:  Extract MySQL table into DDL File table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_495000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Table_KeepSpoolFile.ddl

-USE-CASE # 94
Use case name: MYSQL_Table_Limit1000_to_DDL_Default
Description:  Extract only 1000 rows from MySQL table into DDL Default table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_182000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 95
Use case name: MYSQL_Table_Limit1000_to_DDL_Dir
Description:  Extract only 1000 rows from MySQL table into DDL Dir table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_198000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 96
Use case name: MYSQL_Table_Limit1000_to_DDL_File
Description:  Extract only 1000 rows from MySQL table into DDL File table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_151000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Table_Limit1000.ddl

-USE-CASE # 97
Use case name: MYSQL_Table_to_DDL_Default
Description:  Extract MySQL table into DDL Default table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_667000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 98
Use case name: MYSQL_Table_to_DDL_Dir
Description:  Extract MySQL table into DDL Dir table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_683000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 99
Use case name: MYSQL_Table_to_DDL_File
Description:  Extract MySQL table into DDL File table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_636000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_Table.ddl

-USE-CASE # 100
Use case name: MYSQL_TimezoneQueryFile_to_DDL_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Default table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_792000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin"

-USE-CASE # 101
Use case name: MYSQL_TimezoneQueryFile_to_DDL_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL Dir table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_823000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -D C:\Python27\data_migrator_1239_12c\DDL_OUT

-USE-CASE # 102
Use case name: MYSQL_TimezoneQueryFile_to_DDL_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Extract MySQL query results into DDL File table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -g[--to_file] is "To DDL file."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-ddl ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124623_776000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -g C:\Python27\data_migrator_1239_12c\DDL_OUT\testMYSQL_TimezoneQueryFile.ddl

-USE-CASE # 103
Use case name: MYSQL_Partition_Limit22_to_MYSQL_Table
Description:  Copy only 22 rows from MySQL partition into MySQL Table table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 22 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_106000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 104
Use case name: MYSQL_Partition_to_MYSQL_Table
Description:  Copy MySQL partition into MySQL Table table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_309000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 105
Use case name: MYSQL_QueryDir_Limit333_to_MYSQL_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Copy only 333 rows from MySQL query results into MySQL Table table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 333 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_262000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 106
Use case name: MYSQL_QueryDir_to_MYSQL_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql".
	  Copy MySQL query results into MySQL Table table.
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
  -Q[--query_sql_dir] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_433000 ^
  -5 ".\config\host_map_v2.py" ^
  -Q C:\Python27\data_migrator_1239_12c\test\v101\query\query_dir_mysql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 107
Use case name: MYSQL_QueryFile_Limit100_to_MYSQL_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy only 100 rows from MySQL query results into MySQL Table table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 100 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_137000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 108
Use case name: MYSQL_QueryFile_to_MYSQL_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy MySQL query results into MySQL Table table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_466000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 109
Use case name: MYSQL_ShardedPartition_to_MYSQL_Table
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL sharded partition into MySQL Table table.
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
  -P[--from_partition] is "From partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_184000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Partitioned_test_from ^
  -P rx2015 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 110
Use case name: MYSQL_ShardedQuery_to_MYSQL_Table
Description:  Break input query results into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL query results into MySQL Table table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_371000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 111
Use case name: MYSQL_ShardedSubpartition_to_MYSQL_Table
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL sharded sub-partition into MySQL Table table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_246000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 112
Use case name: MYSQL_ShardedTable_to_MYSQL_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy MySQL table into MySQL Table table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_481000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 113
Use case name: MYSQL_Subpartition_Limit33_to_MYSQL_Table
Description:  Copy only 33 rows from MySQL sub-partition into MySQL Table table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 33 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_418000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 114
Use case name: MYSQL_Subpartition_to_MYSQL_Table
Description:  Copy MySQL sub-partition into MySQL Table table.
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
  -S[--from_sub_partition] is "From sub-partition."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_215000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Sub_Partitioned_test_from ^
  -S subpart200 ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 115
Use case name: MYSQL_Table_KeepSpoolFile_to_MYSQL_Table
Description:  Copy MySQL table into MySQL Table table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_293000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 116
Use case name: MYSQL_Table_Limit1000_to_MYSQL_Table
Description:  Copy only 1000 rows from MySQL table into MySQL Table table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 1000 ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_168000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 117
Use case name: MYSQL_Table_to_MYSQL_Table
Description:  Copy MySQL table into MySQL Table table.
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
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_340000 ^
  -5 ".\config\host_map_v2.py" ^
  -c TEST.Timestamp_test_from ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"

-USE-CASE # 118
Use case name: MYSQL_TimezoneQueryFile_to_MYSQL_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql".
	  Copy MySQL query results into MySQL Table table.
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
  -q[--query_sql_file] is "Input file with MySQL query sql."
  -j[--from_user] is "MySQL source user."
  -x[--from_passwd] is "MySQL source user password."
  -b[--from_db_name] is "MySQL source database."
  -n[--from_db_server] is "MySQL source instance name."
  -z[--source_client_home] is "Path to MySQL client home."
  -u[--to_user] is "Target MySQL db user."
  -p[--to_passwd] is "Target db user password."
  -d[--to_db_name] is "Target database."
  -s[--to_db_server] is "Target db instance name."
  -a[--to_table] is "Target table."
  -Z[--target_client_home] is "Path to mysql client home."	
Example: 
  echo y|C:\Python27\qc_dist_32\20150514_124622\qc32\qc32.exe ^
  -w mysql-mysql ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -M C:\Temp\qc_log ^
  -F C:\tmp\TEST_default_spool ^
  -B qc_job ^
  -Y 20150514_124624_387000 ^
  -5 ".\config\host_map_v2.py" ^
  -q C:\Python27\data_migrator_1239_12c\test\v101\query\mysql_query.sql ^
  -j "alex" ^
  -x "mysql_pwd" ^
  -b "test" ^
  -n "localhost" ^
  -z "C:\Temp\mysql\bin" ^
  -u alex ^
  -p mysql_pwd ^
  -d test ^
  -s localhost ^
  -a Timestamp_test_to ^
  -Z "C:\Temp\mysql\bin"