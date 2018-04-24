import os
import tempfile
import imp

def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod
d=os.path.split(os.path.split(os.path.dirname( __file__))[0])[0]
fn=os.path.join(d,'include','v101','host_map.py')
print fn
hmap=import_module(fn)	

class base(object):
	"""Oracle db"""
	def __init__(self,log):
		self.log=log
		self.T, self.TL, self.P,self.PL, self.SP,self.SPL, self.QF, self.QD =(False, False, False, False, False,False, False, False)
		self.IF, self.ID =(False,  False)
		self.F, self.D =(False,  False)
		#if hasattr(args, 'args') and args.query_sql_file:
		host_map_loc= self.args.host_map
		#print host_map_loc
		self.hm = hmap.host_map(self.args.copy_vector.split(self.conf._to),host_map_loc,0)		
	def save_qry(self,name, qry):
		assert self.datadir, 'Datadir is not set'	
		cqdir='%s\\sql' % (self.datadir)
		cqfn='%s\\%s.sql' % (cqdir,name)
		cqf = open(cqfn, "w")
		cqf.write(qry)
		cqf.close()
		if self.dbg>2:
			print qry		
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
	def get_outdn(self,shard, qname=None):
		#print self.uargs.to_file
		#print self.uargs.to_dir
		return os.path.dirname(self.uargs.get_sharded_outfn(shard, qname))
		
	def printerr(self,logger,err):
		logger.error('#'*20)
		logger.error( '#'*6,'ERROR!', '#'*6)
		logger.error( '#'*20)
		logger.error( err)
		logger.error( '#'*20)
		logger.error( '#'*20)
	def get_ddl_extract_config(self,from_pld):
		return None			
	def spool_ddl(self,outfn, spConf, payload):
		self.log.error('DDL extract is not supported')
		return (-1, -1)