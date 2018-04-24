import sys, os
import shlex
from pprint import pprint
from subprocess import Popen, PIPE
import common.v101.config as conf 
from test.v101.test import run_test, test, csvfile, home
import itertools
default_vector=None #'pgres2pgres'



from_table='Persons_pipe_datetime'
from_part_table='Persons_partitioned'
to_table='Persons_pipe_datetime_1'
to_part_table='Persons_partitioned_2'
citi=conf.citi
dbclients=conf.dbclients


	

#print __name__
if __name__=='__main__':
	if 0: #ORA
		t=['SLITE', 'MARIA', 'CSV','ORA','TTEN','SYANY','SYIQ','INFOR','INFORC','SYASE','EXAD','DBTUDB']
		t_from=['ORA_Partitioned']
		t_from=['ORA_Table']
		#t_from=['ORA_ShardedTable']
		#t_from=['ORA_ShardedPartitioned']
		t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned', 'SLITE', 'MARIA', 'CSV','TTEN','SYANY','SYIQ','INFOR','INFORC','SYASE','EXAD','DBTUDB']
		t_to=['ORA']
		t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned']
		t_to=['ORA', 'SLITE', 'MARIA', 'CSV','TTEN','SYANY','SYIQ','INFOR','INFORC','SYASE','EXAD','DBTUDB']
		t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned','ORA_Query']
		t_from=['ORA_Query']
		t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned','ORA_Query','CSV']
		
		t_to=['ORA','CSV']

		#t_from=['ORA_Query_NoNLSDate']
		#t_from=['ORA_Query']
		t_from=['ORA_Partitioned','CSV']
		t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned','ORA_Query','CSV']
		#t_from=['ORA_Table', 'ORA_Partitioned', 'ORA_ShardedTable', 'ORA_ShardedPartitioned','ORA_Query','SLITE', 'MARIA', 'CSV','TTEN','SYANY','SYIQ','INFOR','INFORC','SYASE','EXAD','DBTUDB']
		t_to=['ORA','CSV']
	t_from=['SS','CSV']
	t_to=['SS','CSV']
	t_from=['ORA_Table']
	#t_from=['CSV']
	t_to=['SS']
	t_from=['ORA_Table']
	#t_from=['CSV']
	t_to=['ORA']

	
	
	cmd=[]
	prog=['python','datamule.py']
	#prog=[conf.appname]
	for element in itertools.product(t_from,t_to):
		
		print element
		(db_from, db_to) = element
		paramkey_from=db_from.split('_')[0]
		
		if '%s2%s' % (paramkey_from.lower(),db_to.lower()) not  in ('csv2csv'):
			
			if db_from in ('ORA_ShardedPartitioned', 'ORA_ShardedTable'):			
				test['core']=('%s2%s' % (paramkey_from.lower(),db_to.lower()),3,			3,				'"|"',		'')		
			else:
				test['core']=('%s2%s' % (paramkey_from.lower(),db_to.lower()),1,			1,				'"|"',		'')		
						
			cmd.append ((db_from, db_to,run_test(db_from, db_to, prog,  citi=citi)))
		
	#pprint(cmd)
	scr=r'all.bat'

	f=open( scr,'w')
	for i in cmd:
		(db_from, db_to,c) = i
		f.write('\n\nREM From %s to %s\n%s' % (db_from, db_to, c))
	f.close()
	
	#run_test(db_from, db_to)

	


