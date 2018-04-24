CREATE TABLE Persons_pipe2
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
City2 varchar(255)
);


CREATE TABLE Persons_pipe2_
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
City2 varchar(255)
);

CREATE TABLE Persons_pipe_date
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
City2 date
);


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
CreateDt datetime
);

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',GETDATE());


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
City2 timestamp);





drop table Persons_pipe2

CREATE TABLE Persons_pipe
(
PersonID int,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
);

commit;


truncate table Persons

truncate table Persons_pipe2

drop table Persons

insert into Persons_pipe values (1,'--LastName','--FirstName','--Address','--City');

insert into Persons_pipe2 values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address','--City');


insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',GETDATE());

insert into Persons_pipe_date values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',GETDATE());

insert into Persons_pipe_date values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',sysdate);

insert into Persons_pipe_date select * from Persons_pipe_date;

insert into Persons_pipe2 select * from Persons_pipe2;

insert into Persons_pipe2_ select * from Persons_pipe2_;

insert into Persons_pipe1 select * from Persons_pipe1;

insert into Persons_pipe select * from Persons_pipe;

truncate table dbo.Persons_pipe_datetime_1;

select * from Persons_pipe;

select PersonId, count(*) from Persons_pipe2 group by PersonId;

select count(*) from dbo.Persons_pipe_datetime;

1441792

truncate table Persons_pipe_datetime_1;


select * from Persons_pipe_datetime;

insert into Persons_pipe_datetime_1 values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address','2014-09-22 23:16:55');

create table Persons_pipe1  select * from dbo.Persons_pipe2 where 1=2;

select TOP 1 PERCENT * from Persons;

SELECT LastName "LN" FROM     dbo.Persons p

select count(*) from Persons_pipe_datetime_1

SELECT p.*
FROM     Persons p
ORDER BY newId() 
OFFSET  50 ROWS 
FETCH NEXT 125 ROWS ONLY

select count(*) from (SELECT p.* FROM     dbo.Persons p) as t
 
SET NOCOUNT ON

select LastName FROM (
SELECT 1, p.*
FROM     dbo.Persons p
ORDER BY 1 ASC
OFFSET  50 ROWS 
FETCH NEXT 200125 ROWS ONLY
) t

SELECT p.*
FROM     Persons p
ORDER BY 1 ASC
OFFSET  50 ROWS 
FETCH NEXT 125 ROWS ONLY


select 'ROW COUNT:' filter ,count(*) cnt from (SELECT p.*
FROM     Persons p) as t


select * from (
SELECT Item.*,
ROW_NUMBER() OVER (ORDER_BY LastName) AS row_number
FROM (SELECT p.*
FROM     Persons p) as Item) as t
WHERE row_number between 1 and 100

select * from (
SELECT Item.*, ROW_NUMBER() OVER (ORDER BY NewId())  row_number
FROM (SELECT p.*  FROM     Persons p) as Item) as t
WHERE row_number between 1 and 100

select row_number from ( SELECT Item.*,   CAST(ABS(CHECKSUM(NEWID())) % 10000000 AS bigint)  as  row_number
FROM (SELECT p.*
FROM     dbo.Persons p
) as Item) as t WHERE row_number between 0 and 65536

 CAST(ABS(CHECKSUM(NEWID())) % 10000000 AS bigint)

SELECT p.*
FROM     Persons p

select 'ROW COUNT:' filter ,count(*) cnt from (SELECT p.* FROM     dbo.Persons p ) as t
GO
END


BULK INSERT dbo.Persons_pipe2
FROM 'C:\Python27\ora_data_pipe\logs\20140902_154523\shard_0.data'
WITH
  (
    FORMATFILE = 'C:\Python27\ora_data_pipe\logs\20140902_154523\to_fmt.fmt'
  );

  
ALTER DATABASE test ADD FILEGROUP [Filegroup_2010]   
ALTER DATABASE test ADD FILEGROUP [Filegroup_2011] 
ALTER DATABASE test ADD FILEGROUP [Filegroup_2014] 
ALTER DATABASE test ADD FILEGROUP [Filegroup_2015] 
ALTER DATABASE test ADD FILEGROUP [Filegroup_2016] 


ALTER DATABASE test
  ADD FILE
  (NAME = N'data_2015',
  FILENAME = N'C:\Temp\sqlserver_ent_data\data_2015.ndf',
  SIZE = 10MB,
  MAXSIZE = 100MB,
  FILEGROWTH = 5MB)
  TO FILEGROUP [Filegroup_2015]  

  ALTER DATABASE test
  ADD FILE
  (NAME = N'data_2015',
  FILENAME = N'C:\Temp\sqlserver_data\data_2015.ndf',
  SIZE = 10MB,
  MAXSIZE = 100MB,
  FILEGROWTH = 5MB)
  TO FILEGROUP [Filegroup_2015]  

  ALTER DATABASE test
  ADD FILE
  (NAME = N'data_2016',
  FILENAME = N'C:\Temp\sqlserver_data\data_2016.ndf',
  SIZE = 10MB,
  MAXSIZE = 100MB,
  FILEGROWTH = 5MB)
  TO FILEGROUP [Filegroup_2016] 
  
  
CREATE PARTITION FUNCTION DateRange2016(DATETIME)  AS
  RANGE LEFT FOR VALUES 
  ('20101231 23:59:59.997',
  '20111231 23:59:59.997',
  '20141231 23:59:59.997',
  '20151231 23:59:59.997',
  '20161231 23:59:59.997')

CREATE PARTITION FUNCTION DateRangeF(DATETIME)  AS
  RANGE LEFT FOR VALUES 
  ('20101231 23:59:59.997',
  '20111231 23:59:59.997',
  '20141231 23:59:59.997',
  '20151231 23:59:59.997')

CREATE PARTITION SCHEME DateRange  AS
  PARTITION DateRangeF  TO 
  ([Filegroup_2010],
  [Filegroup_2011],
  [Filegroup_2014],
  [Filegroup_2015],
  [PRIMARY]  )


CREATE TABLE Persons_partitioned
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
) ON DateRange  (CreateDt)

select count(*) from Persons_partitioned;

SELECT * FROM dbo.Persons_partitioned
  WHERE $Partition.DateRangeF(CreateDt)=3

insert into Persons_partitioned values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',GETDATE());