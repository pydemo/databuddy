# release setup
free=None #'#FreeUkraine #SaveUkraine #StopRussia #PutinKhuilo #CrimeaIsUkraine'
bin='32'
version='0.3.5'
ts='2016/05/28 00:02:07'
for_db=['PGRES']
from_to_dbs=['PGRES', 'CSV']
ff=['CSV']
release=True
app_author='Alex Buzunov'
apptitle='QueryCopy'
appn='qc'
appex='exe'
appname='qc32.exe'
tests=[[['PGRES_DateTable', 'PGRES_Table_KeepSpoolFile', 'PGRES_Table', 'PGRES_QueryFile', 'PGRES_Table_Limit15', 'PGRES_QueryDir', 'PGRES_QueryDir_Limit12', 'PGRES_ShardedPartition', 'PGRES_TimestampTable', 'PGRES_QueryFile_Limit11', 'PGRES_ShardedQueryFile', 'PGRES_ParallelQueryDir', 'PGRES_Partition_Limit33', 'PGRES_TimezoneTable', 'PGRES_ShardedTable', 'PGRES_Partition'], ['PGRES_Table_SkipHeader', 'PGRES_Table']], [['PGRES_DateTable', 'PGRES_Table_KeepSpoolFile', 'PGRES_Table', 'PGRES_QueryFile', 'PGRES_Table_Limit15', 'PGRES_QueryDir', 'PGRES_QueryDir_Limit12', 'PGRES_ShardedPartition', 'PGRES_TimestampTable', 'PGRES_QueryFile_Limit11', 'PGRES_ShardedQueryFile', 'PGRES_ParallelQueryDir', 'PGRES_Partition_Limit33', 'PGRES_TimezoneTable', 'PGRES_ShardedTable', 'PGRES_Partition'], ['CSV_Dir', 'CSV_Default', 'CSV_File']], [['CSV_Dirs', 'CSV_ShardedFile', 'CSV_Dirs_Limit10', 'CSV_File_TableNamedFile', 'CSV_File_Limit10', 'CSV_ShardedFileSkip1', 'CSV_DateFile', 'CSV_TimestampFile', 'CSV_TimezoneFile', 'CSV_Files_TableNamedFile', 'CSV_Dir', 'CSV_ShardedDir_Limit10', 'CSV_FileSkip1', 'CSV_ShardedDirSkip1', 'CSV_File', 'CSV_DateFiles', 'CSV_MongoFile', 'CSV_ShardedFile_Limit10', 'CSV_ShardedDir', 'CSV_DirsSkip1'], ['PGRES_Table_SkipHeader', 'PGRES_Table']]]
_to='-'
ucases=None
import __builtin__
__builtin__.for_db = for_db
__builtin__.from_to_dbs=from_to_dbs
__builtin__.free=free
__builtin__.apptitle=apptitle
__builtin__.version=version
__builtin__.bin=bin
__builtin__.appname=appname
__builtin__.release=release
__builtin__._to=_to
import test.v101.build_include.include_dm_for_db as inc
def get_ucases():
	return ucases
def show_default_help():
	inc.show_default_help(for_db, from_to_dbs,appname,dbs,ff)
def supported(x):
	return inc.supported(x, for_db, from_to_dbs)
def getAppTitle():
	return inc.getAppTitle(for_db, apptitle,dbs)
def getExeTitle():
	return inc.getExeTitle(apptitle, for_db, bin, dbs)	
def show_help(cvarg,copy_vector,params):
	inc.show_help(for_db,from_to_dbs,dbs,cvarg,copy_vector,params,ucases)

