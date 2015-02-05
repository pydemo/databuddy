# Title:	SLITE_ShardedTable -->> INFORC_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2inforc', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 3, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"test"', 'Target Informix Innovator C database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM Informix Software Bundle\\bin"', 'Path to Informix Innovator C client home bin dir.'), 'to_user': ('-u', '--to_user', '"informix"', 'Target Informix Innovator C db user.'), 'to_passwd': ('-p', '--to_passwd', '"infor_pwd"', 'Target Informix Innovator C db user password.'), 'to_db_server': ('-s', '--to_db_server', '"ol_s_121414_204157"', 'Target Informix Innovator C db instance name.'), 'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target Informix Innovator C table.')})
	