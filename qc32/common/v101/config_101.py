import time, os, sys
import logging
from common.v101.exceptions import CopyVectorError

def config_log(app):
	
	ts= time.strftime('%Y%m%d_%H%M%S')
	abspath= os.path.abspath(os.path.dirname(sys.argv[0]))
	if 1:
		logdir='logs'
		ldir = '%s\\%s' % (abspath,logdir)
		if not os.path.isdir(ldir):
			os.makedirs(ldir) 	
	spooldir='logs'
	datadir= '%s\\%s\\%s' % (abspath,spooldir,ts)
	dumpdir = '%s\\spool' % datadir
	if not os.path.isdir(datadir):
		os.makedirs(datadir) 
	if 1:	
		sqlgdir ='%s\\sql' % (datadir)
		if not os.path.isdir(sqlgdir):
			os.makedirs(sqlgdir) 
		if not os.path.isdir(dumpdir):
			os.makedirs(dumpdir) 

	
	logging.basicConfig(filename='%s\\%s%s.log' % (datadir,app,ts), filemode='w', level=logging.DEBUG,format='%(asctime)s | %(name)s | %(levelname)s | %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
	log = logging.getLogger(app)
	log.setLevel(logging.DEBUG)
	ch = logging.StreamHandler()
	ch.setLevel(logging.DEBUG)
	# create formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	ch.setFormatter(formatter)
	log.addHandler(ch)
	log.info('Extracting to: \n"%s"', dumpdir)	
	return (log,datadir)

def add_argument(log,vector,parser):
	# From CSV file
	(source,target) = vector.split('2')
	#print vector
	#print (source,target)
	#sys.exit(0)
	if source.upper() in ('MYSQL') or target.upper() in ('MYSQL'):		
		parser.add_argument('-z','--mysql_client_home', type=str,  help='Mysql client home.')

	if source.upper() in ('ORA'):
		parser.add_argument('-f','--from_db', type=str,  help='From database.')		
		parser.add_argument('-c','--from_table', type=str,  help='From table.')		
		parser.add_argument('-e','--nls_date_format', type=str, default='DD-Mon-YYYY HH:MI:SS AM', help='nls_date_format for spool.')
		parser.add_argument('-m','--nls_time_format', type=str, default='DD-Mon-RR HH.MI.SSXFF AM', help='nls_time_format for spool.')
	elif source.upper() in ('CSV'):
		parser.add_argument('-i','--input_file',type=str,  help='Input CSV file.')
		#parser.add_argument('-k','--skip_rows',type=int, default=0, help='Header size. Number of rows to skip in input file.')
		parser.add_argument('-y','--sample_size_pct', type=int,  default=1, help='Sample size in %% to extimate number of lines in input CSV file.')		
	elif source.upper() in ('SS'):
		parser.add_argument('-q','--query_sql_file',type=str,  help='Input file with query sql.')
		parser.add_argument('-j','--from_user',type=str,  help='SQL Server user')
		parser.add_argument('-x','--from_passwd',type=str,  help='SQL Server user password')
		parser.add_argument('-b','--from_db_name', type=str,  help='SQL Server database')
		parser.add_argument('-n','--from_db_server', type=str,  help='SQL Server instance name.')
		parser.add_argument('-i','--wait_limit_sec', type=str,  help='Secons to wait for spool file to become available.')
	elif source.upper() in ('MYSQL'):
		parser.add_argument('-q','--query_sql_file',type=str,  help='Input file with query sql.')
		parser.add_argument('-j','--from_user',type=str,  help='Mysql user')
		parser.add_argument('-x','--from_passwd',type=str,  help='Mysql user password')
		parser.add_argument('-b','--from_db_name', type=str,  help='Mysql database')
		parser.add_argument('-n','--from_db_server', type=str,  help='Mysql instance name.')

	else:
		raise CopyVectorError(vector)
	if target.upper() in ('ORA'):
		parser.add_argument('-g','--to_db', type=str,  help='To database.')
		parser.add_argument('-a','--to_table', type=str,  help='To table.')
		if not source.upper() in ('ORA'):
			parser.add_argument('-e','--nls_date_format', type=str, default='DD-Mon-YYYY HH:MI:SS AM', help='nls_date_format for spool.')
			parser.add_argument('-m','--nls_time_format', type=str, default='DD-Mon-RR HH.MI.SSXFF AM', help='nls_time_format for spool.')
	elif target.upper() in ('CSV'):
		parser.add_argument('-a','--to_file', type=str,  help='To file.')		
	elif target.upper() in ('SS'):
		parser.add_argument('-u','--to_user',type=str,  help='SQL Server user')
		parser.add_argument('-p','--to_passwd',type=str,  help='SQL Server user password')
		parser.add_argument('-d','--to_db_name', type=str,  help='SQL Server database')
		parser.add_argument('-s','--to_db_server', type=str,  help='SQL Server instance name.')
		parser.add_argument('-a','--to_table', type=str,  help='To table.')
	elif target.upper() in ('MYSQL'):
		parser.add_argument('-u','--to_user',type=str,  help='Target db user')
		parser.add_argument('-p','--to_passwd',type=str,  help='Target db user password')
		parser.add_argument('-d','--to_db_name', type=str,  help='Target database')
		parser.add_argument('-s','--to_db_server', type=str,  help='Target db instance name.')
		parser.add_argument('-a','--to_table', type=str,  help='Target table.')		
	else:
		raise CopyVectorError(vector)
		
