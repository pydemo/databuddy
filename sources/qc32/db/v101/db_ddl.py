import types, re, os
from subprocess import Popen, PIPE
from common.v101.base import base 
import codecs, tempfile
class DDL(base):
	"""DDL file"""
	def __init__(self,log,csv_dir,datadir):
		base.__init__(self, log)
		self.log=log
		self.csv_dir=csv_dir
		self.datadir=datadir
		self.tab_cols={}
		

	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
		
