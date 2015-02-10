#__builtin__ args
import sys
from pprint import pprint
e=sys.exit
#
# Define your custom load query
#	
def get_load_query(infile, row_from, row_to):
	global args
	lr=''
	if row_to:
		lr=r""",
	LASTROW = %s""" % row_to
	out=r"""
BULK INSERT %s
FROM '%s'
WITH
  (	
    DATAFILETYPE = 'char',
    FIELDTERMINATOR = '%s',
    ROWTERMINATOR='\n',
	FIRSTROW = %s%s
  );
		""" % (args.to_table, infile,args.field_term,row_from,lr)
	return out
		
#e(0)