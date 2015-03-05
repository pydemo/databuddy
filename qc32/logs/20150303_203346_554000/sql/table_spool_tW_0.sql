SET TAB OFF timing off head on line 32767 pages 0 newpage 0 echo off feedback on define off feed off arraysize 5000



set feedback on
 
SELECT ID ||'|'||
 TITLE ||'|'||
 ISIN ||'|'||
 COUNTRY ||'|'||
 DESCRIPTION ||'|'||
 SECURITYTYPE ||'|'||
 TO_CHAR(CREATED,'YYYY-MM-DD HH24.MI.SS')||'' FROM (SELECT * FROM (SELECT * FROM SCOTT.Date_test_from ) )   ;
exit;
