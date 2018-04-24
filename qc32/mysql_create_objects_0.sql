CREATE TABLE Persons_pipe_datetime_1
(
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
City2 datetime
);

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

"C:\Program Files\MariaDB 10.0\bin\mysql.exe" "--defaults-file=C:\Program Files\MariaDB 10.0\data\my.ini"



insert into Persons_pipe_datetime select * from Persons_pipe_datetime;

C:\Temp\mysql\bin

mysql -u alex -D test -pmysql_pwd


source C:\\Python27\\data_mule_mysql\\spool_test.sql;

SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13;
SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 13,14;
SELECT City2 FROM     Persons_pipe_datetime Order by City2 LIMIT 27,17;

LOAD DATA LOCAL  INFILE 'C:\\Python27\\data_mule_mysql\\mysql_shard_0.data' INTO TABLE Persons_pipe_datetime
FIELDS OPTIONALLY ENCLOSED BY '"' TERMINATED BY '|'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL  INFILE 'C:\\Python27\\data_mule_mysql\\mysql_shard_0.data' INTO TABLE Persons_pipe_datetime
FIELDS OPTIONALLY ENCLOSED BY '"' TERMINATED BY '|'
LINES TERMINATED BY '
';

LOAD DATA LOCAL  INFILE 'C:\\Python27\\data_mule_mysql\\mysql_shard_0.data' INTO TABLE Persons_pipe_datetime FIELDS OPTIONALLY ENCLOSED BY '"' TERMINATED BY '|' LINES TERMINATED BY '\n';