import sys, os, re
from pprint import pprint
e=sys.exit
login = conf.args.to_db
#print args.query_sql_dir
#if conf.args.from_user.strip().upper() in [conf.args.to_user.strip().upper()]:
#	assert not conf.args.from_db.strip().upper() in [conf.args.to_db.strip().upper()], 'Target and Source are the same. Exiting...'
(from_db,to_db) = conf.args.copy_vector.strip().upper().split('-')
print from_db,to_db
#self.uargs_db=self.uargs.target.target(self.log,datadir,self.login,self.conf,db,self.args.to_collection)
c= conf.uargs.target.target(conf.log, conf.datadir,login,conf,to_db,None)
regexp=re.compile(r'(.*)')	

def delete_query(log, qry,qname ):
	#print qry
	#starting with degree 128 (2**8)
	log.info('Deleting target query "%s"' % qname)
	for i in reversed(range(8)):
		print i;
		iferror=False
		q="""
	ALTER SESSION ENABLE PARALLEL DML;
	ALTER SESSION FORCE PARALLEL QUERY PARALLEL %d;
	ALTER SESSION SET PARALLEL_MIN_PERCENT=100;
	DELETE FROM (%s);
	COMMIT;
	ALTER SESSION DISABLE PARALLEL DML;
	ALTER SESSION FORCE PARALLEL QUERY PARALLEL 1;
	""" % (2**i, qry.strip().strip(';'))
		
		log.info('Trying parallelism degree %d' % 2**i) 
		(result,status,err) =  c.do_query (login, query=q ,regexp=regexp,qname=qname)
		log.info('SUCCESS: Parallelism degree %d' % 2**i) 
		if not status:	
			for r in result:
				if 'ORA-12827: insufficient parallel query slaves' in r[0]:
					iferror=True
				log.info(r[0])
		else:
			log.error(err)
		if not iferror:
			break
def main(log, etl):	
	
	for i in range(len(etl.fromDb.from_query)):	
		qry= etl.fromDb.from_query[i]
		qname= etl.fromDb.from_query_name[i]
		delete_query(log, qry,qname )
	#e(0) 



