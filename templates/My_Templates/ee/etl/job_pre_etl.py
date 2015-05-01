import sys, os, re
from pprint import pprint
e=sys.exit
login = conf.args.to_db

#print args.query_sql_dir

c= conf.uargs.db.target(conf.log,conf.datadir,login,conf,'ORA11G',None)
regexp=re.compile(r'(.*)')	

def delete_query(log, qry,qname ):
	#print qry
	q='DELETE FROM (%s);\n' % qry.strip().strip(';')
	#print q
	#e(0)
	log.info('Deleting target query "%s"' % qname)
	(result,status,err) =  c.do_query (login, query=q ,regexp=regexp,qname=qname)
	if not status:		
		log.info(result[0][0])

def main(log, etl):	
	
	for i in range(len(etl.fromDb.from_query)):	
		qry= etl.fromDb.from_query[i]
		qname= etl.fromDb.from_query_name[i]
		delete_query(log, qry,qname )
	#e(0) 



