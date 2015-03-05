
	set serveroutput on echo on termout on feedback off timing off
	DECLARE
	c           NUMBER;
	d           NUMBER;
	col_cnt     INTEGER;
	f           BOOLEAN;
	rec_tab     DBMS_SQL.DESC_TAB;
	col_num    NUMBER;
	v_sql dbms_sql.varchar2a;
	v_sql_1 varchar2(32767);
	v_sql_2 varchar2(32767);
	v_sql_3 varchar2(32767);
	v_sql_4 varchar2(32767);
	v_type VARCHAR2(32):='';
	PROCEDURE print_rec(rec in DBMS_SQL.DESC_REC) IS
	BEGIN
	v_type:=CASE rec.col_type
				WHEN 1 THEN 'VARCHAR2'
				WHEN 12 THEN 'DATE'
				WHEN 2 THEN 'NUMBER'
				WHEN 180 THEN 'TIMESTAMP'
			ELSE ''||rec.col_type
			END;
	DBMS_OUTPUT.PUT_LINE(rec.col_name||':'||rec.col_name_len||':'||v_type);
	END;
	BEGIN
	v_sql(1):='select *  from Timestamp_test_from';
	v_sql(2):='';
	v_sql(3):='';
	v_sql(4):='';
	v_sql(5):='';
	c := DBMS_SQL.OPEN_CURSOR;
	DBMS_SQL.PARSE(c, v_sql,1,5,False, DBMS_SQL.NATIVE);
	d := DBMS_SQL.EXECUTE(c);
	DBMS_SQL.DESCRIBE_COLUMNS(c, col_cnt, rec_tab);
	/*
	* Following loop could simply be for j in 1..col_cnt loop.
	* Here we are simply illustrating some of the PL/SQL table
	* features.
	*/
	col_num := rec_tab.first;
	IF (col_num IS NOT NULL) THEN
	LOOP
	  print_rec(rec_tab(col_num));
	  col_num := rec_tab.next(col_num);
	  EXIT WHEN (col_num IS NULL);
	END LOOP;
	END IF;
	DBMS_SQL.CLOSE_CURSOR(c);
	END;
	/
	exit;

	