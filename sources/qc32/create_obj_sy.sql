INPUT INTO "Persons_pipe_datetime" DELIMITED BY '|' FROM 'C:\Python27\data_mule_sybase\\shard_0.data' SKIP 1

CREATE TABLE Persons_pipe_datetime_1 (
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
City2 datetime);



C:\Program Files\SQL Anywhere 16\Bin64>dbisql.com -nogui -c "uid=dba;pwd=sql"

dbisql.com -nogui -c "uid=dba;pwd=sql;server=localhost"

C:\Program Files\SQL Anywhere 16\Bin64

dbisql.com -nogui -c "uid=dba;pwd=sql;server=demo16;dbn=demo"

dbisql.com -nogui -c "uid=dba;pwd=sql;server=demo16;dbn=demo"

"C:\\Program Files\\SQL Anywhere 16\\Bin64\\dbisql.com" -nogui -c "uid=dba;pwd=sql;dbn=demo;server=demo16"
0
