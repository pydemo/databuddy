# Title:	DBTE_Table -->> INFOB_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'dbte2infob', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"SAMPLE"', 'DB2 Express source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Express client home.'), 'from_user': ('-j', '--from_user', '"ALEX_BUZ"', 'DB2 Express source user.'), 'from_passwd': ('-x', '--from_passwd', '"198Morgan"', 'DB2 Express source user password.'), 'from_db_server': ('-n', '--from_db_server', '"DB2"', 'DB2 Express source instance name.')}, 
	{'to_db_name': ('-d', '--to_db_name', 'test', 'Target database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to mysql client home.'), 'to_user': ('-u', '--to_user', 'alex', 'Target Infobright db user.'), 'to_passwd': ('-p', '--to_passwd', 'mysql_pwd', 'Target db user password.'), 'to_db_server': ('-s', '--to_db_server', 'localhost', 'Target db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.')})
	