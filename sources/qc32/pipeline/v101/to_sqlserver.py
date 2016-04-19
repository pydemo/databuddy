import types, re, os, time, sys
from subprocess import Popen, PIPE,STDOUT
from db.v101.db_sqlserver import SQLServer
import codecs, tempfile
import config.config as conf
#import common.v101.config as conf 
from pprint import pprint
from common.v101.exceptions import SqlCmdError
e=sys.exit
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
#os.chdir(d)
#print '##########',os.getcwd()
#from include.v101.host_map import host_map as hmap
hmap=import_module(os.path.join(d,'include','v101','host_map.py'))
hmap= hmap.host_map

class ToSQLServer(SQLServer):
	"""SQLServer db"""
	def __init__(self,parent,log,datadir,conf, db):
		(self.args,self.uargs,self.conf)=(conf.args, conf.uargs	,conf)
		login=(self.args.to_user,self.args.to_passwd,self.args.to_db_name,self.args.to_db_server)
		SQLServer.__init__(self,log,login,datadir,self.args) 
		self.log=log
		#self.login=login
		self.to_table=self.args.to_table
		self.db=db
		self.field_term=self.args.field_term
		#self.wait_sec=int(args.wait_limit_sec)
		self.datadir=datadir
		self.tab_cols={}
		#self.args=args
		self.to_pld={}
		self.etl=self.uargs.target.target(datadir,self.login,self.conf,db,self.args.to_table)
		host_map_loc= self.args.host_map
		#print host_map_loc
		#print hmap
		#print self.args.copy_vector, self.args.copy_vector.split(self.conf._to)
		
		self.hm = hmap(self.args.copy_vector.split(self.conf._to),host_map_loc,0)
		
	def print_copy_details(self):		
		print """		
	To SQLServer:	
		to db: %s
		to table: %s
		""" % ('%s/%s/%s' % (self.args.to_user,self.args.to_db_name,self.args.to_db_server),self.to_table)
	def set_payload(self,shard,num_of_shards, qname=None):
		#options={'_PARTITION':pt}
		
		return (self.login, self.to_table) 	
	def set_payload_ora(self,shard,num_of_shards, qname=None):
		#options={'_PARTITION':pt}
		tabname= self.to_table
		if self.to_table:
			return (self.login, self.to_table) 	
		else:
			assert qname, 'Query name should be set if table name is not defined.'
			q=qname.split('.')
			assert len(q)>2, 'Wrong query file name format "%s".\nShould be: TOSCHEMA.TOTABLE.id.sql' % qname #;TOPART;TOSUBPART
			schema,table=q[:2]
			#t=tab.split(';')
			
			return (self.login, '.'.join([schema,table])) 		
	def get_inserted_count(self,cnt):
		return cnt
	def load_data(self,logger,loadConf,outfn,shard):
		out=[]
		err=[]
		ins_cnt=-1
		#pprint(loadConf)
		#db_client_dbshell= self.hm.local_source_client_home #self.get_db_client_dbshell()
		p = Popen(loadConf, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		out, err = p.communicate()
		status=p.wait()
		if ' rows affected)' in out:
			#logger.info('SUCCESS')
			r=re.compile(r'\((\d+) rows affected\)')
			g=re.search(r,out)
			if g:
				ins_cnt= g.groups()[0]
		elif out.startswith('Msg '):
			print '#'*60
			print '#'*60
			logger.error(out)
			print '#'*60
			print '#'*60			
			status =1
		elif err:
			print '#'*60
			print '#'*60		
			logger.error(err)
			print '#'*60
			print '#'*60			
			status=1

		loader=conf.dbtools['LOADER'][self.db]
		
		if status==0:
			logger.info('%s status =%s' % (loader,status))
		if status!=0:
			logger.error('%s status =%s' % (loader,status))
		stat=-1
		if os.path.isfile(outfn):
			stat=os.stat(outfn).st_size
		return (out,status,err,ins_cnt,stat)	
	def get_load_config(self,to_pld):
		#(shard_name,from_pld,to_pld)=payload
		#pprint( to_pld)
		#sys.exit(0)
		#(infile, row_from, row_to,field_term) =from_pld
		(login, to_table, shard_name, infile, row_from, row_to)=to_pld
		(ss_user, ss_passwd, ss_db_name, ss_db_server)=login
		#(fmtfn,out,status,err)=self.create_format_file(self.log)
		#assert os.path.isfile(fmtfn), 'Format file does not exists'
		#shard=shard_name.split('-')[1]
		assert infile, 'Input CSV file is not set.'
		load_qry=self.etl.get_load_query (infile,row_from,row_to)
		#print (load_qry)
		#e(0)
		#lqfn = self.save_qry('load_query_%s' % shard_name, load_qry)
		sqdir= '%s\\sql' % self.datadir
		lqfn='%s\\load_query_%s.sql' % (sqdir,shard_name)
		sqf = open(lqfn, "w")
		sqf.write(load_qry)
		sqf.close()
		#print self.hm
		#print self.hm.local_target_client_home
		db_client_dbshell= os.path.join (self.hm.local_target_client_home,'sqlcmd.exe')  #self.get_db_client_dbshell()
		loadConf=[db_client_dbshell, '-U', ss_user, '-P', ss_passwd, '-d', ss_db_name, '-S', ss_db_server, '-i',lqfn]
		#print ' '.join(loadConf)
		#loadConf=['sqlldr']
		#pprint( loadConf)
		#sys.exit(1)
		#print ' '.join(loadConf)
		#sqlcmd -U sa -P 198Morgan -d master -S ALEX_BUZ-PC\SQLEXPRESS -i C:\Python27\data_migrator_for_ss\logs\20141021_112733\sql\load_query_Shard-0.sql
		
		return loadConf		
	
