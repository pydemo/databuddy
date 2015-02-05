# Title:	SYASE_Table -->> CSV_Dir
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api({'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'), 'copy_vector': ('-w', '--copy_vector', 'syase2csv', 'Data copy direction.'), 'num_of_shards': ('-r', '--num_of_shards', 1, 'Number of shards.'), 'pool_size': ('-o', '--pool_size', 1, 'Pool size.')}, 
	{'from_db_name': ('-b', '--from_db_name', '"demo"', 'SAP Sybase ASE source database.'), 'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'), 'source_client_home': ('-z', '--source_client_home', '"C:\\Program Files\\SQL Anywhere 16\\Bin64"', 'Path to SAP Sybase ASE client home.'), 'from_user': ('-j', '--from_user', '"dba"', 'SAP Sybase ASE source user.'), 'from_passwd': ('-x', '--from_passwd', '"sql"', 'SAP Sybase ASE source user password.'), 'from_db_server': ('-n', '--from_db_server', '"demo16"', 'SAP Sybase ASE source instance name.')}, 
	{'to_dir': ('-D', '--to_dir', 'c:\\Python27\\data_migrator_1239\\CSV_OUT', 'To directory.')})
	