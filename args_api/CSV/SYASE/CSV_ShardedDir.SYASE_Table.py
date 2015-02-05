# Title:	CSV_ShardedDir -->> SYASE_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2syase', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'input_dir': ('-I', '--input_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\sybase_data_dir', 'Input CSV directory.'), 'shard_size_kb': ('-y', '--shard_size_kb', 50, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).')}, 
	{'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target SAP Sybase ASE database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target SAP Sybase ASE db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target SAP Sybase ASE db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target SAP Sybase ASE db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target SAP Sybase ASE table.')})
	