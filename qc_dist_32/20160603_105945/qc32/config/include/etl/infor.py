#__builtin__ args
import sys, os
from pprint import pprint
e=sys.exit
#
# Define your custom load query
#	
def get_load_query(infile):
	global args
	
	out=r"""
CONNECT to '%s@%s' user %s using '%s';
LOAD FROM "%s" DELIMITER '%s' INSERT INTO %s;
""" % (args.to_db_name, args.to_db_server, args.to_user, args.to_passwd, os.path.normpath(infile), args.field_term, args.to_table)	
	#pprint(out)
	return out
		
#e(0)