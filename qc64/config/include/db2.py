#__builtin__ args
import sys
from common.v101.base import base 
import re, types, os, codecs
from subprocess import Popen, PIPE,STDOUT
from pprint import pprint

e=sys.exit

#
# Define your custom IMPORT or LOAD command here
#	
# Example of using DB2 LOAD command v.s. INSERT command
USE_LOAD_COMMAND = False
if USE_LOAD_COMMAND:
	def get_load_query(infile,):
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
# Define your custom SQL*Loader config
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
		
	# Same using DB2 IMPORT command
	def get_load_query(self, infile, use_load=True):
		global args
		limit=''
		loader ='LOAD'
		if not use_load:
			loader='IMPORT'
		if hasattr(args, 'from_sub_partition') and args.lame_duck:
			limit='ROWCOUNT %s' % args.lame_duck
		out=r"""CONNECT TO SAMPLE  user %s using %s 
	%s FROM %s OF DEL modified by COLDEL%s %s INSERT INTO %s
	CONNECT RESET
	""" % (args.to_user, args.to_passwd, loader, infile ,args.field_term,limit,args.to_table.strip().strip(';'))	
		print(out)
		return out	

		