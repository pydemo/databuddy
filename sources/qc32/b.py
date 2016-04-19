import sys, os
import shlex
from pprint import pprint
from subprocess import Popen, PIPE
import datetime
import __builtin__
__builtin__.copy_vector = None
__builtin__.cvarg = None
#import common.v101.config as conf 
import config.config as conf
import zipfile
from test.v101.test import run_test,  home, citi
import itertools
import shutil
import imp	
import release as rel 	
e=sys.exit

dmhome=os.path.dirname(os.path.realpath(__file__))
default_vector=None #'pgres2pgres'
prog=None
def get_dir_from_ts(ts):
	return ts.replace('/','').replace(' ','_').replace(':','')		
	
if __name__=='__main__':
	"""['CSV', 'DBTAES', 'DBTAWS', 'DBTDE', 'DBTE', 'DBTEC', 'DBTES', 'DBTWS', 
'ORAEXA','INFOB', 'INFOR', 'INFORC', 'MARIA', 'MYSQL', 'ORAORA11G', 'ORAXE', 'PGRES', 'SLITE',
'SSENT', 'SSEXP', 'SYANY', 'SYASE', 'SYIQ', 'TTEN']"""

	b=None
	
	if 1:
		app = ('Alex Buzunov', "QueryCopy", 'qc')
		regs=['64','32']
		regs=['32']
		#regs=['64']
		from test.v101.build_dm_for_db import build		
		ft_dbs_all=[ 'DBTAES', 'DBTAWS', 'DBTDE', 'DBTE', 'DBTEC', 'DBTES', 'DBTWS', 
'ORAEXA','INFOB', 'INFOR', 'INFORC', 'MARIA', 'MYSQL', 'ORA11G', 'ORAXE', 'PGRES', 'SLITE',
'SSENT', 'SSEXP', 'SYANY', 'SYASE', 'SYIQ', 'TTEN']
		#ft_dbs=['ORA11G', 'ORAXE', 'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['MYSQL','ORA11G', 'ORAXE', 'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['SYIQ','SYASE','SYANY','PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['SYANY','SLITE','SYIQ','SYASE','PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=[ 'DBTWS',  'DBTES', 'DBTEC', 'DBTE','DBTDE','DBTAWS', 'DBTAES',  'SYANY','SLITE','SYIQ','SYASE','PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['MARIA',  'INFORC', 'INFOR', 'DBTWS',  'DBTES', 'DBTEC', 'DBTE','DBTDE','DBTAWS', 'DBTAES',  'SYANY','SLITE','SYIQ','SYASE','PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		ft_dbs=['ORA12C', 'MARIA',  'INFORC', 'INFOR', 'DBTWS',  'DBTES', 'DBTEC', 'DBTE','DBTDE','DBTAWS', 'DBTAES',  'SYANY','SLITE','SYIQ','SYASE','PGRES', 'TTEN','INFOB', 'ORAXE', 'MYSQL','ORA11G',  'ORAEXA','SSENT', 'SSEXP']
		#ft_ss=[ 'SSENT', 'SSEXP']
		ft_ss=['SSEXP', 'SS2012','SS2014','SS2016','SS70','SS2000','SS2005','SS2008']
		ft_db2=['DBTWS',  'DBTES', 'DBTEC', 'DBTE','DBTDE','DBTAWS', 'DBTAES']
		ft_ora=['ORA12C', 'ORAXE','ORAEXA','ORA10G','ORA9I','ORA8I','ORA733','ORA11G']
		ft_dt=['CURL']
		ft_dbs=ft_ss+ft_db2+ft_dt+ft_ora+[ 'MONGO', 'MARIA',  'INFORC', 'INFOR',  'SYANY','SLITE','SYIQ','SYASE','PGRES', 'TTEN','INFOB',  'MYSQL']
		#'SSEXP':'SQL Server','SS2012':'SQL Server','SS2014':'SQL Server','SS2016':'SQL Server',
		#'SS70':'SQL Server', 'SS2000':'SQL Server', 'SS2005':'SQL Server', 'SS2008':'SQL Server',	
		#ft_dbs=['ORA8I','MONGO']
		#ft_dbs=conf.dbs.keys()
		#print ft_dbs[::-1]
		#for db in ft_dbs[::-1]
		#ft_dbs=['ORA11G']; 
		
		#gen_args_api=False; ft_dbs=['ORA11G']; ff=['CSV']
		#gen_args_api=False; ft_dbs=['SS2012']; ff=['CSV']
		#gen_args_api=False; ft_dbs=['SSEXP']; ff=['CSV'] #curl
		#gen_args_api=True; ff=['CSV','DDL','JSON']
		#gen_args_api=False; ff=['CSV','DDL','JSON']
		ff=['CSV']
		gen_args_api=True
		for ftd in (ft_dbs):			
			#dbs=['ORA12C', 'ORAXE','ORAEXA','ORA10G','ORA9I','ORA8I','ORA733','ORA11G']
			#for db in 
			#print dbs
			#del dbs[dbs.index(ftd)]
			#print ftd
			#print dbs + [ftd]
			#new = dbs #+[ftd]
			#e(0)			
			#b=build(dmhome,for_db=[ftd],from_to_dbs=ft_dbs+['ORAXE','ORAEXA'],ff=['CSV','DDL'],app=app, regs=regs,v=('0.3.3'),
			b=build(dmhome,for_db=[ftd],from_to_dbs=ft_dbs,ff=ff,app=app, regs=regs,v=('0.3.5'),
				#b=build(dmhome,for_db=[ftd],from_to_dbs=ft_dbs+['CSV'],app=app, regs=regs,v=('0.2.9'),
				#b=build(dmhome,for_db=[ftd],from_to_dbs=ft_dbs_all+['CSV'],app=app, regs=regs,v=('0.2.9'),
			is_release=True,nor_t=(None,None),run=not gen_args_api)
			#is_release=False,nor_t=(['CURL_UrlList'],['CSV_Dir']),run=True)
			#is_release=False,nor_t=(['%s_Url_To_File' % ftd],['CSV_File']),run=True)			
			#is_release=False,nor_t=(['%s_Url' % ftd],['CSV_File']),run=True)			
			#is_release=False,nor_t=(['%s_UrlList' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['%s_UrlFile' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['%s_Url' % ftd],['CSV_Default']),run=True)			
			#is_release=False,nor_t=(['%s_UrlFiles' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['%s_UrlDir' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['%s_UrlDirs' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['ORA11G_Parallel_SubpartitionList'],['ORA11G_Subpartition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['ORA12C_ShardedTable'],['ORA12C_Table_GetTabnameFromQuery']),run=True)
			#is_release=False,nor_t=(['ORA12C_QueryFile_TableNamedFile'],['ORA12C_Table_GetTabnameFromQuery']),run=True)
			#is_release=False,nor_t=(['ORA12C_Parallel_PartitionList'],['ORA12C_Table_GetTabnameFromQuery']),run=True)			
			#is_release=False,nor_t=(['CSV_File_TableNamedFile'],['ORA12C_Partition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['ORA12C_ShardedQueryDir_withHeader'],['ORA12C_Table_GetTabnameFromQuery']),run=True)
			#is_release=False,nor_t=(['ORA12C_Parallel_ShardedTable'],['ORA12C_Table']),run=True)
			#is_release=False,nor_t=(['ORA12C_ShardedQueryDir_withHeader'],['ORA12C_Subpartition']),run=True)
			#is_release=False,nor_t=(['CSV_ShardedFile'],['ORA12C_Partition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['ORA12C_Subpartition'],['ORA12C_Table_TruncateTarget_NoClient']),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['ORA12C_Table_GetTabnameFromQuery']),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['ORA12C_Partition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['CSV_File_NoTable'],['ORA12C_Partition_TruncateTarget']),run=True)			
			#is_release=False,nor_t=(['%s_ShardedPartition' % ftd],['CSV_Dir']),run=True)			
			#is_release=False,nor_t=(['%s_Table' % ftd],['%s_Table' % ftd]),run=True)			
			#is_release=False,nor_t=(['%s_Table_withHeader' % ftd],['CSV_File']),run=True)
			#is_release=False,nor_t=(['%s_Parallel_TableList' % ftd],['%s_Table' % ftd]),run=True)					 
			#is_release=False,nor_t=(['ORAXE_DateTable'],['ORA12C_Partition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['%s_Table' % ftd],['%s_Table_NoTableName' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_TableList' % ftd],['%s_Table_NoTableName' % ftd]),run=True)
			#is_release=False,nor_t=(['ORA8I_Partition_TruncateTarget_AskToTruncate'],['ORA8I_Partition']),run=True)
			#is_release=False,nor_t=(['ORA12C_ShardedSubpartition'],['CSV_Dir']),run=True)
			#is_release=False,nor_t=(['ORA12C_Partition_TruncateTarget_AskToTruncate'],['CSV_File']),run=True)	
			#is_release=False,nor_t=(['ORA8I_Partition_Validate'],['ORA11G_NoTable_TruncateTarget']),run=True)	
			#is_release=False,nor_t=(['CSV_Dirs'],['ORA8I_Table_GetTabnameFromQuery_DeleteTargetRecs']),run=True)	
			#is_release=False,nor_t=(['ORA8I_Partition_Validate'],['ORA11G_Subpartition_TruncateTarget']),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['%s_Table_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['%s_Table' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_LargeFile'],['%s_Table' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_LargeFile'],['%s_NoTable_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_File_NoTable'],['%s_NoTable_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_Files_NoTable'],['%s_NoTable_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['%s_NoTable_TruncateTarget' % ftd]),run=True)	
			#ORA8I_Parallel_PartitionList ORA11G_Table_TruncateTarget			
			#is_release=False,nor_t=(['%s_Parallel_PartitionList' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_SubpartitionList' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_TableList' % ftd],['%s_Table' % ftd]),run=True)			
			#is_release=False,nor_t=(['%s_TableList' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)			
			#is_release=False,nor_t=(['%s_Table' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)			
			#is_release=False,nor_t=(['%s_TableList' % ftd],['%s_NoTable_TruncateTarget' % ftd]),run=True)			
			#is_release=False,nor_t=(['%s_Subpartition' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_Subpartition' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)	
			#is_release=False,nor_t=(['%s_PartitionList' % ftd],['%s_Table_TruncateTarget' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_Partition_Validate' % ftd],['%s_Table' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_Collection' % ftd],['%s_Collection' % ftd]),run=True)
			#is_release=False,nor_t=(['%s_Table' % ftd],['%s_Table' % ftd]),run=True)
			#print ftd
			#is_release=False,nor_t=(['ORA11G_Subpartition_WithWideRows'],['CSV_File']),run=True)	
			#is_release=False,nor_t=(['INFORC_QueryDir'],['ORA11G_Partition_TruncateTarget']),run=True)	
			#is_release=False,nor_t=(['ORA11G_QueryFile'],['ORA11G_Table']),run=True)	
			#is_release=False,nor_t=(['CSV_DateFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['CSV_TimestampFile'],['ORA8I_Table']),run=True)
			#is_release=False,nor_t=(['CSV_Dirs'],['ORA11G_Table']),run=True)
			
			#is_release=False,nor_t=(['CSV_ShardedFile'],['ORA11G_Table']),run=True)						
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['CSV_Dir']),run=True)
			#is_release=False,nor_t=(['ORA11G_Parallel_ShardedTable'],['CSV_Dir']),run=True)
			#is_release=False,nor_t=(['ORA11G_Table'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_TableList'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_SubpartitionList'],['ORA11G_Table']),run=True)			
			#is_release=False,nor_t=(['ORA11G_Parallel_SubpartitionList'],['ORA11G_Table']),run=True)			
			#is_release=False,nor_t=(['ORA11G_PartitionList'],['ORA11G_Table']),run=False)			
			#is_release=False,nor_t=(['ORA11G_Parallel_PartitionList'],['ORA11G_Table']),run=False)	
			#is_release=False,nor_t=(['ORA11G_Table'],['ORA11G_Partition']),run=True)			
			#is_release=False,nor_t=(['ORA11G_Partition'],['ORA11G_Table']),run=False)			
			#is_release=False,nor_t=(['MONGO_Query'],['JSON_File']),run=True)
			#is_release=False,nor_t=(['MONGO_Collection'],['PGRES_Table_SkipHeader']),run=True)
			#is_release=False,nor_t=(['MONGO_Collection'],['CSV_File']),run=True)
			#is_release=False,nor_t=(['MONGO_Collection'],['JSON_File']),run=True)
			#is_release=False,nor_t=(['JSON_Files_noIDs'],['MONGO_Collection']),run=True)
			#is_release=False,nor_t=(['JSON_Files_noIDs'],['MONGO_Collection_3_insertionWorkers']),run=True)			
			#is_release=False,nor_t=(['MONGO_Collection_Skip10'],['JSON_File']),run=True)
			#is_release=False,nor_t=(['JSON_File'],['MONGO_Collection']),run=True)
			#is_release=False,nor_t=(['JSON_File'],['MONGO_Collection_Upsert']),run=True)
			#is_release=False,nor_t=(['JSON_Dirs'],['MONGO_Collection_Upsert']),run=True)
			#is_release=False,nor_t=(['JSON_ShardedDirs'],['MONGO_Collection_Upsert']),run=True)
			#is_release=False,nor_t=(['MONGO_Collection_withHeader'],['CSV_File']),run=True)
			#is_release=False,nor_t=(['MARIA_Table'],['CSV_File']),run=True)
			#is_release=False,nor_t=(['MONGO_Table'],['MONGO_Table']),run=True)
			#is_release=False,nor_t=(['CSV_ComaFile'],['MONGO_Table']),run=True)
			#is_release=False,nor_t=(['ORA12C_TimestampTable_withComaHeader'],['MONGO_Table']),run=True)
			#is_release=False,nor_t=(['ORA12C_ShardedQueryDir_withComaHeader'],['MONGO_Table']),run=True)
			#is_release=False,nor_t=(['MONGO_Table'],['ORA12C_Table']),run=True)
			#is_release=False,nor_t=(['MONGO_Table_withComaHeader'],['ORA12C_Table_SkipHeader']),run=True)
			#is_release=False,nor_t=(['MONGO_Table_withComaHeader'],['MONGO_Table']),run=True)
			#is_release=False,nor_t=(['MONGO_Table_withComaHeader'],['CSV_File']),run=True)
			#is_release=False,nor_t=(['CSV_TimestampFile'],['MARIA_Table']),run=True)
			#is_release=False,nor_t=(['CSV_TimestampFile'],['ORA12C_Table']),run=True)
			#is_release=False,nor_t=(['ORA12C_Table'],['CSV_File']),run=True)			
			#is_release=False,nor_t=(['DBTAES_Table'],['DBTAES_Table']),run=True)			
			#is_release=False,nor_t=(['ORA11G_Table'],['SYANY_Table']),run=True)			
			#is_release=False,nor_t=(['SYANY_Table'],['ORA11G_Table']),run=True)			
			#is_release=False,nor_t=([''],['SYANY_Table']),run=True)			
			#is_release=False,nor_t=(['SYANY_Table'],['DDL_File']),run=True)
			#is_release=False,nor_t=(['SYANY_Table'],['SYANY_Table']),run=True)
			#is_release=False,nor_t=(['PGRES_Table'],['PGRES_Table']),run=True)
			#is_release=False,nor_t=(['TTEN_Table'],['TTEN_Table']),run=True)		
			#is_release=False,nor_t=(['TTEN_Table'],['DDL_Dir']),run=True)		

			#MySQL
			#is_release=False,nor_t=(['MYSQL_Table'],['MYSQL_Table']),run=True)	
			#Infob				 			
			#is_release=False,nor_t=(['INFOB_QueryFile'],['ORAXE_Table']),run=True)	
			#is_release=False,nor_t=(['INFOB_QueryFile_Limit100'],['CSV_Default']),run=True)	
			#is_release=False,nor_t=(['INFOB_Table'],['INFOB_Table']),run=True)	
			#SSE
			#_ShardedQueryFile	 			
			#is_release=False,nor_t=(['CSV_DateFile'],['SSEXP_Table']),run=True)
			#is_release=False,nor_t=(['SSEXP_QueryDir_Limit25'],['CSV_Dir']),run=True)
			#is_release=False,nor_t=(['SSEXP_ShardedQueryFile'],['DDL_Dir']),run=True)
			#is_release=False,nor_t=(['SSENT_Table'],['SSENT_Table']),run=True)
			#is_release=False,nor_t=(['SSEXP_Table'],['SSEXP_Table']),run=True)
			#is_release=False,nor_t=(['CSV_DateFile'],['SSEXP_Table']),run=True)
			#is_release=False,nor_t=(['SSEXP_Table'],['CSV_File']),run=True)			
			#DB2
			#is_release=False,nor_t=(['CSV_DateFile'],['DBTAES_Table']),run=True)
			#is_release=False,nor_t=(['DBTAES_Table'],['CSV_File']),run=True)
			#ORA		
			#ORA11G_QueryFile_TableNamedFile ORA11G_Table_DeleteTargetRecs	
			#is_release=False,nor_t=(['ORA11G_QueryFile_TableNamedFile'],['ORA11G_Table_DeleteTargetRecs']),run=True)				
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['ORA11G_Subpartition_TruncateTarget']),run=True)			
			#is_release=False,nor_t=(['ORA11G_ShardedTimestampTable_keepWhitespace_Validate'],['ORA11G_Subpartition_TruncateTarget']),run=True)			
			#is_release=False,nor_t=(['ORA11G_TimezoneTable_KeepSpoolFile'],['ORA11G_Subpartition']),run=True)			
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['ORA11G_Table_TruncateTarget_NoClient']),run=True)			
			#is_release=False,nor_t=(['ORA11G_QueryFile_TableNamedFile'],['ORA11G_Table_GetTabnameFromQuery']),run=True)			
			#ORA11G_QueryFile_TableNamedFile ORA11G_Table_GetTabnameFromQuery
			#Copy_Oracle11G_ShardedTable_into_Oracle11GSubpartition_TruncateTarget.bat'	 			
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_TimezoneQueryFile'],['ORA11G_Table_TruncateTarget']),run=True)			
			#is_release=False,nor_t=(['ORAXE_Table'],['ORAXE_Table']),run=True)				
			#is_release=False,nor_t=(['ORA11G_Table'],['ORA11G_Table_NoClient']),run=True)			
			#is_release=False,nor_t=(['CSV_DateFile'],['ORA11G_Table']),run=True)			
			#is_release=False,nor_t=(['ORA11G_Table'],['CSV_File']),run=True)			
						
			#is_release=False,nor_t=(['ORA11G_Table'],['DDL_File']),run=True)
			#is_release=False,nor_t=(['ORA11G_Table'],['ORA11G_Table_WithLoaderProfile']),run=True)
			#is_release=False,nor_t=(['ORA11G_Table'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_QueryFile_WithWideRows'],['ORA11G_Table']),run=False)
			#is_release=False,nor_t=(['ORA11G_QueryFile_WithWideRows'],['CSV_Dir']),run=False)
			#is_release=False,nor_t=(['ORA11G_Table_WithWideRows'],['ORA11G_Table_WithWideRows']),run=True)
			#is_release=False,nor_t=(['ORA11G_QueryDir'],['ORA11G_Table_DeleteTargetRecs']),run=True)
			#is_release=False,nor_t=(['ORA11G_Partition_TruncateTarget_AskToTruncate'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['CSV_DateFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_QueryFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_QueryDir'],['ORA11G_Table']),run=True)
			#fail is_release=False,nor_t=(['ORA11G_QueryDir'],['ORA11G_Table_GetTabnameFromQuery']),run=True)
			#is_release=False,nor_t=(['ORA11G_QueryDir'],['ORA11G_Table']),run=True)
			#Oracle11G_QueryFile_TableNamedFile_into_Oracle11GTable_GetTabnameFromQuery
			#is_release=False,nor_t=(['ORA11G_QueryFile_TableNamedFile'],['ORA11G_Table_GetTabnameFromQuery']),run=True)
			#QueryFile_TableNamedFile_into_Oracle11GTable_TruncateTarget
			#is_release=False,nor_t=(['ORA11G_QueryFile_TableNamedFile'],['ORA11G_Table_TruncateTarget']),run=True)
			#GetTabnameFromQuery_DeleteTargetRecs
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['ORA11G_Table_GetTabnameFromQuery_DeleteTargetRecs']),run=True)	
			#is_release=False,nor_t=(['ORA11G_QueryDir_TableNamedFiles'],['ORA11G_Table_GetTableNameFromQueryFileName']),run=True)
			
			#is_release=False,nor_t=(['ORA11G_QueryFile_TableNamedFile'],['ORA11G_Table_GetTableNameFromQueryFileName']),run=True)
			 
			#is_release=False,nor_t=(['ORA11G_ShardedTable'],['ORA11G_Subpartition']),run=True)
			#is_release=False,nor_t=(['ORA11G_Partition_NoClient'],['CSV_File']),run=True)
			#is_release=False,nor_t=(['CSV_DateFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_DateTable_Email'],['ORA11G_Table']),run=True)
			#s_DateTable_Email
			#_TimezoneTable_KeepSpoolFile
			#is_release=False,nor_t=(['ORA11G_TimezoneTable_KeepSpoolFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_DateTable_JobName'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['CSV_TimestampFile'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_Partition'],['CSV_Default']),run=False)
			#is_release=False,nor_t=(['CSV_Dirs'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['CSV_DateFiles'],['ORA11G_Table']),run=True)
			#is_release=False,nor_t=(['ORA11G_ShardedTimestampTable_keepWhitespace_Validate'],['ORA11G_Table_TruncateTarget']),run=False)
			
			
			
			#print ftd
			#e(0)
			b.build_and_release()
	if 0:
		app = ('Alex Buzunov', "QueryCopy", 'qc')
		regs=['64','32']
		regs=['32']
		from test.v101.build_db2db import build
		
		b=build(dmhome,from_dbs=['TTEN'],to_dbs=['ORA'],app=app, regs=regs,v=('0.23.9'),
		#is_release=True,nor_t=(None,None))		
		is_release=False,nor_t=(['TTEN_QueryFile'],['CSV_File']))
		#b.build_and_release()
	if 0:
		app = ('Alex Buzunov', "CSV*Extractor", 'csvextractor')
		regs=['64','32']
		#regs=['32']
		from test.v101.build_csv_extractor import build

		b=build(dmhome,for_dbs=['ORA11G'],from_dbs=['ORA11G'],to_dbs=['CSV'],app=app, regs=regs,v=('1.23.9'),
		#is_release=True,nor_t=None)
		is_release=False,nor_t=(['ORA11G_TimezoneQueryFile'],['CSV_File']))
	

		
	

	
