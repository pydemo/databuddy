import os
class base_host_map(object):
	def __init__(self,conf, host_map_loc):
		self.host_map_loc=host_map_loc
		self.conf=conf

	def get_host_map(self):
		self.remote_user='default'
		#obj=self.args_panel.obj
		if 1: #obj.has_key('host_map'):
			#host_map_loc= obj['host_map'][1].GetValue()
			if os.path.exists(self.host_map_loc):
				self.host_map_loc=os.path.realpath(self.host_map_loc)
			print self.host_map_loc
			assert os.path.isfile(self.host_map_loc), 'Host mapping file "%s" does not exists.' % self.host_map_loc
			hm=self.conf.import_module(self.host_map_loc)
			hmap=hm.mapping

			#pprint(hmap)
			#for host_map in hmap['host_map'].keys():
			#	print host_map
			#pprint(h2s_map)
		return (hmap['host_map'],hmap['active_mapping'])

class host_map_v1( base_host_map):
	"""Host Map object"""
	def __init__(self,conf, host_map_loc):
		base_host_map.__init__(self,conf, host_map_loc)
class host_map_v2( base_host_map):
	"""Host Map object"""
	def __init__(self,conf, host_map_loc):
		base_host_map.__init__(self,conf, host_map_loc)
		
class host_map( host_map_v1,host_map_v2):
	"""Host Map object"""
	def __init__(self,conf, host_map_loc):		
		self.v=1
		if host_map_loc.upper().endswith('_V2.PY'):
			self.v=2
		if self.v==1:
			host_map_v1.__init__(self,conf, host_map_loc)
		elif self.v==2:
			host_map_v2.__init__(self,conf, host_map_loc)
		else:
			assert 1==2, 'host map is not supported\n%s' % host_map_loc
			

		
		