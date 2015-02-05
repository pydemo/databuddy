# Title:	SLITE_QueryDir -->> SYIQ_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2syiq', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'query_sql_dir': ('-Q', '--query_sql_dir', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\query_dir_slite', 'Input dir with SQL Lite query files sql.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"demo"', 'Target Sybase IQ database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to Sybase IQ client home bin dir.'), 'to_user': ('-u', '--to_user', '"dba"', 'Target Sybase IQ db user.'), 'to_passwd': ('-p', '--to_passwd', '"sql"', 'Target Sybase IQ db user password.'), 'to_db_server': ('-s', '--to_db_server', '"demo16"', 'Target Sybase IQ db instance name.'), 'to_table': ('-a', '--to_table', '"Timestamp_test_to"', 'Target Sybase IQ table.')})
	