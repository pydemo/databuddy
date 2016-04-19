import sys
import shlex
from pprint import pprint
from subprocess import Popen, PIPE
#import common.v101.config as conf 
import config.config as conf
default_vector=None #'pgres2pgres'
#ff=('CSV')
#dbs={'ORA':'Oracle','SS':'SQLServer','MYSQL':'MySQL','CSV':'CSV','PGRES':'PostgreSQL'}
test={}
home=r'C:\Python27\data_mule_postgre'
dbclients={ 'PGRES':r"C:\Program Files\PostgreSQL\9.3\bin",
			'ORA11G':r'C:\oraclexe\app\oracle\product\11.2.0\server\bin',
			'SS':'C:\Program Files\Microsoft SQL Server\Client SDK\ODBC\110\Tools\Binn',
			'MYSQL':r'C:\Temp\mysql\bin'}
db_from ='PGRES'
db_to= 'PGRES'			
test['core']=('%s2%s' % (db_from.lower(),db_to.lower()),1,			1,				'"|"',		'')
			 #copy_vector,	pool_size,	num_of_shards,	field_term,	limit
test['FROM']={}
tfrom=test['FROM']
dbkey='PGRES'				
tfrom[dbkey]= ( '%s\\postgre_query.sql' % home, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
				#query_sql_file, 	from_user,  from_passwd,	from_db_name, from_db_server, 	postgres_client_home


				
test['TO']={}
tto=test['TO']
to_table='Persons_pipe_datetime'
(nls_d, nls_t)=('"DD-Mon-YYYY HH:MI:SS AM"','"DD-Mon-RR HH.MI.SSXFF AM"')
if db_from in ('PGRES'):
	(nls_d, nls_t)=('"RRRR-MM-DD HH24.MI.SS"','"RRRR-MM-DD HH24.MI.SS.FF"')
 
tto['ORA11G']=('SCOTT/tiger2@XE', 'SCOTT.%s' % to_table,nls_d, nls_t )
			#to_db, 			to_table, 			  nls_date_format, 			 nls_time_format
				
tto['CSV']=('test.data')
			#to_file
dbkey='SS'				
tto[dbkey]=( 'sa',  '198Morgan', 'master', 'ALEX_BUZ-PC\SQLEXPRESS', 'dbo.%s' % to_table)
			#to_user, to_passwd, 	to_db_name, to_db_server,			  to_table
				
dbkey='MYSQL'			
tto[dbkey]=('alex',  'mysql_pwd', 'test', 	'localhost',	to_table, dbclients[dbkey])
			#to_user, to_passwd, to_db_name, to_db_server,  to_table, mysql_client_home
			
dbkey='PGRES'			
tto[dbkey]=('"postgres"', '"postgre_pwd"', '"postgres"', 	'"localhost"', '"%s"' % to_table, '"%s"' % dbclients[dbkey])
			#to_user, 	to_passwd, 		to_db_name, to_db_server, to_table, postgres_client_home

core_keys=conf.params['core'].keys()

#print test['FROM']['PGRES']
#sys.exit(0)
pt='core'
pars=conf.params['core']
#print map(lambda x: '%s %s' % (pars[core_keys[x]]['short'], test[pt][x]),range(len(core_keys)))
core_p= ["%s %s" % (pars[core_keys[i]]['short'],test[pt][i])  for i in range(len(core_keys)) if test[pt][i]] #conf.params['core'][core_keys[i]]['short']]
#print ' '.join(core_p)

pt='FROM'

par_keys=conf.params['FROM'][db_from].keys()
pars=conf.params['FROM'][db_from]
#print map(lambda x: '%s %s' % (pars[par_keys[x]]['short'], test[pt]['PGRES'][x]),range(len(par_keys)))
from_p= ["%s %s" % (pars[par_keys[i]]['short'],test[pt][db_from][i])  for i in range(len(par_keys)) if test[pt][db_from][i]] #conf.params['core'][par_keys[i]]['short']]
#print ' '.join(from_p)

pt='TO'

par_keys=conf.params[pt][db_to].keys()
pars=conf.params[pt][db_to]
#print map(lambda x: '%s %s' % (pars[par_keys[x]]['short'], test[pt]['PGRES'][x]),range(len(par_keys)))
to_p= ["%s %s" % (pars[par_keys[i]]['short'],test[pt][db_to][i])  for i in range(len(par_keys)) if test[pt][db_to][i]] #conf.params['core'][par_keys[i]]['short']]
plist=['python','datamule5.py']+core_p+from_p+to_p
#pprint (plist)

tall=[]
if 1:
	tall.append(' '.join(plist))	
else:	
	cmd=' '.join(plist)
	print cmd

	lexer=shlex.shlex(cmd)
	#lexer = shlex.shlex(input)
	lexer.quotes = '"'
	#lexer.wordchars += '\''
	lexer.whitespace_split = True
	lexer.commenters = ''
	conf = list(lexer)
	#sys.exit(1)
	p = Popen(conf,stdin=PIPE,  stdout=PIPE  )
	out, err = p.communicate('y\n')
	p.wait()
	print out
	print '-'*40
	print err
tout= '\r\n'.join(tall)
print tout
#sys.exit(0)
f=open('pgres_test.bat','w')

f.write(tout)
f.close()



