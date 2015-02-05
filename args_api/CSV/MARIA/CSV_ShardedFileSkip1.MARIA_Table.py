# Title:	CSV_ShardedFileSkip1 -->> MARIA_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'csv2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'shard_size_kb': ('-y', '--shard_size_kb', 10, 'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'), 'skip_rows': ('-k', '--skip_rows', 1, 'Header size. Number of rows to skip in input file.'), 'input_file': ('-i', '--input_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\data\\mariadb_shard_0.data', 'Input CSV file.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	