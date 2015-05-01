import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.base import base 
import codecs
from_tab_cols={}
#datadir=''


		
class pipeline(base):
	"""Pipeline template"""
	def __init__(self,log,args):
		self.log=log
		self.args=args
	def print_stats(self,globalStatus, startTime):
		args=self.args
		log=self.log
		status=0
		print '#'*60
		print 'Copy stats (%d threads, %d shards):' % (args.pool_size,args.num_of_shards)
		total=0

		rows_total=0

		#print globalStatus
		#sys.exit(1)
		for i in range(len(globalStatus)):
			if globalStatus[i][0]:
				failed=' (Failed)'
			if globalStatus[i][0]==99:
				failed=' (Not started)'		
			else:
				failed=''
			#print globalStatus[i]
			rows_copied=globalStatus[i][2]
			rows_total +=rows_copied
			if rows_copied>-1:
				log.info('Shard-%s/%s:%12d rows' %(i,globalStatus[i][0],rows_copied))
			else:
				log.info('Shard-%s/%s:\t\tn/a' %(i,globalStatus[i][0]))
			status +=globalStatus[i][0]
			if globalStatus[i][1]:
				total +=int(globalStatus[i][1])

			outfn='%s\\shard_%s.data' % (self.datadir,i)
			#os.unlink(outfn)
		if total>-1:
			log.info( 'TOTAL Bytes:%12d Bytes' % (total))
		else:
			log.info( 'TOTAL Bytes:\tn/a' )
		if rows_total>-1:	
			log.info( 'TOTAL Rows: %12d Rows' % (rows_total))
		else:
			log.info( 'TOTAL Rows:\t\tn/a' )

		print '#'*60	


		 
		if status:
			log.error('Copy failed.')
		else:
			log.info("Done.")
		elapsedTime = time.gmtime(time.time() - startTime)
		strTime = time.strftime("%H:%M:%S", elapsedTime)
		log.info("Elapsed: %s" % time.strftime("%H:%M:%S", elapsedTime))		
	def set_payload(self):				
		assert self.datadir, 'datadir is not set'
		(num_of_shards,lame_duck)=(self.args.num_of_shards,self.args.lame_duck)
		#print 2
		#print num_of_shards, self.toDb
		(shards,from_pld) = self.fromDb.set_payload(num_of_shards, self.toDb)

		nameList=[]		
		globalStatus={}
		
		#(to_db,to_table)
		#pprint(from_pld)
		#sys.exit(1)
		for i in range(len(from_pld)):	
			to_pld=self.toDb.set_payload(i,num_of_shards)
			#pprint (to_pld)
			nameList.append(("Shard-%d" % i,from_pld[i],to_pld))
			globalStatus[i]=(-1, -1,-1)	
		#pprint(nameList)
		#sys.exit(0)
		return (nameList,globalStatus) 		

	
	def execute(self,logger,payload, ts):
		(shard_name,from_pld,to_pld)=payload
		(field_term, lame_duck) =(self.args.field_term, self.args.lame_duck)
		#pprint (from_pld)
		(shard_name, rowid_from, rowid_to,outfn,cols_info) =from_pld
		(login, to_table)=to_pld	
		status=-1
		if 1:
			#conf=self.fromDb.get_spool_config(payload,field_term,limit)
			conf=self.fromDb.get_spool_config(from_pld,field_term,lame_duck)
			#outfn=self.spool_source_data(outfn,conf,payload)
			status=self.fromDb.spool_source_data(outfn,conf,payload)
			#print outfn
			#stat=os.stat(outfn).st_size
			#print 'spooled %d B' % stat
			#print 5
			#sys.exit(0)
			if 1:
				#pprint (payload)
				first_row=self.fromDb.get_firstrow()
				conf=self.toDb.get_load_config(field_term,first_row,payload,outfn)
				
				#print conf
				#sys.exit(0)
				#print payload
				#sys.exit(0)
				shard=payload[0].split('-')[1]
				#print shard
				(out,status,err,ins_cnt)=self.toDb.load_data(logger,conf,outfn,shard)
				#(out,status,err)=self.load_data(logger,conf)

		else:
			print 'Cannot fetch common columns.'

		stat=os.stat(outfn).st_size
		print 'spooled %d B' % stat
				
		return (stat,status,ins_cnt)
		
	

	