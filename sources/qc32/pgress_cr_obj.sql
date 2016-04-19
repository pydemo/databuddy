'C:\Program Files\PostgreSQL\9.4\bin' -U postgres -d postgres -h localhost

drop table Persons_pipe_datetime_1

CREATE TABLE Date_test
(
PersonID SERIAL,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt date NOT NULL DEFAULT now()
);


CREATE TABLE Timestamp_test
(
PersonID SERIAL,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt timestamp NOT NULL DEFAULT now()
);

insert into Timestamp_test (LastName,FirstName,Address,City ,PersonID2,LastName2,FirstName2,Address2,CreateDt) values ('--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

CREATE TABLE Timezone_test
(
PersonID SERIAL,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt timestamptz NOT NULL DEFAULT now()
);


insert into Persons_pipe_datetime (LastName,FirstName,Address,City ,PersonID2,LastName2,FirstName2,Address2,CreateDt) values ('--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());


	
	
insert into Timezone_test_from values('Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());	
	
SELECT
    nmsp_parent.nspname AS parent_schema,
    parent.relname      AS parent,
    nmsp_child.nspname  AS child,
    child.relname       AS child_schema
FROM pg_inherits
    JOIN pg_class parent        ON pg_inherits.inhparent = parent.oid
    JOIN pg_class child         ON pg_inherits.inhrelid   = child.oid
    JOIN pg_namespace nmsp_parent   ON nmsp_parent.oid  = parent.relnamespace
    JOIN pg_namespace nmsp_child    ON nmsp_child.oid   = child.relnamespace

SELECT
    nmsp_parent.nspname     AS parent_schema,
    parent.relname          AS parent,
    COUNT(*)
FROM pg_inherits
    JOIN pg_class parent        ON pg_inherits.inhparent = parent.oid
    JOIN pg_class child     ON pg_inherits.inhrelid   = child.oid
    JOIN pg_namespace nmsp_parent   ON nmsp_parent.oid  = parent.relnamespace
    JOIN pg_namespace nmsp_child    ON nmsp_child.oid   = child.relnamespace
GROUP BY
    parent_schema,
    parent;

SELECT tableoid::regclass AS source, *
FROM   my_schema.foo
WHERE <some_condition>;

SELECT count(*) AS partitions
FROM   pg_inherits i
WHERE  i.inhparent = 'my_schema.my_parent_tbl'::regclass;

http://stackoverflow.com/questions/12902072/find-out-which-schema-based-on-table-values/12902441#12902441

SELECT
    nmsp_parent.nspname     AS parent_schema,
    parent.relname          AS parent,
    COUNT(*)
FROM pg_inherits
    JOIN pg_class parent        ON pg_inherits.inhparent = parent.oid
    JOIN pg_class child     ON pg_inherits.inhrelid   = child.oid
    JOIN pg_namespace nmsp_parent   ON nmsp_parent.oid  = parent.relnamespace
    JOIN pg_namespace nmsp_child    ON nmsp_child.oid   = child.relnamespace
GROUP BY
    parent_schema,
    parent;


CREATE TABLE product (title text);

insert into product values('title0')

CREATE TABLE product_a (product_id serial PRIMARY KEY, col2 text)
INHERITS (product);

insert into product_a values('title',1,'col2')

CREATE TABLE product_b (product_id serial PRIMARY KEY, col2 text, col3 text)
INHERITS (product);

insert into product_b values('title2',1,'col2','col3')

SELECT title, tableoid::regclass::text AS source
FROM   product
WHERE  title ILIKE '%test%';

select * from product

SELECT *
FROM   product
where  tableoid::regclass::text ='product_a'

SELECT n.nspname,t.tableoid
FROM   product   t
JOIN   pg_class     c ON c.oid = t.tableoid
JOIN   pg_namespace n ON c.relnamespace = n.oid
WHERE t.tableoid=16411
--WHERE  t.id = 2;

SELECT t.*
FROM   product   t
JOIN   pg_class     c ON c.oid = t.tableoid
JOIN   pg_namespace n ON c.relnamespace = n.oid
WHERE t.tableoid=16411


CREATE SCHEMA master;  -- no access of others ..

CREATE SEQUENCE master.myseq;  -- global sequence to have globally unique id
CREATE table master.tbl (
  id int primary key DEFAULT nextval('master.myseq')
, foo text);

CREATE SCHEMA x;
CREATE table x.tbl() INHERITS (master.tbl);
INSERT INTO  x.tbl(foo) VALUES ('x');

CREATE SCHEMA y;
CREATE table y.tbl() INHERITS (master.tbl);
INSERT INTO  y.tbl(foo) VALUES ('y');


SELECT * FROM x.tbl;  -- returns 'x'
SELECT * FROM y.tbl;  -- returns 'y'
SELECT * FROM master.tbl;  -- returns 'x' and 'y' <-- !!

SELECT *,tableoid::regclass::text
FROM   master.tbl
where  tableoid::regclass::text ='y.tbl'

SELECT n.nspname 
FROM   master.tbl   t
JOIN   pg_class     c ON c.oid = t.tableoid
JOIN   pg_namespace n ON c.relnamespace = n.oid
WHERE  t.id = 2;

CREATE TABLE master.product (title text);

CREATE TABLE a.product (product_id serial PRIMARY KEY, col2 text)
INHERITS (master.product);

CREATE TABLE b.product (product_id serial PRIMARY KEY, col2 text, col3 text)
INHERITS (master.product);

CREATE SEQUENCE persons_seq;  -- global sequence to have globally unique id
CREATE table master.tbl (
  id int primary key DEFAULT nextval('master.myseq')
, foo text);

CREATE TABLE Persons_partitioned
(
PersonID SERIAL,
LastName varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255),
PersonID2 int,
LastName2 varchar(255),
FirstName2 varchar(255),
Address2 varchar(255),
CreateDt timestamptz NOT NULL DEFAULT now()
);

insert into Persons_partitioned (LastName,FirstName,Address,City ,PersonID2,LastName2,FirstName2,Address2,CreateDt) values ('--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

select * from Persons_partitioned
where  tableoid::regclass::text ='persons_partitioned_2014'


CREATE TABLE Persons_partitioned_2013 (
    CHECK ( CreateDt >= DATE '2013-01-01' AND CreateDt < DATE '2014-01-01' )
) INHERITS (Persons_partitioned);

CREATE TABLE Persons_partitioned_2014 (
    CHECK ( CreateDt >= DATE '2014-01-01' AND CreateDt < DATE '2015-01-01' )
) INHERITS (Persons_partitioned);

CREATE TABLE Persons_partitioned_2015 (
    CHECK ( CreateDt >= DATE '2015-01-01' AND CreateDt < DATE '2016-01-01' )
) INHERITS (Persons_partitioned);

CREATE INDEX Persons_partitioned_2013_CreateDt ON Persons_partitioned_2013 (CreateDt);
CREATE INDEX Persons_partitioned_2014_CreateDt ON Persons_partitioned_2014 (CreateDt);
CREATE INDEX Persons_partitioned_2015_CreateDt ON Persons_partitioned_2015 (CreateDt);

CREATE OR REPLACE FUNCTION persons_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF ( NEW.CreateDt >= DATE '2013-01-01' AND
         NEW.CreateDt < DATE '2014-01-01' ) THEN
        INSERT INTO Persons_partitioned_2013 VALUES (NEW.*);
    ELSIF ( NEW.CreateDt >= DATE '2014-01-01' AND
            NEW.CreateDt < DATE '2015-01-01' ) THEN
        INSERT INTO Persons_partitioned_2014 VALUES (NEW.*);
    ELSIF ( NEW.CreateDt >= DATE '2015-01-01' AND
            NEW.CreateDt < DATE '2016-01-01' ) THEN
        INSERT INTO Persons_partitioned_2015 VALUES (NEW.*);
    ELSE
        RAISE EXCEPTION 'Date out of range.  Fix the persons_insert_trigger() function!';
    END IF;
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

drop insert_persons_trigger;

CREATE TRIGGER insert_persons_trigger
    BEFORE INSERT ON Persons_partitioned
    FOR EACH ROW EXECUTE PROCEDURE persons_insert_trigger();





CREATE TABLE Persons_subpartitioned
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
CreateDt timestamptz NOT NULL DEFAULT now()
);

insert into Persons_subpartitioned values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

select * from Persons_subpartitioned 
where  tableoid::regclass::text='persons_partition_2014_2'

select * from Persons_subpartitioned 
where  tableoid::regclass in ('public.persons_partition_2014_2'::regclass,'public.persons_partition_2014_1'::regclass)


 'public.persons_partitioned'::regclass
 
select tableoid from Persons_subpartitioned 
--where  tableoid::regclass::text 'persons_partitioned_2014'

SELECT n.nspname 
FROM   master.tbl   t
JOIN   pg_class     c ON c.oid = t.tableoid
JOIN   pg_namespace n ON c.relnamespace = n.oid
WHERE  t.id = 2;


SELECT
    nmsp_parent.nspname AS parent_schema,
    parent.relname      AS parent,
    nmsp_child.nspname  AS child,
    child.relname       AS child_schema
FROM pg_inherits
    JOIN pg_class parent        ON pg_inherits.inhparent = parent.oid
    JOIN pg_class child         ON pg_inherits.inhrelid   = child.oid
    JOIN pg_namespace nmsp_parent   ON nmsp_parent.oid  = parent.relnamespace
    JOIN pg_namespace nmsp_child    ON nmsp_child.oid   = child.relnamespace

SELECT
    nmsp_parent.nspname     AS parent_schema,
    parent.relname          AS parent,
    COUNT(*)
FROM pg_inherits
    JOIN pg_class parent        ON pg_inherits.inhparent = parent.oid
    JOIN pg_class child     ON pg_inherits.inhrelid   = child.oid
    JOIN pg_namespace nmsp_parent   ON nmsp_parent.oid  = parent.relnamespace
    JOIN pg_namespace nmsp_child    ON nmsp_child.oid   = child.relnamespace
GROUP BY
    parent_schema,
    parent;

SELECT tableoid::regclass AS source, *
FROM   my_schema.foo
WHERE <some_condition>;

SELECT count(*) AS partitions
FROM   pg_inherits i
WHERE  i.inhparent = 'public.persons_partitioned'::regclass;

SELECT *,'public.persons_partitioned'::regclass
FROM   pg_inherits i
WHERE  i.inhparent = 'public.persons_partitioned'::regclass;

drop table Persons_partition_1

CREATE TABLE Persons_partition_2014 (
    CHECK ( CreateDt >= DATE '2014-01-01' AND CreateDt < DATE '2015-01-01' )
) INHERITS (Persons_subpartitioned);

drop table Persons_partition_1;
drop table Persons_partition_2;
drop table Persons_partition_3;

CREATE TABLE Persons_partition_2014_1 (
    CHECK (PersonID=1 )
) INHERITS (Persons_partition_2014);

CREATE TABLE Persons_partition_2014_2 (
    CHECK (PersonID=2 )
) INHERITS (Persons_partition_2014);

CREATE TABLE Persons_partition_2014_3 (
    CHECK (PersonID=3 )
) INHERITS (Persons_partition_2014);


CREATE TABLE Persons_partition_2015 (
    CHECK ( CreateDt >= DATE '2015-01-01' AND CreateDt < DATE '2016-01-01' )
) INHERITS (Persons_subpartitioned);



CREATE TABLE Persons_partition_2015_1 (
    CHECK (PersonID=1 )
) INHERITS (Persons_partition_2015);

CREATE TABLE Persons_partition_2015_2 (
    CHECK (PersonID=2 )
) INHERITS (Persons_partition_2015);

CREATE TABLE Persons_partition_2015_3 (
    CHECK (PersonID=3 )
) INHERITS (Persons_partition_2015);


CREATE TABLE Persons_partitioned_2014 (
    CHECK ( CreateDt >= DATE '2014-01-01' AND CreateDt < DATE '2015-01-01' )
) INHERITS (Persons_partitioned);

CREATE TABLE Persons_partitioned_2015 (
    CHECK ( CreateDt >= DATE '2015-01-01' AND CreateDt < DATE '2016-01-01' )
) INHERITS (Persons_partitioned);


CREATE INDEX Persons_partition_2014_CreateDt ON Persons_partition_2014 (CreateDt);

CREATE INDEX Persons_partition_2014_1_PersonID ON Persons_partition_2014_1 (PersonID);
CREATE INDEX Persons_partition_2014_2_PersonID ON Persons_partition_2014_2 (PersonID);
CREATE INDEX Persons_partition_2014_3_PersonID ON Persons_partition_2014_3 (PersonID);

CREATE INDEX Persons_partition_2015_CreateDt ON Persons_partition_2015 (CreateDt);

CREATE INDEX Persons_partition_2015_1_PersonID ON Persons_partition_2015_1 (PersonID);
CREATE INDEX Persons_partition_2015_2_PersonID ON Persons_partition_2015_2 (PersonID);
CREATE INDEX Persons_partition_2015_3_PersonID ON Persons_partition_2015_3 (PersonID);



CREATE INDEX Persons_partition_2015_CreateDt ON Persons_partition_2015 (CreateDt);



CREATE OR REPLACE FUNCTION subp_persons_insert_trigger()
RETURNS TRIGGER AS $$
BEGIN
    IF ( NEW.CreateDt >= DATE '2014-01-01' AND
         NEW.CreateDt < DATE '2015-01-01' ) THEN
         IF (NEW.PersonID=1) THEN
	    INSERT INTO Persons_partition_2014_1 VALUES (NEW.*);
	 ELSIF (NEW.PersonID=2) THEN
	    INSERT INTO Persons_partition_2014_2 VALUES (NEW.*);
	 ELSIF (NEW.PersonID=3) THEN
	    INSERT INTO Persons_partition_2014_3 VALUES (NEW.*);
	 ELSE
	   RAISE EXCEPTION 'PersonID out of range.  Fix the subp_persons_insert_trigger() function!';
	 END IF;       
    ELSIF ( NEW.CreateDt >= DATE '2015-01-01' AND
         NEW.CreateDt < DATE '2016-01-01' ) THEN
         IF (NEW.PersonID=1) THEN
	    INSERT INTO Persons_partition_2015_1 VALUES (NEW.*);
	 ELSIF (NEW.PersonID=2) THEN
	    INSERT INTO Persons_partition_2015_2 VALUES (NEW.*);
	 ELSIF (NEW.PersonID=3) THEN
	    INSERT INTO Persons_partition_2015_3 VALUES (NEW.*);
	 ELSE
	   RAISE EXCEPTION 'PersonID out of range.  Fix the subp_persons_insert_trigger() function!';
	 END IF;
    ELSE
        RAISE EXCEPTION 'CreateDt out of range.  Fix the persons_insert_trigger() function!';
    END IF;
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

drop trigger insert_subp_persons_trigger on Persons_subpartitioned

CREATE TRIGGER insert_subp_persons_trigger
    BEFORE INSERT ON Persons_subpartitioned
    FOR EACH ROW EXECUTE PROCEDURE subp_persons_insert_trigger();

truncate table Persons_partitioned.


    
insert into Persons_partitioned values (nextval('persons_seq'),'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

select * from Persons_partitioned
where  tableoid::regclass::text ='persons_partitioned_2014'
	
	'C:\Program Files\PostgreSQL\9.3\scripts\runpsql.bat'
	
insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',now());

'C:\Program Files\MariaDB 10.0\bin\mysql.exe' '--defaults-file=C:\Program Files\MariaDB 10.0\data\my.ini'

select * from information_schema.TABLES where TABLE_SCHEMA = 'test' and TABLE_NA='Persons_partitioned' \G

select table_schema, table_name, table_type from information_schema.TABLES;


select table_schema, table_name, table_type from information_schema.PARTITIONS where TABLE_SCHEMA = 'test' and TABLE_NA='Persons_partitioned' ;

select TABLE_SCHEMA,TABLE_NAME, PARTITION_NAME from information_schema.PARTITIONS  where TABLE_SCHEMA = 'test' and TABLE_NAME='Persons_partitioned' and partition_name='rx201411' \G;

SELECT * FROM     Persons_pipe_datetime LIMIT 20;


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

CREATE TABLE Persons_sub_partitioned_2
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
FIELDS OPTIONALLY ENCLOSED BY ''' TERMINATED BY '|'
LINES TERMINATED BY '\n';

LOAD DATA LOCAL  INFILE 'C:\\Python27\\data_mule_mysql\\mysql_shard_0.data' INTO TABLE Persons_pipe_datetime
FIELDS OPTIONALLY ENCLOSED BY ''' TERMINATED BY '|'
LINES TERMINATED BY '
';

LOAD DATA LOCAL  INFILE 'C:\\Python27\\data_mule_mysql\\mysql_shard_0.data' INTO TABLE Persons_pipe_datetime FIELDS OPTIONALLY ENCLOSED BY ''' TERMINATED BY '|' LINES TERMINATED BY '\n';