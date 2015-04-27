(lp0
Vee2
p1
a(lp2
S'ORA11G'
p3
ag3
aaVORA11G_QueryFile.ORA11G_Table_GetTabnameFromQuery_DeleteTargetRecs
p4
a(lp5
(dp6
S'job_pre_etl'
p7
(lp8
S'-1'
p9
aS'--job_pre_etl'
p10
aVC:\u005cUsers\u005calex_buz\u005csessions\u005cMy_Sessions\u005cee\u005cetl\u005cjob_pre_etl.py
p11
aS'Path to job level pre-ETL Python script.'
p12
asS'field_term'
p13
(lp14
S'-t'
p15
aS'--field_term'
p16
aS'"|"'
p17
aS'Field terminator.'
p18
asS'num_of_shards'
p19
(lp20
S'-r'
p21
aS'--num_of_shards'
p22
aI1
aS'Number of shards.'
p23
asS'loader_profile'
p24
(lp25
S'-C'
p26
aS'--loader_profile'
p27
aVC:\u005cUsers\u005calex_buz\u005csessions\u005cMy_Sessions\u005cee\u005cloader\u005csqlloader.yaml
p28
aS'SQL*Loader profile (user defined).'
p29
asS'copy_vector'
p30
(lp31
S'-w'
p32
aS'--copy_vector'
p33
aS'ora11g2ora11g'
p34
aS'Data copy direction.'
p35
asS'log_dir'
p36
(lp37
S'-M'
p38
aS'--log_dir'
p39
aS'C:\\Temp\\qc_log'
p40
aS'Log destination.'
p41
asS'default_spool_dir'
p42
(lp43
S'-F'
p44
aS'--default_spool_dir'
p45
aS'C:\\tmp\\TEST_default_spool'
p46
aS'Default data dump dir (default_spool_dir/job_name/timestamp).'
p47
asS'time_stamp'
p48
(lp49
S'-Y'
p50
aS'--time_stamp'
p51
aV20150414_140027_955000
p52
aS'Timestamp (log_dir/job_name/timestamp).'
p53
asS'host_map'
p54
(lp55
S'-5'
p56
aS'--host_map'
p57
aVC:\u005cUsers\u005calex_buz\u005csessions\u005cMy_Sessions\u005cee\u005chost_map.py
p58
aS'Host-to-shard map.'
p59
asS'pool_size'
p60
(lp61
S'-o'
p62
aS'--pool_size'
p63
aI1
aS'Pool size.'
p64
asS'job_name'
p65
(lp66
S'-B'
p67
aS'--job_name'
p68
aS'qc_job'
p69
aS'Job name (log_dir/job_name).'
p70
asS'keep_data_file'
p71
(lp72
S'-K'
p73
aS'--keep_data_file'
p74
aI1
aS'Keep data dump.'
p75
asa(dp76
S'query_sql_file'
p77
(lp78
S'-q'
p79
aS'--query_sql_file'
p80
aVC:\u005cPython27\u005cdata_migrator_1239_ddl\u005ctest\u005cv101\u005cquery\u005cquery_dir_ora_table_named\u005cSCOTT.TIMESTAMP_TEST_TO.1.sql
p81
aS'Input file with Oracle 11G query sql.'
p82
asS'from_db_name'
p83
(lp84
S'-b'
p85
aS'--from_db_name'
p86
aVorcl
p87
aS'Oracle 11G source database.'
p88
asS'nls_date_format'
p89
(lp90
S'-e'
p91
aS'--nls_date_format'
p92
aVYYYY-MM-DD HH24.MI.SS
p93
aS'nls_date_format for source.'
p94
asS'nls_timestamp_format'
p95
(lp96
S'-m'
p97
aS'--nls_timestamp_format'
p98
aVYYYY-MM-DD HH24.MI.SS.FF2
p99
aS'nls_timestamp_format for source.'
p100
asS'source_client_home'
p101
(lp102
S'-z'
p103
aS'--source_client_home'
p104
aVC:\u005capp\u005calex_buz\u005cproduct\u005c11.2.0\u005cdbhome_2\u005cBIN
p105
aS'Path to Oracle 11G client home.'
p106
asS'nls_timestamp_tz_format'
p107
(lp108
S'-O'
p109
aS'--nls_timestamp_tz_format'
p110
aVYYYY-MM-DD HH:MI:SS.FF2 TZH:TZM
p111
aS'nls_timestamp_tz_format for source.'
p112
asS'from_user'
p113
(lp114
S'-j'
p115
aS'--from_user'
p116
aVSCOTT
p117
aS'Oracle 11G source user.'
p118
asS'from_passwd'
p119
(lp120
S'-x'
p121
aS'--from_passwd'
p122
aS'dGlnZXIy'
p123
aS'Oracle 11G source user password.'
p124
asa(dp125
S'to_db_name'
p126
(lp127
S'-d'
p128
aS'--to_db_name'
p129
aVorcl_ol7
p130
aS'Oracle 11G database.'
p131
asS'target_client_home'
p132
(lp133
S'-Z'
p134
aS'--target_client_home'
p135
aVC:\u005capp\u005calex_buz\u005cproduct\u005c11.2.0\u005cdbhome_2\u005cBIN
p136
aS'Path to Oracle 11G client home bin dir.'
p137
asg89
(lp138
g91
ag92
aVYYYY-MM-DD HH24.MI.SS
p139
aS'nls_date_format for target.'
p140
asg95
(lp141
g97
ag98
aVYYYY-MM-DD HH24.MI.SS.FF2
p142
aS'nls_timestamp_format for target.'
p143
asS'to_user'
p144
(lp145
S'-u'
p146
aS'--to_user'
p147
aVSCOTT
p148
aS'Target Oracle 11G db user.'
p149
asS'to_passwd'
p150
(lp151
S'-p'
p152
aS'--to_passwd'
p153
aS'dGlnZXI='
p154
aS'Oracle 11G user password.'
p155
asg107
(lp156
g109
ag110
aVYYYY-MM-DD HH:MI:SS.FF2 TZH:TZM
p157
aS'nls_timestamp_tz_format for target.'
p158
asaa.