#__builtin__ args
import sys
from pprint import pprint
e=sys.exit
#
# Define your custom load query here
#	
# 
def get_load_query(infile):
	global args
	out="""
BEGIN TRANSACTION;
select 'ROWCOUNT'||count(*) cnt from %s t;
.separator "%s"
.import '%s' %s
select 'ROWCOUNT'||count(*) cnt from %s t;
COMMIT TRANSACTION;
.quit
""" % (args.to_table,args.field_term, infile, args.to_table,args.to_table)
	return out	
#e(0)