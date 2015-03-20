create table wide_row_from as SELECT LPAD('x',4000,'x') col1, LPAD('x',4000,'x') col2, LPAD('x',4000,'x') col3 FROM DUAL;

drop table wide_row_to;
create table wide_row_to as select * from wide_row_from where 1=2;

drop table wide_row_to_4;
create table wide_row_to_4 as select col1,col2,col3,col4 from wide_row_from where 1=2;

create table wide_row_from_4 as select col1,col2,col3,col4 from wide_row_from;



drop table wide_row_from;
create table wide_row_from as SELECT LPAD('x',900,'x') col1, LPAD('x',900,'x') col2, LPAD('x',900,'x') col3, LPAD('x',900,'x') col4, 
LPAD('x',900,'x') col5, LPAD('x',900,'x') col6, LPAD('x',900,'x') col7, LPAD('x',900,'x') col8 FROM DUAL;

