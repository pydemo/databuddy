use products
db.createUser( { "user" : "test_user",
                 "pwd": "tast_pwd",
                 "customData" : { employeeId: 12345 },
                 "roles" : [ { role: "clusterAdmin", db: "admin" },
                             { role: "readAnyDatabase", db: "admin" },
                             "readWrite"
                             ] },
               { w: "majority" , wtimeout: 5000 } )
			   
use reporting
db.createUser(
    {
      user: "reportsUser",
      pwd: "12345678",
      roles: [
         { role: "read", db: "reporting" },
         { role: "read", db: "products" },
         { role: "read", db: "sales" },
         { role: "readWrite", db: "accounts" }
      ]
    }
)

http://sthreesoft.com/wp/sql-to-mongodb-mapping-chart/


db.users.insert(
   { user_id: "bcd001", age: 45, status: "A" }
)
#create collection

db.test.insert( {
    user_id: "abc123",
    age: 55,
    status: "A"
 } )
 
db.users.insert(
   { user_id: "bcd001", age: 45, status: "A" }
)

host = db.serverStatus().host;

prompt = function() {
             return db+"@"+host+"$ ";
         }
		 
		 
db.test.find(    { status: { $ne: "A" } })

print("name,age,status");
db.test.find().forEach(function(test){
  print("#{test.user_id},#{test.age.valueOf()},{test.status}");
});


DBQuery.shellBatchSize = 10;

mongo test export.js > out.csv

mongo.exe -u test_user -p test_pwd


db.system.profile.find().pretty()


'db.test.find({ status: "A" })'
#export
mongoexport.exe  /d test /c test  /f "user_id,age,status" --csv
mongoexport.exe  /d test /c test  /f "user_id,age,status" --csv  /o c:\tmp\test.csv

mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "user_id,age,status" --csv  /o c:\tmp\test.csv /h localhost /port 27017

mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "user_id,age,status" --type=csv  /o c:\tmp\test.csv /h localhost /port 27017 --query c:\tmp\mongo_q.js 

mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "user_id,age,status" --type=csv  /o c:\tmp\test.csv /h localhost /port 27017 --query "{status:'A'}"



mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" --type=json  /o c:\tmp\test.csv /h localhost /port 27017 

mongoexport.exe -u test_user -p tast_pwd /d test /c test  /f "ID,TITLE,ISIN,COUNTRY,DESCRIPTION,SECURITYTYPE,CREATED" --type=json  /o c:\tmp\test.csv /h localhost /port 27017  /query "{'COUNTRY':'United States'}"



/limit 1
 
mongoimport.exe  /d test /c test /file c:\tmp\test_in.txt /f "user_id,age,status" /type csv

mongoimport.exe  -u test_user -p tast_pwd /d test /c test /file c:\tmp\test_in.txt /f "user_id,age,status" /type csv '/headerline'

mongoimport.exe  -u test_user -p tast_pwd /d test /c test /file c:\tmp\test.csv  /type csv /headerline

mongoimport.exe  -u test_user -p tast_pwd /d test /c test /file C:\Python27\data_migrator_1239_mongo\CSV_OUT\testMONGO_Table.data  /type csv /headerline
mongoimport.exe -u test_user -p tast_pwd /d test /h localhost /c test /file C:\Python27\data_migrator_1239_mongo\test\v101\data\mongo_shard_0.data /type csv /headerline

C:\Python27\data_migrator_1239_mongo\CSV_OUT\testMONGO_Table.data


mongo.exe -u test_user -p tast_pwd c:\tmp\mongo_q.js --quiet

mongo.exe -u test_user -p tast_pwd --eval 'printjson(db.test.find({ status: "A" }).toArray())'

mongo.exe -u test_user -p tast_pwd --eval "printjson(db.test.find({ status:'A'}).toArray())"

mongo.exe -u test_user -p tast_pwd --eval "print(db.test.find({ status:'A'}))"

db.test.remove({})

db.test.count()



 


 
 



			   