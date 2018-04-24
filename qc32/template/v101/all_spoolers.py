ppl={}
from pipeline.v101.from_oracle import FromOracle		
from pipeline.v101.from_mongo import FromMongo
from pipeline.v101.from_sqlserver import FromSQLServer
from pipeline.v101.from_postgresql import FromPostgreSQL
from pipeline.v101.from_sybasesqlanywhere import FromSybaseSQLAnywhere
#from pipeline.v101.from_sybasease import FromSybaseASE
from pipeline.v101.from_timesten import FromTimesTen
from pipeline.v101.from_db2udb import FromDb2UDB
from pipeline.v101.from_informix import FromInformix
from pipeline.v101.from_mysql import FromMysql
from pipeline.v101.from_sqllite import FromSQLLite
from pipeline.v101.from_curl import FromCurl		

ppl['ORA']=FromOracle
ppl['MONGO']=FromMongo
ppl['DBT']=FromDb2UDB			
ppl['SS']=FromSQLServer
ppl['PGR']=FromPostgreSQL
ppl['SY']=FromSybaseSQLAnywhere
#ppl['SY']=FromSybaseASE
ppl['TTE']=FromTimesTen
ppl['INFOR']=FromInformix
#ppl['MAR']=ToMariaDB
ppl['MYS']=ppl['INFOB']=ppl['MAR']=FromMysql
ppl['SLI']=FromSQLLite
ppl['CURL']=FromCurl
def get_ppl(db):
	for d in [db[:i+1].upper() for i in range(len(db)) if i>0][::-1]:
		#print d, 1
		if ppl.has_key(d):
			#print ppl[d]
			return ppl[d]
	return None