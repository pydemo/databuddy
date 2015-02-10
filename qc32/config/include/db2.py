#__builtin__ args
from pprint import pprint
#
# Define your custom IMPORT or LOAD command here
#	
# Example of using DB2 LOAD command v.s. INSERT command
USE_LOAD_COMMAND = False
if USE_LOAD_COMMAND:
	def get_load_query(infile):
		global args
		limit=''
		if hasattr(args, 'from_sub_partition') and args.lame_duck:
			limit='ROWCOUNT %s' % args.lame_duck
		out=r"""CONNECT TO SAMPLE  user %s using %s 
	LOAD FROM %s OF DEL modified by COLDEL%s %s INSERT INTO %s
	CONNECT RESET
	""" % (args.to_user, args.to_passwd, infile ,args.field_term,limit,args.to_table.strip().strip(';'))	
		return out
else:
	# Same using DB2 IMPORT command
	def get_load_query(infile):
		global args
		limit=''
		if hasattr(args, 'from_sub_partition') and args.lame_duck:
			limit='ROWCOUNT %s' % args.lame_duck
		out=r"""CONNECT TO SAMPLE  user %s using %s 
	IMPORT FROM %s OF DEL modified by COLDEL%s %s INSERT INTO %s
	CONNECT RESET
	""" % (args.to_user, args.to_passwd, infile ,args.field_term,limit,args.to_table.strip().strip(';'))	
		return out