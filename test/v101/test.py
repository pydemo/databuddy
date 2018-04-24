import os, sys
from pprint import pprint
#import common.v101.config as conf 
import config.config as conf 
from args_api import args_api
e=sys.exit
#test={}
csvf_dt={}
csvf_ts={}
csvf_tz={}
qryf={}
home=os.path.dirname(os.path.realpath(__file__))
data_loc=r'%s\data' % home

wide_test=False


if 0:
	csvf['SYASE'] = '%s\\sybase_shard_0.data' % data_loc
	csvf['SYIQ'] = '%s\\sybase_shard_0.data' % data_loc
	csvf['SYANY'] = '%s\\sybase_shard_0.data' % data_loc
	csvf['INFOR'] = '%s\\informix_shard_0.data' % data_loc
	csvf['INFORC'] = '%s\\informix_shard_0.data' % data_loc
	csvf['MARIA'] = '%s\\mariadb_shard_0.data' % data_loc
	csvf['MYSQL'] = '%s\\mysql_shard_0.data' % data_loc
	csvf['INFOB'] = '%s\\mysql_shard_0.data' % data_loc
	csvf['PGRES'] = '%s\\pgres_shard_0.data' % data_loc
	csvf['SLITE'] = '%s\\sqllite_shard_0.data' % data_loc

	for db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
		csvf[db] = r'%s\db2_shard_0.data' % data_loc	
		
	if conf.citi:
		csvf['ORA11G'] = '%s\\oracle_citi_shard_0.data' % data_loc
	else:
		csvf['ORA11G'] = '%s\\oracle_shard_0_ts.data' % data_loc
		csvf['ORA12C'] = '%s\\oracle_shard_0_ts.data' % data_loc
	csvf['ORAXE'] = '%s\\oracle_shard_0_ts.data' % data_loc	
	csvf['TTEN'] = '%s\\tt_shard_0.data' % data_loc
	csvf['ORAEXA'] = '%s\\oracle_shard_0_ts.data' % data_loc
	csvf['SSEXP'] = '%s\\ss_shard_0.data' % data_loc
	csvf['SSENT'] = '%s\\ss_shard_0.data' % data_loc


#timezone files
csvf_tz['SYASE'] = '%s\\sybase_shard_0.data' % data_loc
csvf_tz['SYIQ'] = '%s\\sybase_shard_0.data' % data_loc
csvf_tz['SYANY'] = '%s\\sybase_shard_0.data' % data_loc
csvf_tz['INFOR'] = '%s\\informix_shard_0.data' % data_loc
csvf_tz['INFORC'] = '%s\\informix_shard_0.data' % data_loc
csvf_tz['MARIA'] = '%s\\mariadb_shard_0.data' % data_loc
csvf_tz['MYSQL'] = '%s\\mysql_shard_0.data' % data_loc
csvf_tz['INFOB'] = '%s\\mysql_shard_0.data' % data_loc
csvf_tz['PGRES'] = '%s\\pgres_shard_0_tz.data' % data_loc
csvf_tz['SLITE'] = '%s\\sqllite_shard_0.data' % data_loc
for db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	csvf_tz[db] = r'%s\db2_shard_0.data' % data_loc	
if conf.citi:
	csvf_tz['ORA11G'] = '%s\\oracle_citi_shard_0_tz.data' % data_loc
else:
	csvf_tz['ORA12C'] = '%s\\oracle_shard_0_tz.data' % data_loc
	csvf_tz['ORA11G'] = '%s\\oracle_shard_0_tz.data' % data_loc
csvf_tz['ORAXE'] = '%s\\oracle_shard_0_tz.data' % data_loc	
csvf_tz['TTEN'] = '%s\\tt_shard_0.data' % data_loc
csvf_tz['ORAEXA'] = '%s\\oracle_shard_0_ts.data' % data_loc
csvf_tz['SSEXP'] = '%s\\ss_shard_0.data' % data_loc
csvf_tz['SSENT'] = '%s\\ss_shard_0.data' % data_loc


#timestamp files
csvf_ts['SYASE'] = '%s\\sybase_shard_0.data' % data_loc
csvf_ts['SYIQ'] = '%s\\sybase_shard_0.data' % data_loc
csvf_ts['SYANY'] = '%s\\sybase_shard_0.data' % data_loc
csvf_ts['INFOR'] = '%s\\informix_shard_0.data' % data_loc
csvf_ts['INFORC'] = '%s\\informix_shard_0.data' % data_loc
csvf_ts['MARIA'] = '%s\\mariadb_shard_0.data' % data_loc
csvf_ts['MYSQL'] = '%s\\mysql_shard_0.data' % data_loc
csvf_ts['INFOB'] = '%s\\mysql_shard_0.data' % data_loc
csvf_ts['PGRES'] = '%s\\pgres_shard_0_ts.data' % data_loc
csvf_ts['SLITE'] = '%s\\sqllite_shard_0.data' % data_loc
for db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	csvf_ts[db] = r'%s\db2_shard_0.data' % data_loc	
if conf.citi:
	csvf_ts['ORA11G'] = '%s\\oracle_citi_shard_0.data' % data_loc
else:
	csvf_ts['ORA12C'] = '%s\\oracle_shard_0_ts.data' % data_loc
	csvf_ts['ORA11G'] = '%s\\oracle_shard_0_ts.data' % data_loc
csvf_ts['ORAXE'] = '%s\\oracle_shard_0_ts.data' % data_loc	
csvf_ts['TTEN'] = '%s\\tt_shard_0.data' % data_loc
csvf_ts['ORAEXA'] = '%s\\oracle_shard_0_ts.data' % data_loc
csvf_ts['SSEXP'] = '%s\\ss_shard_0.data' % data_loc
csvf_ts['SSENT'] = '%s\\ss_shard_0.data' % data_loc

#date files
csvf_dt['SYASE'] = '%s\\sybase_shard_0.data' % data_loc
csvf_dt['SYIQ'] = '%s\\sybase_shard_0.data' % data_loc
csvf_dt['SYANY'] = '%s\\sybase_shard_0.data' % data_loc
csvf_dt['INFOR'] = '%s\\informix_shard_0.data' % data_loc
csvf_dt['INFORC'] = '%s\\informix_shard_0.data' % data_loc
csvf_dt['MARIA'] = '%s\\mariadb_shard_0.data' % data_loc
csvf_dt['MYSQL'] = '%s\\mysql_shard_0.data' % data_loc
csvf_dt['INFOB'] = '%s\\mysql_shard_0.data' % data_loc
csvf_dt['PGRES'] = '%s\\pgres_shard_0_dt.data' % data_loc
csvf_dt['SLITE'] = '%s\\sqllite_shard_0.data' % data_loc
for db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	csvf_dt[db] = r'%s\db2_shard_0.data' % data_loc	
if conf.citi:
	csvf_dt['ORA11G'] = '%s\\oracle_citi_shard_0_dt.data' % data_loc
else:
	csvf_dt['ORA12C'] = '%s\\oracle_shard_0_dt.data' % data_loc
	csvf_dt['ORA11G'] = '%s\\oracle_shard_0_dt.data' % data_loc
csvf_dt['ORAXE'] = '%s\\oracle_shard_0_dt.data' % data_loc	
csvf_dt['TTEN'] = '%s\\tt_shard_0.data' % data_loc
csvf_dt['ORAEXA'] = '%s\\oracle_shard_0_ts.data' % data_loc
csvf_dt['SSEXP'] = '%s\\ss_shard_0.data' % data_loc
csvf_dt['SSENT'] = '%s\\ss_shard_0.data' % data_loc
csvf_dt['MONGO'] =csvf_ts['MONGO'] = csvf_tz['MONGO'] = '%s\\mongo_shard_0.data' % data_loc



qry_loc=r'%s\query' % home

qryf['SYASE'] = '%s\\sybase_query.sql' % qry_loc
qryf['SYANY'] = '%s\\sybase_query.sql' % qry_loc
qryf['SYIQ'] = '%s\\sybase_query.sql' % qry_loc
qryf['INFOR'] = '%s\\informix_query.sql' % qry_loc


qryf['INFORC'] = '%s\\informix_query.sql' % qry_loc

qryf['SLITE'] = '%s\\sqllite_query.sql' % qry_loc
qryf['ORA12C'] = '%s\\oracle_query.sql' % qry_loc
qryf['ORA11G'] = '%s\\oracle_query.sql' % qry_loc
qryf['ORA_TimezoneQueryFile:MYSQL'] = '%s\\oracle_query_tz_to_mysql.sql' % qry_loc
qryf['ORA_TimezoneQueryFile:TTEN'] = '%s\\oracle_query_tz_to_tten.sql' % qry_loc
qryf['ORA_TimezoneQueryFile:INFOR'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['ORA_TimezoneQueryFile:INFORC'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['TTEN'] = '%s\\timesten_query.sql' % qry_loc
qryf['ORAXE'] = '%s\\oracle_query.sql' % qry_loc
qryf['ORAXE_TimezoneQueryFile:MYSQL'] = '%s\\oracle_query_tz_to_mysql.sql' % qry_loc
qryf['ORAXE_TimezoneQueryFile:TTEN'] = '%s\\oracle_query_tz_to_tten.sql' % qry_loc
qryf['ORAXE_TimezoneQueryFile:INFOR'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['ORAXE_TimezoneQueryFile:INFORC'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['ORAEXA'] = '%s\\oracle_query.sql' % qry_loc
qryf['ORAEXA_TimezoneQueryFile:MYSQL'] = '%s\\oracle_query_tz_to_mysql.sql' % qry_loc
qryf['ORAEXA_TimezoneQueryFile:TTEN'] = '%s\\oracle_query_tz_to_tten.sql' % qry_loc
qryf['ORAEXA_TimezoneQueryFile:INFOR'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['ORAEXA_TimezoneQueryFile:INFORC'] = '%s\\oracle_query_tz_to_infor.sql' % qry_loc
qryf['SSEXP'] = '%s\\ss_query.sql' % qry_loc
qryf['SSENT'] = '%s\\ss_query.sql' % qry_loc
qryf['MYSQL'] = '%s\\mysql_query.sql' % qry_loc
qryf['MYSQL_TimezoneQueryFile:ORA'] = '%s\\mysql_query_tz_to_ora.sql' % qry_loc
qryf['INFOB'] = '%s\\mysql_query.sql' % qry_loc
qryf['INFOB_TimezoneQueryFile:ORA'] = '%s\\mysql_query_tz_to_ora.sql' % qry_loc
qryf['MARIA'] = '%s\\mariadb_query.sql' % qry_loc
qryf['MARIA_TimezoneQueryFile:ORA'] = '%s\\mysql_query_tz_to_ora.sql' % qry_loc

qryf['PGRES'] = '%s\\postgre_query.sql' % qry_loc
for db in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	qryf[db] = r'%s\db2_query.sql' % qry_loc
	qryf['ORA_TimezoneQueryFile:%s' % db]  = r'%s\oracle_query_tz_to_db2.sql' % qry_loc
	qryf['ORAXE_TimezoneQueryFile:%s' % db]= r'%s\oracle_query_tz_to_db2.sql' % qry_loc
	qryf['ORAEXA_TimezoneQueryFile:%s' % db] = r'%s\oracle_query_tz_to_db2.sql' % qry_loc
	
qry_dir_ora=os.path.join(home,'query','query_dir_ora')
qry_dir_ora_table_named = os.path.join(home,'query','query_dir_ora_table_named')
qry_dir_ora_wwr=os.path.join(home,'query','query_dir_ora_wwr')
qry_dir_tt=os.path.join(home,'query','query_dir_tt')
qry_dir_pgres=os.path.join(home,'query','query_dir_pgres')
qry_dir_sy=os.path.join(home,'query','query_dir_sy')
qry_dir_infor=os.path.join(home,'query','query_dir_infor')
qry_dir_db2=os.path.join(home,'query','query_dir_db2')
qry_dir_slite=os.path.join(home,'query','query_dir_slite')
qry_dir_ss=os.path.join(home,'query','query_dir_ss')
qry_dir_mysql=os.path.join(home,'query','query_dir_mysql')

ora_data_dir=os.path.join(data_loc,'ora_data_dir')

#qdir['PGRES'] = qry_dir_pgres
ddir={}
ddir['PGRES'] = os.path.join(data_loc,'pgres_data_dir')
ddir['ORAEXA'] = ddir['ORA11G'] = ddir['ORA12C'] = ddir['ORAXE'] =os.path.join(data_loc,'ora_data_dir_1')+';'+os.path.join(data_loc,'ora_data_dir_2')
ddir['SSENT'] =  ddir['SSEXP'] = os.path.join(data_loc,'ss_data_dir')
ddir['DBTAES']=ddir['DBTES']=ddir['DBTAWS']=ddir['DBTWS']=ddir['DBTE']=ddir['DBTEC']=ddir['DBTDE']=os.path.join(data_loc,'db2_data_dir')
ddir['INFOR'] = ddir['INFORC']= os.path.join(data_loc,'infor_data_dir')
ddir['TTEN'] = os.path.join(data_loc,'tt_data_dir')
ddir['SLITE'] = os.path.join(data_loc,'slite_data_dir')
ddir['SYASE']=ddir['SYANY']=ddir['SYIQ'] = os.path.join(data_loc,'sybase_data_dir')
ddir['MYSQL']=ddir['MARIA']=ddir['INFOB']=os.path.join(data_loc,'mysql_data_dir')
ddir['MONGO'] = os.path.join(data_loc,'mongo_data_dir')


#'DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'

from_table='Timestamp_test_from'
date_from = 'Date_test_from'
timestamp_from ='Timestamp_test_from'
timezone_from ='Timezone_test_from'
from_part_table='Partitioned_test_from'
from_sub_part_table='Sub_Partitioned_test_from'

to_table='Timestamp_test_to'
date_to = 'Date_test_to'
timestamp_to='Timestamp_test_to'
timezone_to = 'Timezone_test_to'
to_part_table='Partitioned_test_to'
to_sub_part_table='Sub_Partitioned_test_to'

citi=conf.citi
dbclients=conf.dbclients



if 0:
	from_table = 'wide_row_from_4'
	to_table = 'wide_row_to_4'

def zip_lists(a,b):
	assert len(a)==len(b), 'Cannot zip lists of different length.'
	out=[]
	for i in range(len(a)):
		out.append(a[i])
		out.append(b[i])
	return out
def create_run_tests(db_from, db_to, test,citi=False):
	global conf, from_table, to_table
	#print db_from, db_to
	#test={}
	#	print prog
	#e(0)
	#sys.exit(0)
	(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD HH24.MI.SS"','"YYYY-MM-DD HH24.MI.SS.FF2"','"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"')
	if db_to.startswith('SS'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD HH24:MI:SS"','"YYYY-MM-DD HH24:MI:SS.FF3"','"YYYY-MM-DD HH:MI:SS.FF3 TZH:TZM"')	
	elif db_to.startswith('PGRES'): #2014-12-09 14:51:26.219-05
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD HH24:MI:SS"','"YYYY-MM-DD HH24:MI:SS"','"YYYY-MM-DD HH24:MI:SS.FF3 TZH:TZM"')	
	elif db_from.startswith('PGRES'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD HH24:MI:SS"','"YYYY-MM-DD HH24.MI.SS.FF3"','"YYYY-MM-DD HH24:MI:SS.FF3 TZH:TZM"')
	elif db_to.startswith('DBT'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD"','"YYYY-MM-DD-HH24.MI.SS.FF"','"YYYY-MM-DD-HH24:MI:SS.FF"')	
	elif db_from.startswith('DBT'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD"','"YYYY-MM-DD-HH24.MI.SS.FF"','"YYYY-MM-DD-HH24:MI:SS.FF"')	
	elif db_to.startswith('CSV') and db_from.startswith('TT'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD"','"YYYY-MM-DD-HH24.MI.SS.FF"','"YYYY-MM-DD-HH24:MI:SS.FF"')	
	elif db_from.startswith('CSV') and db_to.startswith('TT'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD"','"YYYY-MM-DD-HH24.MI.SS.FF"','"YYYY-MM-DD-HH24:MI:SS.FF"')	
		#e(0)
	elif db_from.startswith('SS'):
		(nls_d, nls_t, nls_tz)=('"YYYY-MM-DD"','"YYYY-MM-DD HH24:MI:SS.FF3"','"YYYY-MM-DD HH24:MI:SS.FF"')	

	elif db_to.startswith('INF'):
		(nls_d, nls_t, nls_tz)=('"MM/DD/YYYY"','"YYYY-MM-DD HH24:MI:SS.FF2"','"YYYY-MM-DD HH24:MI:SS.FF2"')		
	elif db_to.startswith('CSV'):
		(nls_d, nls_t, nls_tz)=('"YYYY/MM/DD"','"YYYY-MM-DD-HH24.MI.SS.FF"','"YYYY-MM-DD-HH24:MI:SS.FF"')		
		
	test['FROM']={}
	tfrom=test['FROM']	
	if db_from.startswith('ORA') and db_to.startswith('PGRES'):
		from_table='Timestamp_test_from'
		to_table='Timestamp_test_to'	

		#print db_from, db_to,
	if db_to.startswith('PGRES') or db_from.startswith('PGRES') or db_from.startswith('ORA') or db_to.startswith('ORA'):
		if 'Date' in db_from:
			from_table='Date_test_from'
			to_table='Date_test_to'
		elif 'Timestamp' in db_from:
			from_table='Timestamp_test_from'
			to_table='Timestamp_test_to'
		elif 'Timezone' in db_from:
			from_table='Timezone_test_from'
			to_table='Timezone_test_to'
		else:			
			from_table='Timestamp_test_from'
			to_table='Timestamp_test_to'

		
	qryfile=r'"%s\oracle_query.sql"' % qry_loc
	qryfile_table_named=r'"%s\SCOTT.TIMESTAMP_TEST_TO.0.sql"' % qry_loc

	key_from = db_from.split('_')[0].upper()
	key_to = db_to.split('_')[0].upper()
	if qryf.has_key(key_from):
		qryfile=qryf[key_from]
	key_key='%s:%s' % (db_from,key_to)
	if qryf.has_key(key_key):
		qryfile=qryf[key_key]
	
	if wide_test:
		from_table = 'wide_row_from'
		to_table = 'wide_row_to'				
		qryfile= r'"%s\oracle_query_with_widerows.sql"' % qry_loc	
	#print qryfile
	#e(0)
	csvfile_dt=r'"%s\oracle_shard_0_dt.data"' % data_loc
	csvfile_ts=r'"%s\oracle_shard_0_ts.data"' % data_loc
	csvfile_tz=r'"%s\oracle_shard_0_tz.data"' % data_loc
	#
	if db_from.startswith('CSV'):
		key_to = db_to.split('_')[0].upper()
		assert csvf_dt.has_key(key_to), 'Input file is not defined for %s(%s)' % (key_to,db_to)
		csvfile_dt=csvf_dt[key_to]
		assert csvf_ts.has_key(key_to), 'Input file is not defined for %s(%s)' % (key_to,db_to)
		csvfile_ts=csvf_ts[key_to]
		assert csvf_tz.has_key(key_to), 'Input file is not defined for %s(%s)' % (key_to,db_to)
		csvfile_tz=csvf_tz[key_to]
		data_dir = ddir[key_to]
	else:
		data_dir = ora_data_dir
	small_csvfile=r'"%s\oracle_shard_0_small.data"' % data_loc
	tfrom['CSV_DateFile']= 			( csvfile_dt, None, 0,	1000)
	mongo_file=r'C:\Python27\data_migrator_1239_mongo\test\v101\data\oracle_shard_0_mongo.csv'
	tfrom['CSV_MongoFile']= 			( mongo_file, None, 0,	1000)
	tfrom['CSV_DateFiles']= 			( '%s;%s' % (csvfile_dt,csvfile_dt), None, 0,	1000)
	tfrom['CSV_TimestampFile']= 	( csvfile_ts, None, 0,	1000)
	tfrom['CSV_TimezoneFile']= 		( csvfile_tz, None, 0,	1000)
	tfrom['CSV_File_Limit10']= 		( csvfile_ts, None, 0,	1000)
	tfrom['CSV_FileSkip1']= 	( csvfile_ts, None, 1,	100)
	
	tfrom['CSV_ShardedFile']= 	( csvfile_ts, None, 0,	10)
	tfrom['CSV_ShardedFile_Limit10']= ( csvfile_ts, None, 0,	10)
	tfrom['CSV_ShardedFileSkip1']= 	( csvfile_ts, None, 1,	10)
	
	tfrom['CSV_Dirs']= 			( None, data_dir, 0,	1000)
	tfrom['CSV_Dirs_Limit10']= 	( None, data_dir, 0,	1000)
	tfrom['CSV_DirsSkip1']= 	( None, data_dir, 1,	1000)
	tfrom['CSV_ShardedDir']= 	( None, data_dir, 0,	50)
	tfrom['CSV_ShardedDir_Limit10']= 	( None, data_dir, 0,	50)
	tfrom['CSV_ShardedDirSkip1']= 	( None, data_dir, 1,	50)

	home=os.path.dirname(os.path.realpath(__file__))	
	json_file=os.path.join(data_loc,'JSON_Mongo_Collection.js')
	json_file_noids=os.path.join(data_loc,'JSON_Mongo_Collection_noIDs.js')
	json_dir = os.path.join(data_loc,'JSON_data_dir')
	tfrom['JSON_Files']=( json_file, None, 0, 1000)
	tfrom['JSON_Files_noIDs']=( json_file_noids, None, 0, 1000)
	#tfrom['JSON_Dir']=( json_dir, None, 0, 1000)
	tfrom['JSON_Dirs']=( None,json_dir, 0, 1000)
	tfrom['JSON_ShardedDirs']=( None,json_dir, 0, 1000)

	ezconnect='SCOTT/tiger@//192.168.15.47:1521/orcl.localdomain'		
	orapart= 'part_15'
	oraspart='part_15_sp1'
	#noclient="SCOTT/tiger2@'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))'"
	#ora_conn='SCOTT/tiger2@orcl'
	if 0:
		ora_user, ora_pwd, ora_sid=('SCOTT', 'tiger', 'orcl_ol7',)
		noclient_connect_string='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=192.168.15.47)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl.localdomain)))';
		if db_from.startswith('CSV') or db_to.startswith('CSV'):
			ora_user, ora_pwd, ora_sid=('SCOTT', 'tiger2', 'orcl',)
			noclient_connect_string='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))'
	else:
		ora_user, ora_pwd, ora_sid=('SCOTT', 'tiger', 'orcl',)
		noclient_connect_string="'(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=orcl)))'"
	
	for dbkey in ('ORA12C','ORA11G', 'ORAEXA'):
		tfrom['%s_QueryFile' % dbkey]= (qryfile, None, None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		#tfrom['%s_QueryFile_withComaHeader' % dbkey]= (qryfile, None, None , None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_QueryFile_WithWideRows' % dbkey]= (qryfile, None, None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		
		tfrom['%s_QueryFile_noHeader' % dbkey]= (qryfile, None, None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_keepWhitespace' % dbkey]= (qryfile, None, None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,1)
		tfrom['%s_QueryFile_keepWhitespace_noHeader' % dbkey]= (qryfile, None, None ,None, None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,1)
		tfrom['%s_QueryFile_keepWhitespace_withHeader' % dbkey]= (qryfile, None, None , None,None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,1)
		tfrom['%s_QueryFile_trimWhitespace' % dbkey]= (qryfile, None, None , None,	None,None, None,None,ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_trimWhitespace_noHeader' % dbkey]= (qryfile, None, None , None,None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_trimWhitespace_withHeader' % dbkey]= (qryfile, None, None , None,None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_TimezoneQueryFile' % dbkey]= (qryfile, None, None , None,	None, None,None,None,ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_Limit10' % dbkey]= (qryfile, None, None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		tfrom['%s_QueryDir' % dbkey]= (None,qry_dir_ora,  None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_ShardedQueryDir' % dbkey]= (None,qry_dir_ora,  None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_Table_withHeader' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,None,None,None,	 ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_withHeader' % dbkey]= (qryfile, None, None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_QueryDir_withHeader' % dbkey]= (None,qry_dir_ora,  None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_ShardedQueryDir_withHeader' % dbkey]= (None,qry_dir_ora,  None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		#tfrom['%s_ShardedQueryDir_withComaHeader' % dbkey]= (None,qry_dir_ora,  None , None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		#tfrom['%s_QueryDir_withComaHeader' % dbkey]= (None,qry_dir_ora,  None , None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_QueryDir_TableNamedFiles' % dbkey]= (None,qry_dir_ora_table_named,  None ,None,None,None, None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryFile_TableNamedFile' % dbkey]= (qryfile_table_named, None, None ,None, None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryDir_WithWideRows' % dbkey]= (None,qry_dir_ora,  None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		tfrom['%s_QueryDir_keepWhitespace' % dbkey]= (None,qry_dir_ora,  None , None,None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,1)
		tfrom['%s_QueryDir_keepWhitespace_withHeader' % dbkey]= (None,qry_dir_ora,  None , None,None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,1)
		tfrom['%s_QueryDir_trimWhitespace' % dbkey]= (None,qry_dir_ora,  None , None,None,None,None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_QueryDir_Limit10' % dbkey]= (None,qry_dir_ora,  None , None,	None,None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		if citi:
			tfrom['ORA_QueryFile' ]= ('%s\\oracle_citi_query.sql' % qry_loc,  None , None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,   0,0)
			tfrom['ORA_QueryDir' ]= ( qry_dir_ora,  None , None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,   0,0)
			tfrom['ORA_Query_NoNLSDate']= ('%s\\oracle_citi_query.sql' % qry_loc,  None , None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,   0,0)
						# from_table, from_db, nls_date_format, nls_time_format
		
		tfrom['%s_Table_WithWideRows' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		tfrom['%s_JSON_Table' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None,ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_Table' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_TimestampTable' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_TimestampTable_withHeader' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,None,None,None,	 ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_TimestampTable_withComaHeader' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None, None,None,ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,0)
		tfrom['%s_TimestampTable_keepWhitespace_withHeader' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None, None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   1,1)
		tfrom['%s_TimestampTable_trimWhitespace' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_TimestampTable_keepWhitespace_Validate' % dbkey]= (None,None,'SCOTT.%s' % from_table, None,None,None, None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,1)
		tfrom['%s_ShardedTimestampTable_keepWhitespace_Validate' % dbkey]= (None,None,'SCOTT.%s' % from_table,None,None, None, None,None,	 ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,1)
		tfrom['%s_DateTable' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None, None,None,ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_DateTable_Email' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_DateTable_JobName' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_TimezoneTable' % dbkey]= (None,None,'SCOTT.%s' % from_table, None, None,None,	None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_TimezoneTable_KeepSpoolFile' % dbkey]= (None,None,'SCOTT.%s' % from_table,None,None,None, None, None,	 ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_Table_KeepSpoolFile' % dbkey]= 		 (None,None,'SCOTT.%s' % from_table,None,None,None, None, None,	 ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_Table_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_table, None,None,None, None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		if citi:
			tfrom['ORA_Table' ]= (None,None,'CSMARTOTD.OTD_VOL_FX', None, None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,    0,0)

		tfrom['%s_ShardedTable' % dbkey]= (None,None,'SCOTT.%s' % from_table,None,None, None, None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Parallel_ShardedTable' % dbkey]= (None,None,'SCOTT.%s' % from_table,None,None, None, None,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_ShardedTable_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_table, None,None,None,None, None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		
		tfrom['%s_TableList' % dbkey]= (None,None,None, 'SCOTT.%s,SCOTT.%s_2' % (from_table,from_table), None,	None,None,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,   0,0)
		
		if citi:
			tfrom['ORA_ShardedTable' ]= (None,None,'CSMARTOTD.OTD_VOL_FX', None, None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,    0,0)	

		tfrom['%s_Partition' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, orapart,None,None, None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_WithWideRows' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None, None, None,ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_NoClient' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, orapart,None,None,None, 	ora_user, ora_pwd, noclient_connect_string,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_TruncateTarget_AskToTruncate' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None,None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_withHeader' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None, None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   1,0)
		tfrom['%s_Partition_Validate' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None, orapart,None,None,None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_keepWhitespace' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, orapart,None,None,None,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,1)
		tfrom['%s_Partition_trimWhitespace' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None,None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_KeepSpoolFile' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, orapart,None,None,None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Partition_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None,	None,  ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,    0,0)
		if citi:
			tfrom['ORA_Partition' ]= (None,None,'CSMARTOTD.OTD_VOL_FX', 'P20141014',None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,    0,0)
		tfrom['%s_ShardedPartition' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None,	None,  ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,    0,0)
		tfrom['%s_ShardedPartition_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_part_table ,None,  orapart,None,None,None, 	 ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		
		tfrom['%s_PartitionList' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, None,'part_13,part_14,part_15,part_16' ,None, None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		
		tfrom['%s_Parallel_PartitionList' % dbkey]= (None,None,'SCOTT.%s' % from_part_table , None, None,'part_13,part_14,part_15,part_16' ,None,None,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		
		if citi:
			tfrom['ORA_ShardedPartition' ]= (None,None,'CSMARTOTD.OTD_VOL_FX' , 'P20141014',None,	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t, nls_tz,   0,0)
		tfrom['%s_Subpartition' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,  None,None, oraspart,None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Subpartition_WithWideRows' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,  None,None, oraspart,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Subpartition_withHeader' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table , None,None,None,  oraspart,None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   1,0)
		tfrom['%s_Subpartition_Validate' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table , None, None,None, oraspart,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_Subpartition_keepWhitespace' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table , None, None,None, oraspart,None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,1)
		tfrom['%s_Subpartition_KeepSpoolFile' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table , None,None, None, oraspart,None, ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,    0,0)
		tfrom['%s_Subpartition_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table , None,None,None,  oraspart,None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		if citi:
			tfrom['ORA_Subpartition' ]= (None,None,'CSMARTOTD.OTD_VOL_FX', None, 'P20141014',	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_ShardedSubpartition' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,None,  None,oraspart,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		tfrom['%s_ShardedSubpartition_Limit10' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,None,  None,oraspart,	None, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)
		if citi:
			tfrom['ORA_ShardedSubpartition' ]= (None,None,'CSMARTOTD.OTD_VOL_FX' , None, 'P20141014', 	'AD45676/Sep2014@SMARTC1B',nls_d, nls_t,  nls_tz,  0,0)

		tfrom['%s_SubpartitionList' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,  None,None, None,'%s,%s,%s,%s' % (oraspart,'part_15_sp2','part_14_sp1','part_14_sp2'), 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)					
		tfrom['%s_Parallel_SubpartitionList' % dbkey]= (None,None,'SCOTT.%s' % from_sub_part_table ,None,  None,None, None,'%s,%s,%s,%s' % (oraspart,'part_10_sp2','part_14_sp1','part_14_sp2'), 	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,   0,0)					
			
	dbkey='ORAXE'
	tfrom['ORAXE_QueryFile']= (qryfile,  None , None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,  0,0)
	tfrom['ORAXE_QueryDir']= (None,  qry_dir_ora , None,  	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,0,0)
	tfrom['ORAXE_ParallelQueryDir']= (None,  qry_dir_ora , None,  	ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz, 0,0)
	tfrom['ORAXE_DateTable']= (None,None,'SCOTT.%s' % from_table,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,0,0)
	tfrom['ORAXE_TimestampTable']= (None,None,'SCOTT.%s' % from_table,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,0,0)
	tfrom['ORAXE_Table']= (None,None,'SCOTT.%s' % from_table,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,0,0)
	tfrom['ORAXE_TimezoneTable']= (None,None,'SCOTT.%s' % from_table,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz, 0,0)
	tfrom['ORAXE_Table_KeepSpoolFile']= (None,None,'SCOTT.%s' % from_table,  ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz, 0,0)
	tfrom['ORAXE_ShardedTable']= (None,None,'SCOTT.%s' % from_table, ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz, 0,0)

	dbkey='MONGO'
	coll='test'
	db='test'
	jquery="\"{'COUNTRY':'United States'}\""
	#tfrom['MONGO_QueryFile']= (qryfile,  None , None, 	ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz,  0,0)
	#tfrom['MONGO_QueryDir']= (None,  qry_dir_ora , None,  	ora_user, ora_pwd, ora_sid,nls_d, nls_t,  nls_tz,0,0)
	#tfrom['MONGO_ParallelQueryDir']= (None,  qry_dir_ora , None,  	ora_user, ora_pwd, ora_sid,nls_d, nls_t, nls_tz, 0,0)
	#tfrom['MONGO_Table']= (None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',1)
	tfrom['MONGO_Query']= (jquery, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',0,0)
	tfrom['MONGO_Collection']= (None, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',0,0)
	tfrom['MONGO_Collection_JSON']= (None, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',0,0)
	tfrom['MONGO_Collection_Limit10']= (None, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',0,0)
	tfrom['MONGO_Collection_withHeader']= (None, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',1,0)
	tfrom['MONGO_Collection_Skip10']= (None, None,None, coll,  '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 'test_user', 'tast_pwd', db, 'localhost',  '27017',0,1)
	
	#mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "user_id,age,status" --type=csv  /o c:\tmp\test.csv /h localhost /port 27017
	
	dbkey='TTEN'
	tfrom['TTEN_QueryFile']= ( qryfile,None, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t, '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_QueryFile_Limit15']= ( qryfile,None, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_ShardedQueryFile']= ( qryfile,None, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_ParallelQueryDir']= ( None, qry_dir_tt, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_ParallelQueryDir_Limit30']= ( None, qry_dir_tt, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_QueryDir']= ( None, qry_dir_tt, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t, '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_QueryDir_Limit25']= ( None, qry_dir_tt, None,	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_Table']= ( None,None, 'TERRY.%s' % from_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_Table_KeepSpoolFile']= ( None,None, 'TERRY.%s' % from_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_Table_Limit20']= ( None,None, 'TERRY.%s' % from_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t, '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_ShardedTable']= ( None,None, 'TERRY.%s' % from_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t, '"%s"' %	dbclients[dbkey])
	tfrom['TTEN_ShardedTable_Limit40']= ( None,None, 'TERRY.%s' % from_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t,  '"%s"' %	dbclients[dbkey])
					
					# from_table, from_user, from_passwd, from_DSN_name, nls_date_format, nls_timestamp_format, source_client_home	

	dbkey='SSENT'
	ss_part='DateRange(Created)=3'
	tfrom['SSENT_QueryFile']= ( qryfile,None, None,None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_QueryFile_Limit15']= ( qryfile,None, None,None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_QueryDir']= ( None,qry_dir_ss, None,None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_QueryDir_Limit25']= ( None,qry_dir_ss, None,None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	
	tfrom['SSENT_ShardedQueryFile']= ( qryfile,None, None, None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])	
	tfrom['SSENT_Table']= ( None,None, from_table, None, 	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_Table_KeepSpoolFile']= ( None,None, from_table, None, 	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_Table_Limit10']= ( None,None, from_table, None, 	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_ShardedTable']= ( None, None,from_table, None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])	
	tfrom['SSENT_ShardedTable_Limit50']= ( None, None,from_table, None,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])	
	tfrom['SSENT_Partition']= ( None, None, from_part_table, ss_part,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_Partition_Limit20']= ( None, None, from_part_table, ss_part,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])
	tfrom['SSENT_ShardedPartition']= ( None,None, from_part_table, ss_part,	'sa', 'ssent_pwd', 'test',	'ALEX_BUZ-PC\MSSQLSERVER_ENT',	'"%s"' %	dbclients[dbkey])	
	
	dbkey='SSEXP'
	tfrom['SSEXP_QueryFile']= ( qryfile,None, None,	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_QueryFile_Limit15']= ( qryfile,None, None,	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_QueryDir']= ( None,qry_dir_ss,None,	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_QueryDir_Limit25']= ( None,qry_dir_ss,None,	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_ShardedQueryFile']= ( qryfile,None, None, 	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])	
	tfrom['SSEXP_Table']= ( None,None, from_table,  	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_Table_KeepSpoolFile']= ( None,None, from_table,  	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_Table_Limit10']= ( None,None, from_table,  	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
	tfrom['SSEXP_ShardedTable']= ( None, None,from_table, 'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])	
	tfrom['SSEXP_ShardedTable_Limit50']= ( None, None,from_table, 'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])	


	
	
	if 0:
		tfrom['SS_Query']= ( qryfile, 	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])
		tfrom['SS_ShardedQuery']= ( qryfile, 	'sa', '198Morgan', 'master',	'ALEX_BUZ-PC\SQLEXPRESS',	'"%s"' %	dbclients[dbkey])	
	
					#query_sql_file, 	from_user,  from_passwd,	from_db_name, from_db_server, 	source_client_home				
					
	dbkey='PGRES'
	pgres_part='Partitioned_test_from_2014'
	tfrom['PGRES_QueryFile']= 		( qryfile, None, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_QueryFile_Limit11']= 		( qryfile, None, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_ShardedQueryFile']=( qryfile, None, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_QueryDir']= 		( None, qry_dir_pgres, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_QueryDir_Limit12']= 		( None, qry_dir_pgres, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	
	tfrom['PGRES_ParallelQueryDir']=( None, qry_dir_pgres, None,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	
	tfrom['PGRES_DateTable']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_TimestampTable']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_Table']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_TimezoneTable']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_Table_KeepSpoolFile']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_Table_Limit15']= 			( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_ShardedTable']= 	( None, None, from_table,None, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_Partition']= 		( None, None, from_part_table,pgres_part, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_Partition_Limit33']= 		( None, None, from_part_table,pgres_part, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	tfrom['PGRES_ShardedPartition']=( None, None, from_part_table,pgres_part, 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey],'5434')
	#tfrom['PGRES_Subpartition']= ( None, None, 'Persons_partitioned','Persons_partition_2014_1_PersonID', 	'"postgres"', '"postgre_pwd"', '"postgres"',	'"localhost"',	'"%s"' %	dbclients[dbkey])

					#query_sql_file, 	from_user,  from_passwd,	from_db_name, from_db_server, 	postgres_client_home
					
	for dbkey in ('SYANY', 'SYIQ', 'SYASE'):
		tfrom['%s_QueryFile' % dbkey]=			(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)	
		tfrom['%s_QueryFile_Limit10' % dbkey]=			(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)	
		tfrom['%s_ShardedQueryFile' % dbkey]= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir' % dbkey]=(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir_Limit14' % dbkey]=(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir' % dbkey]= 		(None, qry_dir_sy, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir_Limit15' % dbkey]= 		(None, qry_dir_sy, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table' % dbkey]= 			(None, None, from_table, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_KeepSpoolFile' % dbkey]= 			(None, None, from_table, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_Limit22' % dbkey]= 			(None, None, from_table, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedTable' % dbkey]= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
	if 0:
		dbkey='SYIQ'				
		tfrom['SYIQ_QueryFile']=			(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)	
		tfrom['SYIQ_ShardedQueryFile']= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYIQ_ParallelQueryDir']=(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYIQ_QueryDir']= 		(None, qry_dir_sy, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYIQ_Table']= 			(None, None, from_table, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYIQ_ShardedTable']= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)

		dbkey='SYASE'				
		tfrom['SYASE_QueryFile']=			(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)	
		tfrom['SYASE_ShardedQueryFile']= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYASE_ParallelQueryDir']=(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYASE_QueryDir']= 		(None, qry_dir_sy, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYASE_Table']= 			(None, None, from_table, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
		tfrom['SYASE_ShardedTable']= 	(qryfile, None, None, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)

	
					#query_sql_file,	from_user,  from_passwd,	from_db_name, from_db_server,  source_client_home, header

	#dbkey='SYIQ'				
	#tfrom['SYIQ_Query']=(qryfile, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
					#query_sql_file,	from_user,  from_passwd,	from_db_name, from_db_server,  source_client_home, header
	#dbkey='SYASE'				
	#tfrom['SYASE_Query']=(qryfile, '"dba"', '"sql"', '"demo"', '"demo16"', '"%s"' % dbclients[dbkey], 0)
					#query_sql_file,	from_user,  from_passwd,	from_db_name, from_db_server,  source_client_home, header
	#dbkey='DBTUDB'		
	for dbkey in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
		tfrom['%s_QueryFile' % dbkey]=(qryfile,None, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryFile_Limit10' % dbkey]=(qryfile,None, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir' % dbkey]=(None, qry_dir_db2, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir_Limit10' % dbkey]=(None, qry_dir_db2, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir' % dbkey]=(None, qry_dir_db2, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir_Limit10' % dbkey]=(None, qry_dir_db2, None, None,'"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedQueryFile' % dbkey]=(qryfile,None, None, None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table' % dbkey]=(None,None, from_table,None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_Limit20' % dbkey]=(None,None, from_table,None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_KeepSpoolFile' % dbkey]=(None,None, from_table,None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedTable' % dbkey]=(None,None, from_table, None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedTable_Limit65' % dbkey]=(None,None, from_table, None, '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedPartition' % dbkey]=(None,None, from_part_table, '0', '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedPartition_Limit50' % dbkey]=(None,None, from_part_table, '0', '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Partition' % dbkey]=(None,None,from_part_table, '0', '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Partition_Limit30' % dbkey]=(None,None, from_part_table, '0', '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
	

	#query_sql_file,	from_user,  from_passwd,	from_db_name, from_db_server,  source_client_home, header	
	infor='ol_s_121414_204157'
	infordb='test'
	infor_pwd='test_pwd'
	#dbkey='INFOR'
	for dbkey in ('INFOR','INFORC'):
		tfrom['%s_QueryFile' % dbkey]=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryFile_Limit20' % dbkey]=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir' % dbkey]=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_QueryDir_Limit25' % dbkey]=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir' % dbkey]=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ParallelQueryDir_Limit30' % dbkey]=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedQueryFile' % dbkey]=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedQueryFile_Limit55' % dbkey]=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table' % dbkey]=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_KeepSpoolFile' % dbkey]=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_Table_Limit15' % dbkey]=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedTable' % dbkey]=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['%s_ShardedTable_Limit66' % dbkey]=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
					#query_sql_file,	from_user,  from_passwd,	from_db_name, from_db_server,  source_client_home, header
	if 0:
		dbkey='INFORC'				
		tfrom['INFORC_QueryFile']=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['INFORC_QueryDir']=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['INFORC_ParallelQueryDir']=(None, qry_dir_infor, None,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['INFORC_ShardedQueryFile']=(qryfile,None, None, '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
		tfrom['INFORC_Table']=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 1)	
		tfrom['INFORC_ShardedTable']=(None,None, 'Persons_pipe_datetime_1', '"informix"', '"%s"' % infor_pwd, '"%s"' % infordb,  '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
	
	dbkey='MARIA'
	mysql_part='rx2015'
	tfrom['MARIA_QueryFile']= ( qryfile, None,None,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_QueryFile_Limit100']= ( qryfile,None, None,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_QueryDir']= ( None, qry_dir_mysql,None,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_QueryDir_Limit333']= ( None, qry_dir_mysql,None,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_ShardedQuery']= ( qryfile,None, None,None,	None,'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Table']= ( None,None, 'TEST.%s' % from_table,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Table_Limit1000']= ( None,None, 'TEST.%s' % from_table,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Table_KeepSpoolFile']= ( None,None, 'TEST.%s' % from_table,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	
						  
	tfrom['MARIA_ShardedTable']= ( None,None, 'TEST.%s' % from_table,None,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Partition']= ( None,None, 'TEST.%s' % from_part_table,mysql_part,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Partition_Limit22']= ( None,None, 'TEST.%s' % from_part_table,mysql_part,None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_ShardedPartition']= ( None,None, 'TEST.%s' % from_part_table,mysql_part, None,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Subpartition']= ( None, None,'TEST.%s' % from_sub_part_table,None,mysql_part,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_Subpartition_Limit33']= ( None, None,'TEST.%s' % from_sub_part_table,None,mysql_part,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	tfrom['MARIA_ShardedSubpartition']= ( None,None, 'TEST.%s' % from_sub_part_table,None,mysql_part,	'"root"', '"maria_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])

	mysql_spart='subpart200'
	for dbkey in ('MYSQL','INFOB'):
		tfrom['%s_QueryFile' % dbkey]= ( qryfile, None, None,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_TimezoneQueryFile' % dbkey]= ( qryfile, None, None,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		
		tfrom['%s_QueryFile_Limit100' % dbkey]= ( qryfile, None, None,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_QueryDir' % dbkey]= ( None,qry_dir_mysql, None, None, None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_QueryDir_Limit333' % dbkey]= ( None,qry_dir_mysql, None, None, None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_ShardedQuery' % dbkey]= ( qryfile, None, None,None,	None,'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Table' % dbkey]= ( None, None, 'TEST.%s' % from_table,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Table_Limit1000' % dbkey]= ( None, None, 'TEST.%s' % from_table,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Table_KeepSpoolFile' % dbkey]= ( None, None, 'TEST.%s' % from_table,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
						
		tfrom['%s_ShardedTable' % dbkey]= ( None, None, 'TEST.%s' % from_table,None,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Partition' % dbkey]= ( None, None, 'TEST.%s' % from_part_table,mysql_part,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Partition_Limit22' % dbkey]= ( None, None, 'TEST.%s' % from_part_table,mysql_part,None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_ShardedPartition' % dbkey]= ( None, None, 'TEST.%s' % from_part_table,mysql_part, None,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Subpartition' % dbkey]= ( None, None, 'TEST.%s' % from_sub_part_table,None,mysql_spart,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_Subpartition_Limit33' % dbkey]= ( None, None, 'TEST.%s' % from_sub_part_table,None,mysql_spart,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
		tfrom['%s_ShardedSubpartition' % dbkey]= ( None, None, 'TEST.%s' % from_sub_part_table,None,mysql_spart,	'"alex"', '"mysql_pwd"', '"test"',	'"localhost"',	'"%s"' %	dbclients[dbkey])
	#"C:\Program Files\MySQL\MySQL Server 5.6\bin\mysql.exe" "--defaults-file=C:\Program Files\MySQL\MySQL Server 5.6\my.ini" "-uroot" "-p" "--default-character-set=utf8"
	
					#query_sql_file, 	from_user,  from_passwd,	from_db_name, from_db_server, 	source_client_home	 	, source_defaults_file		
	dbkey='SLITE'
	db='database.db'
	tfrom['SLITE_QueryFile']= ( qryfile, None,None, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_ShardedQueryFile']= ( qryfile, None,None, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_QueryDir']= ( None, qry_dir_slite,None, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_ParallelQueryDir']= ( None, qry_dir_slite,None, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_Table']= ( None, None,from_table, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_Table_KeepSpoolFile']= ( None, None,from_table, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
	tfrom['SLITE_ShardedTable']= ( None, None,from_table, 'C:\Temp\SqlLite\\%s' % db, 0, '"%s"' %	dbclients[dbkey])
					#query_sql_file, 				from_db_name, 	source_client_home	 

	test['TO']={}
	tto=test['TO']

	to_orapart='part_13'
	for dbkey in ['ORA12C','ORA11G', 'ORAEXA']:
		
		
		tto['%s_Table' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, 0)
		tto['%s_Table_SkipHeader' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, "1")
		#tto['%s_Table_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
		tto['%s_Table_GetTabnameFromQuery' % dbkey]=(ora_user, ora_pwd, ora_sid, '',None,None,nls_d, nls_t,nls_tz, 0)
		tto['%s_Table_GetTabnameFromQuery_DeleteTargetRecs' % dbkey]=(ora_user, ora_pwd, ora_sid, '',None,None,nls_d, nls_t,nls_tz, 0 )
		tto['%s_Table_DeleteTargetRecs' % dbkey]=(ora_user, ora_pwd, ora_sid,'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, 0)
		#tto['%s_Table_WithWideRows' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
		tto['%s_Table_NoClient' % dbkey]=(ora_user, ora_pwd, noclient_connect_string, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, 0  )
		tto['%s_Table_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, 0  )
		tto['%s_Table_TruncateTarget_NoClient' % dbkey]=(ora_user, ora_pwd, noclient_connect_string, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, 0  )
		tto['%s_Partition' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,to_orapart,None,nls_d, nls_t,nls_tz, 0  )
		#tto['%s_Partition_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,orapart,None,nls_d, nls_t,nls_tz  )
		tto['%s_Partition_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,orapart,None,nls_d, nls_t,nls_tz, 0  )
		tto['%s_Subpartition' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,oraspart,nls_d, nls_t,nls_tz, 0  )
		#tto['%s_Subpartition_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,oraspart,nls_d, nls_t,nls_tz  )
		tto['%s_Subpartition_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_sub_part_table,None,oraspart,nls_d, nls_t,nls_tz, 0  )
	if 0:
		for dbkey in ['ORA11G', 'ORAEXA']:
			tto['%s_Table' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			#tto['%s_Table_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_GetTabnameFromQuery' % dbkey]=(ora_user, ora_pwd, ora_sid, '',None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_GetTabnameFromQuery_DeleteTargetRecs' % dbkey]=(ora_user, ora_pwd, ora_sid, '',None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_DeleteTargetRecs' % dbkey]=(ora_user, ora_pwd, ora_sid,'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			#tto['%s_Table_WithWideRows' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_NoClient' % dbkey]=(ora_user, ora_pwd, noclient_connect_string, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Table_TruncateTarget_NoClient' % dbkey]=(ora_user, ora_pwd, noclient_connect_string, 'SCOTT.%s' % to_table,None,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Partition' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,orapart,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			#tto['%s_Partition_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,orapart,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Partition_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_part_table,orapart,None,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Subpartition' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,oraspart,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			#tto['%s_Subpartition_WithLoaderProfile' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table,None,oraspart,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )
			tto['%s_Subpartition_TruncateTarget' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_sub_part_table,None,oraspart,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )


		
	if citi:
		tto['%s_Table' % dbkey]=('CSMARTOTD/sl14Hm@SMARTD1', 'CSMARTOTD.OTD_VOL_FX',nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )

	dbkey='ORAXE'		
	tto['%s_Table' % dbkey]=(ora_user, ora_pwd, ora_sid, 'SCOTT.%s' % to_table ,nls_d, nls_t,nls_tz, '"%s"' % dbclients[dbkey] )	
	dbkey='MONGO'		
	tto['MONGO_Collection' ]=('test_user', 'tast_pwd', 'test', 'localhost', '27017', 'test', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"', 0,1)	
	tto['MONGO_Collection_Upsert' ]=('test_user', 'tast_pwd', 'test', 'localhost', '27017', 'test', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"',1,1)	
	tto['MONGO_Collection_3_insertionWorkers' ]=('test_user', 'tast_pwd', 'test', 'localhost', '27017', 'test', '"ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED"',0,3)	
	#mongoimport.exe  -u test_user -p tast_pwd /d test /c test /file c:\tmp\test_in.txt /f "user_id,age,status" /type csv
		
		
				
	csvOUTfile=os.path.join(conf.home,'CSV_OUT', 'test%s.csv' % db_from)
	csvOUTdir= os.path.join(conf.home, 'CSV_OUT')
	#print ts
	#e(0)
	#csvRemoteOUTfile= '/tmp/qctest/CSV_OUT/%s_spool.data' % db_from

	dbkey='CSV'
	
	tto['CSV_File']=(csvOUTfile, None)
	#tto['CSV_RemoteFile']=(csvRemoteOUTfile, None)
	tto['CSV_Dir']=(None, csvOUTdir)
	tto['CSV_Default']=(None, None)

	jsonOUTfile=os.path.join(conf.home,'JSON_OUT', 'test%s.js' % db_from)
	jsonOUTdir= os.path.join(conf.home, 'JSON_OUT')
	#print ts
	#e(0)
	#csvRemoteOUTfile= '/tmp/qctest/CSV_OUT/%s_spool.data' % db_from

	dbkey='JSON'
	
	tto['JSON_File']=(jsonOUTfile, None)
	#tto['CSV_RemoteFile']=(csvRemoteOUTfile, None)
	tto['JSON_Dir']=(None, jsonOUTdir)
	tto['JSON_Default']=(None, None)
	
	ddlOUTfile=os.path.join(conf.home,'DDL_OUT', 'test%s.ddl' % db_from)
	ddlOUTdir= os.path.join(conf.home, 'DDL_OUT')

	dbkey='DDL'
	
	tto['DDL_File']=(ddlOUTfile, None)
	tto['DDL_Dir']=(None, ddlOUTdir)
	tto['DDL_Default']=(None, None)
	
	
				#to_file
	dbkey='SSEXP'				
	tto['%s_Table' % dbkey]=( 'sa',  '198Morgan', 'master', 'ALEX_BUZ-PC\SQLEXPRESS', 'dbo.%s' % to_table,'"%s"' % dbclients[dbkey],0)
				#to_user, to_passwd, 	to_db_name, to_db_server,			  to_table
	dbkey='SSENT'				
	tto['%s_Table' % dbkey]=( 'sa',  'ssent_pwd', 'test', 'ALEX_BUZ-PC\MSSQLSERVER_ENT', 'dbo.%s' % to_table,'"%s"' % dbclients[dbkey],0)
	 
				#to_user, to_passwd, 	to_db_name, to_db_server,			  to_table

					
	dbkey='MYSQL'			
	tto['%s_Table' % dbkey]=('alex',  'mysql_pwd', 'test', 	'localhost',	to_table, '"%s"' % dbclients[dbkey])
	dbkey='INFOB'			
	tto['%s_Table' % dbkey]=('alex',  'mysql_pwd', 'test', 	'localhost',	to_table, '"%s"' % dbclients[dbkey])
	
				#to_user, to_passwd, to_db_name, to_db_server,  to_table, mysql_client_home
				
	dbkey='PGRES'			
	tto['%s_Table' % dbkey]=('"postgres"', '"postgre_pwd"', '"postgres"', 	'"localhost"', '"%s"' % to_table, '"%s"' % dbclients[dbkey],'5434',0)
	tto['%s_Table_SkipHeader' % dbkey]=('"postgres"', '"postgre_pwd"', '"postgres"', 	'"localhost"', '"%s"' % to_table, '"%s"' % dbclients[dbkey],'5434',1)
				#to_user, 	to_passwd, 		to_db_name, to_db_server, to_table, postgres_client_home
	dbkey='SYANY'			
	tto['%s_Table' % dbkey]=('"dba"', '"sql"', '"demo"', 	'"demo16"', '"%s"' % to_table, '"%s"' % dbclients[dbkey],0)
				#to_user, 	to_passwd, 		to_db_name, to_db_server, to_table, postgres_client_home, 	skip_rows
	dbkey='SYIQ'			
	tto['%s_Table' % dbkey]=('"dba"', '"sql"', '"demo"', 	'"demo16"', '"%s"' % to_table, '"%s"' % dbclients[dbkey],0)
				#to_user, 	to_passwd, 		to_db_name, to_db_server, to_table, postgres_client_home, 	skip_rows			
	dbkey='SYASE'			
	tto['%s_Table' % dbkey]=('"dba"', '"sql"', '"demo"', 	'"demo16"', '"%s"' % to_table, '"%s"' % dbclients[dbkey],0)
				#to_user, 	to_passwd, 		to_db_name, to_db_server, to_table, postgres_client_home, 	skip_rows			
	dbkey='TTEN'			
	tto['%s_Table' % dbkey]= ( 'TERRY.%s' % to_table , 	'TERRY', 'secret', 'my_ttdb', nls_d, nls_t, nls_tz, '"%s"' %	dbclients[dbkey],0)
					# to_table, from_user, to_passwd, from_DSN_name, nls_date_format, nls_timestamp_format, target_client_home, skip_rows	
	#pprint(tto['%s_Table' % dbkey])
	#e(0)
	#dbkey='DBTUDB'	
	for dbkey in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
		tto['%s_Table' % dbkey]=('ALEX_BUZ.%s' % to_table , '"ALEX_BUZ"', '"198Morgan"', '"SAMPLE"', '"DB2"', '"%s"' % dbclients[dbkey], 0)
			   #to_table,	from_user,  to_passwd,	to_db_name, to_db_server,  target_client_home, skip_rows

	infor='ol_s_121414_204157'
	infordb='test'
	infor_pwd='test_pwd'
	# C:\Windows\System32\cmd.exe cmd /k C:\PROGRA~2\IBMINF~1\ol_s_112614_175026.cmd
	dbkey='INFOR'				
	tto['%s_Table' % dbkey]=( '%s' % to_table ,'"informix"', '"%s"' % infor_pwd, '"%s"' % infordb, '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
				#to_table,	from_user,  to_passwd,	to_db_name, to_db_server,  target_client_home, skip_rows
	dbkey='INFORC'				
	tto['%s_Table' % dbkey]=( '%s' % to_table ,'"informix"', '"infor_pwd"', '"test"', '"%s"' % infor, '"%s"' % dbclients[dbkey], 0)
				#to_table,	from_user,  to_passwd,	to_db_name, to_db_server,  target_client_home, skip_rows				
	dbkey='MARIA'			
	tto['%s_Table' % dbkey]=('"root"', '"maria_pwd"', '"test"',	'"localhost"',	to_table, '"%s"' % dbclients[dbkey])
				#to_user, to_passwd, to_db_name, to_db_server,  to_table, mysql_client_home	
	dbkey='SLITE'
	tto['%s_Table' % dbkey]= (  '%s' % to_table,  'C:\Temp\SqlLite\\database2.db', 0, '"%s"' %	dbclients[dbkey])
					#query_sql_file, 				from_db_name, 	source_client_home	 
	return test

def run_test(db_from, db_to, prog, test,citi=False):
	e(0)
	global conf, from_table, to_table
	#print db_from, db_to
	#	print prog
	#e(0)
	core_keys=conf.params['core'].keys()
	#pprint(core_keys)
	#e(0)
	pt='core'
	#pprint(test[pt])
	pars=conf.params['core']
	#pprint (pars.keys())
	#pprint test[pt])
	#e(0)
	#print map(lambda x: '%s %s' % (pars[core_keys[x]]['short'], test[pt][x]),range(len(core_keys)))
	api_core={pars[core_keys[i]]['long'].strip('-'):(pars[core_keys[i]]['short'], pars[core_keys[i]]['long'],test[pt][i],pars[core_keys[i]]['help'])  for i in range(len(core_keys)) if test[pt][i]} 
	#pprint(api_core)
	core_p= ["%s %s" % (pars[core_keys[i]]['short'],test[pt][i])  for i in range(len(core_keys)) if test[pt][i]] #conf.params['core'][core_keys[i]]['short']]
	core_p_long= ["%s %s" % (pars[core_keys[i]]['long'],test[pt][i])  for i in range(len(core_keys)) if test[pt][i]] #conf.params['core'][core_keys[i]]['short']]
	core_p_help= ["%s" % (pars[core_keys[i]]['help'])  for i in range(len(core_keys)) if test[pt][i]] #conf.params['core'][core_keys[i]]['short']]
	#print str(args_api)	
	
	#print ' '.join(core_p)
	#pprint(core_p)
	#pprint(core_p_long)
	#pprint(core_p_help)
	#e(0)

	pt='FROM'
	paramkey_from=db_from.split('_')[0]
	#pprint (paramkey_from)
	#pprint(conf.params['FROM'].keys())
	par_keys=conf.params['FROM'][paramkey_from].keys()
	#pprint(par_keys)
	#pprint(test[pt][db_from])
	pars=conf.params['FROM'][paramkey_from]
	#pprint  (pars.keys())
	#pprint(test[pt][db_from])
	#print  test[pt][db_from]
	print db_from, db_to
	api_from={pars[par_keys[i]]['long'].strip('-'):(pars[par_keys[i]]['short'], pars[par_keys[i]]['long'],test[pt][db_from][i],pars[par_keys[i]]['help'])  for i in range(len(par_keys)) if test[pt][db_from][i]} 
	
	#pprint(api_from)
	from_p= ["%s %s" % (pars[par_keys[i]]['short'],test[pt][db_from][i])  for i in range(len(par_keys)) if test[pt][db_from][i]]
	
	from_p_long= ["%s %s" % (pars[par_keys[i]]['long'],test[pt][db_from][i])  for i in range(len(par_keys)) if test[pt][db_from][i]] #conf.params['core'][par_keys[i]]['short']]
	from_p_help= ["%s" % (pars[par_keys[i]]['help'])  for i in range(len(par_keys)) if test[pt][db_from][i]] #conf.params['core'][par_keys[i]]['short']]
	#print ' '.join(from_p)
	#pprint(from_p)
	#sys.exit(0)
	pt='TO'
	paramkey_to=db_to.split('_')[0]
	#print paramkey_to
	
	par_keys=conf.params[pt][paramkey_to].keys()
	#pprint (par_keys)
	pars=conf.params[pt][paramkey_to]
	#print pars
	#print map(lambda x: '%s %s' % (pars[par_keys[x]]['short'], test[pt]['PGRES'][x]),range(len(par_keys)))
	#print par_keys
	#pprint (pars)
	#print test[pt]['ORA11G']
	#pprint (test[pt][db_to])
	api_to={ pars[par_keys[i]]['long'].strip('-'):(pars[par_keys[i]]['short'], pars[par_keys[i]]['long'],test[pt][db_to][i],pars[par_keys[i]]['help'])  for i in range(len(par_keys)) if test[pt][db_to][i]} 
	to_p= ["%s %s" % (pars[par_keys[i]]['short'],test[pt][db_to][i])  for i in range(len(par_keys)) if test[pt][db_to][i]] #conf.params['core'][par_keys[i]]['short']]
	to_p_long= ["%s %s" % (pars[par_keys[i]]['long'],test[pt][db_to][i])  for i in range(len(par_keys)) if test[pt][db_to][i]] #conf.params['core'][par_keys[i]]['short']]
	to_p_help= ["%s" % (pars[par_keys[i]]['help'])  for i in range(len(par_keys)) if test[pt][db_to][i]]
	#e(0)
	#print to_p
	#sys.exit(1)
	#plist=prog+core_p+from_p+to_p
	#pprint (plist)
	#print to_p
	tall=[]
	if 1:
		print prog
		comment=['%s[%s] is "%s"' % (core_p[i].split(' ')[0], core_p_long[i].split(' ')[0],core_p_help[i]) for i in range(len(core_p))]
		comment=comment+ ['%s[%s] is "%s"' % (from_p[i].split(' ')[0], from_p_long[i].split(' ')[0],from_p_help[i]) for i in range(len(from_p))]
		comment=comment+ ['%s[%s] is "%s"' % (to_p[i].split(' ')[0], to_p_long[i].split(' ')[0],to_p_help[i]) for i in range(len(to_p))]
		pcmd = ' '.join(prog)+' ^\n'+' ^\n'.join(core_p+from_p+to_p)
		tall.append(pcmd)	
		#pprint (pcmd)
		#pprint(core_p)
		#e(0)
	else:	
		cmd=' '.join(plist)
		print cmd

		lexer=shlex.shlex(cmd)
		#lexer = shlex.shlex(input)
		lexer.quotes = '"'
		#lexer.wordchars += '\''
		lexer.whitespace_split = True
		lexer.commenters = ''
		cfg = list(lexer)
		#sys.exit(1)
		p = Popen(cfg, stdin=PIPE, stdout=PIPE)
		out, err = p.communicate('y\n')
		p.wait()
		print out
		print '-'*40
		print err
	tout= ('__').join(tall)
	#if conf.release:
	#	tout= tout.replace('198Morgan','test_pwd')
		
	mult=40
	cmt='::'*mult+'\n::'+'\n::'.join(comment)+'\n'+'::'*mult
	#cmt='REM\n'+'\nREM '+'\nREM '.join(comment)+'\n'+'REM\n'
	#print tout
	#sys.exit(0)
	echo ='echo y'
	if ('TruncateTarget' in db_from or  'TruncateTarget' in db_to) and ('AskToTruncate' in db_from or  'TruncateTarget' in db_to):
		echo=r"""..\\python -c "print 'y\ny'" """
	if 1:
		scr=r'%s\bat\%s%s%s_test.bat' % (home,conf._to,db_from.lower(), db_to.lower())
		print ''
		print scr
		f=open( scr,'w')

		f.write(cmt+'\n%s|%s' % (echo,tout))
		f.close()
	
	scr=r't.bat'

	f=open( scr,'w')

	f.write(cmt+'\n%s|%s' % (echo, tout))
	f.close()
		
	if 'DBTUDB' in (db_from, db_to):
		
		db2_cmd=r'"C:\Program Files (x86)\IBM\SQLLIB_01\BIN\db2cmdadmin" db2setcp "%s"' % (scr)
		f=open('db2_test.bat', 'w')

		f.write(db2_cmd)
		f.close()
	#pprint (tout)
	#e(0)
	api="""# Title:	%s -->> %s
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
from args_api import args_api
api=args_api(%s, 
	%s, 
	%s)
	""" % (db_from,db_to,str(api_core), str(api_from), str(api_to))
	#pprint(api_core)
	#e(0)
	#print db_from, db_to
	source=db_from.split('_')[0]
	target=db_to.split('_')[0]
	if 0:
		api_dirname= os.path.join(home,'args_api')
		if not os.path.isdir(api_dirname):
			os.makedirs(api_dirname) 
		dirname= os.path.join(api_dirname,source,target)
		if not os.path.isdir(dirname):
			os.makedirs(dirname) 
		py_name='%s.%s.py' % (db_from, db_to)
		fname= os.path.join(dirname,py_name)
		
	
	#scr=r't.bat'
	if 0:
		f=open( fname,'w')

		f.write(api)
		f.close()
		print dirname
		#pprint (globals())
		import shutil
		
		api_todir=os.path.join(r'C:\Users\alex_buz\Documents\GitHub\DataBuddy\sources','args_api',source,target)
		api_tofile= os.path.join(api_todir, py_name)
		if not os.path.isdir(api_todir):
			os.makedirs(api_todir) 
		if os.path.isfile(api_tofile):
			print 'file exists'
			os.remove(api_tofile)
		shutil.copyfile(fname,api_tofile)
		print api_tofile
	if 1:
		keys=[]
		from_args=conf.params['FROM'][source]
		to_args=conf.params['TO'][target]
		for key,arg in conf.params['core'].items():
			keys.append(key)
			print arg['short'], key,
		for key,arg in from_args.items():
			keys.append(key)
			print arg['short'], key,
		for key,arg in to_args.items():
			if not key in keys:
				keys.append(key)
				print arg['short'], key,
		print '\n'
		print 'Here:'
		#print keys
		default_core={}
		default_from={}
		default_to={}
		for key in keys:
			if key in conf.params['core'].keys():
				arg=conf.params['core'][key]
				print '(Common) %s [%s]\t%s\t' % (arg['short'],arg['long'],arg['help'])	
				default_core[arg['long'].strip('-')]=[arg['short'], arg['long'],'',arg['help']]				
			elif key in from_args.keys():
				arg=from_args[key]
				print '(From %s) %s [%s]\t%s\t' % (dbs[source],arg['short'],arg['long'],arg['help'])
				default_from[arg['long'].strip('-')]=[arg['short'], arg['long'],'',arg['help']]	
			else:
				arg=to_args[key]
				print '(To %s) %s [%s]\t%s\t' % (dbs[target],arg['short'],arg['long'],arg['help'])
				default_to[arg['long'].strip('-')]=[arg['short'], arg['long'],'',arg['help']]
	default_api="""# Title:	Default API.
# Description:	Arguments API for data-buddy.
__author__ = "Alex Buzunov, Sequelworks Inc."
__copyright__ = "Copyright 2015, data-buddy"
# do not change below this line
from args_api import args_api
api=args_api(%s, 
	%s, 
	%s)
	""" % (str(default_core), str(default_from), str(default_to))
	#default_py_name='%s_%s_default.py' % (source, target)
	#def_fname= os.path.join(dirname,default_py_name)
	
	
	#scr=r't.bat'
	if 0:
		f=open( def_fname,'w')

		f.write(default_api)
		f.close()
		default_api_tofile= os.path.join(api_todir, default_py_name)
		if os.path.isfile(default_api_tofile):
			print 'default file exists'
			os.remove(default_api_tofile)
		shutil.copyfile(def_fname,default_api_tofile)
	#print def_fname	
	#e(0)
	return (comment,r'%s|%s' % (echo,tout),((db_from,db_to),[api_core, api_from, api_to],[default_core, default_from,default_to]))

	