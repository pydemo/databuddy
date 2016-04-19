database test@ol_s_111214_125432

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
Address2 varchar(255), City2 DATETIME YEAR TO SECOND);

 CONNECT to 'test5@ol_s_111614_133312';
 
 
 C:\Windows\System32\cmd.exe cmd /k C:\PROGRA~2\IBMINF~1\ol_s_112614_175026.cmd

CREATE TABLE Persons_pipe_datetime_1(PersonID int,LastName varchar(255),FirstName varchar(255),Address varchar(255),City varchar(255),PersonID2 int,LastName2 varchar(255),FirstName2 varchar(255),ddress2 varchar(255), City2 DATETIME YEAR TO SECOND);
 
insert into Persons_pipe_datetime_1 values 
(2,'--LastName','--FirstName','--Address','--City',2,
'--LastName','--FirstName','--Address','2012-11-10 09:08:07');

truncate table PERSONS_PIPE_DATETIME_1

insert into Persons_pipe_datetime_1 values (2,'--LastName',
'--FirstName','--Address',
'--City',2,'--LastName','--FirstName',
'--Address', extend(current,year to second));

LOAD FROM 'C:\Python27\data_mule_informix\informix_data.csv' DELIMITER '|' INSERT INTO test.Persons_pipe_datetime_1

WITHOUT HEADINGS

SELECT count(*) FROM PERSONS_PIPE_DATETIME_1;

SELECT FIRST 5  * FROM PERSONS_PIPE_DATETIME_1;

SELECT SKIP 55 LIMIT 10  * FROM PERSONS_PIPE_DATETIME_1;
SELECT SKIP 60  * FROM PERSONS_PIPE_DATETIME_1;

C:\Windows\System32\cmd.exe cmd /k C:\PROGRA~2\IBMINF~1\ol_s_111214_125432.cmd


set INFORMIXDIR=C:\PROGRA~2\IBMINF~1
set INFORMIXSERVER=ol_s_111214_125432
set ONCONFIG=ONCONFIG.ol_s_101014_181102
set PATH=C:\PROGRA~2\IBMINF~1\bin;%PATH%
set CLASSPATH=%INFORMIXDIR%\extend\krakatoa\krakatoa.jar;%INFORMIXDIR%\extend\krakatoa\jdbc.jar;%CLASSPATH%
set INFORMIXSQLHOSTS=C:\PROGRA~2\IBMINF~1\etc\sqlhosts.ol_s_101014_181102
set DBTEMP=C:\PROGRA~2\IBMINF~1\infxtmp
set CLIENT_LOCALE=EN_US.CP1252
set DB_LOCALE=EN_US.8859-1
mode con codepage select=1252

dbaccess test@ol_s_101014_181102 conn.sql

C:\Windows\System32\cmd.exe cmd /k C:\PROGRA~2\IBMINF~1\ol_s_101014_181102.cmd

dbaccess  'test5@ol_s_111214_125432' C:\Python27\csvextractor_1235\test\v101\query\informix_query.sql


> info columns for PERSONS_PIPE_DATETIME_1;


Column name          Type                                    Nulls

personid             integer                                 yes
lastname             varchar(255)                            yes
firstname            varchar(255)                            yes
address              varchar(255)                            yes
city                 varchar(255)                            yes
personid2            integer                                 yes
lastname2            varchar(255)                            yes
firstname2           varchar(255)                            yes
address2             varchar(255)                            yes
city2                datetime year to second                 yes

http://www.iiug.org/software/

C:\Program Files (x86)\IBM Informix Software Bundle\bin\dbaccess.exe - c:\Pytho27\CSVEXT~3\208BE9~1\CSVEXT~1\logs\20141202_094951_656000\sql\get_query_columns_20141202_094951.sql

c:\\Python27\\csvextractor_dist_64\\20141202_094946\\csvextractor64\\tests\\InformixIDS_to_CSV\\Extract_InformixIDS_ShardedQueryFile_into_CSVDefault.bat




