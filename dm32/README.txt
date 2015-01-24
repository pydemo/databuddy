##
##dm32.exe -h ALL 

----------------------------------------------------------------------
#FreeUkraine #SaveUkraine #StopRussia #PutinKhuilo #CrimeaIsUkraine
----------------------------------------------------------------------
DataMigrator for Oracle (v1.23.9, beta, 2015/01/12 05:14:20) [32bit]
Copyright (c): 2014 Alex Buzunov, All rights reserved.
Agreement: Use this tool at your own risk. Author is not liable for any damages or losses related to the use of this software.
----------------------------------------------------------------------
From Oracle:

Set following command line arguments to copy from Oracle to Oracle:

-w copy_vector -o pool_size -r num_of_shards -t field_term -l lame_duck -K keep_data_file -V validate -U truncate_target -E ask_to_truncate -1 arg_1 -2 arg_2 -3 arg_3 -q query_sql_file -Q query_sql_dir -c from_table -P from_partition -S from_sub_partition -f from_db -e nls_date_format -m nls_timestamp_format -O nls_timestamp_tz_format -z source_client_home -A header -W trim_whitespace -g to_db -a to_table -G to_partition -N to_sub_partition -Z target_client_home 

Here:
(Common) -w [--copy_vector]	Data copy direction.	
(Common) -o [--pool_size]	Pool size.	
(Common) -r [--num_of_shards]	Number of shards.	
(Common) -t [--field_term]	Field terminator.	
(Common) -l [--lame_duck]	Limit rows (lame duck run).	
(Common) -K [--keep_data_file]	Keep data dump.	
(Common) -V [--validate]	Check if source and target objects exist.	
(Common) -U [--truncate_target]	Truncate target table/partition/subpartition.	
(Common) -E [--ask_to_truncate]	Ask to truncate.	
(Common) -1 [--arg_1]	Generic string argument 1.	
(Common) -2 [--arg_2]	Generic string argument 2.	
(Common) -3 [--arg_3]	Generic string argument 3.	
(From Oracle) -q [--query_sql_file]	Input file with Oracle query sql.	
(From Oracle) -Q [--query_sql_dir]	Input dir with Oracle query files sql.	
(From Oracle) -c [--from_table]	From table.	
(From Oracle) -P [--from_partition]	From partition.	
(From Oracle) -S [--from_sub_partition]	From sub-partition.	
(From Oracle) -f [--from_db]	From database.	
(From Oracle) -e [--nls_date_format]	nls_date_format for source.	
(From Oracle) -m [--nls_timestamp_format]	nls_timestamp_format for source.	
(From Oracle) -O [--nls_timestamp_tz_format]	nls_timestamp_tz_format for source.	
(From Oracle) -z [--source_client_home]	Path to Oracle client home.	
(From Oracle) -A [--header]	Include header to Oracle extract.	
(From Oracle) -W [--trim_whitespace]	Trim whitespace from varchar2 in "Oracle" extract.	
(To Oracle) -g [--to_db]	To Oracle database.	
(To Oracle) -a [--to_table]	To Oracle table.	
(To Oracle) -G [--to_partition]	To Oracle table.	
(To Oracle) -N [--to_sub_partition]	To Oracle table.	
(To Oracle) -Z [--target_client_home]	Path to Oracle client home bin dir.	

Set following command line arguments to copy from Oracle to CSV:

-w copy_vector -o pool_size -r num_of_shards -t field_term -l lame_duck -K keep_data_file -V validate -U truncate_target -E ask_to_truncate -1 arg_1 -2 arg_2 -3 arg_3 -q query_sql_file -Q query_sql_dir -c from_table -P from_partition -S from_sub_partition -f from_db -e nls_date_format -m nls_timestamp_format -O nls_timestamp_tz_format -z source_client_home -A header -W trim_whitespace -g to_file -D to_dir 

Here:
(Common) -w [--copy_vector]	Data copy direction.	
(Common) -o [--pool_size]	Pool size.	
(Common) -r [--num_of_shards]	Number of shards.	
(Common) -t [--field_term]	Field terminator.	
(Common) -l [--lame_duck]	Limit rows (lame duck run).	
(Common) -K [--keep_data_file]	Keep data dump.	
(Common) -V [--validate]	Check if source and target objects exist.	
(Common) -U [--truncate_target]	Truncate target table/partition/subpartition.	
(Common) -E [--ask_to_truncate]	Ask to truncate.	
(Common) -1 [--arg_1]	Generic string argument 1.	
(Common) -2 [--arg_2]	Generic string argument 2.	
(Common) -3 [--arg_3]	Generic string argument 3.	
(From Oracle) -q [--query_sql_file]	Input file with Oracle query sql.	
(From Oracle) -Q [--query_sql_dir]	Input dir with Oracle query files sql.	
(From Oracle) -c [--from_table]	From table.	
(From Oracle) -P [--from_partition]	From partition.	
(From Oracle) -S [--from_sub_partition]	From sub-partition.	
(From Oracle) -f [--from_db]	From database.	
(From Oracle) -e [--nls_date_format]	nls_date_format for source.	
(From Oracle) -m [--nls_timestamp_format]	nls_timestamp_format for source.	
(From Oracle) -O [--nls_timestamp_tz_format]	nls_timestamp_tz_format for source.	
(From Oracle) -z [--source_client_home]	Path to Oracle client home.	
(From Oracle) -A [--header]	Include header to Oracle extract.	
(From Oracle) -W [--trim_whitespace]	Trim whitespace from varchar2 in "Oracle" extract.	
(To CSV) -g [--to_file]	To CSV file.	
(To CSV) -D [--to_dir]	To directory.	
To Oracle:

Set following command line arguments to copy from Oracle to Oracle:

-w copy_vector -o pool_size -r num_of_shards -t field_term -l lame_duck -K keep_data_file -V validate -U truncate_target -E ask_to_truncate -1 arg_1 -2 arg_2 -3 arg_3 -q query_sql_file -Q query_sql_dir -c from_table -P from_partition -S from_sub_partition -f from_db -e nls_date_format -m nls_timestamp_format -O nls_timestamp_tz_format -z source_client_home -A header -W trim_whitespace -g to_db -a to_table -G to_partition -N to_sub_partition -Z target_client_home 

Here:
(Common) -w [--copy_vector]	Data copy direction.	
(Common) -o [--pool_size]	Pool size.	
(Common) -r [--num_of_shards]	Number of shards.	
(Common) -t [--field_term]	Field terminator.	
(Common) -l [--lame_duck]	Limit rows (lame duck run).	
(Common) -K [--keep_data_file]	Keep data dump.	
(Common) -V [--validate]	Check if source and target objects exist.	
(Common) -U [--truncate_target]	Truncate target table/partition/subpartition.	
(Common) -E [--ask_to_truncate]	Ask to truncate.	
(Common) -1 [--arg_1]	Generic string argument 1.	
(Common) -2 [--arg_2]	Generic string argument 2.	
(Common) -3 [--arg_3]	Generic string argument 3.	
(From Oracle) -q [--query_sql_file]	Input file with Oracle query sql.	
(From Oracle) -Q [--query_sql_dir]	Input dir with Oracle query files sql.	
(From Oracle) -c [--from_table]	From table.	
(From Oracle) -P [--from_partition]	From partition.	
(From Oracle) -S [--from_sub_partition]	From sub-partition.	
(From Oracle) -f [--from_db]	From database.	
(From Oracle) -e [--nls_date_format]	nls_date_format for source.	
(From Oracle) -m [--nls_timestamp_format]	nls_timestamp_format for source.	
(From Oracle) -O [--nls_timestamp_tz_format]	nls_timestamp_tz_format for source.	
(From Oracle) -z [--source_client_home]	Path to Oracle client home.	
(From Oracle) -A [--header]	Include header to Oracle extract.	
(From Oracle) -W [--trim_whitespace]	Trim whitespace from varchar2 in "Oracle" extract.	
(To Oracle) -g [--to_db]	To Oracle database.	
(To Oracle) -a [--to_table]	To Oracle table.	
(To Oracle) -G [--to_partition]	To Oracle table.	
(To Oracle) -N [--to_sub_partition]	To Oracle table.	
(To Oracle) -Z [--target_client_home]	Path to Oracle client home bin dir.	

Set following command line arguments to copy from CSV to Oracle:

-w copy_vector -o pool_size -r num_of_shards -t field_term -l lame_duck -K keep_data_file -V validate -U truncate_target -E ask_to_truncate -1 arg_1 -2 arg_2 -3 arg_3 -i input_file -I input_dir -k skip_rows -y shard_size_kb -g to_db -a to_table -G to_partition -N to_sub_partition -e nls_date_format -m nls_timestamp_format -O nls_timestamp_tz_format -Z target_client_home 

Here:
(Common) -w [--copy_vector]	Data copy direction.	
(Common) -o [--pool_size]	Pool size.	
(Common) -r [--num_of_shards]	Number of shards.	
(Common) -t [--field_term]	Field terminator.	
(Common) -l [--lame_duck]	Limit rows (lame duck run).	
(Common) -K [--keep_data_file]	Keep data dump.	
(Common) -V [--validate]	Check if source and target objects exist.	
(Common) -U [--truncate_target]	Truncate target table/partition/subpartition.	
(Common) -E [--ask_to_truncate]	Ask to truncate.	
(Common) -1 [--arg_1]	Generic string argument 1.	
(Common) -2 [--arg_2]	Generic string argument 2.	
(Common) -3 [--arg_3]	Generic string argument 3.	
(From CSV) -i [--input_file]	Input CSV file.	
(From CSV) -I [--input_dir]	Input CSV directory.	
(From CSV) -k [--skip_rows]	Header size. Number of rows to skip in input file.	
(From CSV) -y [--shard_size_kb]	Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).	
(To Oracle) -g [--to_db]	To Oracle database.	
(To Oracle) -a [--to_table]	To Oracle table.	
(To Oracle) -G [--to_partition]	To Oracle table.	
(To Oracle) -N [--to_sub_partition]	To Oracle table.	
(To Oracle) -e [--nls_date_format]	nls_date_format for target.	
(To Oracle) -m [--nls_timestamp_format]	nls_timestamp_format for target.	
(To Oracle) -O [--nls_timestamp_tz_format]	nls_timestamp_tz_format for target.	
(To Oracle) -Z [--target_client_home]	Path to Oracle client home bin dir.	

--USE CASES--

1. CSV_to_Oracle. 112 use cases.
2. Oracle_to_CSV. 124 use cases.
3. Oracle_to_Oracle. 296 use cases.


CSV_to_Oracle: 112 use case(s) available:

1. CSV_DateFile_to_ORA_Partition - Load CSV file into Oracle Partition table.
2. CSV_DateFile_to_ORA_Partition_TruncateTarget - Load CSV file into Oracle Partition TruncateTarget table.
3. CSV_DateFile_to_ORA_Subpartition - Load CSV file into Oracle Subpartition table.
4. CSV_DateFile_to_ORA_Subpartition_TruncateTarget - Load CSV file into Oracle Subpartition TruncateTarget table.
5. CSV_DateFile_to_ORA_Table - Load CSV file into Oracle Table table.
6. CSV_DateFile_to_ORA_Table_NoClient - Load CSV file into Oracle Table NoClient table.
7. CSV_DateFile_to_ORA_Table_TruncateTarget - Load CSV file into Oracle Table TruncateTarget table.
8. CSV_DateFile_to_ORA_Table_TruncateTarget_NoClient - Load CSV file into Oracle Table TruncateTarget NoClient table.
9. CSV_DirSkip1_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Partition table.
10. CSV_DirSkip1_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
11. CSV_DirSkip1_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
12. CSV_DirSkip1_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
13. CSV_DirSkip1_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table table.
14. CSV_DirSkip1_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
15. CSV_DirSkip1_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
16. CSV_DirSkip1_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
17. CSV_Dir_Limit10_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Partition table.
18. CSV_Dir_Limit10_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
19. CSV_Dir_Limit10_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Subpartition table.
20. CSV_Dir_Limit10_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
21. CSV_Dir_Limit10_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table table.
22. CSV_Dir_Limit10_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
23. CSV_Dir_Limit10_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
24. CSV_Dir_Limit10_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
25. CSV_Dir_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Partition table.
26. CSV_Dir_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Partition TruncateTarget table.
27. CSV_Dir_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Subpartition table.
28. CSV_Dir_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Subpartition TruncateTarget table.
29. CSV_Dir_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table table.
30. CSV_Dir_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table NoClient table.
31. CSV_Dir_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table TruncateTarget table.
32. CSV_Dir_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
33. CSV_FileSkip1_to_ORA_Partition - Skip 1 rows and load CSV file into Oracle Partition table.
34. CSV_FileSkip1_to_ORA_Partition_TruncateTarget - Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
35. CSV_FileSkip1_to_ORA_Subpartition - Skip 1 rows and load CSV file into Oracle Subpartition table.
36. CSV_FileSkip1_to_ORA_Subpartition_TruncateTarget - Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
37. CSV_FileSkip1_to_ORA_Table - Skip 1 rows and load CSV file into Oracle Table table.
38. CSV_FileSkip1_to_ORA_Table_NoClient - Skip 1 rows and load CSV file into Oracle Table NoClient table.
39. CSV_FileSkip1_to_ORA_Table_TruncateTarget - Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
40. CSV_FileSkip1_to_ORA_Table_TruncateTarget_NoClient - Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
41. CSV_File_Limit10_to_ORA_Partition - Load only 10 rows from CSV file into Oracle Partition table.
42. CSV_File_Limit10_to_ORA_Partition_TruncateTarget - Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
43. CSV_File_Limit10_to_ORA_Subpartition - Load only 10 rows from CSV file into Oracle Subpartition table.
44. CSV_File_Limit10_to_ORA_Subpartition_TruncateTarget - Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
45. CSV_File_Limit10_to_ORA_Table - Load only 10 rows from CSV file into Oracle Table table.
46. CSV_File_Limit10_to_ORA_Table_NoClient - Load only 10 rows from CSV file into Oracle Table NoClient table.
47. CSV_File_Limit10_to_ORA_Table_TruncateTarget - Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
48. CSV_File_Limit10_to_ORA_Table_TruncateTarget_NoClient - Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
49. CSV_ShardedDirSkip1_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Partition table.
50. CSV_ShardedDirSkip1_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
51. CSV_ShardedDirSkip1_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
52. CSV_ShardedDirSkip1_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
53. CSV_ShardedDirSkip1_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table table.
54. CSV_ShardedDirSkip1_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
55. CSV_ShardedDirSkip1_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
56. CSV_ShardedDirSkip1_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
57. CSV_ShardedDir_Limit10_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Partition table.
58. CSV_ShardedDir_Limit10_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
59. CSV_ShardedDir_Limit10_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Subpartition table.
60. CSV_ShardedDir_Limit10_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
61. CSV_ShardedDir_Limit10_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table table.
62. CSV_ShardedDir_Limit10_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
63. CSV_ShardedDir_Limit10_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
64. CSV_ShardedDir_Limit10_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
65. CSV_ShardedDir_to_ORA_Partition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Partition table.
66. CSV_ShardedDir_to_ORA_Partition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Partition TruncateTarget table.
67. CSV_ShardedDir_to_ORA_Subpartition - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Subpartition table.
68. CSV_ShardedDir_to_ORA_Subpartition_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Subpartition TruncateTarget table.
69. CSV_ShardedDir_to_ORA_Table - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table table.
70. CSV_ShardedDir_to_ORA_Table_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table NoClient table.
71. CSV_ShardedDir_to_ORA_Table_TruncateTarget - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table TruncateTarget table.
72. CSV_ShardedDir_to_ORA_Table_TruncateTarget_NoClient - Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
73. CSV_ShardedFileSkip1_to_ORA_Partition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Partition table.
74. CSV_ShardedFileSkip1_to_ORA_Partition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
75. CSV_ShardedFileSkip1_to_ORA_Subpartition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
76. CSV_ShardedFileSkip1_to_ORA_Subpartition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
77. CSV_ShardedFileSkip1_to_ORA_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table table.
78. CSV_ShardedFileSkip1_to_ORA_Table_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
79. CSV_ShardedFileSkip1_to_ORA_Table_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
80. CSV_ShardedFileSkip1_to_ORA_Table_TruncateTarget_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
81. CSV_ShardedFile_Limit10_to_ORA_Partition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Partition table.
82. CSV_ShardedFile_Limit10_to_ORA_Partition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
83. CSV_ShardedFile_Limit10_to_ORA_Subpartition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Subpartition table.
84. CSV_ShardedFile_Limit10_to_ORA_Subpartition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
85. CSV_ShardedFile_Limit10_to_ORA_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table table.
86. CSV_ShardedFile_Limit10_to_ORA_Table_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
87. CSV_ShardedFile_Limit10_to_ORA_Table_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
88. CSV_ShardedFile_Limit10_to_ORA_Table_TruncateTarget_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
89. CSV_ShardedFile_to_ORA_Partition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Partition table.
90. CSV_ShardedFile_to_ORA_Partition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Partition TruncateTarget table.
91. CSV_ShardedFile_to_ORA_Subpartition - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Subpartition table.
92. CSV_ShardedFile_to_ORA_Subpartition_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Subpartition TruncateTarget table.
93. CSV_ShardedFile_to_ORA_Table - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table table.
94. CSV_ShardedFile_to_ORA_Table_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table NoClient table.
95. CSV_ShardedFile_to_ORA_Table_TruncateTarget - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table TruncateTarget table.
96. CSV_ShardedFile_to_ORA_Table_TruncateTarget_NoClient - Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
97. CSV_TimestampFile_to_ORA_Partition - Load CSV file into Oracle Partition table.
98. CSV_TimestampFile_to_ORA_Partition_TruncateTarget - Load CSV file into Oracle Partition TruncateTarget table.
99. CSV_TimestampFile_to_ORA_Subpartition - Load CSV file into Oracle Subpartition table.
100. CSV_TimestampFile_to_ORA_Subpartition_TruncateTarget - Load CSV file into Oracle Subpartition TruncateTarget table.
101. CSV_TimestampFile_to_ORA_Table - Load CSV file into Oracle Table table.
102. CSV_TimestampFile_to_ORA_Table_NoClient - Load CSV file into Oracle Table NoClient table.
103. CSV_TimestampFile_to_ORA_Table_TruncateTarget - Load CSV file into Oracle Table TruncateTarget table.
104. CSV_TimestampFile_to_ORA_Table_TruncateTarget_NoClient - Load CSV file into Oracle Table TruncateTarget NoClient table.
105. CSV_TimezoneFile_to_ORA_Partition - Load CSV file into Oracle Partition table.
106. CSV_TimezoneFile_to_ORA_Partition_TruncateTarget - Load CSV file into Oracle Partition TruncateTarget table.
107. CSV_TimezoneFile_to_ORA_Subpartition - Load CSV file into Oracle Subpartition table.
108. CSV_TimezoneFile_to_ORA_Subpartition_TruncateTarget - Load CSV file into Oracle Subpartition TruncateTarget table.
109. CSV_TimezoneFile_to_ORA_Table - Load CSV file into Oracle Table table.
110. CSV_TimezoneFile_to_ORA_Table_NoClient - Load CSV file into Oracle Table NoClient table.
111. CSV_TimezoneFile_to_ORA_Table_TruncateTarget - Load CSV file into Oracle Table TruncateTarget table.
112. CSV_TimezoneFile_to_ORA_Table_TruncateTarget_NoClient - Load CSV file into Oracle Table TruncateTarget NoClient table.
Oracle_to_CSV: 124 use case(s) available:

113. ORA_DateTable_to_CSV_Default - Extract Oracle table into CSV Default location.
114. ORA_DateTable_to_CSV_Dir - Extract Oracle table into CSV Dir location.
115. ORA_DateTable_to_CSV_File - Extract Oracle table into CSV File location.
116. ORA_Partition_Limit10_to_CSV_Default - Extract only 10 rows from Oracle partition into CSV Default location.
117. ORA_Partition_Limit10_to_CSV_Dir - Extract only 10 rows from Oracle partition into CSV Dir location.
118. ORA_Partition_Limit10_to_CSV_File - Extract only 10 rows from Oracle partition into CSV File location.
119. ORA_Partition_NoClient_to_CSV_Default - Extract Oracle partition into CSV Default location.
120. ORA_Partition_NoClient_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
121. ORA_Partition_NoClient_to_CSV_File - Extract Oracle partition into CSV File location.
122. ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_Default - Extract Oracle partition into CSV Default location.
123. ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
124. ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_File - Extract Oracle partition into CSV File location.
125. ORA_Partition_Validate_to_CSV_Default - Extract Oracle partition into CSV Default location.
126. ORA_Partition_Validate_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
127. ORA_Partition_Validate_to_CSV_File - Extract Oracle partition into CSV File location.
128. ORA_Partition_keepWhitespace_to_CSV_Default - Extract Oracle partition into CSV Default location.
129. ORA_Partition_keepWhitespace_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
130. ORA_Partition_keepWhitespace_to_CSV_File - Extract Oracle partition into CSV File location.
131. ORA_Partition_to_CSV_Default - Extract Oracle partition into CSV Default location.
132. ORA_Partition_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
133. ORA_Partition_to_CSV_File - Extract Oracle partition into CSV File location.
134. ORA_Partition_trimWhitespace_to_CSV_Default - Extract Oracle partition into CSV Default location.
135. ORA_Partition_trimWhitespace_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
136. ORA_Partition_trimWhitespace_to_CSV_File - Extract Oracle partition into CSV File location.
137. ORA_Partition_withHeader_to_CSV_Default - Extract Oracle partition into CSV Default location.
138. ORA_Partition_withHeader_to_CSV_Dir - Extract Oracle partition into CSV Dir location.
139. ORA_Partition_withHeader_to_CSV_File - Extract Oracle partition into CSV File location.
140. ORA_QueryDir_Limit10_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV Default location.
141. ORA_QueryDir_Limit10_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV Dir location.
142. ORA_QueryDir_Limit10_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV File location.
143. ORA_QueryDir_keepWhitespace_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
144. ORA_QueryDir_keepWhitespace_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
145. ORA_QueryDir_keepWhitespace_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
146. ORA_QueryDir_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
147. ORA_QueryDir_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
148. ORA_QueryDir_trimWhitespace_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
149. ORA_QueryDir_trimWhitespace_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
150. ORA_QueryDir_trimWhitespace_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
151. ORA_QueryDir_trimWhitespace_withHeader_to_CSV_Default - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
152. ORA_QueryDir_trimWhitespace_withHeader_to_CSV_Dir - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
153. ORA_QueryDir_trimWhitespace_withHeader_to_CSV_File - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
154. ORA_QueryFile_Limit10_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV Default location.
155. ORA_QueryFile_Limit10_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV Dir location.
156. ORA_QueryFile_Limit10_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV File location.
157. ORA_QueryFile_keepWhitespace_noHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
158. ORA_QueryFile_keepWhitespace_noHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
159. ORA_QueryFile_keepWhitespace_noHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
160. ORA_QueryFile_keepWhitespace_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
161. ORA_QueryFile_keepWhitespace_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
162. ORA_QueryFile_keepWhitespace_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
163. ORA_QueryFile_keepWhitespace_withHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
164. ORA_QueryFile_keepWhitespace_withHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
165. ORA_QueryFile_keepWhitespace_withHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
166. ORA_QueryFile_noHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
167. ORA_QueryFile_noHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
168. ORA_QueryFile_noHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
169. ORA_QueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
170. ORA_QueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
171. ORA_QueryFile_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
172. ORA_QueryFile_trimWhitespace_noHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
173. ORA_QueryFile_trimWhitespace_noHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
174. ORA_QueryFile_trimWhitespace_noHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
175. ORA_QueryFile_trimWhitespace_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
176. ORA_QueryFile_trimWhitespace_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
177. ORA_QueryFile_trimWhitespace_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
178. ORA_QueryFile_trimWhitespace_withHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
179. ORA_QueryFile_trimWhitespace_withHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
180. ORA_QueryFile_trimWhitespace_withHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
181. ORA_QueryFile_withHeader_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
182. ORA_QueryFile_withHeader_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
183. ORA_QueryFile_withHeader_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
184. ORA_ShardedPartition_Limit10_to_CSV_Default - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded partition into CSV Default location.
185. ORA_ShardedPartition_Limit10_to_CSV_Dir - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded partition into CSV Dir location.
186. ORA_ShardedPartition_to_CSV_Default - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded partition into CSV Default location.
187. ORA_ShardedPartition_to_CSV_Dir - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded partition into CSV Dir location.
188. ORA_ShardedSubpartition_Limit10_to_CSV_Default - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded sub-partition into CSV Default location.
189. ORA_ShardedSubpartition_Limit10_to_CSV_Dir - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded sub-partition into CSV Dir location.
190. ORA_ShardedSubpartition_to_CSV_Default - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded sub-partition into CSV Default location.
191. ORA_ShardedSubpartition_to_CSV_Dir - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded sub-partition into CSV Dir location.
192. ORA_ShardedTable_Limit10_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle table into CSV Default location.
193. ORA_ShardedTable_Limit10_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle table into CSV Dir location.
194. ORA_ShardedTable_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Default location.
195. ORA_ShardedTable_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Dir location.
196. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_CSV_Default - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Default location.
197. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_CSV_Dir - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Dir location.
198. ORA_Subpartition_Limit10_to_CSV_Default - Extract only 10 rows from Oracle sub-partition into CSV Default location.
199. ORA_Subpartition_Limit10_to_CSV_Dir - Extract only 10 rows from Oracle sub-partition into CSV Dir location.
200. ORA_Subpartition_Limit10_to_CSV_File - Extract only 10 rows from Oracle sub-partition into CSV File location.
201. ORA_Subpartition_Validate_to_CSV_Default - Extract Oracle sub-partition into CSV Default location.
202. ORA_Subpartition_Validate_to_CSV_Dir - Extract Oracle sub-partition into CSV Dir location.
203. ORA_Subpartition_Validate_to_CSV_File - Extract Oracle sub-partition into CSV File location.
204. ORA_Subpartition_to_CSV_Default - Extract Oracle sub-partition into CSV Default location.
205. ORA_Subpartition_to_CSV_Dir - Extract Oracle sub-partition into CSV Dir location.
206. ORA_Subpartition_to_CSV_File - Extract Oracle sub-partition into CSV File location.
207. ORA_Subpartition_trimWhitespace_to_CSV_Default - Extract Oracle sub-partition into CSV Default location.
208. ORA_Subpartition_trimWhitespace_to_CSV_Dir - Extract Oracle sub-partition into CSV Dir location.
209. ORA_Subpartition_trimWhitespace_to_CSV_File - Extract Oracle sub-partition into CSV File location.
210. ORA_Subpartition_withHeader_to_CSV_Default - Extract Oracle sub-partition into CSV Default location.
211. ORA_Subpartition_withHeader_to_CSV_Dir - Extract Oracle sub-partition into CSV Dir location.
212. ORA_Subpartition_withHeader_to_CSV_File - Extract Oracle sub-partition into CSV File location.
213. ORA_Table_Limit10_to_CSV_Default - Extract only 10 rows from Oracle table into CSV Default location.
214. ORA_Table_Limit10_to_CSV_Dir - Extract only 10 rows from Oracle table into CSV Dir location.
215. ORA_Table_Limit10_to_CSV_File - Extract only 10 rows from Oracle table into CSV File location.
216. ORA_TimestampTable_keepWhitespace_to_CSV_Default - Extract Oracle table into CSV Default location.
217. ORA_TimestampTable_keepWhitespace_to_CSV_Dir - Extract Oracle table into CSV Dir location.
218. ORA_TimestampTable_keepWhitespace_to_CSV_File - Extract Oracle table into CSV File location.
219. ORA_TimestampTable_to_CSV_Default - Extract Oracle table into CSV Default location.
220. ORA_TimestampTable_to_CSV_Dir - Extract Oracle table into CSV Dir location.
221. ORA_TimestampTable_to_CSV_File - Extract Oracle table into CSV File location.
222. ORA_TimestampTable_trimWhitespace_Validate_to_CSV_Default - Extract Oracle table into CSV Default location.
223. ORA_TimestampTable_trimWhitespace_Validate_to_CSV_Dir - Extract Oracle table into CSV Dir location.
224. ORA_TimestampTable_trimWhitespace_Validate_to_CSV_File - Extract Oracle table into CSV File location.
225. ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_Default - Extract Oracle table into CSV Default location.
226. ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_Dir - Extract Oracle table into CSV Dir location.
227. ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_File - Extract Oracle table into CSV File location.
228. ORA_TimestampTable_withHeader_to_CSV_Default - Extract Oracle table into CSV Default location.
229. ORA_TimestampTable_withHeader_to_CSV_Dir - Extract Oracle table into CSV Dir location.
230. ORA_TimestampTable_withHeader_to_CSV_File - Extract Oracle table into CSV File location.
231. ORA_TimezoneQueryFile_to_CSV_Default - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
232. ORA_TimezoneQueryFile_to_CSV_Dir - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
233. ORA_TimezoneQueryFile_to_CSV_File - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
234. ORA_TimezoneTable_to_CSV_Default - Extract Oracle table into CSV Default location.
235. ORA_TimezoneTable_to_CSV_Dir - Extract Oracle table into CSV Dir location.
236. ORA_TimezoneTable_to_CSV_File - Extract Oracle table into CSV File location.
Oracle_to_Oracle: 296 use case(s) available:

237. ORA_DateTable_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
238. ORA_DateTable_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
239. ORA_DateTable_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
240. ORA_DateTable_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
241. ORA_DateTable_to_ORA_Table - Copy Oracle table into Oracle Table table.
242. ORA_DateTable_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
243. ORA_DateTable_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
244. ORA_DateTable_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
245. ORA_Partition_KeepSpoolFile_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
246. ORA_Partition_KeepSpoolFile_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
247. ORA_Partition_KeepSpoolFile_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
248. ORA_Partition_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
249. ORA_Partition_KeepSpoolFile_to_ORA_Table - Copy Oracle partition into Oracle Table table.
250. ORA_Partition_KeepSpoolFile_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
251. ORA_Partition_KeepSpoolFile_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
252. ORA_Partition_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
253. ORA_Partition_Limit10_to_ORA_Partition - Copy only 10 rows from Oracle partition into Oracle Partition table.
254. ORA_Partition_Limit10_to_ORA_Partition_TruncateTarget - Copy only 10 rows from Oracle partition into Oracle Partition TruncateTarget table.
255. ORA_Partition_Limit10_to_ORA_Subpartition - Copy only 10 rows from Oracle partition into Oracle Subpartition table.
256. ORA_Partition_Limit10_to_ORA_Subpartition_TruncateTarget - Copy only 10 rows from Oracle partition into Oracle Subpartition TruncateTarget table.
257. ORA_Partition_Limit10_to_ORA_Table - Copy only 10 rows from Oracle partition into Oracle Table table.
258. ORA_Partition_Limit10_to_ORA_Table_NoClient - Copy only 10 rows from Oracle partition into Oracle Table NoClient table.
259. ORA_Partition_Limit10_to_ORA_Table_TruncateTarget - Copy only 10 rows from Oracle partition into Oracle Table TruncateTarget table.
260. ORA_Partition_Limit10_to_ORA_Table_TruncateTarget_NoClient - Copy only 10 rows from Oracle partition into Oracle Table TruncateTarget NoClient table.
261. ORA_Partition_NoClient_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
262. ORA_Partition_NoClient_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
263. ORA_Partition_NoClient_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
264. ORA_Partition_NoClient_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
265. ORA_Partition_NoClient_to_ORA_Table - Copy Oracle partition into Oracle Table table.
266. ORA_Partition_NoClient_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
267. ORA_Partition_NoClient_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
268. ORA_Partition_NoClient_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
269. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
270. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
271. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
272. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
273. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table - Copy Oracle partition into Oracle Table table.
274. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
275. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
276. ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
277. ORA_Partition_Validate_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
278. ORA_Partition_Validate_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
279. ORA_Partition_Validate_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
280. ORA_Partition_Validate_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
281. ORA_Partition_Validate_to_ORA_Table - Copy Oracle partition into Oracle Table table.
282. ORA_Partition_Validate_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
283. ORA_Partition_Validate_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
284. ORA_Partition_Validate_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
285. ORA_Partition_keepWhitespace_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
286. ORA_Partition_keepWhitespace_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
287. ORA_Partition_keepWhitespace_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
288. ORA_Partition_keepWhitespace_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
289. ORA_Partition_keepWhitespace_to_ORA_Table - Copy Oracle partition into Oracle Table table.
290. ORA_Partition_keepWhitespace_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
291. ORA_Partition_keepWhitespace_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
292. ORA_Partition_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
293. ORA_Partition_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
294. ORA_Partition_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
295. ORA_Partition_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
296. ORA_Partition_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
297. ORA_Partition_to_ORA_Table - Copy Oracle partition into Oracle Table table.
298. ORA_Partition_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
299. ORA_Partition_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
300. ORA_Partition_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
301. ORA_Partition_trimWhitespace_to_ORA_Partition - Copy Oracle partition into Oracle Partition table.
302. ORA_Partition_trimWhitespace_to_ORA_Partition_TruncateTarget - Copy Oracle partition into Oracle Partition TruncateTarget table.
303. ORA_Partition_trimWhitespace_to_ORA_Subpartition - Copy Oracle partition into Oracle Subpartition table.
304. ORA_Partition_trimWhitespace_to_ORA_Subpartition_TruncateTarget - Copy Oracle partition into Oracle Subpartition TruncateTarget table.
305. ORA_Partition_trimWhitespace_to_ORA_Table - Copy Oracle partition into Oracle Table table.
306. ORA_Partition_trimWhitespace_to_ORA_Table_NoClient - Copy Oracle partition into Oracle Table NoClient table.
307. ORA_Partition_trimWhitespace_to_ORA_Table_TruncateTarget - Copy Oracle partition into Oracle Table TruncateTarget table.
308. ORA_Partition_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
309. ORA_QueryDir_Limit10_to_ORA_Partition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Partition table.
310. ORA_QueryDir_Limit10_to_ORA_Partition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Partition TruncateTarget table.
311. ORA_QueryDir_Limit10_to_ORA_Subpartition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition table.
312. ORA_QueryDir_Limit10_to_ORA_Subpartition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition TruncateTarget table.
313. ORA_QueryDir_Limit10_to_ORA_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table table.
314. ORA_QueryDir_Limit10_to_ORA_Table_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table NoClient table.
315. ORA_QueryDir_Limit10_to_ORA_Table_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget table.
316. ORA_QueryDir_Limit10_to_ORA_Table_TruncateTarget_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget NoClient table.
317. ORA_QueryDir_keepWhitespace_to_ORA_Partition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
318. ORA_QueryDir_keepWhitespace_to_ORA_Partition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
319. ORA_QueryDir_keepWhitespace_to_ORA_Subpartition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
320. ORA_QueryDir_keepWhitespace_to_ORA_Subpartition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
321. ORA_QueryDir_keepWhitespace_to_ORA_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
322. ORA_QueryDir_keepWhitespace_to_ORA_Table_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
323. ORA_QueryDir_keepWhitespace_to_ORA_Table_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
324. ORA_QueryDir_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
325. ORA_QueryDir_to_ORA_Partition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
326. ORA_QueryDir_to_ORA_Partition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
327. ORA_QueryDir_to_ORA_Subpartition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
328. ORA_QueryDir_to_ORA_Subpartition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
329. ORA_QueryDir_to_ORA_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
330. ORA_QueryDir_to_ORA_Table_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
331. ORA_QueryDir_to_ORA_Table_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
332. ORA_QueryDir_to_ORA_Table_TruncateTarget_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
333. ORA_QueryDir_trimWhitespace_to_ORA_Partition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
334. ORA_QueryDir_trimWhitespace_to_ORA_Partition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
335. ORA_QueryDir_trimWhitespace_to_ORA_Subpartition - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
336. ORA_QueryDir_trimWhitespace_to_ORA_Subpartition_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
337. ORA_QueryDir_trimWhitespace_to_ORA_Table - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
338. ORA_QueryDir_trimWhitespace_to_ORA_Table_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
339. ORA_QueryDir_trimWhitespace_to_ORA_Table_TruncateTarget - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
340. ORA_QueryDir_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient - Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
341. ORA_QueryFile_Limit10_to_ORA_Partition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Partition table.
342. ORA_QueryFile_Limit10_to_ORA_Partition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Partition TruncateTarget table.
343. ORA_QueryFile_Limit10_to_ORA_Subpartition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition table.
344. ORA_QueryFile_Limit10_to_ORA_Subpartition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition TruncateTarget table.
345. ORA_QueryFile_Limit10_to_ORA_Table - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table table.
346. ORA_QueryFile_Limit10_to_ORA_Table_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table NoClient table.
347. ORA_QueryFile_Limit10_to_ORA_Table_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget table.
348. ORA_QueryFile_Limit10_to_ORA_Table_TruncateTarget_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget NoClient table.
349. ORA_QueryFile_keepWhitespace_to_ORA_Partition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
350. ORA_QueryFile_keepWhitespace_to_ORA_Partition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
351. ORA_QueryFile_keepWhitespace_to_ORA_Subpartition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
352. ORA_QueryFile_keepWhitespace_to_ORA_Subpartition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
353. ORA_QueryFile_keepWhitespace_to_ORA_Table - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
354. ORA_QueryFile_keepWhitespace_to_ORA_Table_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
355. ORA_QueryFile_keepWhitespace_to_ORA_Table_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
356. ORA_QueryFile_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
357. ORA_QueryFile_to_ORA_Partition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
358. ORA_QueryFile_to_ORA_Partition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
359. ORA_QueryFile_to_ORA_Subpartition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
360. ORA_QueryFile_to_ORA_Subpartition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
361. ORA_QueryFile_to_ORA_Table - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
362. ORA_QueryFile_to_ORA_Table_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
363. ORA_QueryFile_to_ORA_Table_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
364. ORA_QueryFile_to_ORA_Table_TruncateTarget_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
365. ORA_QueryFile_trimWhitespace_to_ORA_Partition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
366. ORA_QueryFile_trimWhitespace_to_ORA_Partition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
367. ORA_QueryFile_trimWhitespace_to_ORA_Subpartition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
368. ORA_QueryFile_trimWhitespace_to_ORA_Subpartition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
369. ORA_QueryFile_trimWhitespace_to_ORA_Table - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
370. ORA_QueryFile_trimWhitespace_to_ORA_Table_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
371. ORA_QueryFile_trimWhitespace_to_ORA_Table_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
372. ORA_QueryFile_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
373. ORA_ShardedPartition_Limit10_to_ORA_Partition - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Partition table.
374. ORA_ShardedPartition_Limit10_to_ORA_Partition_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Partition TruncateTarget table.
375. ORA_ShardedPartition_Limit10_to_ORA_Subpartition - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Subpartition table.
376. ORA_ShardedPartition_Limit10_to_ORA_Subpartition_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Subpartition TruncateTarget table.
377. ORA_ShardedPartition_Limit10_to_ORA_Table - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table table.
378. ORA_ShardedPartition_Limit10_to_ORA_Table_NoClient - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table NoClient table.
379. ORA_ShardedPartition_Limit10_to_ORA_Table_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table TruncateTarget table.
380. ORA_ShardedPartition_Limit10_to_ORA_Table_TruncateTarget_NoClient - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table TruncateTarget NoClient table.
381. ORA_ShardedPartition_to_ORA_Partition - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Partition table.
382. ORA_ShardedPartition_to_ORA_Partition_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Partition TruncateTarget table.
383. ORA_ShardedPartition_to_ORA_Subpartition - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Subpartition table.
384. ORA_ShardedPartition_to_ORA_Subpartition_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Subpartition TruncateTarget table.
385. ORA_ShardedPartition_to_ORA_Table - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table table.
386. ORA_ShardedPartition_to_ORA_Table_NoClient - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table NoClient table.
387. ORA_ShardedPartition_to_ORA_Table_TruncateTarget - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table TruncateTarget table.
388. ORA_ShardedPartition_to_ORA_Table_TruncateTarget_NoClient - Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table TruncateTarget NoClient table.
389. ORA_ShardedSubpartition_Limit10_to_ORA_Partition - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Partition table.
390. ORA_ShardedSubpartition_Limit10_to_ORA_Partition_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Partition TruncateTarget table.
391. ORA_ShardedSubpartition_Limit10_to_ORA_Subpartition - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Subpartition table.
392. ORA_ShardedSubpartition_Limit10_to_ORA_Subpartition_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Subpartition TruncateTarget table.
393. ORA_ShardedSubpartition_Limit10_to_ORA_Table - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table table.
394. ORA_ShardedSubpartition_Limit10_to_ORA_Table_NoClient - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table NoClient table.
395. ORA_ShardedSubpartition_Limit10_to_ORA_Table_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table TruncateTarget table.
396. ORA_ShardedSubpartition_Limit10_to_ORA_Table_TruncateTarget_NoClient - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table TruncateTarget NoClient table.
397. ORA_ShardedSubpartition_to_ORA_Partition - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Partition table.
398. ORA_ShardedSubpartition_to_ORA_Partition_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Partition TruncateTarget table.
399. ORA_ShardedSubpartition_to_ORA_Subpartition - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Subpartition table.
400. ORA_ShardedSubpartition_to_ORA_Subpartition_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Subpartition TruncateTarget table.
401. ORA_ShardedSubpartition_to_ORA_Table - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table table.
402. ORA_ShardedSubpartition_to_ORA_Table_NoClient - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table NoClient table.
403. ORA_ShardedSubpartition_to_ORA_Table_TruncateTarget - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table TruncateTarget table.
404. ORA_ShardedSubpartition_to_ORA_Table_TruncateTarget_NoClient - Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table TruncateTarget NoClient table.
405. ORA_ShardedTable_Limit10_to_ORA_Partition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Partition table.
406. ORA_ShardedTable_Limit10_to_ORA_Partition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Partition TruncateTarget table.
407. ORA_ShardedTable_Limit10_to_ORA_Subpartition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Subpartition table.
408. ORA_ShardedTable_Limit10_to_ORA_Subpartition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Subpartition TruncateTarget table.
409. ORA_ShardedTable_Limit10_to_ORA_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table table.
410. ORA_ShardedTable_Limit10_to_ORA_Table_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table NoClient table.
411. ORA_ShardedTable_Limit10_to_ORA_Table_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget table.
412. ORA_ShardedTable_Limit10_to_ORA_Table_TruncateTarget_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget NoClient table.
413. ORA_ShardedTable_to_ORA_Partition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition table.
414. ORA_ShardedTable_to_ORA_Partition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition TruncateTarget table.
415. ORA_ShardedTable_to_ORA_Subpartition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition table.
416. ORA_ShardedTable_to_ORA_Subpartition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition TruncateTarget table.
417. ORA_ShardedTable_to_ORA_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table table.
418. ORA_ShardedTable_to_ORA_Table_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table NoClient table.
419. ORA_ShardedTable_to_ORA_Table_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget table.
420. ORA_ShardedTable_to_ORA_Table_TruncateTarget_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
421. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Partition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition table.
422. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Partition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition TruncateTarget table.
423. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Subpartition - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition table.
424. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Subpartition_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition TruncateTarget table.
425. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table table.
426. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table NoClient table.
427. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget table.
428. ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget_NoClient - Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
429. ORA_Subpartition_KeepSpoolFile_to_ORA_Partition - Copy Oracle sub-partition into Oracle Partition table.
430. ORA_Subpartition_KeepSpoolFile_to_ORA_Partition_TruncateTarget - Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
431. ORA_Subpartition_KeepSpoolFile_to_ORA_Subpartition - Copy Oracle sub-partition into Oracle Subpartition table.
432. ORA_Subpartition_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget - Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
433. ORA_Subpartition_KeepSpoolFile_to_ORA_Table - Copy Oracle sub-partition into Oracle Table table.
434. ORA_Subpartition_KeepSpoolFile_to_ORA_Table_NoClient - Copy Oracle sub-partition into Oracle Table NoClient table.
435. ORA_Subpartition_KeepSpoolFile_to_ORA_Table_TruncateTarget - Copy Oracle sub-partition into Oracle Table TruncateTarget table.
436. ORA_Subpartition_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
437. ORA_Subpartition_Limit10_to_ORA_Partition - Copy only 10 rows from Oracle sub-partition into Oracle Partition table.
438. ORA_Subpartition_Limit10_to_ORA_Partition_TruncateTarget - Copy only 10 rows from Oracle sub-partition into Oracle Partition TruncateTarget table.
439. ORA_Subpartition_Limit10_to_ORA_Subpartition - Copy only 10 rows from Oracle sub-partition into Oracle Subpartition table.
440. ORA_Subpartition_Limit10_to_ORA_Subpartition_TruncateTarget - Copy only 10 rows from Oracle sub-partition into Oracle Subpartition TruncateTarget table.
441. ORA_Subpartition_Limit10_to_ORA_Table - Copy only 10 rows from Oracle sub-partition into Oracle Table table.
442. ORA_Subpartition_Limit10_to_ORA_Table_NoClient - Copy only 10 rows from Oracle sub-partition into Oracle Table NoClient table.
443. ORA_Subpartition_Limit10_to_ORA_Table_TruncateTarget - Copy only 10 rows from Oracle sub-partition into Oracle Table TruncateTarget table.
444. ORA_Subpartition_Limit10_to_ORA_Table_TruncateTarget_NoClient - Copy only 10 rows from Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
445. ORA_Subpartition_Validate_to_ORA_Partition - Copy Oracle sub-partition into Oracle Partition table.
446. ORA_Subpartition_Validate_to_ORA_Partition_TruncateTarget - Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
447. ORA_Subpartition_Validate_to_ORA_Subpartition - Copy Oracle sub-partition into Oracle Subpartition table.
448. ORA_Subpartition_Validate_to_ORA_Subpartition_TruncateTarget - Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
449. ORA_Subpartition_Validate_to_ORA_Table - Copy Oracle sub-partition into Oracle Table table.
450. ORA_Subpartition_Validate_to_ORA_Table_NoClient - Copy Oracle sub-partition into Oracle Table NoClient table.
451. ORA_Subpartition_Validate_to_ORA_Table_TruncateTarget - Copy Oracle sub-partition into Oracle Table TruncateTarget table.
452. ORA_Subpartition_Validate_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
453. ORA_Subpartition_to_ORA_Partition - Copy Oracle sub-partition into Oracle Partition table.
454. ORA_Subpartition_to_ORA_Partition_TruncateTarget - Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
455. ORA_Subpartition_to_ORA_Subpartition - Copy Oracle sub-partition into Oracle Subpartition table.
456. ORA_Subpartition_to_ORA_Subpartition_TruncateTarget - Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
457. ORA_Subpartition_to_ORA_Table - Copy Oracle sub-partition into Oracle Table table.
458. ORA_Subpartition_to_ORA_Table_NoClient - Copy Oracle sub-partition into Oracle Table NoClient table.
459. ORA_Subpartition_to_ORA_Table_TruncateTarget - Copy Oracle sub-partition into Oracle Table TruncateTarget table.
460. ORA_Subpartition_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
461. ORA_Subpartition_trimWhitespace_to_ORA_Partition - Copy Oracle sub-partition into Oracle Partition table.
462. ORA_Subpartition_trimWhitespace_to_ORA_Partition_TruncateTarget - Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
463. ORA_Subpartition_trimWhitespace_to_ORA_Subpartition - Copy Oracle sub-partition into Oracle Subpartition table.
464. ORA_Subpartition_trimWhitespace_to_ORA_Subpartition_TruncateTarget - Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
465. ORA_Subpartition_trimWhitespace_to_ORA_Table - Copy Oracle sub-partition into Oracle Table table.
466. ORA_Subpartition_trimWhitespace_to_ORA_Table_NoClient - Copy Oracle sub-partition into Oracle Table NoClient table.
467. ORA_Subpartition_trimWhitespace_to_ORA_Table_TruncateTarget - Copy Oracle sub-partition into Oracle Table TruncateTarget table.
468. ORA_Subpartition_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
469. ORA_Table_KeepSpoolFile_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
470. ORA_Table_KeepSpoolFile_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
471. ORA_Table_KeepSpoolFile_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
472. ORA_Table_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
473. ORA_Table_KeepSpoolFile_to_ORA_Table - Copy Oracle table into Oracle Table table.
474. ORA_Table_KeepSpoolFile_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
475. ORA_Table_KeepSpoolFile_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
476. ORA_Table_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
477. ORA_Table_Limit10_to_ORA_Partition - Copy only 10 rows from Oracle table into Oracle Partition table.
478. ORA_Table_Limit10_to_ORA_Partition_TruncateTarget - Copy only 10 rows from Oracle table into Oracle Partition TruncateTarget table.
479. ORA_Table_Limit10_to_ORA_Subpartition - Copy only 10 rows from Oracle table into Oracle Subpartition table.
480. ORA_Table_Limit10_to_ORA_Subpartition_TruncateTarget - Copy only 10 rows from Oracle table into Oracle Subpartition TruncateTarget table.
481. ORA_Table_Limit10_to_ORA_Table - Copy only 10 rows from Oracle table into Oracle Table table.
482. ORA_Table_Limit10_to_ORA_Table_NoClient - Copy only 10 rows from Oracle table into Oracle Table NoClient table.
483. ORA_Table_Limit10_to_ORA_Table_TruncateTarget - Copy only 10 rows from Oracle table into Oracle Table TruncateTarget table.
484. ORA_Table_Limit10_to_ORA_Table_TruncateTarget_NoClient - Copy only 10 rows from Oracle table into Oracle Table TruncateTarget NoClient table.
485. ORA_TimestampTable_keepWhitespace_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
486. ORA_TimestampTable_keepWhitespace_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
487. ORA_TimestampTable_keepWhitespace_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
488. ORA_TimestampTable_keepWhitespace_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
489. ORA_TimestampTable_keepWhitespace_to_ORA_Table - Copy Oracle table into Oracle Table table.
490. ORA_TimestampTable_keepWhitespace_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
491. ORA_TimestampTable_keepWhitespace_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
492. ORA_TimestampTable_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
493. ORA_TimestampTable_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
494. ORA_TimestampTable_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
495. ORA_TimestampTable_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
496. ORA_TimestampTable_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
497. ORA_TimestampTable_to_ORA_Table - Copy Oracle table into Oracle Table table.
498. ORA_TimestampTable_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
499. ORA_TimestampTable_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
500. ORA_TimestampTable_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
501. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
502. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
503. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
504. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
505. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table - Copy Oracle table into Oracle Table table.
506. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
507. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
508. ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
509. ORA_TimezoneQueryFile_to_ORA_Partition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
510. ORA_TimezoneQueryFile_to_ORA_Partition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
511. ORA_TimezoneQueryFile_to_ORA_Subpartition - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
512. ORA_TimezoneQueryFile_to_ORA_Subpartition_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
513. ORA_TimezoneQueryFile_to_ORA_Table - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
514. ORA_TimezoneQueryFile_to_ORA_Table_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
515. ORA_TimezoneQueryFile_to_ORA_Table_TruncateTarget - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
516. ORA_TimezoneQueryFile_to_ORA_Table_TruncateTarget_NoClient - Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
517. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
518. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
519. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
520. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
521. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table - Copy Oracle table into Oracle Table table.
522. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
523. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
524. ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.
525. ORA_TimezoneTable_to_ORA_Partition - Copy Oracle table into Oracle Partition table.
526. ORA_TimezoneTable_to_ORA_Partition_TruncateTarget - Copy Oracle table into Oracle Partition TruncateTarget table.
527. ORA_TimezoneTable_to_ORA_Subpartition - Copy Oracle table into Oracle Subpartition table.
528. ORA_TimezoneTable_to_ORA_Subpartition_TruncateTarget - Copy Oracle table into Oracle Subpartition TruncateTarget table.
529. ORA_TimezoneTable_to_ORA_Table - Copy Oracle table into Oracle Table table.
530. ORA_TimezoneTable_to_ORA_Table_NoClient - Copy Oracle table into Oracle Table NoClient table.
531. ORA_TimezoneTable_to_ORA_Table_TruncateTarget - Copy Oracle table into Oracle Table TruncateTarget table.
532. ORA_TimezoneTable_to_ORA_Table_TruncateTarget_NoClient - Copy Oracle table into Oracle Table TruncateTarget NoClient table.

--DETAILS--

-USE-CASE # 1
Use case name: CSV_DateFile_to_ORA_Partition
Description:  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 2
Use case name: CSV_DateFile_to_ORA_Partition_TruncateTarget
Description:  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 3
Use case name: CSV_DateFile_to_ORA_Subpartition
Description:  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 4
Use case name: CSV_DateFile_to_ORA_Subpartition_TruncateTarget
Description:  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 5
Use case name: CSV_DateFile_to_ORA_Table
Description:  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 6
Use case name: CSV_DateFile_to_ORA_Table_NoClient
Description:  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 7
Use case name: CSV_DateFile_to_ORA_Table_TruncateTarget
Description:  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 8
Use case name: CSV_DateFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_dt.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 9
Use case name: CSV_DirSkip1_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 10
Use case name: CSV_DirSkip1_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 11
Use case name: CSV_DirSkip1_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 12
Use case name: CSV_DirSkip1_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 13
Use case name: CSV_DirSkip1_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 14
Use case name: CSV_DirSkip1_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 15
Use case name: CSV_DirSkip1_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 16
Use case name: CSV_DirSkip1_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 17
Use case name: CSV_Dir_Limit10_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 18
Use case name: CSV_Dir_Limit10_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 19
Use case name: CSV_Dir_Limit10_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 20
Use case name: CSV_Dir_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 21
Use case name: CSV_Dir_Limit10_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 22
Use case name: CSV_Dir_Limit10_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 23
Use case name: CSV_Dir_Limit10_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 24
Use case name: CSV_Dir_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 25
Use case name: CSV_Dir_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 26
Use case name: CSV_Dir_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 27
Use case name: CSV_Dir_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 28
Use case name: CSV_Dir_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 29
Use case name: CSV_Dir_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 30
Use case name: CSV_Dir_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 31
Use case name: CSV_Dir_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 32
Use case name: CSV_Dir_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 33
Use case name: CSV_FileSkip1_to_ORA_Partition
Description:  Skip 1 rows and load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 34
Use case name: CSV_FileSkip1_to_ORA_Partition_TruncateTarget
Description:  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 35
Use case name: CSV_FileSkip1_to_ORA_Subpartition
Description:  Skip 1 rows and load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 36
Use case name: CSV_FileSkip1_to_ORA_Subpartition_TruncateTarget
Description:  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 37
Use case name: CSV_FileSkip1_to_ORA_Table
Description:  Skip 1 rows and load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 38
Use case name: CSV_FileSkip1_to_ORA_Table_NoClient
Description:  Skip 1 rows and load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 39
Use case name: CSV_FileSkip1_to_ORA_Table_TruncateTarget
Description:  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 40
Use case name: CSV_FileSkip1_to_ORA_Table_TruncateTarget_NoClient
Description:  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 100 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 41
Use case name: CSV_File_Limit10_to_ORA_Partition
Description:  Load only 10 rows from CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 42
Use case name: CSV_File_Limit10_to_ORA_Partition_TruncateTarget
Description:  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 43
Use case name: CSV_File_Limit10_to_ORA_Subpartition
Description:  Load only 10 rows from CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 44
Use case name: CSV_File_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 45
Use case name: CSV_File_Limit10_to_ORA_Table
Description:  Load only 10 rows from CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 46
Use case name: CSV_File_Limit10_to_ORA_Table_NoClient
Description:  Load only 10 rows from CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 47
Use case name: CSV_File_Limit10_to_ORA_Table_TruncateTarget
Description:  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 48
Use case name: CSV_File_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 49
Use case name: CSV_ShardedDirSkip1_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 50
Use case name: CSV_ShardedDirSkip1_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 51
Use case name: CSV_ShardedDirSkip1_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 52
Use case name: CSV_ShardedDirSkip1_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 53
Use case name: CSV_ShardedDirSkip1_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 54
Use case name: CSV_ShardedDirSkip1_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 55
Use case name: CSV_ShardedDirSkip1_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 56
Use case name: CSV_ShardedDirSkip1_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -k 1 ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 57
Use case name: CSV_ShardedDir_Limit10_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 58
Use case name: CSV_ShardedDir_Limit10_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 59
Use case name: CSV_ShardedDir_Limit10_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 60
Use case name: CSV_ShardedDir_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 61
Use case name: CSV_ShardedDir_Limit10_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 62
Use case name: CSV_ShardedDir_Limit10_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 63
Use case name: CSV_ShardedDir_Limit10_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 64
Use case name: CSV_ShardedDir_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 65
Use case name: CSV_ShardedDir_to_ORA_Partition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 66
Use case name: CSV_ShardedDir_to_ORA_Partition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 67
Use case name: CSV_ShardedDir_to_ORA_Subpartition
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 68
Use case name: CSV_ShardedDir_to_ORA_Subpartition_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 69
Use case name: CSV_ShardedDir_to_ORA_Table
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 70
Use case name: CSV_ShardedDir_to_ORA_Table_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 71
Use case name: CSV_ShardedDir_to_ORA_Table_TruncateTarget
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 72
Use case name: CSV_ShardedDir_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each CSV file from a directory "C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir".
	  Break input CSV files into logical partitions (shards) and run load 
	  process on each shard in thread pool (-o[--pool_size] 3)
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -I[--input_dir] is "Input CSV directory."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -I C:\Python27\data_migrator_1239\test\v101\data\ora_data_dir ^
  -y 50 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 73
Use case name: CSV_ShardedFileSkip1_to_ORA_Partition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 74
Use case name: CSV_ShardedFileSkip1_to_ORA_Partition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 75
Use case name: CSV_ShardedFileSkip1_to_ORA_Subpartition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 76
Use case name: CSV_ShardedFileSkip1_to_ORA_Subpartition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 77
Use case name: CSV_ShardedFileSkip1_to_ORA_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 78
Use case name: CSV_ShardedFileSkip1_to_ORA_Table_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 79
Use case name: CSV_ShardedFileSkip1_to_ORA_Table_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 80
Use case name: CSV_ShardedFileSkip1_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Skip 1 rows and load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -k[--skip_rows] is "Header size. Number of rows to skip in input file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -k 1 ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 81
Use case name: CSV_ShardedFile_Limit10_to_ORA_Partition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 82
Use case name: CSV_ShardedFile_Limit10_to_ORA_Partition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 83
Use case name: CSV_ShardedFile_Limit10_to_ORA_Subpartition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 84
Use case name: CSV_ShardedFile_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 85
Use case name: CSV_ShardedFile_Limit10_to_ORA_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 86
Use case name: CSV_ShardedFile_Limit10_to_ORA_Table_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 87
Use case name: CSV_ShardedFile_Limit10_to_ORA_Table_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 88
Use case name: CSV_ShardedFile_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load only 10 rows from CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 89
Use case name: CSV_ShardedFile_to_ORA_Partition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 90
Use case name: CSV_ShardedFile_to_ORA_Partition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 91
Use case name: CSV_ShardedFile_to_ORA_Subpartition
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 92
Use case name: CSV_ShardedFile_to_ORA_Subpartition_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 93
Use case name: CSV_ShardedFile_to_ORA_Table
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 94
Use case name: CSV_ShardedFile_to_ORA_Table_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 95
Use case name: CSV_ShardedFile_to_ORA_Table_TruncateTarget
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 96
Use case name: CSV_ShardedFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input CSV file into 3 logical partitions (-r[--num_of_shards] 3) 
	  and run load process on each shard in thread pool (-o[--pool_size] 3).
	  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 10 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 97
Use case name: CSV_TimestampFile_to_ORA_Partition
Description:  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 98
Use case name: CSV_TimestampFile_to_ORA_Partition_TruncateTarget
Description:  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 99
Use case name: CSV_TimestampFile_to_ORA_Subpartition
Description:  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 100
Use case name: CSV_TimestampFile_to_ORA_Subpartition_TruncateTarget
Description:  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 101
Use case name: CSV_TimestampFile_to_ORA_Table
Description:  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 102
Use case name: CSV_TimestampFile_to_ORA_Table_NoClient
Description:  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 103
Use case name: CSV_TimestampFile_to_ORA_Table_TruncateTarget
Description:  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 104
Use case name: CSV_TimestampFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_ts.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 105
Use case name: CSV_TimezoneFile_to_ORA_Partition
Description:  Load CSV file into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 106
Use case name: CSV_TimezoneFile_to_ORA_Partition_TruncateTarget
Description:  Load CSV file into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 107
Use case name: CSV_TimezoneFile_to_ORA_Subpartition
Description:  Load CSV file into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 108
Use case name: CSV_TimezoneFile_to_ORA_Subpartition_TruncateTarget
Description:  Load CSV file into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 109
Use case name: CSV_TimezoneFile_to_ORA_Table
Description:  Load CSV file into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 110
Use case name: CSV_TimezoneFile_to_ORA_Table_NoClient
Description:  Load CSV file into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 111
Use case name: CSV_TimezoneFile_to_ORA_Table_TruncateTarget
Description:  Load CSV file into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 112
Use case name: CSV_TimezoneFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Load CSV file into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -i[--input_file] is "Input CSV file."
  -y[--shard_size_kb] is "Shard size in KBytes (to partition file and to estimate number of lines in input CSV file)."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w csv2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -i C:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0_tz.data ^
  -y 1000 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 113
Use case name: ORA_DateTable_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 114
Use case name: ORA_DateTable_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 115
Use case name: ORA_DateTable_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_DateTable.data

-USE-CASE # 116
Use case name: ORA_Partition_Limit10_to_CSV_Default
Description:  Extract only 10 rows from Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 117
Use case name: ORA_Partition_Limit10_to_CSV_Dir
Description:  Extract only 10 rows from Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 118
Use case name: ORA_Partition_Limit10_to_CSV_File
Description:  Extract only 10 rows from Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_Limit10.data

-USE-CASE # 119
Use case name: ORA_Partition_NoClient_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 120
Use case name: ORA_Partition_NoClient_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 121
Use case name: ORA_Partition_NoClient_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_NoClient.data

-USE-CASE # 122
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 123
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 124
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_TruncateTarget_AskToTruncate.data

-USE-CASE # 125
Use case name: ORA_Partition_Validate_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 126
Use case name: ORA_Partition_Validate_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 127
Use case name: ORA_Partition_Validate_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_Validate.data

-USE-CASE # 128
Use case name: ORA_Partition_keepWhitespace_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 129
Use case name: ORA_Partition_keepWhitespace_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 130
Use case name: ORA_Partition_keepWhitespace_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_keepWhitespace.data

-USE-CASE # 131
Use case name: ORA_Partition_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 132
Use case name: ORA_Partition_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 133
Use case name: ORA_Partition_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition.data

-USE-CASE # 134
Use case name: ORA_Partition_trimWhitespace_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 135
Use case name: ORA_Partition_trimWhitespace_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 136
Use case name: ORA_Partition_trimWhitespace_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_trimWhitespace.data

-USE-CASE # 137
Use case name: ORA_Partition_withHeader_to_CSV_Default
Description:  Extract Oracle partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1

-USE-CASE # 138
Use case name: ORA_Partition_withHeader_to_CSV_Dir
Description:  Extract Oracle partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 139
Use case name: ORA_Partition_withHeader_to_CSV_File
Description:  Extract Oracle partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Partition_withHeader.data

-USE-CASE # 140
Use case name: ORA_QueryDir_Limit10_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 141
Use case name: ORA_QueryDir_Limit10_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 142
Use case name: ORA_QueryDir_Limit10_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract only 10 rows from Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryDir_Limit10.data

-USE-CASE # 143
Use case name: ORA_QueryDir_keepWhitespace_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 144
Use case name: ORA_QueryDir_keepWhitespace_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 145
Use case name: ORA_QueryDir_keepWhitespace_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryDir_keepWhitespace.data

-USE-CASE # 146
Use case name: ORA_QueryDir_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 147
Use case name: ORA_QueryDir_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 148
Use case name: ORA_QueryDir_trimWhitespace_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 149
Use case name: ORA_QueryDir_trimWhitespace_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 150
Use case name: ORA_QueryDir_trimWhitespace_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryDir_trimWhitespace.data

-USE-CASE # 151
Use case name: ORA_QueryDir_trimWhitespace_withHeader_to_CSV_Default
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1

-USE-CASE # 152
Use case name: ORA_QueryDir_trimWhitespace_withHeader_to_CSV_Dir
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 153
Use case name: ORA_QueryDir_trimWhitespace_withHeader_to_CSV_File
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryDir_trimWhitespace_withHeader.data

-USE-CASE # 154
Use case name: ORA_QueryFile_Limit10_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 155
Use case name: ORA_QueryFile_Limit10_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 156
Use case name: ORA_QueryFile_Limit10_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract only 10 rows from Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_Limit10.data

-USE-CASE # 157
Use case name: ORA_QueryFile_keepWhitespace_noHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 158
Use case name: ORA_QueryFile_keepWhitespace_noHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 159
Use case name: ORA_QueryFile_keepWhitespace_noHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_keepWhitespace_noHeader.data

-USE-CASE # 160
Use case name: ORA_QueryFile_keepWhitespace_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 161
Use case name: ORA_QueryFile_keepWhitespace_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 162
Use case name: ORA_QueryFile_keepWhitespace_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_keepWhitespace.data

-USE-CASE # 163
Use case name: ORA_QueryFile_keepWhitespace_withHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1

-USE-CASE # 164
Use case name: ORA_QueryFile_keepWhitespace_withHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 165
Use case name: ORA_QueryFile_keepWhitespace_withHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_keepWhitespace_withHeader.data

-USE-CASE # 166
Use case name: ORA_QueryFile_noHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 167
Use case name: ORA_QueryFile_noHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 168
Use case name: ORA_QueryFile_noHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_noHeader.data

-USE-CASE # 169
Use case name: ORA_QueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 170
Use case name: ORA_QueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 171
Use case name: ORA_QueryFile_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile.data

-USE-CASE # 172
Use case name: ORA_QueryFile_trimWhitespace_noHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 173
Use case name: ORA_QueryFile_trimWhitespace_noHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 174
Use case name: ORA_QueryFile_trimWhitespace_noHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_trimWhitespace_noHeader.data

-USE-CASE # 175
Use case name: ORA_QueryFile_trimWhitespace_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 176
Use case name: ORA_QueryFile_trimWhitespace_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 177
Use case name: ORA_QueryFile_trimWhitespace_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_trimWhitespace.data

-USE-CASE # 178
Use case name: ORA_QueryFile_trimWhitespace_withHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1

-USE-CASE # 179
Use case name: ORA_QueryFile_trimWhitespace_withHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 180
Use case name: ORA_QueryFile_trimWhitespace_withHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_trimWhitespace_withHeader.data

-USE-CASE # 181
Use case name: ORA_QueryFile_withHeader_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1

-USE-CASE # 182
Use case name: ORA_QueryFile_withHeader_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 183
Use case name: ORA_QueryFile_withHeader_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_QueryFile_withHeader.data

-USE-CASE # 184
Use case name: ORA_ShardedPartition_Limit10_to_CSV_Default
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 185
Use case name: ORA_ShardedPartition_Limit10_to_CSV_Dir
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 186
Use case name: ORA_ShardedPartition_to_CSV_Default
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 187
Use case name: ORA_ShardedPartition_to_CSV_Dir
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 188
Use case name: ORA_ShardedSubpartition_Limit10_to_CSV_Default
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 189
Use case name: ORA_ShardedSubpartition_Limit10_to_CSV_Dir
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle sharded sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 190
Use case name: ORA_ShardedSubpartition_to_CSV_Default
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 191
Use case name: ORA_ShardedSubpartition_to_CSV_Dir
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle sharded sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 192
Use case name: ORA_ShardedTable_Limit10_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 193
Use case name: ORA_ShardedTable_Limit10_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract only 10 rows from Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 194
Use case name: ORA_ShardedTable_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 195
Use case name: ORA_ShardedTable_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 196
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_CSV_Default
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 197
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_CSV_Dir
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run extract process on each shard in thread pool (-o[--pool_size] 3).
	  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 198
Use case name: ORA_Subpartition_Limit10_to_CSV_Default
Description:  Extract only 10 rows from Oracle sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 199
Use case name: ORA_Subpartition_Limit10_to_CSV_Dir
Description:  Extract only 10 rows from Oracle sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 200
Use case name: ORA_Subpartition_Limit10_to_CSV_File
Description:  Extract only 10 rows from Oracle sub-partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Subpartition_Limit10.data

-USE-CASE # 201
Use case name: ORA_Subpartition_Validate_to_CSV_Default
Description:  Extract Oracle sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 202
Use case name: ORA_Subpartition_Validate_to_CSV_Dir
Description:  Extract Oracle sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 203
Use case name: ORA_Subpartition_Validate_to_CSV_File
Description:  Extract Oracle sub-partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Subpartition_Validate.data

-USE-CASE # 204
Use case name: ORA_Subpartition_to_CSV_Default
Description:  Extract Oracle sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 205
Use case name: ORA_Subpartition_to_CSV_Dir
Description:  Extract Oracle sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 206
Use case name: ORA_Subpartition_to_CSV_File
Description:  Extract Oracle sub-partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Subpartition.data

-USE-CASE # 207
Use case name: ORA_Subpartition_trimWhitespace_to_CSV_Default
Description:  Extract Oracle sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 208
Use case name: ORA_Subpartition_trimWhitespace_to_CSV_Dir
Description:  Extract Oracle sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 209
Use case name: ORA_Subpartition_trimWhitespace_to_CSV_File
Description:  Extract Oracle sub-partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Subpartition_trimWhitespace.data

-USE-CASE # 210
Use case name: ORA_Subpartition_withHeader_to_CSV_Default
Description:  Extract Oracle sub-partition into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1

-USE-CASE # 211
Use case name: ORA_Subpartition_withHeader_to_CSV_Dir
Description:  Extract Oracle sub-partition into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 212
Use case name: ORA_Subpartition_withHeader_to_CSV_File
Description:  Extract Oracle sub-partition into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Subpartition_withHeader.data

-USE-CASE # 213
Use case name: ORA_Table_Limit10_to_CSV_Default
Description:  Extract only 10 rows from Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 214
Use case name: ORA_Table_Limit10_to_CSV_Dir
Description:  Extract only 10 rows from Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 215
Use case name: ORA_Table_Limit10_to_CSV_File
Description:  Extract only 10 rows from Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_Table_Limit10.data

-USE-CASE # 216
Use case name: ORA_TimestampTable_keepWhitespace_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 217
Use case name: ORA_TimestampTable_keepWhitespace_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 218
Use case name: ORA_TimestampTable_keepWhitespace_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimestampTable_keepWhitespace.data

-USE-CASE # 219
Use case name: ORA_TimestampTable_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 220
Use case name: ORA_TimestampTable_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 221
Use case name: ORA_TimestampTable_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimestampTable.data

-USE-CASE # 222
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1

-USE-CASE # 223
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 224
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimestampTable_trimWhitespace_Validate.data

-USE-CASE # 225
Use case name: ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1

-USE-CASE # 226
Use case name: ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 227
Use case name: ORA_TimestampTable_trimWhitespace_withHeader_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -W 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimestampTable_trimWhitespace_withHeader.data

-USE-CASE # 228
Use case name: ORA_TimestampTable_withHeader_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1

-USE-CASE # 229
Use case name: ORA_TimestampTable_withHeader_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 230
Use case name: ORA_TimestampTable_withHeader_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -A[--header] is "Include header to Oracle extract."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -A 1 ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimestampTable_withHeader.data

-USE-CASE # 231
Use case name: ORA_TimezoneQueryFile_to_CSV_Default
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 232
Use case name: ORA_TimezoneQueryFile_to_CSV_Dir
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 233
Use case name: ORA_TimezoneQueryFile_to_CSV_File
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Extract Oracle query results into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimezoneQueryFile.data

-USE-CASE # 234
Use case name: ORA_TimezoneTable_to_CSV_Default
Description:  Extract Oracle table into CSV Default location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 235
Use case name: ORA_TimezoneTable_to_CSV_Dir
Description:  Extract Oracle table into CSV Dir location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -D[--to_dir] is "To directory."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -D C:\Python27\data_migrator_1239\CSV_OUT

-USE-CASE # 236
Use case name: ORA_TimezoneTable_to_CSV_File
Description:  Extract Oracle table into CSV File location.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_file] is "To CSV file."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2csv ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY/MM/DD" ^
  -m "YYYY-MM-DD-HH24.MI.SS.FF" ^
  -O "YYYY-MM-DD-HH24:MI:SS.FF" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g C:\Python27\data_migrator_1239\CSV_OUT\testORA_TimezoneTable.data

-USE-CASE # 237
Use case name: ORA_DateTable_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 238
Use case name: ORA_DateTable_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 239
Use case name: ORA_DateTable_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 240
Use case name: ORA_DateTable_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 241
Use case name: ORA_DateTable_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 242
Use case name: ORA_DateTable_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 243
Use case name: ORA_DateTable_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 244
Use case name: ORA_DateTable_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Date_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Date_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 245
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 246
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 247
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 248
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 249
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 250
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 251
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 252
Use case name: ORA_Partition_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 253
Use case name: ORA_Partition_Limit10_to_ORA_Partition
Description:  Copy only 10 rows from Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 254
Use case name: ORA_Partition_Limit10_to_ORA_Partition_TruncateTarget
Description:  Copy only 10 rows from Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 255
Use case name: ORA_Partition_Limit10_to_ORA_Subpartition
Description:  Copy only 10 rows from Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 256
Use case name: ORA_Partition_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Copy only 10 rows from Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 257
Use case name: ORA_Partition_Limit10_to_ORA_Table
Description:  Copy only 10 rows from Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 258
Use case name: ORA_Partition_Limit10_to_ORA_Table_NoClient
Description:  Copy only 10 rows from Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 259
Use case name: ORA_Partition_Limit10_to_ORA_Table_TruncateTarget
Description:  Copy only 10 rows from Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 260
Use case name: ORA_Partition_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy only 10 rows from Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 261
Use case name: ORA_Partition_NoClient_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 262
Use case name: ORA_Partition_NoClient_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 263
Use case name: ORA_Partition_NoClient_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 264
Use case name: ORA_Partition_NoClient_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 265
Use case name: ORA_Partition_NoClient_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 266
Use case name: ORA_Partition_NoClient_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 267
Use case name: ORA_Partition_NoClient_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 268
Use case name: ORA_Partition_NoClient_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 269
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 270
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 271
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 272
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 273
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 274
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 275
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 276
Use case name: ORA_Partition_TruncateTarget_AskToTruncate_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -E[--ask_to_truncate] is "Ask to truncate."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -E 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 277
Use case name: ORA_Partition_Validate_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 278
Use case name: ORA_Partition_Validate_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 279
Use case name: ORA_Partition_Validate_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 280
Use case name: ORA_Partition_Validate_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 281
Use case name: ORA_Partition_Validate_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 282
Use case name: ORA_Partition_Validate_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 283
Use case name: ORA_Partition_Validate_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 284
Use case name: ORA_Partition_Validate_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 285
Use case name: ORA_Partition_keepWhitespace_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 286
Use case name: ORA_Partition_keepWhitespace_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 287
Use case name: ORA_Partition_keepWhitespace_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 288
Use case name: ORA_Partition_keepWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 289
Use case name: ORA_Partition_keepWhitespace_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 290
Use case name: ORA_Partition_keepWhitespace_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 291
Use case name: ORA_Partition_keepWhitespace_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 292
Use case name: ORA_Partition_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 293
Use case name: ORA_Partition_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 294
Use case name: ORA_Partition_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 295
Use case name: ORA_Partition_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 296
Use case name: ORA_Partition_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 297
Use case name: ORA_Partition_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 298
Use case name: ORA_Partition_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 299
Use case name: ORA_Partition_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 300
Use case name: ORA_Partition_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 301
Use case name: ORA_Partition_trimWhitespace_to_ORA_Partition
Description:  Copy Oracle partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 302
Use case name: ORA_Partition_trimWhitespace_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 303
Use case name: ORA_Partition_trimWhitespace_to_ORA_Subpartition
Description:  Copy Oracle partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 304
Use case name: ORA_Partition_trimWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 305
Use case name: ORA_Partition_trimWhitespace_to_ORA_Table
Description:  Copy Oracle partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 306
Use case name: ORA_Partition_trimWhitespace_to_ORA_Table_NoClient
Description:  Copy Oracle partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 307
Use case name: ORA_Partition_trimWhitespace_to_ORA_Table_TruncateTarget
Description:  Copy Oracle partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 308
Use case name: ORA_Partition_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 309
Use case name: ORA_QueryDir_Limit10_to_ORA_Partition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 310
Use case name: ORA_QueryDir_Limit10_to_ORA_Partition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 311
Use case name: ORA_QueryDir_Limit10_to_ORA_Subpartition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 312
Use case name: ORA_QueryDir_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 313
Use case name: ORA_QueryDir_Limit10_to_ORA_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 314
Use case name: ORA_QueryDir_Limit10_to_ORA_Table_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 315
Use case name: ORA_QueryDir_Limit10_to_ORA_Table_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 316
Use case name: ORA_QueryDir_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 317
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Partition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 318
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Partition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 319
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Subpartition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 320
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 321
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 322
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Table_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 323
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Table_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 324
Use case name: ORA_QueryDir_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 325
Use case name: ORA_QueryDir_to_ORA_Partition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 326
Use case name: ORA_QueryDir_to_ORA_Partition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 327
Use case name: ORA_QueryDir_to_ORA_Subpartition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 328
Use case name: ORA_QueryDir_to_ORA_Subpartition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 329
Use case name: ORA_QueryDir_to_ORA_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 330
Use case name: ORA_QueryDir_to_ORA_Table_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 331
Use case name: ORA_QueryDir_to_ORA_Table_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 332
Use case name: ORA_QueryDir_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 333
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Partition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 334
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Partition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 335
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Subpartition
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 336
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 337
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Table
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 338
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Table_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 339
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Table_TruncateTarget
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 340
Use case name: ORA_QueryDir_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Read each SQL query file from a directory "C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -Q[--query_sql_dir] is "Input dir with Oracle query files sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -Q C:\Python27\data_migrator_1239\test\v101\query\query_dir_ora ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 341
Use case name: ORA_QueryFile_Limit10_to_ORA_Partition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 342
Use case name: ORA_QueryFile_Limit10_to_ORA_Partition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 343
Use case name: ORA_QueryFile_Limit10_to_ORA_Subpartition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 344
Use case name: ORA_QueryFile_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 345
Use case name: ORA_QueryFile_Limit10_to_ORA_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 346
Use case name: ORA_QueryFile_Limit10_to_ORA_Table_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 347
Use case name: ORA_QueryFile_Limit10_to_ORA_Table_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 348
Use case name: ORA_QueryFile_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy only 10 rows from Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 349
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Partition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 350
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Partition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 351
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Subpartition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 352
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 353
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 354
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Table_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 355
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Table_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 356
Use case name: ORA_QueryFile_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 357
Use case name: ORA_QueryFile_to_ORA_Partition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 358
Use case name: ORA_QueryFile_to_ORA_Partition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 359
Use case name: ORA_QueryFile_to_ORA_Subpartition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 360
Use case name: ORA_QueryFile_to_ORA_Subpartition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 361
Use case name: ORA_QueryFile_to_ORA_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 362
Use case name: ORA_QueryFile_to_ORA_Table_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 363
Use case name: ORA_QueryFile_to_ORA_Table_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 364
Use case name: ORA_QueryFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 365
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Partition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 366
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Partition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 367
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Subpartition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 368
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 369
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 370
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Table_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 371
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Table_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 372
Use case name: ORA_QueryFile_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 373
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Partition
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 374
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Partition_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 375
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Subpartition
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 376
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 377
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Table
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 378
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Table_NoClient
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 379
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Table_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 380
Use case name: ORA_ShardedPartition_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 381
Use case name: ORA_ShardedPartition_to_ORA_Partition
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 382
Use case name: ORA_ShardedPartition_to_ORA_Partition_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 383
Use case name: ORA_ShardedPartition_to_ORA_Subpartition
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 384
Use case name: ORA_ShardedPartition_to_ORA_Subpartition_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 385
Use case name: ORA_ShardedPartition_to_ORA_Table
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 386
Use case name: ORA_ShardedPartition_to_ORA_Table_NoClient
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 387
Use case name: ORA_ShardedPartition_to_ORA_Table_TruncateTarget
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 388
Use case name: ORA_ShardedPartition_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input sharded partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -P[--from_partition] is "From partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Partitioned_test_from ^
  -P part_15 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 389
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Partition
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 390
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Partition_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 391
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Subpartition
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 392
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 393
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Table
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 394
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Table_NoClient
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 395
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Table_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 396
Use case name: ORA_ShardedSubpartition_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle sharded sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 397
Use case name: ORA_ShardedSubpartition_to_ORA_Partition
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 398
Use case name: ORA_ShardedSubpartition_to_ORA_Partition_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 399
Use case name: ORA_ShardedSubpartition_to_ORA_Subpartition
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 400
Use case name: ORA_ShardedSubpartition_to_ORA_Subpartition_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 401
Use case name: ORA_ShardedSubpartition_to_ORA_Table
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 402
Use case name: ORA_ShardedSubpartition_to_ORA_Table_NoClient
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 403
Use case name: ORA_ShardedSubpartition_to_ORA_Table_TruncateTarget
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 404
Use case name: ORA_ShardedSubpartition_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input sharded sub-partition into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle sharded sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 405
Use case name: ORA_ShardedTable_Limit10_to_ORA_Partition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 406
Use case name: ORA_ShardedTable_Limit10_to_ORA_Partition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 407
Use case name: ORA_ShardedTable_Limit10_to_ORA_Subpartition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 408
Use case name: ORA_ShardedTable_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 409
Use case name: ORA_ShardedTable_Limit10_to_ORA_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 410
Use case name: ORA_ShardedTable_Limit10_to_ORA_Table_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 411
Use case name: ORA_ShardedTable_Limit10_to_ORA_Table_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 412
Use case name: ORA_ShardedTable_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 413
Use case name: ORA_ShardedTable_to_ORA_Partition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 414
Use case name: ORA_ShardedTable_to_ORA_Partition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 415
Use case name: ORA_ShardedTable_to_ORA_Subpartition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 416
Use case name: ORA_ShardedTable_to_ORA_Subpartition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 417
Use case name: ORA_ShardedTable_to_ORA_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 418
Use case name: ORA_ShardedTable_to_ORA_Table_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 419
Use case name: ORA_ShardedTable_to_ORA_Table_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 420
Use case name: ORA_ShardedTable_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 421
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Partition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 422
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Partition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 423
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Subpartition
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 424
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Subpartition_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 425
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 426
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 427
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 428
Use case name: ORA_ShardedTimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget_NoClient
Description:  Break input table into 3 logical shards (-r[--num_of_shards] 3) 
	  and run copy process on each shard in thread pool (-o[--pool_size] 3).
	  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 3 ^
  -r 3 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 429
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Partition
Description:  Copy Oracle sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 430
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 431
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Subpartition
Description:  Copy Oracle sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 432
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 433
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Table
Description:  Copy Oracle sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 434
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Table_NoClient
Description:  Copy Oracle sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 435
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Table_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 436
Use case name: ORA_Subpartition_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 437
Use case name: ORA_Subpartition_Limit10_to_ORA_Partition
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 438
Use case name: ORA_Subpartition_Limit10_to_ORA_Partition_TruncateTarget
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 439
Use case name: ORA_Subpartition_Limit10_to_ORA_Subpartition
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 440
Use case name: ORA_Subpartition_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 441
Use case name: ORA_Subpartition_Limit10_to_ORA_Table
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 442
Use case name: ORA_Subpartition_Limit10_to_ORA_Table_NoClient
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 443
Use case name: ORA_Subpartition_Limit10_to_ORA_Table_TruncateTarget
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 444
Use case name: ORA_Subpartition_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy only 10 rows from Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 445
Use case name: ORA_Subpartition_Validate_to_ORA_Partition
Description:  Copy Oracle sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 446
Use case name: ORA_Subpartition_Validate_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 447
Use case name: ORA_Subpartition_Validate_to_ORA_Subpartition
Description:  Copy Oracle sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 448
Use case name: ORA_Subpartition_Validate_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 449
Use case name: ORA_Subpartition_Validate_to_ORA_Table
Description:  Copy Oracle sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 450
Use case name: ORA_Subpartition_Validate_to_ORA_Table_NoClient
Description:  Copy Oracle sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 451
Use case name: ORA_Subpartition_Validate_to_ORA_Table_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 452
Use case name: ORA_Subpartition_Validate_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 453
Use case name: ORA_Subpartition_to_ORA_Partition
Description:  Copy Oracle sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 454
Use case name: ORA_Subpartition_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 455
Use case name: ORA_Subpartition_to_ORA_Subpartition
Description:  Copy Oracle sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 456
Use case name: ORA_Subpartition_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 457
Use case name: ORA_Subpartition_to_ORA_Table
Description:  Copy Oracle sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 458
Use case name: ORA_Subpartition_to_ORA_Table_NoClient
Description:  Copy Oracle sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 459
Use case name: ORA_Subpartition_to_ORA_Table_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 460
Use case name: ORA_Subpartition_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 461
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Partition
Description:  Copy Oracle sub-partition into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 462
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 463
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Subpartition
Description:  Copy Oracle sub-partition into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 464
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 465
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Table
Description:  Copy Oracle sub-partition into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 466
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Table_NoClient
Description:  Copy Oracle sub-partition into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 467
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Table_TruncateTarget
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 468
Use case name: ORA_Subpartition_trimWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle sub-partition into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -S[--from_sub_partition] is "From sub-partition."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Sub_Partitioned_test_from ^
  -S part_15_sp1 ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 469
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 470
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 471
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 472
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 473
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 474
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 475
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 476
Use case name: ORA_Table_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 477
Use case name: ORA_Table_Limit10_to_ORA_Partition
Description:  Copy only 10 rows from Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 478
Use case name: ORA_Table_Limit10_to_ORA_Partition_TruncateTarget
Description:  Copy only 10 rows from Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 479
Use case name: ORA_Table_Limit10_to_ORA_Subpartition
Description:  Copy only 10 rows from Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 480
Use case name: ORA_Table_Limit10_to_ORA_Subpartition_TruncateTarget
Description:  Copy only 10 rows from Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 481
Use case name: ORA_Table_Limit10_to_ORA_Table
Description:  Copy only 10 rows from Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 482
Use case name: ORA_Table_Limit10_to_ORA_Table_NoClient
Description:  Copy only 10 rows from Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 483
Use case name: ORA_Table_Limit10_to_ORA_Table_TruncateTarget
Description:  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 484
Use case name: ORA_Table_Limit10_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy only 10 rows from Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -l[--lame_duck] is "Limit rows (lame duck run)."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -l 10 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 485
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 486
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 487
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 488
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 489
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 490
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 491
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 492
Use case name: ORA_TimestampTable_keepWhitespace_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 493
Use case name: ORA_TimestampTable_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 494
Use case name: ORA_TimestampTable_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 495
Use case name: ORA_TimestampTable_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 496
Use case name: ORA_TimestampTable_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 497
Use case name: ORA_TimestampTable_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 498
Use case name: ORA_TimestampTable_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 499
Use case name: ORA_TimestampTable_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 500
Use case name: ORA_TimestampTable_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 501
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 502
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 503
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 504
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 505
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 506
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 507
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 508
Use case name: ORA_TimestampTable_trimWhitespace_Validate_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -V[--validate] is "Check if source and target objects exist."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -W[--trim_whitespace] is "Trim whitespace from varchar2 in "Oracle" extract."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -V 1 ^
  -U 1 ^
  -c SCOTT.Timestamp_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -W 1 ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timestamp_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 509
Use case name: ORA_TimezoneQueryFile_to_ORA_Partition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 510
Use case name: ORA_TimezoneQueryFile_to_ORA_Partition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 511
Use case name: ORA_TimezoneQueryFile_to_ORA_Subpartition
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 512
Use case name: ORA_TimezoneQueryFile_to_ORA_Subpartition_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 513
Use case name: ORA_TimezoneQueryFile_to_ORA_Table
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 514
Use case name: ORA_TimezoneQueryFile_to_ORA_Table_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 515
Use case name: ORA_TimezoneQueryFile_to_ORA_Table_TruncateTarget
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 516
Use case name: ORA_TimezoneQueryFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Read SQL from a query file "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql".
	  Copy Oracle query results into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -q[--query_sql_file] is "Input file with Oracle query sql."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -q C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 517
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 518
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 519
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 520
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 521
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 522
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 523
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 524
Use case name: ORA_TimezoneTable_KeepSpoolFile_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -K[--keep_data_file] is "Keep data dump."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -K 1 ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 525
Use case name: ORA_TimezoneTable_to_ORA_Partition
Description:  Copy Oracle table into Oracle Partition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 526
Use case name: ORA_TimezoneTable_to_ORA_Partition_TruncateTarget
Description:  Copy Oracle table into Oracle Partition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -G[--to_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Partitioned_test_to ^
  -G part_15 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 527
Use case name: ORA_TimezoneTable_to_ORA_Subpartition
Description:  Copy Oracle table into Oracle Subpartition table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 528
Use case name: ORA_TimezoneTable_to_ORA_Subpartition_TruncateTarget
Description:  Copy Oracle table into Oracle Subpartition TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -N[--to_sub_partition] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Sub_Partitioned_test_to ^
  -N part_15_sp1 ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 529
Use case name: ORA_TimezoneTable_to_ORA_Table
Description:  Copy Oracle table into Oracle Table table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 530
Use case name: ORA_TimezoneTable_to_ORA_Table_NoClient
Description:  Copy Oracle table into Oracle Table NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  echo y|C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 531
Use case name: ORA_TimezoneTable_to_ORA_Table_TruncateTarget
Description:  Copy Oracle table into Oracle Table TruncateTarget table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@orcl ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"

-USE-CASE # 532
Use case name: ORA_TimezoneTable_to_ORA_Table_TruncateTarget_NoClient
Description:  Copy Oracle table into Oracle Table TruncateTarget NoClient table.
Arguments:
  -w[--copy_vector] is "Data copy direction."
  -o[--pool_size] is "Pool size."
  -r[--num_of_shards] is "Number of shards."
  -t[--field_term] is "Field terminator."
  -U[--truncate_target] is "Truncate target table/partition/subpartition."
  -c[--from_table] is "From table."
  -f[--from_db] is "From database."
  -e[--nls_date_format] is "nls_date_format for source."
  -m[--nls_timestamp_format] is "nls_timestamp_format for source."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for source."
  -z[--source_client_home] is "Path to Oracle client home."
  -g[--to_db] is "To Oracle database."
  -a[--to_table] is "To Oracle table."
  -e[--nls_date_format] is "nls_date_format for target."
  -m[--nls_timestamp_format] is "nls_timestamp_format for target."
  -O[--nls_timestamp_tz_format] is "nls_timestamp_tz_format for target."
  -Z[--target_client_home] is "Path to Oracle client home bin dir."	
Example: 
  python -c "print 'y\ny'" |C:\Python27\dm_dist_32\20150112_051420\dm32\dm32.exe ^
  -w ora2ora ^
  -o 1 ^
  -r 1 ^
  -t "|" ^
  -U 1 ^
  -c SCOTT.Timezone_test_from ^
  -f SCOTT/tiger2@orcl ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
  -g SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))' ^
  -a SCOTT.Timezone_test_to ^
  -e "YYYY-MM-DD HH24.MI.SS" ^
  -m "YYYY-MM-DD HH24.MI.SS.FF2" ^
  -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
  -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"