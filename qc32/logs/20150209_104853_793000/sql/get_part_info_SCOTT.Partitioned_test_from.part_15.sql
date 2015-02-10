SELECT 'ROW_COUNT:'||count(*) cnt from ALL_TAB_PARTITIONS where UPPER(TABLE_OWNER||'.'||TABLE_NAME)=UPPER('SCOTT.Partitioned_test_from') AND UPPER(partition_name)=UPPER('part_15');
exit;
