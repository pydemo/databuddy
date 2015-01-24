#__builtin__ args
import sys
from pprint import pprint
e=sys.exit
#
# Define your custom options to ttBulkCp.exe command here
#	
# 
def get_load_config(db_client_loc,infile):
	global args
	connect_str= 'UID=%s;PWD=%s;DSN=%s;' % (args.to_user, args.to_passwd, args.to_DSN_name)
	
	loadConf=[  db_client_loc , '-i' , 			 
			'-dformat',  args.nls_date_format, 
			'-tsformat', args.nls_timestamp_format, 
			'-s', '^%s' % args.field_term, 
			'-Q','0',
			#'-F','3',
			#'-L', '110',	
			'-connstr', connect_str,
			 args.to_table,
			infile]
	return loadConf
		
#e(0)