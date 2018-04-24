#		__builtin__.copy_vector = copy_vector
#		__builtin__.cvarg = cvarg
#print copy_vector
#print cvarg
#e(0)
import time, os, sys
import logging
import random
import shutil
from  collections import OrderedDict
from common.v101.exceptions import CopyVectorError
import datetime
from common.v101.loaders import import_module
e=sys.exit
home=os.path.abspath(os.path.dirname(sys.argv[0]))
abspath=os.path.join(home,'qc32')
print abspath
if not os.path.isdir(abspath):
	abspath=home
print abspath

import_module=import_module
from pprint import pprint
import argparse
#from common_conf import *

imp_file = os.path.join(abspath,'config','common_conf.py')
#print imp_file
#e(0)
cconf=import_module(imp_file)
dbs=cconf.dbs

dbfam=cconf.dbfam
import __builtin__
__builtin__.dbs = dbs		
import release as rel 
appn,bin,appex=(rel.appn,rel.bin,'exe')
appname='Datamule' #rel.appname
rv='v101'
#app_author=rel.app_author
#apptitle=rel.apptitle 
e=sys.exit
default_vector=None 
#version=rel.version
rel_date=rel.ts
citi=False
if_hg=False #hourglass
_to='-'
ff=['CSV','JSON','DDL'] #file v.s. db 
tt=['PCSP.r10156']
dt=['CURL'] #download tools
#SQL*Loader init
#dlp={}
#dlp['ORA12C']=dlp['ORA11G']=dlp['ORAEXA']=dlp['ORAXE']=os.path.join(home,r'config','sqlloader.py')
#dlp['ORA11G']=r'"C:\Python27\data_migrator_1239\config\loader\sqlloader.yaml"'

def getRegSize():
	return rel.bin

#getAppTitle=rel.getAppTitle


def setreg(reg):
	global bin,appname, rel
	bin=reg
	rel.bin=reg
	appname= '%s%s.%s' % (appn,bin,appex)

# Datamule args
app_descr= "" #rel.app_descr
def get_descr_del():
	
	descr="""
Command line tool for CSV data extraction from %s databases:\n\n%s\n""" % (len(dbs)-1,'\n'.join(sorted([x for x in dbs.values() if not x.startswith('CSV') ])))
	if from_dbs and to_dbs:
		if for_dbs:
			if from_dbs[0]==to_dbs[0]:
				descr="""
Command line tool for %s data migration to/from %s databases:\n\n%s\n""" % (dbs[from_dbs[0]],len(to_dbs)-1,'\n'.join(sorted([dbs[x] for x in to_dbs if not x.startswith('CSV') ])))
			else:
				descr="""
Command line tool for %s data migration to %s:\n\n%s\n""" % (dbs[from_dbs[0]],dbs[to_dbs[0]],'\n'.join(sorted(['%s->%s' % (dbs[from_dbs[0]],dbs[x]) for x in to_dbs if not x.startswith('CSV') ])))
				
		else:
			if from_dbs[0] in ['CSV']:
				descr="""
	Command line tool for CSV data load to %s database.""" % (dbs[to_dbs[0]])
			elif to_dbs[0] in ['CSV']:
				descr="""
	Command line tool for CSV data extraction from %s database.""" % (dbs[from_dbs[0]])
			else:
				if 'Table' in apptitle:
					descr="""
	Command line tool for Table data copy from %s to %s database.""" % (dbs[from_dbs[0]],dbs[to_dbs[0]])
				elif 'Query' in apptitle:
					descr="""
	Command line tool for query results copy from %s to %s database.""" % (dbs[from_dbs[0]],dbs[to_dbs[0]])
			#elif from_dbs[0]
	return descr
def set_params(params):
	#print '/'*60
	#print copy_vector
	FROMDB,TODB = None, None
	if copy_vector:
		FROMDB= copy_vector.split(_to)[0].upper()
		TODB= copy_vector.split(_to)[1].upper()
	params['core']={}
	pcore=OrderedDict()
	if 1:		
		#pfrom[dbkey]=OrderedDict()
		import __builtin__
		__builtin__.pcore = pcore
		imp_file = os.path.join(abspath,'config','include','args','core.py')
		#print imp_file
		import_module(imp_file)
	params['core']=pcore	
	if 0:
		params['core']['copy_vector']={'short':'-w','long':'--copy_vector', 'type':str, 'default':default_vector, 'help':'Data copy direction.'}
		params['core']['pool_size']={'short':'-o','long':'--pool_size', 	'type':int, 'default':1, 'help':'Pool size.'}
		params['core']['num_of_shards']={'short':'-r','long':'--num_of_shards', 'type':int, 'default':1, 'help':'Number of shards.'}
		params['core']['field_term']= {'short': '-t','long':'--field_term', 'type':str, 'default':'|', 'help':'Field terminator.'}
		params['core']['lame_duck']={'short':'-l','long':'--lame_duck', 'type':int, 'default':0, 'help':'Limit rows (lame duck run).'}
		params['core']['keep_data_file']={'short':'-K','long':'--keep_data_file', 'type':int, 'default':0, 'help':'Keep data dump.'}
		params['core']['validate']={'short':'-V','long':'--validate', 'type':int, 'default':0, 'help':'Check if source and target objects exist.'}
		params['core']['truncate_target']={'short':'-U','long':'--truncate_target', 'type':int, 'default':0, 'help':'Truncate target table/partition/subpartition.'}
		params['core']['ask_to_truncate']={'short':'-E','long':'--ask_to_truncate', 'type':int, 'default':0, 'help':'Ask to truncate.'}
		params['core']['key_on_exit']={'short':'-X','long':'--key_on_exit', 'type':int, 'default':0, 'help':'Ask for an "Enter" key upon exit.'}
		params['core']['email_to']={'short':'-L','long':'--email_to', 'type':str, 'default':0, 'help':'Email job status.'}
		params['core']['log_dir']={'short':'-M','long':'--log_dir', 'type':str, 'default':0, 'help':'Log destination.'}
		params['core']['default_spool_dir']={'short':'-F','long':'--default_spool_dir', 'type':str, 'default':0, 'help':'Default data dump dir (default_spool_dir/job_name/timestamp).'}
		params['core']['job_name']={'short':'-B','long':'--job_name', 'type':str, 'default':0, 'help':'Job name (log_dir/job_name).'}
		params['core']['time_stamp']={'short':'-Y','long':'--time_stamp', 'type':str, 'default':0, 'help':'Timestamp (log_dir/job_name/timestamp).'}
		params['core']['column_buckets']={'short':'-0','long':'--column_buckets', 'type':int, 'default':0, 'help':'Wide row support.'}
		params['core']['job_pre_etl']={'short':'-1','long':'--job_pre_etl', 'type':str, 'default':'', 'help':'Path to job level pre-ETL Python script.'}
		params['core']['shard_pre_etl']={'short':'-2','long':'--shard_pre_etl', 'type':str, 'default':'', 'help':'Path to shard level pre-ETL Python script.'}
		params['core']['job_post_etl']={'short':'-3','long':'--job_post_etl', 'type':str, 'default':'', 'help':'Job''s post-etl script.'}
		params['core']['shard_post_etl']={'short':'-4','long':'--shard_post_etl', 'type':str, 'default':'', 'help':'Shard''s post-etl script.'}
		
		params['core']['loader_profile']={'short':'-C','long':'--loader_profile', 'type':str, 'default':'', 'help':'SQL*Loader profile (user defined).'}
		params['core']['host_map']={'short':'-5','long':'--host_map', 'type':str, 'default':'', 'help':'Host-to-shard map.'}
		params['core']['spool_type']={'short':'-6','long':'--spool_type', 'type':str, 'default':'csv', 'help':'Spool file type (CSV or JSON).'}
		params['core']['debug_level']={'short':'-7','long':'--debug_level', 'type':str, 'default':'', 'help':'QC Debug level.'}
		params['core']['status_pipe_id']={'short':'-spID','long':'--status_pipe_id', 'type':str, 'default':'0', 'help':'Status reporting pipe ID.'}
		#params['core']['arg_9']={'short':'-9','long':'--arg_9', 'type':str, 'default':'', 'help':'Generic string argument 9.'}
					
	params['FROM']={}
	pfrom=params['FROM']
	for dbkey in dbs.keys():
		if FROMDB in [None,dbkey]:		
			pfrom[dbkey]=OrderedDict()
			import __builtin__
			__builtin__.pfrom = pfrom
			__builtin__.dbkey = dbkey
			__builtin__.dbs = dbs
			imp_file = os.path.join(abspath,'config','include','args','%s_from.py' % dbkey)
			import_module(imp_file)	
	if 0:
		dbkey='SSEXP'				
		if FROMDB in [None,dbkey]:
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
			pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query sqls.'  % dbs[dbkey]}
			pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
			pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
			pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
			pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
	if 0:
		dbkey='SSENT'				
		if FROMDB in [None,dbkey]:
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
			pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query sqls.'  % dbs[dbkey]}
			pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
			pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
			pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
			pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
			pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
	if 0:
		for dbkey in ('ORA12C','ORA11G', 'ORAEXA','ORAXE'): 
			if FROMDB in [None,dbkey]:
				pfrom[dbkey]=OrderedDict()				
				pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
				pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
				if dbkey not in ['ORAXE']:
					pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
					pfrom[dbkey]['from_sub_partition']=  {'short':'-S','long':'--from_sub_partition', 	'type':str, 'default':None, 'help':'From sub-partition.'}
				pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
				pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
				
				#pfrom[dbkey]['from_db']={'short':'-f','long':'--from_db', 'type':str, 'default':None, 'help':'From database.'}
				pfrom[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'', 'help':'nls_date_format for source.'}
				pfrom[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'', 'help':'nls_timestamp_format for source.'}
				pfrom[dbkey]['nls_timestamp_tz_format']={'short':'-O','long':'--nls_timestamp_tz_format', 'type':str, 'default':'', 'help':'nls_timestamp_tz_format for source.'}
				#pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
				pfrom[dbkey]['header']={'short':'-A','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
				pfrom[dbkey]['keep_whitespace']={'short':'-W','long':'--keep_whitespace', 'type':int, 'default':0, 'help':'Keep whitespace from CHAR type in "%s" extract.' % dbs[dbkey]}
	if 0:
		dbkey='ORAXE'				
		pfrom[dbkey]=OrderedDict()				
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
		#pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
		#pfrom[dbkey]['from_sub_partition']=  {'short':'-S','long':'--from_sub_partition', 	'type':str, 'default':None, 'help':'From sub-partition.'}
		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		
		#pfrom[dbkey]['from_db']={'short':'-f','long':'--from_db', 'type':str, 'default':None, 'help':'From database.'}
		pfrom[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'', 'help':'nls_date_format for source.'}
		pfrom[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'', 'help':'nls_timestamp_format for source.'}
		pfrom[dbkey]['nls_timestamp_tz_format']={'short':'-O','long':'--nls_timestamp_tz_format', 'type':str, 'default':'', 'help':'nls_timestamp_tz_format for source.'}
		#pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		pfrom[dbkey]['header']={'short':'-A','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
		pfrom[dbkey]['keep_whitespace']={'short':'-W','long':'--keep_whitespace', 'type':int, 'default':0, 'help':'Keep whitespace from CHAR type in "%s" extract.' % dbs[dbkey]}

	if 0:
		for dbkey in ('MYSQL', 'INFOB','MARIA'):
			if FROMDB in [None,dbkey]:
				pfrom[dbkey]=OrderedDict()
				pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
				pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
				pfrom[dbkey]['from_sub_partition']=  {'short':'-S','long':'--from_sub_partition', 	'type':str, 'default':None, 'help':'From sub-partition.'}

				pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
				pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
				pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}				

	if 0:
		dbkey='MYSQL'				
		pfrom[dbkey]=OrderedDict()
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
	if 0:
		dbkey='MARIA'				
		pfrom[dbkey]=OrderedDict()
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
		pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
		pfrom[dbkey]['from_sub_partition']=  {'short':'-S','long':'--from_sub_partition', 	'type':str, 'default':None, 'help':'From sub-partition.'}

		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}				
	if 0:
		dbkey='PGRES'	
		if FROMDB in [None,dbkey]:	
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
			pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
			pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
			pfrom[dbkey]['from_any_partition']=  {'short':'-P','long':'--from_any_partition', 	'type':str, 'default':None, 'help':'From partition.'}
			pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
			pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
			pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
			pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
			pfrom[dbkey]['source_port']={'short':'-R','long':'--source_port', 'type':str, 'default':'5432', 'help':'Connection port for source %s.' % dbs[dbkey]}

	if 0:
		dbkey='SYANY'				
		pfrom[dbkey]=OrderedDict()
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}

		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}

	if 0:
		dbkey='SYIQ'
		pfrom[dbkey]=OrderedDict()
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}

		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
		
	if 0:
		
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}

	#dbkey='SYASE'
	if 0:	
		for dbkey in ['SYIQ','SYASE','SYANY']:
			if FROMDB in [None,dbkey]:
				pfrom[dbkey]=OrderedDict()
				pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
				pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}

				pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
				pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
				pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
				pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
	
	if 0:
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
	if 0:
		dbkey='TTEN'	
		if FROMDB in [None,dbkey]:	
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
			pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
			pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
			pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
			pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
			pfrom[dbkey]['from_DSN_name']={'short':'-b','long':'--from_DSN_name', 'type':str, 'default':None, 'help':'Source server DSN for %s.' % dbs[dbkey]}			
			pfrom[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'YYYY-MM-DD', 'help':'nls_date_format for source.'}
			pfrom[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'YYYY-MM-DD HH24.MI.SS.FF', 'help':'nls_timestamp_format for source.'}
			pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}

	#'DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'
		
	#dbkey='DBTUDB'		
	if 0:	
		for dbkey in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
			if FROMDB in [None,dbkey]:
				pfrom[dbkey]=OrderedDict()
				pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
				pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
				pfrom[dbkey]['from_partition']=  {'short':'-P','long':'--from_partition', 	'type':str, 'default':None, 'help':'From partition.'}
				pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
				pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
				pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
				#pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}

	if 0:
		for dbkey in ('INFOR', 'INFORC'):
			if FROMDB in [None,dbkey]:
				pfrom[dbkey]=OrderedDict()
				pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
				pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
				pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
				pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
				pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
				pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
				pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
				pfrom[dbkey]['osauth_for_source']={'short':'-J','long':'--osauth_for_source', 'type':int, 'default':0, 'help':'Path to %s client home.' % dbs[dbkey]}
				#pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}

	if 0:
		dbkey='INFORC'				
		pfrom[dbkey]=OrderedDict()
		pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
		pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
		pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
		pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
		pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
		#pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
	if 0:
		dbkey='JSON'
		if FROMDB in [None,dbkey]:	
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['input_files']={'short':'-i','long':'--input_files', 'type':str, 'default':None, 'help':'Input JSON file(s).'}
			pfrom[dbkey]['input_dirs']={'short':'-I','long':'--input_dirs', 'type':str, 'default':None, 'help':'Input JSON directory.'}
			pfrom[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
			pfrom[dbkey]['shard_size_kb']={'short':'-y','long':'--shard_size_kb', 'type':int, 'default':10, 'help':'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'}				
	if 0:
		dbkey='CSV'	
		if FROMDB in [None,dbkey]:
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['input_files']={'short':'-i','long':'--input_files', 'type':str, 'default':None, 'help':'Input CSV file(s).'}
			pfrom[dbkey]['input_dirs']={'short':'-I','long':'--input_dirs', 'type':str, 'default':None, 'help':'Input CSV directory.'}
			#pfrom[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
			pfrom[dbkey]['shard_size_kb']={'short':'-y','long':'--shard_size_kb', 'type':int, 'default':10, 'help':'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'}				
	if 0:
		dbkey='DDL'	
		if FROMDB in [None,dbkey]:
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['input_files']={'short':'-i','long':'--input_files', 'type':str, 'default':None, 'help':'Input CSV file(s).'}
			pfrom[dbkey]['input_dirs']={'short':'-I','long':'--input_dirs', 'type':str, 'default':None, 'help':'Input CSV directory.'}
			pfrom[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
			pfrom[dbkey]['shard_size_kb']={'short':'-y','long':'--shard_size_kb', 'type':int, 'default':10, 'help':'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'}				

	if 0:
		#pfrom[dbkey]['source_defaults_file']={'short':'-D','long':'--source_defaults_file', 'type':str, 'default':None, 'help':'Path to %s source defaults file.' % dbs[dbkey]}				
		dbkey='SLITE'
		if FROMDB in [None,dbkey]:
			pfrom[dbkey]=OrderedDict()
			pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
			pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
			pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
			pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
			pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
			pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}				

	#pfrom[dbkey]['source_defaults_file']={'short':'-D','long':'--source_defaults_file', 'type':str, 'default':None, 'help':'Path to %s source defaults file.' % dbs[dbkey]}				

					
	params['TO']={}
	pto=params['TO']
	
	for dbkey in dbs.keys():
		#dbkey='MONGO'	
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()
			#pfrom[dbkey]=OrderedDict()
			import __builtin__
			__builtin__.pto = pto
			__builtin__.dbkey = dbkey
			__builtin__.dbs = dbs
			imp_file = os.path.join(abspath,'config','include','args','%s_to.py' % dbkey)
			import_module(imp_file)
	
	#dbkey='ORA11G'
	if 0:
		for dbkey in ['ORAEXA', 'ORA11G','ORA12C','ORAXE']:
			if TODB in [None,dbkey]:
				pto[dbkey]=OrderedDict()
				#pto[dbkey]['to_db']={'short':'-g','long':'--to_db', 'type':str, 'default':None, 'help':'To %s database.' % dbs[dbkey]}
				pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
				pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
				pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
				
				pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 	'type':str, 'default':None, 'help':'To Oracle table.'}
				if dbkey not in ['ORAXE']:
					pto[dbkey]['to_partition']={'short':'-G','long':'--to_partition', 	'type':str, 'default':None, 'help':'To Oracle table.'}
					pto[dbkey]['to_sub_partition']={'short':'-N','long':'--to_sub_partition', 	'type':str, 'default':None, 'help':'To Oracle table.'}
				pto[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'', 'help':'nls_date_format for target.'}				
				pto[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'', 'help':'nls_timestamp_format for target.'}
				pto[dbkey]['nls_timestamp_tz_format']={'short':'-O','long':'--nls_timestamp_tz_format', 'type':str, 'default':'', 'help':'nls_timestamp_tz_format for target.'}
				#pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
				pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Number of rows to skip in input file.'}

	if 0:
		dbkey='ORAXE'
		pto[dbkey]=OrderedDict()
		pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
		pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
		pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
		
		pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 	'type':str, 'default':None, 'help':'To Oracle table.'}
		#pto[dbkey]['to_partition']={'short':'-G','long':'--to_partition', 	'type':str, 'default':None, 'help':'To Oracle table.'}
		#pto[dbkey]['to_sub_partition']={'short':'-N','long':'--to_sub_partition', 	'type':str, 'default':None, 'help':'To Oracle table.'}
		pto[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'', 'help':'nls_date_format for target.'}				
		pto[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'', 'help':'nls_timestamp_format for target.'}
		pto[dbkey]['nls_timestamp_tz_format']={'short':'-O','long':'--nls_timestamp_tz_format', 'type':str, 'default':'', 'help':'nls_timestamp_tz_format for target.'}

	if 0:
		dbkey='ORAEXA'
		pto[dbkey]=OrderedDict()
		pto[dbkey]['to_db']={'short':'-g','long':'--to_db', 'type':str, 'default':None, 'help':'To %s database.' % dbs[dbkey] }
		pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 	'type':str, 'default':None, 'help':'To %s table.' % dbs[dbkey]}
		pto[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'DD-Mon-YYYY HH:MI:SS AM', 'help':'nls_date_format for target.'}				
		pto[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'DD-Mon-RR HH.MI.SSXFF AM', 'help':'nls_time_format for target.'}
		pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
	if 0:
		dbkey='CSV'
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()
			pto[dbkey]['to_file']={'short':'-g','long':'--to_file', 'type':str, 'default':None, 'help':'To %s file.' % dbs[dbkey]  }
			pto[dbkey]['to_dir']={'short':'-D','long':'--to_dir', 'type':str, 'default':None, 'help':'To directory.'}
	if 0:
		dbkey='JSON'
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()
			pto[dbkey]['to_file']={'short':'-g','long':'--to_file', 'type':str, 'default':None, 'help':'To %s file.' % dbs[dbkey]  }
			pto[dbkey]['to_dir']={'short':'-D','long':'--to_dir', 'type':str, 'default':None, 'help':'To %s directory.' % dbs[dbkey]}

	if 0:
		dbkey='DDL'
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()
			pto[dbkey]['to_file']={'short':'-g','long':'--to_file', 'type':str, 'default':None, 'help':'To %s file.' % dbs[dbkey]  }
			pto[dbkey]['to_dir']={'short':'-D','long':'--to_dir', 'type':str, 'default':None, 'help':'To directory.'}

	if 0:
		dbkey='SSEXP'
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()				
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'%s instance name.' % dbs[dbkey]}
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'To table.'}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:
		dbkey='SSENT'	
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()				
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'%s instance name.' % dbs[dbkey]}
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'To table.'}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	
	if 0:
		dbkey='MARIA'
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target db user password.'}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target database.'}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target db instance name.'}
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target table.'}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to mysql client home.'}
			#pto[dbkey]['targets_defaults_file']={'short':'-D','long':'--targets_defaults_file', 'type':str, 'default':None, 'help':'Path to %s target defaults file.' % dbs[dbkey]}				

	if 0:				
		for dbkey in ('MYSQL', 'INFOB'):
			if TODB in [None,dbkey]:
				pto[dbkey]=OrderedDict()		
				pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
				pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target db user password.'}
				pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target database.'}
				pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target db instance name.'}
				pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target table.'}
				pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to mysql client home.'}
				#pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:
		dbkey='PGRES'	
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['target_port']={'short':'-T','long':'--target_port', 'type':str, 'default':'5432', 'help':'Connection port for target %s.' % dbs[dbkey]}
			pto[dbkey]['skip_header']= {'short':'-k','long':'--skip_header', 	'type':int, 'default':0, 'help':'Skip header line.'}
	if 0:
		dbkey='SYANY'				
		pto[dbkey]=OrderedDict()		
		pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
		pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
		pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
		pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
		pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
		pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
		pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}

		dbkey='SYIQ'				
		pto[dbkey]=OrderedDict()		
		pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
		pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
		pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
		pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
		pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
		pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
		pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}

	if 0:
		for dbkey in ['SYASE', 'SYIQ', 'SYANY']:
			if TODB in [None,dbkey]:
				pto[dbkey]=OrderedDict()		
				pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
				pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
				pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
				pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
				pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
				pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
				pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:
		dbkey='TTEN'
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
			pto[dbkey]['to_DSN_name']={'short':'-d','long':'--to_DSN_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
			pto[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'YYYY-MM-DD', 'help':'nls_date_format for target.'}				
			pto[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'YYYY-MM-DD HH24.MI.SS.FF', 'help':'nls_timestamp_format for target.'}
			pto[dbkey]['nls_timestamp_tz_format']={'short':'-O','long':'--nls_timestamp_tz_format', 'type':str, 'default':'', 'help':'nls_timestamp_tz_format for target.'}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	
	if 0:
		dbkey='DBTUDB'	
		for dbkey in ('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
			if TODB in [None,dbkey]:
				pto[dbkey]=OrderedDict()		
				pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
				pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
				pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
				pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
				pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
				pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
				pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:	
		dbkey='INFOR'		
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:		
		dbkey='INFORC'		
		if TODB in [None,dbkey]:	
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target %s table.' % dbs[dbkey]}
			pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
			pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'Target %s db user password.' % dbs[dbkey]}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target %s database.' % dbs[dbkey]}
			pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s db instance name.' % dbs[dbkey]}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
	if 0:		
		dbkey='SLITE'	
		if TODB in [None,dbkey]:
			pto[dbkey]=OrderedDict()		
			pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'Target table.'}
			pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'Target database.'}
			pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
			pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to mysql client home.'}

params={}
set_params(params)
#pprint (params)
def add_argument(vector,parser):
	# From CSV file
	#print vector
	(source,target) = vector.split(_to)
	#print vector
	#print (source,target)
	#sys.exit(0)
	from_shorts=[]
	if source.upper() in params['FROM'].keys():
		for key,val in params['FROM'][source.upper()].items():
			#print 'adding %s  %s\t for source' % (val['short'],key)
			from_shorts.append(val['short'])
			parser.add_argument(val['short'],val['long'], default=val['default'], type=val['type'],  help=val['help'])
	else:
		raise CopyVectorError(vector)
	#print ''
	#print target.upper()
	#print params['TO'].keys()
	if target.upper() in params['TO'].keys():
		for key,val in params['TO'][target.upper()].items():
			if not val['short'] in from_shorts:
				#print 'adding %s  %s\t for target' % (val['short'],key)
				parser.add_argument(val['short'],val['long'], default=val['default'], type=val['type'],  help=val['help'])
			else:
				pass
				#print '%s already added in target' % val['short']
	else:
		raise CopyVectorError(vector)
def config_log(app):
	
	if 1:
		logdir='logs'
		ldir = '%s\\%s' % (abspath,logdir)
		if not os.path.isdir(ldir):
			os.makedirs(ldir)
	

	#dumpdir = '%s\\spool' % datadir
	dumpdir =  datadir
	if not os.path.isdir(datadir):
		os.makedirs(datadir) 
	if 1:	
		sqlgdir ='%s\\sql' % (datadir)
		if not os.path.isdir(sqlgdir):
			os.makedirs(sqlgdir) 
		if not os.path.isdir(dumpdir):
			os.makedirs(dumpdir) 

	logfn='%s\\%s%s.log' % (datadir,app,ts)
	#print logfn
	#e(0)
	logging.basicConfig(filename=logfn, filemode='w', level=logging.DEBUG,format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	log = logging.getLogger(app)
	log.setLevel(logging.DEBUG)
	if not if_hg:
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		# create formatter
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		ch.setFormatter(formatter)
		log.addHandler(ch)
		#log.info('Extracting to: \n"%s"', dumpdir)	
	return (log,datadir)
supported= True #rel.supported
#print copy_vector
#e(0)
#rel.free=True
def copyright():
	if rel.release and rel.free:
		print '-'*70
		print rel.free
	print '-'*70
	
	print '%s (v%s, beta, %s) [%sbit]' % (rel.getAppTitle(),rel.version,rel_date,getRegSize())
	print 'Copyright (c): 2014 %s, All rights reserved.' % rel.app_author
	print 'Agreement: Use this tool at your own risk. Author is not liable for any damages or losses related to the use of this software.'
	print '-'*70	
		

if 1: #copy_vector and '2' in copy_vector and supported(copy_vector.upper().split('2')):
	#print copy_vector
	#global  ts, args, log,datadir
	copyright()
	a,b=None, None
	if copy_vector:
		#print copy_vector
		a,b=copy_vector.upper().split(_to)
	#print rel.from_to_dbs
	if not copy_vector:
		#print 11
		rel.show_default_help()
		#e(1)

	elif not  _to in copy_vector:
		rel.show_help(cvarg,copy_vector,params)
		e(0)
	#elif not supported(copy_vector.upper().split('2')):
	
	elif (a not in rel.from_to_dbs or b not in rel.from_to_dbs):
		
		print '#'*40
		print '#'*40
		print ''
		print 'Copy vector "%s" is not supported.' % copy_vector
		print ''
		print '#'*40
		print '#'*40
		rel.show_default_help()
		e(1)
	#else:		
	#	show_default_help(cvarg)
	#	e(1)
if copy_vector:		
	parser = argparse.ArgumentParser(description=rel.apptitle)
	parser.add_argument("cmd", help=argparse.SUPPRESS, nargs="*")
	core=params['core']
	for key,val in core.items():
		#print 'adding %s  %s\t for core' % (val['short'],key)	
		parser.add_argument(val['short'],val['long'], default=val['default'], type=val['type'],  help=val['help'])
		
	add_argument(copy_vector,parser)
	args = parser.parse_args()		
	import __builtin__
	__builtin__.args = args
	__builtin__._to = _to
	#import a

	uargs = import_module(os.path.join(abspath,'config','user_conf.py'))
	
	#import .config.common as uconf 
	ts= uargs.ts
	#abspath= uargs.abspath 
	spooldir=uargs.spooldir 
	datadir= uargs.datadir 
	lname=copy_vector
	if rel.free:
		fr =rel.free.strip().split(' ')
		
		#random.seed(5)
		rnd =random.randrange(0,5)
		lname=fr[rnd]
	#print datadir, os.path.isdir(datadir)
	if os.path.isdir(datadir):
		print 'WARNING: log dir already exists.'
		print 'Deleting existing log...'
		shutil.rmtree(datadir)
	#e(0)		
	(log,datadir)=config_log(lname)

	#from include.v101.host_map import host_map as hmap	
	#host_map_loc= args.host_map
	#hm = hmap(args.copy_vector,host_map_loc)
	
#else:
#	print 'Not supported'
#	e(1)

#def not_supported	


#'SSEXP':'SQL Server','SS2012':'SQL Server','SS2014':'SQL Server','SS2016':'SQL Server',
#'SS70':'SQL Server', 'SS2000':'SQL Server', 'SS2005':'SQL Server', 'SS2008':'SQL Server',

dbclients=cconf.dbclients

for db in('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	dbclients[db]=r'C:\Program Files (x86)\IBM\SQLLIB_01\BIN'
#C:\Program Files\MySQL\MySQL Server 5.6\bin
if citi:
	dbclients['ORA11G']=r'C:\ORACLE\product\11.1.0\client_1\BIN'			
dbtools={}
dbtools['SPOOLER']={'PGRES':'psql.exe',
			'ORA12C':	'sqlplus.exe','ORA11G':	'sqlplus.exe', 'ORAXE':	'sqlplus.exe', 'ORAEXA':	'sqlplus.exe',
			'ORA10G':	'sqlplus.exe','ORA9I':	'sqlplus.exe','ORA8I':	'sqlplus.exe','ORA733':	'sqlplus.exe',
			#'SSENT':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe',
			'SS70':	'sqlcmd.exe','SS2000':	'sqlcmd.exe', 'SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',			
			#'SSEXP':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttBulkCp.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',
			'SLITE':'sqlite3.exe',
			'MONGO':'mongoexport.exe',
			'CURL':'curl.exe'}
for db in('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	dbtools['SPOOLER'][db]='db2.exe'
	
dbtools['LOADER']={ 
			'PGRES':'psql.exe',
			'ORA12C':	'sqlldr.exe','ORA11G':	'sqlldr.exe', 'ORAXE':	'sqlldr.exe',
			'ORA10G':	'sqlldr.exe','ORA9I':	'sqlldr.exe','ORA8I':	'sqlldr.exe','ORA733':	'sqlldr.exe',
			'ORAEXA':	'sqlldr.exe',
			#'SSENT':	'sqlcmd.exe','SSEXP':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe',
			'SS70':	'sqlcmd.exe','SS2000':	'sqlcmd.exe', 'SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttBulkCp.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',			
			'SLITE':'sqlite3.exe',
			'MONGO':'mongoimport.exe'}
for db in('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	dbtools['LOADER'][db]='db2.exe'
		
dbtools['DBSHELL']={ 
			'PGRES':'psql.exe',
			'ORA12C':	'sqlplus.exe','ORA11G':	'sqlplus.exe','ORAXE':	'sqlplus.exe',
			'ORAEXA':	'sqlplus.exe',
			'ORA10G':	'sqlplus.exe','ORA9I':	'sqlplus.exe','ORA8I':	'sqlplus.exe','ORA733':	'sqlplus.exe',
			#'SSENT':	'sqlcmd.exe','SSEXP':	'sqlcmd.exe',
			'SSEXP':	'sqlcmd.exe','SS2012':	'sqlcmd.exe','SS2014':	'sqlcmd.exe','SS2016':	'sqlcmd.exe','SS70':	'sqlcmd.exe',
			'SS2000':	'sqlcmd.exe','SS2005':	'sqlcmd.exe','SS2008':	'sqlcmd.exe',
			'MYSQL':'mysql.exe', 'MARIA':'mysql.exe', 'INFOB':'mysql.exe',
			'SYANY':'dbisql.com',
			'SYASE':'dbisql.com',
			'SYIQ': 'dbisql.com',
			'TTEN': 'ttIsql.exe',
			#'DBTUDB': 'db2.exe',
			'INFOR': 'dbaccess.exe',
			'INFORC': 'dbaccess.exe',			
			'SLITE':'sqlite3.exe',
			'MONGO':'mongo.exe','CURL':'curl.exe'}
for db in('DBTAES', 'DBTES', 'DBTAWS', 'DBTWS', 'DBTE', 'DBTEC', 'DBTDE'):
	dbtools['DBSHELL'][db]='db2.exe'			
			



		



