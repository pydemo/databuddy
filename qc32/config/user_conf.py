#__builtin__ args

import datetime
import os, sys
from common.v101.loaders import import_module
e=sys.exit
inc={}
inc['DBTAES']=inc['DBTES']=inc['DBTAWS']=inc['DBTWS']=inc[ 'DBTE']=inc['DBTEC']=inc['DBTDE']='db2.py'
inc['SSENT']=inc['SSEXP']='ss.py'
inc['TTEN']='tten.py'
inc['SLITE']='slite.py'
inc['INFOR']=inc['INFORC']='infor.py'
inc['SYASE']=inc['SYANY']=inc['SYIQ']='sybase.py'
inc['ORA11G']=inc['ORAEXA']='oracle.py'
inc['ORAXE']='oraxe.py'
#print  inc

#print args.copy_vector

db=None
from_db, to_db=args.copy_vector.split('2')

if inc.has_key(to_db.upper()):
	import __builtin__
	__builtin__.args = args
	dmhome=os.path.dirname(os.path.realpath(__file__))
	#print os.path.join(dmhome,'include',inc[to_db.upper()])
	#e(0)
	db = import_module(os.path.join(dmhome,'include',inc[to_db.upper()]))
elif inc.has_key(from_db.upper()):
	import __builtin__
	__builtin__.args = args
	dmhome=os.path.dirname(os.path.realpath(__file__))
	#print os.path.join(dmhome,'include',inc[from_db.upper()])
	#e(0)
	db = import_module(os.path.join(dmhome,'include',inc[from_db.upper()]))
	
abspath=os.path.abspath(os.path.dirname(sys.argv[0]))


ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
if hasattr(args, 'time_stamp') and args.time_stamp :
	ts=args.time_stamp
else:
	args.time_stamp=ts
	
job_name='default_job'	
if hasattr(args, 'job_name') and args.job_name :
	job_name=args.job_name
else:
	args.job_name=job_name

logdir=os.path.join(abspath,'logs',job_name)
if hasattr(args, 'log_dir') and args.log_dir :
	logdir=os.path.join(args.log_dir,job_name)
if not os.path.isdir(logdir):
	os.makedirs(logdir)
	

	
spooldir=os.path.join(logdir,'data1')
#print spooldir
#e(0)
datadir= os.path.join(logdir,ts)

##default export location if not provided as command line arg
TIMESTAMPED_DEFAULT_SPOOL_DIR = True
TIMESTAMPED_TO_DIR = True
TIMESTAMPED_TO_FILE = True

#print from_db, to_db
#print args.to_file
#print args.to_dir
#e(0)
default_spool_dir= os.path.join( r'C:\tmp\qc_default_spool',job_name)
if hasattr(args, 'default_spool_dir') and args.default_spool_dir:
	default_spool_dir= os.path.join(args.default_spool_dir,job_name)


to_dir=default_spool_dir

if hasattr(args, 'to_dir') and args.to_dir:
	to_dir=args.to_dir
if TIMESTAMPED_TO_DIR:
	to_dir =os.path.join(to_dir,ts)
if TIMESTAMPED_DEFAULT_SPOOL_DIR:
	default_spool_dir =os.path.join(default_spool_dir,ts)

if not os.path.isdir(to_dir):
	os.makedirs(to_dir)	
to_file=None
if hasattr(args, 'to_file') and args.to_file:
	to_file=args.to_file
else:
	if TIMESTAMPED_TO_FILE:
		to_file=os.path.join(to_dir,'spool_%s.data' % ts)
		if hasattr(args, 'query_sql_file') and args.query_sql_file:
			qfn, qfx = os.path.splitext(os.path.basename(args.query_sql_file))
			to_file=os.path.join(to_dir,'%s_%s.data' % (qfn,ts))
		elif hasattr(args, 'from_sub_partition') and args.from_sub_partition:
			to_file=os.path.join(to_dir,'%s_%s.%s.data' % (args.from_table,args.from_sub_partition,ts ))
		elif hasattr(args, 'from_partition') and args.from_partition:
			to_file=os.path.join(to_dir,'%s_%s.%s.data' % (args.from_table,args.from_partition.replace('(','_').replace(')','_'),ts ))
		elif hasattr(args, 'from_table') and args.from_table:
			to_file=os.path.join(to_dir,'%s_%s.data' % (args.from_table,ts ))
	else:
		to_file=os.path.join(to_dir,'spool.data')
		if hasattr(args, 'query_sql_file')and  args.query_sql_file:
			qfn, qfx = os.path.splitext(os.path.basename(args.query_sql_file))
			to_file=os.path.join(to_dir,'%s.data' % (qfn ))
		elif hasattr(args, 'from_sub_partition') and args.from_sub_partition:
			to_file=os.path.join(to_dir,'%s.%s.data' % (args.from_table,args.from_sub_partition ))
		elif hasattr(args, 'from_partition') and args.from_partition:
			to_file=os.path.join(to_dir,'%s.%s.data' % (args.from_table,args.from_partition))
		elif hasattr(args, 'from_table') and args.from_table:
			to_file=os.path.join(to_dir,'%s.data' % (args.from_table ))
#print to_file
#e(0)
def get_sharded_outfn(shard, qname=None):
	#print self.uargs.to_file
	#print self.uargs.to_dir
	#e(0)
	if qname:
		#q=qname.split('.')
		#if len(q)>2:
		#	owner=q[0]
		#	table_name=q[1]
			
		return os.path.join(to_dir, '%s.shard_%s.data' % (qname, shard))	
		#else:
		#	return os.path.join(to_dir, 'shard_%s.data' % shard)	
			
	else:
		return os.path.join(to_dir, 'shard_%s.data' % shard)	
#print  to_file
#e(0)