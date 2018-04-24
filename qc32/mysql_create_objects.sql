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

drop table Date_test_to;

create table Date_test_to (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date);

drop table Date_test_from;
	
create table Date_test_from (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date);
	
SET time_zone = '+03:00';

	
insert into Persons_pipe_datetime_1 values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

"C:\Program Files\MariaDB 10.0\bin\mysql.exe" "--defaults-file=C:\Program Files\MariaDB 10.0\data\my.ini"

select * from information_schema.TABLES where TABLE_SCHEMA = 'test' and TABLE_NA='Persons_partitioned' \G

select table_schema, table_name, table_type from information_schema.TABLES;


select table_schema, table_name, table_type from information_schema.PARTITIONS where TABLE_SCHEMA = 'test' and TABLE_NA='Persons_partitioned' ;

select TABLE_SCHEMA,TABLE_NAME, PARTITION_NAME from information_schema.PARTITIONS  where TABLE_SCHEMA = 'test' and TABLE_NAME='Persons_partitioned' and partition_name='rx201411' \G;


insert into Persons_pipe_datetime select * from Persons_pipe_datetime;

C:\Temp\mysql\bin

mysql -u alex -D test -pmysql_pwd

drop table Persons_partitioned;

CREATE TABLE Persons_partitioned_2
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
CreateDt datetime
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(CreateDt) ) (
PARTITION rx201408 VALUES LESS THAN( TO_DAYS('2014-08-01 00:00:00') ), 
PARTITION rx201409 VALUES LESS THAN( TO_DAYS('2014-09-01 00:00:00') ), 
PARTITION rx201410 VALUES LESS THAN( TO_DAYS('2014-10-01 00:00:00') ), 
PARTITION rx201411 VALUES LESS THAN( TO_DAYS('2014-11-01 00:00:00') ), 
PARTITION rx201412 VALUES LESS THAN( TO_DAYS('2014-12-01 00:00:00') ), 
PARTITION rx201501 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00') ), 
PARTITION rx201502 VALUES LESS THAN( TO_DAYS('2015-02-01 00:00:00') ), 
PARTITION rx201503 VALUES LESS THAN( TO_DAYS('2015-03-01 00:00:00') ), 
PARTITION rx201504 VALUES LESS THAN( TO_DAYS('2015-04-01 00:00:00') ), 
PARTITION rx201505 VALUES LESS THAN( TO_DAYS('2015-05-01 00:00:00') ), 
PARTITION rx201506 VALUES LESS THAN( TO_DAYS('2015-06-01 00:00:00') ), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) );

CREATE TABLE Persons_sub_partitioned
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
CreateDt datetime
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(CreateDt) )
subpartition by hash (PersonID) (
PARTITION rx201411 VALUES LESS THAN( TO_DAYS('2014-11-01 00:00:00')) (SUBPARTITION subpart100, SUBPARTITION subpart101), 
PARTITION rx201501 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00')) (SUBPARTITION subpart200, SUBPARTITION subpart201), 
PARTITION rx201506 VALUES LESS THAN( TO_DAYS('2015-06-01 00:00:00')) (SUBPARTITION subpart300, SUBPARTITION subpart301), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) (SUBPARTITION subpartM00, SUBPARTITION subparM301));

select count(*) from Persons_sub_partitioned PARTITION (subpart101)

create table t1 (a int) engine myisam
partition by range (a)
subpartition by hash (a)
(partition p0 VALUES LESS THAN (1) 
(SUBPARTITION subpart00, SUBPARTITION subpart01));

create table t2 (PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt datetime) engine myisam
partition by range (CreateDt)
subpartition by hash (a)
(partition p0 VALUES LESS THAN (1) 
(SUBPARTITION subpart00, SUBPARTITION subpart01));

explain partitions select * from Persons_sub_partitioned \G

select count(*) from Persons_sub_partitioned partition(rx201411_subpart101)


rx201411_subpart101

insert into Persons_sub_partitioned values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

insert into Persons_partitioned values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

select * from Persons_partitioned PARTITION (rx201411)


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