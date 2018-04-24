ppl={}
from pipeline.v101.to_oracle import ToOracle		
from pipeline.v101.to_mongo import ToMongo		
from pipeline.v101.to_db2udb import ToDb2UDB
from pipeline.v101.to_sqlserver import ToSQLServer
from pipeline.v101.to_postgresql import ToPostgreSQL
from pipeline.v101.to_sybasease import ToSybaseASE
from pipeline.v101.to_sybasesqlanywhere import ToSybaseSQLAnywhere
from pipeline.v101.to_timesten import ToTimesTen
from pipeline.v101.to_informix import ToInformix
from pipeline.v101.to_mariadb import ToMariaDB
from pipeline.v101.to_mysql import ToMysql
from pipeline.v101.to_sqllite import ToSQLLite

ppl['ORA']=ToOracle
ppl['DBT']=ToDb2UDB			
ppl['SS']=ToSQLServer
ppl['PGR']=ToPostgreSQL
#ppl['SYB']=ToSybaseASE
ppl['SY']=ToSybaseSQLAnywhere
ppl['TTE']=ToTimesTen
ppl['INFOR']=ToInformix
ppl['MAR']=ToMariaDB
ppl['MYS']=ppl['INFOB']=ToMysql
ppl['SLI']=ToSQLLite
ppl['MONGO']=ToMongo

def get_ppl(db):
	for d in [db[:i+1].upper() for i in range(len(db)) if i>0][::-1]:
		if ppl.has_key(d):
			return ppl[d]
	return None