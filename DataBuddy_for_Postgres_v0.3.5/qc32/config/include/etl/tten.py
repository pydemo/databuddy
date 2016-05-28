#__builtin__ args
import sys, os
from pprint import pprint
from common.v101.base import base 
e=sys.exit
#
# Define your custom options to ttBulkCp.exe command here
#	
# 
class common(base):
	"""Common Oracle methods"""
	def __init__(self,datadir,login,conf):
		self.datadir=datadir
		self.login=login
		self.conf=conf
		#self.db=db
		self.args=conf.args
		self.cr={} #code_release(self.conf, self.args)
		host_map_loc= self.args.host_map
		#print host_map_loc
		#self.hm = hmap.host_map(self.args.copy_vector.split(self.conf._to),host_map_loc,0)
class target(common):
	"""Target Oracle methods"""
	def __init__(self,log,datadir,login,conf,db,to_table):
		common.__init__(self,datadir,login,conf)
		#self.datadir=datadir
		#self.login=login
		self.conf=conf
		self.log=log
		self.db=db.upper()
		self.to_table=to_table
		self.args=conf.args
		self.tab_cols={}
		self.db_client_dbshell=None
		self.ctldir='%s\\sqlloader' % self.datadir
		if not os.path.isdir(self.ctldir):
			os.makedirs(self.ctldir)
		#self.cr={} #code release
	def get_load_config(self,db_client_loc,infile):
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