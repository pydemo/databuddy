CREATE TABLE Persons_pipe_datetime
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
City2 timestamp
);


insert into Persons_pipe_datetime_1 values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',systimestamp);

CREATE TABLE Timestamp_test_from
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
CreateDt timestamp
);

insert into Timestamp_test_from values (s_pid.nextval,'--LastName','--FirstName','--Address','--City',s_pid.currval,'--LastName','--FirstName','--Address',systimestamp);


select count(*) from Timestamp_test_from

create sequence s_pid start with 1

drop table Timestamp_test_from

CREATE TABLE Timestamp_test_to
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
CreateDt timestamp
);







 s_pid.nextval
 
 CREATE TABLE Persons_sub_partitioned
(PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt timestamp)
PARTITION BY RANGE(CreateDt) 
SUBPARTITION BY HASH(PersonID)
SUBPARTITION TEMPLATE(SUBPARTITION sp1,SUBPARTITION sp2)
(PARTITION sales_feb2000 VALUES LESS THAN(TO_DATE('03/01/2013','DD/MM/YYYY')),
 PARTITION sales_mar2000 VALUES LESS THAN(TO_DATE('04/01/2014','DD/MM/YYYY')),
 PARTITION sales_apr2000 VALUES LESS THAN(TO_DATE('05/01/2015','DD/MM/YYYY')),
 PARTITION sales_may2000 VALUES LESS THAN(TO_DATE('06/01/2016','DD/MM/YYYY')));
 
 
 
 
 SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_SUBPARTITIONS 
 where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('SCOTT.Persons_sub_partitioned') 
 AND UPPER(partition_name)=UPPER('SALES_APR2000_SP1');
 
 
 insert into Persons_sub_partitioned values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',systimestamp);