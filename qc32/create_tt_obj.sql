C:\Program Files (x86)\TimesTen\tt1122_64\bin>

ttIsql.exe "DSN=my_ttdb;UID=TERRY;PWD=secret";

"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttIsql.exe" "DSN=my_ttdb;UID=TERRY;PWD=secret";


ttBulkCp.exe -i -s "|" -dformat "YYYY-MM-DD"  -tsformat "YYYY-MM-DD HH24:MI:SS.FF" -Q 0 -connstr "DSN=my_ttdb" Persons_pipe_datetime "C:\\Python27\\data_mule_tt\\shard_0.data"


ttBulkCp.exe -i -s "|" -dformat "YYYY-MM-DD"  -tsformat "YYYY-MM-DD HH24.MI.SS.FF" -Q 0 -connstr "DSN=my_ttdb" Persons_pipe_datetime "C:\\Python27\\data_mule_tt\\shard_0.data"

--C:\Program Files (x86)\TimesTen\tt1122_64\bin

ttBulkCp.exe -Cnone  -o -s "|" -dformat "YYYY-MM-DD"  -tsformat "YYYY-MM-DD HH24.MI.SS.FF" -Q 0 -connstr "DSN=my_ttdb" Persons_pipe_datetime "C:\\Python27\\data_mule_tt\\shard_0tt.data"

21/21 rows copied

"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttIsql.exe" -connstr ""DSN=my_ttdb;UID=TERRY;PWD=secret"" -f "C:\Python27\data_mule_tt\logs\20141005_171220\sql\source_row_count.sql"

"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttBulkCp.exe" -Cnone -o -s "|" -dformat "YYYY-MM-DD" -tsformat "YYYY-MM-DD HH24.MI.SS.FF" -Q 0 -connstr "DSN=my_ttdb;UID=TERRY;PWD=secret" TERRY.Persons_pipe_datetime "C:\Python27\data_mule_tt\logs\20141005_175236\shard_0.data"
"C:\Program Files (x86)\TimesTen\tt1122_64\bin\ttBulkCp.exe" -Cnone -o -s "|" -dformat "YYYY-MM-DD" -tsformat "YYYY-MM-DD HH24.MI.SS.FF" -Q 0 -connstr "DSN=my_ttdb;UID=TERRY;PWD=secret" TERRY.Persons_pipe_datetime "C:\Python27\data_mule_tt\logs\20141005_175952\shard_0.data"


CREATE TABLE Persons_pipe_datetime
(
PersonID int,
LastName varchar2(255), 
FirstName varchar2(255),
Address varchar2(255),
City varchar2(255),
PersonID2 int,
LastName2 varchar2(255),
FirstName2 varchar2(255),
Address2 varchar2(255),
City2 timestamp
);

CREATE TABLE Persons_pipe_datetime_1
(
PersonID int,
LastName varchar2(255), 
FirstName varchar2(255),
Address varchar2(255),
City varchar2(255),
PersonID2 int,
LastName2 varchar2(255),
FirstName2 varchar2(255),
Address2 varchar2(255),
City2 timestamp
);

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',TIMESTAMP '1998-10-28 12:00:00');

insert into Persons_pipe_datetime values (2,'--LastName','--FirstName','--Address','--City',2,'--LastName','--FirstName','--Address',systimestamp);