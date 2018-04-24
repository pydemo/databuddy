drop table Persons_pipe_datetime_1


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
City2  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

select count(*) from Persons_pipe_datetime_1;

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',CURRENT_TIMESTAMP);