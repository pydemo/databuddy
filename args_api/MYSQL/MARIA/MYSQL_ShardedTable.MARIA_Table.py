# Title:	MYSQL_ShardedTable -->> MARIA_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'mysql2maria', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"test"', 'MySQL source database.'), 'from_table': ('-c', '--from_table', 'TEST.Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to MySQL client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'MySQL source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'MySQL source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'MySQL source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\MariaDB 10.0\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.'), 'to_passwd': ('-p', '--to_passwd', '"maria_pwd"', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	