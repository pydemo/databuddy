# Title:	INFOB_TimezoneQueryFile -->> CSV_File
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'infob2csv', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\mysql_query.sql', 'Input file with Infobright query sql.'), 'from_db_name': ('-b', '--from_db_name', '"test"', 'Infobright source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Temp\\mysql\\bin"', 'Path to Infobright client home.'), 'from_user': ('-j', '--from_user', '"alex"', 'Infobright source user.'), 'from_passwd': ('-x', '--from_passwd', '"mysql_pwd"', 'Infobright source user password.'), 'from_db_server': ('-n', '--from_db_server', '"localhost"', 'Infobright source instance name.')}, 
	{'to_file': ('-g', '--to_file', 'c:\\Python27\\data_migrator_1239\\CSV_OUT\\testINFOB_TimezoneQueryFile.data', 'To CSV file.')})
	