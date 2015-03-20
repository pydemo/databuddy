#__builtin__ args
import sys
from common.v101.base import base 
from pprint import pprint
e=sys.exit
#

class common(base):
	"""Common Oracle methods"""
	def __init__(self,datadir,login,conf):
		self.datadir=datadir
		self.login=login
		self.conf=conf
		#self.db=db
		self.args=conf.args
		
class source(common):
	"""Source Oracle methods"""
	def __init__(self,datadir,login,conf,db,from_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		#self.conf=conf
		self.db=db
		self.from_table=from_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
	
#
# Define your custom load config
#	
class target(common):
	"""Target Oracle methods"""
	def __init__(self,datadir,login,conf,db,to_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		#self.conf=conf
		self.db=db
		self.to_table=to_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None

	# Define your custom load query
	#	
	def get_load_query(self, infile, row_from, row_to):
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