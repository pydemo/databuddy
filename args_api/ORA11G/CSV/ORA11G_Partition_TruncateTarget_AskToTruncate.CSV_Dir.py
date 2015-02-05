# Title:	ORA11G_Partition_TruncateTarget_AskToTruncate -->> CSV_Dir
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'ask_to_truncate': ('-E', '--ask_to_truncate', 1, 'Ask to truncate.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'ora11g2csv', 'Data copy direction.'), 'truncate_target': ('-U', '--truncate_target', 1, 'Truncate target table/partition/subpartition.')}, 
	{'from_partition': ('-P', '--from_partition', 'part_15', 'From partition.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"', 'Path to Oracle client home.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', '"YYYY-MM-DD-HH24.MI.SS.FF"', 'nls_timestamp_format for source.'), 'nls_date_format': ('-e', '--nls_date_format', '"YYYY/MM/DD"', 'nls_date_format for source.'), 'from_db': ('-f', '--from_db', 'SCOTT/tiger2@orcl', 'From database.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', '"YYYY-MM-DD-HH24:MI:SS.FF"', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'SCOTT.Partitioned_test_from', 'From table.')}, 
	{'to_dir': ('-D', '--to_dir', 'c:\\Python27\\data_migrator_1239\\CSV_OUT', 'To directory.')})
	