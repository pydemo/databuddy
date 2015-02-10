SELECT 'TABLE_INFO='||PARTITIONED||':'||TEMPORARY||':'||STATUS info from ALL_TABLES where UPPER(OWNER||'.'||TABLE_NAME)=UPPER('SCOTT.Partitioned_test_from');
exit;
