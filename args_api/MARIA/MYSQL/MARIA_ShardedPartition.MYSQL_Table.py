# Title:	MARIA_ShardedPartition -->> MYSQL_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'maria2mysql', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MariaDB source database.'), 'from_partition': ('-P', '--from_partition', 'rx2015', 'From partition.'), 'from_table': ('-c', '--from_table', 'TEST.Partitioned_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to MariaDB client home.'), 'from_user': ('-j', '--from_user', '"root"', 'MariaDB source user.'), 'from_passwd': ('-x', '--from_passwd', '"maria_pwd"', 'MariaDB source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MariaDB source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target MySQL db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	