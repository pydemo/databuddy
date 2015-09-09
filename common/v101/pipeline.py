import re, types, string, sys, os, time 
import tempfile
from subprocess import Popen, PIPE
from pprint import pprint
import odbc, dbi
from common.v101.base import base 
import codecs
e=sys.exit

from_tab_cols={}



		
		
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
		(self.shards,self.from_pld) = self.fromDb.set_payload(num_of_shards, self.toDb)

		nameList=[]		
		globalStatus={}
		
		#(to_db,to_table)
		#pprint(self.from_pld)
		#e(0)
		for i in range(len(self.from_pld)):	
			print 
			to_pld=self.toDb.set_payload(i,num_of_shards)
			#pprint (to_pld)
			nameList.append(("Shard-%d" % i,self.from_pld[i],to_pld))
			globalStatus[i]=(-1, -1,-1)	
		#pprint(nameList)
		#sys.exit(0)
		return (nameList,globalStatus) 		

	def truncate_target(self):
		args=self.args
		#print self.fromDb
		#pprint(self.fromDb.input_file_names)
		#e(0)
		if self.fromDb.SPL:
			self.log.warn('Source is subpartition list.')
			assert args.to_table, 'To_Table is not set'
			self.log.warn('Target is subpartition.')
			splist=args.from_sub_partition_list.upper().split(',')
			self.log.warn('Truncating (%d) target subpartition(s).' % len(splist))
			for spart in splist:
				self.toDb.truncate_subpartition(spart.strip().upper())					
		if self.fromDb.SP:
			self.log.warn('Source is subpartition.')
			assert args.to_table, 'Table is not set'
			self.log.warn('Target is subpartition.')
			spart=args.from_sub_partition.upper().strip()
			if hasattr(args, 'to_sub_partition')and  args.to_sub_partition:
				spart=args.to_sub_partition.upper().strip()
			self.log.warn('Truncating target subpartition (%s).' % spart)
			self.toDb.truncate_subpartition(spart)			
		elif self.fromDb.PL:
			self.log.warn('Source is partition list.')
			assert args.to_table, 'Table is not set'
			self.log.warn('Target is partition.')
			plist=args.from_partition_list.upper().split(',')
			self.log.warn('Truncating (%d) target partition(s).' % len(plist))
			for part in plist:
				self.toDb.truncate_partition(part.strip().upper())	
		elif self.fromDb.P:
			if self.toDb.F:
				#delete output file or directory here
				#print self.toDb.out
				for k,out in self.toDb.out.items():
					_,fn=out
					#print fn
					if os.path.isfile(fn):
						self.log.warn('removing target file')
						os.remove(fn)
				#e(0)
			elif self.toDb.D:
				#delete output file or directory here
				#pprint(self.toDb.out)
				for k,out in self.toDb.out.items():
					_,fn=out
					print fn
					if os.path.isfile(fn):
						self.log.warn('removing target file')
						os.remove(fn)
				#e(0)
			else:
			
				assert args.to_table, 'To Table is not set'
				self.log.warn('Target is partition.')
				part=args.from_partition.upper().strip()
				self.log.warn('Truncating target partition "%s".' % part)
				self.toDb.truncate_partition(part)
		elif self.fromDb.TL:
			self.log.warn('Source is table list.')
			to_table=None
			if hasattr(args, 'to_table')and  args.to_table:			
				to_table = args.to_table.upper().strip()
			else:
				self.log.warn('to_table is not set.')
			if to_table:
				self.log.warn('Target is table "%s".' % to_table)
			tlist=args.from_table_list.upper().split(',')
			if to_table:
				#self.log.warn('Truncating target table %s.' % to_table)
				self.toDb.truncate_table(to_table)
			if 0:
				self.log.warn('Truncating (%d) target table(s).' % len(tlist))
				for tab in tlist:					
					self.toDb.truncate_table(tab)
		elif self.fromDb.T:
			self.log.warn('Source is table.')
			to_table=None
			if hasattr(args, 'to_table')and  args.to_table:			
				to_table = args.to_table.upper().strip()
			else:
				self.log.warn('to_table is not set.')
			#assert to_table, 'to_table has to be set fo'
			if to_table:
				#self.log.warn('Truncating target table %s.' % to_table)
				self.toDb.truncate_table(to_table)
			else:
				tab=args.from_table.strip().upper()
				self.log.warn('Getting target table name from source table name.')				
				#self.log.warn('Truncating target table "%s".' % tab)
				self.toDb.truncate_table(tab)
			
		elif self.fromDb.QF:
			self.log.warn('Source is query file.')
		elif self.fromDb.QD:
			self.log.warn('Source is query dir.')
		elif self.fromDb.IF:
			self.log.warn('Source is CSV file.')
			to_table=None
			if hasattr(args, 'to_table')and  args.to_table:			
				to_table = args.to_table.upper().strip()
				self.toDb.truncate_table(to_table)
			else:
				self.log.warn('Reading table name from input file name.')
				for ifn in self.fromDb.input_file_names:
					fn=os.path.basename(ifn)			
					tab='.'.join(fn.split('.')[:2])
					self.toDb.truncate_table(tab)
		elif self.fromDb.ID:
			self.log.warn('Source is CSV dir.')
			to_table=None
			if hasattr(args, 'to_table')and  args.to_table:			
				to_table = args.to_table.upper().strip()
				self.toDb.truncate_table(to_table)
			else:
				self.log.warn('Reading table name from input file name.')
				for ifn in self.fromDb.input_file_names:
					fn=os.path.basename(ifn)			
					tab='.'.join(fn.split('.')[:2])
					self.toDb.truncate_table(tab)
		else:
			print 'unsupported truncate target'
		#e(0)
		if 0:
			#self.toDb.truncate_target()
			if self.SPL:
				assert self.to_table, 'Table is not set'
				self.log.warn('Target is subpartition.')
				for spart in args.from_sub_partition_list.upper().split(','):
					self.truncate_subpartition(spart.strip().upper())		
			if self.SP:
				assert self.to_table, 'Table is not set'
				self.log.warn('Target is subpartition.')
				self.truncate_subpartition(args.from_sub_partition.upper().strip())
			elif self.PL:
				assert self.to_table, 'Table is not set'
				self.log.warn('Target is partition.')
				for part in args.from_partition_list.upper().split(','):
					self.truncate_partition(part.strip().upper())						
			elif self.P:
				assert self.to_table, 'Table is not set'
				self.log.warn('Target is partition.')
				self.truncate_partition(args.from_partition.upper())			
			elif self.T:
				assert self.to_table, 'Table is not set'
				self.log.warn('Target is table.')
				self.truncate_table()
		
	
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
		
	

	