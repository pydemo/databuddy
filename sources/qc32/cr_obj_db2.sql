
CREATE TABLE Persons_pipe_datetime (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255),PersonID2 int,LastName2 varchar(255),FirstName2 varchar(255),Address2 varchar(255),City2 datetime);


CREATE TABLE orders(id INT, shipdate DATE) PARTITION BY RANGE(shipdate)(PARTITION q4_05 STARTING MINVALUE, PARTITION q1_06 STARTING '1/1/2014', PARTITION q2_06 STARTING '4/1/2014',    PARTITION q3_06 STARTING '7/1/2014',    PARTITION q4_06 STARTING '10/1/2014' ENDING '12/31/2014')

PersonID |LastName |FirstName |Address |City |PersonID2|LastName2|FirstName2 |Address2 |City2
	
drop table Persons_pipe_datetime_1


CREATE TABLE Persons_pipe_datetime (PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255),PersonID2 int,LastName2 varchar(255),FirstName2 varchar(255),Address2 varchar(255),City2 timestamp)

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',current timestamp);


create table ts_test (City2 datetime)

EXPORT TO result.csv OF DEL MODIFIED BY CHARDEL;


EXPORT TO C:\Python27\data_mule_db2\result2.csv OF DEL MODIFIED BY NOCHARDEL SELECT * FROM Persons_pipe_datetime_1;

IMPORT FROM C:\Python27\data_mule_db2\result.csv OF DEL INSERT INTO Persons_pipe_datetime_1

db2cmd /c /w /i "db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"


db2cmdadmin db2setcp "db2 -f C:\Python27\data_mule_db2\cmd2.sql -z C:\Python27\data_mule_db2\DB2UploadLog.txt"

connect to SAMPLE user db2admin using 198Morgan

set DB2INSTANCE=DB2 
				
set DB2DATABASE=SAMPLE

db2 -r output_file.txt -tf sql_file.sql


db2 -r mydata\orglist.txt "select * from org"

!db2start;
connect to sample;
select * from Persons_pipe_datetime_1;
terminate;

db2start
db2 connect to sample
db2 select * from org
db2 terminate
db2stop


FETCH FIRST 10 ROWS ONLY









