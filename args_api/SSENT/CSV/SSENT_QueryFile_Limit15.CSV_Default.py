# Title:	SSENT_QueryFile_Limit15 -->> CSV_Default
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'lame_duck': ('-l', '--lame_duck', 15, 'Limit rows (lame duck run).'), 'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'ssent2csv', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'query_sql_file': ('-q', '--query_sql_file', 'c:\\Python27\\data_migrator_1239\\test\\v101\\query\\ss_query.sql', 'Input file with SQL Server Enterprise query sql.'), 'from_db_name': ('-b', '--from_db_name', 'test', 'SQL Server Enterprise source database.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\110\\Tools\\Binn"', 'Path to SQL Server Enterprise client home.'), 'from_user': ('-j', '--from_user', 'sa', 'SQL Server Enterprise source user.'), 'from_passwd': ('-x', '--from_passwd', 'ssent_pwd', 'SQL Server Enterprise source user password.'), 'from_db_server': ('-n', '--from_db_server', 'ALEX_BUZ-PC\\MSSQLSERVER_ENT', 'SQL Server Enterprise source instance name.')}, 
	{})
	