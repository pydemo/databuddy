# Title:	SLITE_QueryFile -->> DBTES_Table
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'slite2dbtes', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\sqllite_query.sql', 'Input file with SQL Lite query sql.'), 'from_db_name': ('-b', '--from_db_name', 'C:\\Temp\\SqlLite\\database.db', 'SQL Lite source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\SqlLite"', 'Path to SQL Lite client home.')}, 
	{'to_db_name': ('-d', '--to_db_name', '"SAMPLE"', 'Target DB2 Enterprise Server database.'), 'target_client_home': ('-Z', '--target_client_home', '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"', 'Path to DB2 Enterprise Server client home bin dir.'), 'to_user': ('-u', '--to_user', '"ALEX_BUZ"', 'Target DB2 Enterprise Server db user.'), 'to_passwd': ('-p', '--to_passwd', '"198Morgan"', 'Target DB2 Enterprise Server db user password.'), 'to_db_server': ('-s', '--to_db_server', '"DB2"', 'Target DB2 Enterprise Server db instance name.'), 'to_table': ('-a', '--to_table', 'ALEX_BUZ.Timestamp_test_to', 'Target DB2 Enterprise Server table.')})
	