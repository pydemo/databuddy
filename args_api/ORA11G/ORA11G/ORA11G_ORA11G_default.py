# Title:	Default API.
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
# do not change below this line
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 'Limit rows (lame duck run).'), 'ask_to_truncate': ('-E', '--ask_to_truncate', 'Ask to truncate.'), 'field_term': ('-t', '--field_term', 'Field terminator.'), 'num_of_shards': ('-r', '--num_of_shards', 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 'Pool size.'), 'copy_vector': ('-w', '--copy_vector', 'Data copy direction.'), 'keep_data_file': ('-K', '--keep_data_file', 'Keep data dump.'), 'truncate_target': ('-U', '--truncate_target', 'Truncate target table/partition/subpartition.'), 'validate': ('-V', '--validate', 'Check if source and target objects exist.'), 'arg_1': ('-1', '--arg_1', 'Generic string argument 1.'), 'arg_2': ('-2', '--arg_2', 'Generic string argument 2.'), 'arg_3': ('-3', '--arg_3', 'Generic string argument 3.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'Input file with Oracle query sql.'), 'from_partition': ('-P', '--from_partition', 'From partition.'), 'from_sub_partition': ('-S', '--from_sub_partition', 'From sub-partition.'), 'source_client_home': ('-z', '--source_client_home', 'Path to Oracle client home.'), 'header': ('-A', '--header', 'Include header to Oracle extract.'), 'from_db': ('-f', '--from_db', 'From database.'), 'nls_date_format': ('-e', '--nls_date_format', 'nls_date_format for source.'), 'trim_whitespace': ('-W', '--trim_whitespace', 'Trim whitespace from varchar2 in "Oracle" extract.'), 'nls_timestamp_format': ('-m', '--nls_timestamp_format', 'nls_timestamp_format for source.'), 'nls_timestamp_tz_format': ('-O', '--nls_timestamp_tz_format', 'nls_timestamp_tz_format for source.'), 'from_table': ('-c', '--from_table', 'From table.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'Input dir with Oracle query files sql.')}, 
	{'to_table': ('-a', '--to_table', 'To Oracle table.'), 'to_sub_partition': ('-N', '--to_sub_partition', 'To Oracle table.'), 'to_partition': ('-G', '--to_partition', 'To Oracle table.'), 'to_db': ('-g', '--to_db', 'To Oracle database.'), 'target_client_home': ('-Z', '--target_client_home', 'Path to Oracle client home bin dir.')})
	