# Title:	SLITE_Table_KeepSpoolFile -->> PGRES_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'keep_data_file': ('-K', '--keep_data_file', 1, 'Keep data dump.'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2pgres', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"postgres"', 'Target PostgreSQL database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\PostgreSQL\\9.4\\bin"', 'Path to PostgreSQL client home bin dir.'), 'to_user': ('-u', '--to_user', '"postgres"', 'Target PostgreSQL db user.'), 'to_passwd': ('-p', '--to_passwd', '"postgre_pwd"', 'Target PostgreSQL db user password.'), 'to_db_server': ('-s', '--to_db_server', '"localhost"', 'Target PostgreSQL db instance name.'), 'target_port': ('-T', '--target_port', '5434', 'Connection port for target PostgreSQL.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target PostgreSQL table.')})
	