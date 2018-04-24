import sys, os, re
from pprint import pprint
e=sys.exit
login = conf.args.to_db
#print args.query_sql_dir

c= conf.uargs.db.target(conf.datadir,login,conf,'ORA11G',None)
regexp=re.compile(r'(.*)')	

def delete_query(log, qry,qname ):
	#print qry
	#starting with degree 128 (2**8)
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
		log.info('Deleting target query "%s"' % qname)
		(result,status,err) =  c.do_query (login, query=q ,regexp=regexp,qname=qname)
		
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



