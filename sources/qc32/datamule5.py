#!/usr/bin/python	
# Data spooler/extractor for SQL Server
import Queue
import threading
import time
#import getopt
import sys, os
from pprint import pprint
import logging 
#import ora_pipe_tools as st
import re, types
import codecs
#import pipeline.v101.from_sqlserver as ppl1
#import pipeline.v101.to_sqlserver as ppl2
import common.v101.config as conf 
from common.v101.exceptions import CopyVectorError
import argparse
import datetime

		
"""

C:\Python27\ora_data_pipe

python csv2ora.py -g SCOTT/tiger2@XE  -a SCOTT.Persons_pipe2 -i C:\Python27\ora2ora_data_pipe\shard_0.data -o 1 -r 1  -t "|"

Scripts\pyinstaller.exe -y data_mule_ora_full_rel_citi\dbtools.py --log-level DEBUG --onefile


csv_extractor -m 'C:\Temp\mysql\bin\' -q mysql_query.sql -j alex  -x mysql_pwd -b test -n localhost -a spool/mysql_data.dump -t "|" -o 3 -r 3 -w mysql2csv


"""
exitFlag = 0


verbose = False
ts= time.strftime('%Y%m%d_%H%M%S')

globalStatus={}
		
startTime = time.time()
dbs=conf.dbs 

#print dbs
#sys.exit(1)
#print startTime
expiration_dt = datetime.datetime(2015,01,01)
now_dt = datetime.datetime.now()
params=conf.params
core=params['core']
if now_dt>expiration_dt:
	print 'Please update %s.' % conf.appname
	sys.exit(0)
def show_help(cvarg,copy_vector):
	assert cvarg, 'Help argument [-h] or [--help] is not set'
	assert copy_vector, 'Copy vector [-w] is not set'
	
	if copy_vector.upper() in ('ALL'):
		for i in conf.dbs:
			print 'From %s:' % conf.dbs[i]
			for vector in ['%s2%s' % (str(i).lower(),x.lower()) for x in conf.dbs if '%s2%s' % (i, x)!='csv2csv']:
				#print vector
				show_vector_help(vector)
	elif copy_vector.upper() in ('LIST'):
		cnt=1
		for i in conf.dbs:
			print 'From %s:' % conf.dbs[i]
			for vector in ['%s2%s' % (str(i).lower(),x.lower()) for x in conf.dbs if '%s2%s' % (i, x)!='CSV2CSV']:
				(ft, to)= vector.upper().split('2')
				print '\t%s. %s->%s' % (cnt, conf.dbs[ft], conf.dbs[to])
				cnt +=1
	elif copy_vector.upper() in ('FEAT'):
		cnt=1
		for i in conf.dbs:
			print 'From %s:' % conf.dbs[i]
			for vector in ['%s2%s' % (str(i).lower(),x.lower()) for x in conf.dbs if '%s2%s' % (i, x)!='CSV2CSV']:
				(ft, to)= vector.upper().split('2')
				if ft in ('CSV'):
					print '\t%s. Load data from "%s file" to "%s"' % (cnt, conf.dbs[ft], conf.dbs[to])
				elif to in ('CSV'):
					print '\t%s. Extract table data from "%s" to "%s file"' % (cnt, conf.dbs[ft], conf.dbs[to])
				else:
					print '\t%s. Copy table data from "%s" to "%s"' % (cnt, conf.dbs[ft], conf.dbs[to])
				cnt +=1				
	else:
		show_vector_help(copy_vector)

		
def show_vector_help(copy_vector):
		(from_db, to_db) = copy_vector.split('2')
		(ufrom_db, uto_db) = copy_vector.upper().split('2')
		from_args=conf.params['FROM'][ufrom_db]
		to_args=conf.params['TO'][uto_db]
		print '\nSet following command line arguments to copy from %s to %s:\n' % (dbs[ufrom_db], dbs[uto_db])
		print conf.appname,
		keys=[]
		for key,arg in core.items():
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
		for key in keys:
			if key in core.keys():
				arg=core[key]
				print '(Common) %s [%s]\t%s\t' % (arg['short'],arg['long'],arg['help'])		
			elif key in from_args.keys():
				arg=from_args[key]
				print '(From %s) %s [%s]\t%s\t' % (dbs[ufrom_db],arg['short'],arg['long'],arg['help'])
			else:
				arg=to_args[key]
				print '(To %s) %s [%s]\t%s\t' % (dbs[uto_db],arg['short'],arg['long'],arg['help'])
			
	


#join(map(lambda x: '[%s ora2%s]' % (cvarg,x),dbs.keys()))
	#print cvarg,copy_vector
def get_copy_vector(default_vector=None):
	if default_vector:
		return default_vector
	else:
		arglist=sys.argv[1:]
		#pprint(arglist)
		#sys.exit(0)
		assert '-w' in arglist, 'Copy vector is not set [-w]'
		cvkey= arglist.index('-w')
		(cvarg,copy_vector) = arglist[cvkey:cvkey+2]
		return copy_vector
		#sys.exit(0)

 #str(datetime.datetime.now()).split('.')[0]
print '-'*70
print '%s %s (beta, %s)' % (conf.apptitle,conf.version,conf.rel_date	)

arglist=sys.argv[1:]
#print arglist
if not arglist:
	cvarg=None
	conf.show_default_help(cvarg)
if '-h' in arglist or '--help' in arglist:
	cvkey=None
	
	copy_vector=None
	if '-h' in arglist:
		cvarg='-h'
		cvkey= arglist.index('-h')		
	else:
		cvarg='--help'
		cvkey= arglist.index('--help')
	if  len(arglist)-cvkey==1:
		pass
	else:	
		(cvarg,copy_vector) = arglist[cvkey:cvkey+2]
	if not copy_vector:
		conf.show_default_help(cvarg)
	else:
		show_help(cvarg, copy_vector)
	sys.exit(0)
#print 'DataMule 1.01 (beta, %s)' % rel_date	
print 'Copyright: (c) 2014 %s, All rigts reserved.' % conf.app_author
print 'Agreement: Use this tool at your own risk. Author is not liable for any damages or losses related to the use of this software.'
print '-'*70	
	
parser = argparse.ArgumentParser(description='Datamule.')
parser.add_argument("cmd", help=argparse.SUPPRESS, nargs="*")
# Datamule args


#pprint (params)

for key,val in core.items():
	#print 'adding %s  %s\t for core' % (val['short'],key)	
	parser.add_argument(val['short'],val['long'], default=val['default'], type=val['type'],  help=val['help'])

print ''
copy_vector=get_copy_vector(conf.default_vector)
#print copy_vector
(log,datadir)=conf.config_log(copy_vector)
conf.add_argument(log,copy_vector,parser)
# From CSV file
if conf.default_vector:
	log.warn('Copy vector is defaulted to %s' % conf.default_vector)
args = parser.parse_args()
(pool_size, num_of_shards) = (args.pool_size, args.num_of_shards)
assert pool_size, 'pool_size is not set.'
assert num_of_shards, 'num_of_shards is not set.'

ff=conf.ff
dbs=conf.dbs
(source,target) = copy_vector.split('2')
if target.upper() in 'MYSQL' or source.upper() in 'MYSQL':
	assert args.mysql_client_home, 'mysql_client_home [-z] is not set'
if source.upper() in ff:
	if target.upper() in 'MYSQL':
		# only serial load
		if args.pool_size>1 or args.num_of_shards>1:
			log.warn('Forcing serial load in MySQL.')
			args.pool_size=1
			args.num_of_shards=1
	from  template.v101.load_from_csv import load_from_csv as etl_tmpl
elif target.upper() in ff:
	from  template.v101.spool_to_csv import spool_to_csv as etl_tmpl
elif target.upper() in dbs and source.upper() in dbs:
	from  template.v101.spool_and_load import spool_and_load as etl_tmpl
else:
	#log.error('Unsupported copy vector %s.' % copy_vector)
	raise CopyVectorError(copy_vector)
	
etl = etl_tmpl(log,datadir,args)
etl.print_copy_details()
if 1:
	var = raw_input("Are you sure you want to proceed?(y/n): ")
	if var.upper() not in ('Y','N','YES','NO'):
		log.info('Exiting...')
		sys.exit(0)
	if var.upper() in ('N','NO'):
		log.info('Exiting...')
		sys.exit(0)

(nameList,globalStatus)= etl.set_payload()

	
class myThread (threading.Thread):
	def __init__(self, threadID, name, q):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.q = q
	def run(self):
		log.info( "Starting " + self.name)
		process_data(self.name,self.threadID, self.q)
		log.info( "Exiting " + self.name)
	
def process_data(threadName, threadID, q):
	global globalStatus
	while not exitFlag:
		queueLock.acquire()
		if not workQueue.empty():
			payload = q.get()
			queueLock.release()
			log.info( "%s processing %s" % (threadName, payload[0]) )
			shard_id=int(payload[0].split('-')[1])
			(out,status,ins_cnt)=etl.execute(log,payload,ts)
			if not ins_cnt>-1:
				(out,status,ins_cnt)=(-1,-1,-1)
			status=0
			#print 'INSERTED:' ,ins_cnt
			globalStatus[shard_id]=(status,out,int(ins_cnt))
			log.info( "%s exit status %d" % (threadName,globalStatus[shard_id][0] ))
		else:
			queueLock.release()

#Create pool

threadList=[]

for i in range(args.pool_size):
	threadList.append("Thread-%d" % i)

		
queueLock = threading.Lock()
workQueue = Queue.Queue(num_of_shards)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
	thread = myThread(threadID, tName, workQueue)
	thread.start()
	threads.append(thread)
	threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
	workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
	pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
	t.join()


etl.print_stats(globalStatus, startTime)	





