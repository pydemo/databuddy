import tempfile

class base(object):
	"""Oracle db"""
	def __init__(self,log):
		self.log=log
	def save_qry(self,name, qry):
		assert self.datadir, 'Datadir is not set'	
		cqdir='%s\\sql' % (self.datadir)
		cqfn='%s\\%s.sql' % (cqdir,name)
		cqf = open(cqfn, "w")
		cqf.write(qry)
		cqf.close()
		return cqfn	
	def ckey2cols(self, col_key):
		return map(lambda x: x.split(':')[0],col_key)	
	def get_temp_token(self):
		temp_file_name=tempfile.mkstemp()[1].split('\\')[-1]
		return temp_file_name.strip('/tmp')			

	def get_temp_table_name(self):
		return 'TCL_%s' % self.get_temp_token()	
	def get_outfn(self,shard, qname=None):
		#print self.uargs.to_file
		#print self.uargs.to_dir
		return self.uargs.get_sharded_outfn(shard, qname)
	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
