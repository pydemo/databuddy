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
City2 timestamp
);

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',CURRENT_TIMESTAMP);


select * from Persons_pipe_datetime

insert into Persons_pipe_datetime select * from Persons_pipe_datetime

select 'ROW COUNT:' filter ,count(*) cnt from (SELECT * FROM (SELECT * FROM Persons_pipe_datetime LIMIT 1000) t) as t;