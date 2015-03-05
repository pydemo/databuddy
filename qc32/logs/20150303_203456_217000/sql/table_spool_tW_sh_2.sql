SET TAB OFF timing off head on line 32767 pages 0 newpage 0 echo off feedback on define off feed off arraysize 5000



set feedback on
 
SELECT ID ||'|'||
 TITLE ||'|'||
 ISIN ||'|'||
 COUNTRY ||'|'||
 DESCRIPTION ||'|'||
 SECURITYTYPE ||'|'||
 CREATED||'' FROM (SELECT * FROM (SELECT * FROM SCOTT.Partitioned_test_from  PARTITION(part_15)  WHERE ROWID BETWEEN 'AAASzaAAEAAAASYAAA' AND 'AAASzaAAEAAAASfABk')  WHERE ROWNUM<11)   ;
exit;
