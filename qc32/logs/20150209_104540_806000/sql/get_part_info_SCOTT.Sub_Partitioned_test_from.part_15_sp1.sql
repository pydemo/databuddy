SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_SUBPARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('SCOTT.Sub_Partitioned_test_from') AND UPPER(subpartition_name)=UPPER('part_15_sp1');
exit;
