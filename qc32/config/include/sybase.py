#__builtin__ args
import sys
from pprint import pprint
e=sys.exit
#
# Define your custom load query
#	
def get_load_query(infile):
	global args
	skip=''
	if args.skip_rows:
		skip='SKIP %d' % args.skip_rows

	out ="""INPUT INTO "%s"  DELIMITED BY '%s'  FROM '%s' %s ;\nexit;\n""" % (args.to_table, args.field_term,infile,skip)
	#pprint(out)
	return out
		
#e(0)