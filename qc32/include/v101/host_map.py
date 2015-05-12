import os
from pprint import pprint
import pprint as pp
from common.v101.loaders import import_module
class base_host_map(object):
	def __init__(self,copy_vector, host_map_loc,shard):
		self.host_map_loc=host_map_loc
		#print host_map_loc
		#self.conf=conf
		self.copy_vector=copy_vector
		self.shard=shard
		#print dir(conf)
		#self.args=conf.args
		self.mapping=None
		self.set_host_map()
		
		(self.local_source_client_home, self.local_target_client_home) = self.get_local_client_home()
	def get_local_client_home(self):
		#print self.conf.uargs.copy_vector
		(from_db, to_db)=self.copy_vector.upper().split('2')
		#pprint(self.mapping)
		env=self.mapping['host_list'][self.mapping['local_host']]['db_env']
		#pprint(env)
		#print from_db, to_db
		return (env[from_db]['source'], env[to_db]['target'])
	def set_host_map(self):
		self.remote_user='default'
		#obj=self.args_panel.obj
		if 1: #obj.has_key('host_map'):
			#host_map_loc= obj['host_map'][1].GetValue()
			if os.path.exists(self.host_map_loc):
				self.host_map_loc=os.path.realpath(self.host_map_loc)
			#print self.host_map_loc
			assert os.path.isfile(self.host_map_loc), 'Host mapping file "%s" does not exists.' % self.host_map_loc
			hm=import_module(self.host_map_loc)
			self.mapping=hm.mapping		
	def get_host_map(self):
		assert self.mapping, 'host_map is not defined\n%s' % self.host_map_loc
		return (self.mapping['host_map'],self.mapping['active_mapping'])
	def set_active_mapping(self,v):
		#change active mapping
		assert self.mapping.has_key('active_mapping'), 'active_mapping is not defined.'
		self.mapping['active_mapping'] = v
		f = open(self.host_map_loc, 'w')
		#f.write('mapping=%s' % cp.pprint(hm.mapping))
		print >>f,'mapping=%s' % pp.pformat(self.mapping)
		f.close()

class host_map_v1( base_host_map):
	"""Host Map object"""
	def __init__(self,copy_vector, host_map_loc, shard):	
		
		base_host_map.__init__(self,copy_vector, host_map_loc,shard)
		self.h2s_map=None
		self.host=None
		self.R=False
		if shard:
			self.R=self.if_remote(shard)
	def get_h2s_map(self):
		h2s_map={}
		for host_map in self.mapping['host_map'][self.mapping['active_mapping']]:
			#print host_map
			#host_map=host_map_list[0]
			shard_range, host= (host_map['shards'], host_map['host'])
			
			a,b=map(int,shard_range.split(':'))
			#print a,b
			#print conf
			#print list(range(a,b))
			
			for s in range(a,b):
				h2s_map[s]= int(host)
		return h2s_map
	def if_remote(self,shard):
		#print 'host_map_v1'
		#if hasattr(self.args, 'host_map') and self.args.host_map:
		#host_map_loc= self.args.host_map
		#hm = hmap(conf,host_map_loc)
		self.h2s_map=self.get_h2s_map()
		assert int(shard) in self.h2s_map.keys(), 'Host mapping for shard %s is not set.' % shard
		self.host =self.mapping['host_list'] [self.h2s_map[int(shard)]]
		#pprint(self.host)
		if not self.host['env'][0] in ['nt']:
			return True
		else:
			return False
		
class host_map_v2( base_host_map):
	"""Host Map object"""
	def __init__(self,copy_vector, host_map_loc, shard):
		#print 'host_map_v2'
		base_host_map.__init__(self,copy_vector, host_map_loc,shard)
		self.h2s_map=None
		self.host=None
		self.R=False
		if shard:
			self.R=self.if_remote(shard)
		
	def get_h2s_map(self):
		h2s_map={}
		for host_map in self.mapping['host_map'][self.mapping['active_mapping']]:
			shard_range, host= (host_map['shards'], host_map['host'])
			a,b=map(int,shard_range.split(':'))
			for s in range(a,b):
				h2s_map[s]= int(host)
		#pprint(h2s_map)
		#e(0)
		return h2s_map
	def if_remote(self,shard):
		self.h2s_map=self.get_h2s_map(self)
		assert int(shard) in self.h2s_map.keys(), 'Host mapping for shard %s is not set.' % shard
		self.host =self.mapping['host_list'] [self.h2s_map[int(shard)]]
		#pprint(host)
		if not self.host['env'][0] in ['nt']:
			return True
		else:
			return False
		
		
class host_map( host_map_v1,host_map_v2):
	"""Host Map object"""
	def __init__(self,copy_vector, host_map_loc, shard=None):		
		self.v=1
		if host_map_loc.upper().endswith('_V2.PY'):
			self.v=2
		#print self.v
		if self.v==1:
			host_map_v1.__init__(self,copy_vector, host_map_loc, shard)
			self.get_h2s_map=host_map_v1.get_h2s_map
			self.if_remote=host_map_v1.if_remote
		elif self.v==2:
			host_map_v2.__init__(self,copy_vector, host_map_loc, shard)
			self.get_h2s_map=host_map_v2.get_h2s_map
			self.if_remote=host_map_v2.if_remote
			
		else:
			assert 1==2, 'host map is not supported\n%s' % host_map_loc
			

		
		