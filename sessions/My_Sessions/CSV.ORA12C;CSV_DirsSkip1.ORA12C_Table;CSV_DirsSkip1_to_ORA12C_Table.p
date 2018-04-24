(lp0
VCSV_DirsSkip1_to_ORA12C_Table
p1
a(lp2
S'CSV'
p3
aS'ORA12C'
p4
aaVCSV_DirsSkip1.ORA12C_Table
p5
a((dp6
S'num_of_shards'
p7
(S'-r'
p8
S'--num_of_shards'
p9
I1
S'Number of shards.'
p10
tp11
sS'loader_profile'
p12
(S'-C'
p13
S'--loader_profile'
p14
S'".\\config\\sqlloader.py"'
p15
S'SQL*Loader profile (user defined).'
p16
tp17
sS'debug_level'
p18
(S'-dbg'
p19
S'--debug_level'
p20
I1
S'QC Debug level.'
p21
tp22
sS'keep_data_file'
p23
(S'-K'
p24
S'--keep_data_file'
p25
I1
S'Keep data dump.'
p26
tp27
sS'lame_duck'
p28
(S'-l'
p29
S'--lame_duck'
p30
I10
S'Limit rows (lame duck run).'
p31
tp32
sS'field_term'
p33
(S'-t'
p34
S'--field_term'
p35
S'"|"'
p36
S'Field terminator.'
p37
tp38
sS'pool_size'
p39
(S'-ps'
p40
S'--pool_size'
p41
I1
S'Pool size.'
p42
tp43
sS'copy_vector'
p44
(S'-w'
p45
S'--copy_vector'
p46
S'CSV-ORA12C'
p47
S'Data copy direction.'
p48
tp49
sS'log_dir'
p50
(S'-M'
p51
S'--log_dir'
p52
S'C:\\Temp\\qc_log'
p53
S'Log destination.'
p54
tp55
sS'time_stamp'
p56
(S'-Y'
p57
S'--time_stamp'
p58
S'20160417_234312_947000'
p59
S'Timestamp (log_dir/job_name/timestamp).'
p60
tp61
sS'job_name'
p62
(S'-B'
p63
S'--job_name'
p64
S'qc_job'
p65
S'Job name (log_dir/job_name).'
p66
tp67
sS'host_map'
p68
(S'-5'
p69
S'--host_map'
p70
S'".\\config\\host_map\\host_map.py"'
p71
S'Host-to-shard map.'
p72
tp73
s(dp74
S'input_dirs'
p75
(S'-I'
p76
S'--input_dirs'
p77
S'.\\test\\v101\\data\\ora_data_dir_1,.\\test\\v101\\data\\ora_data_dir_2'
p78
S'Input CSV directory.'
p79
tp80
sS'skip_rows'
p81
(S'-k'
p82
S'--skip_rows'
p83
I1
S'Header size. Number of rows to skip in input file.'
p84
tp85
sS'shard_size_kb'
p86
(lp87
S'-y'
p88
aS'--shard_size_kb'
p89
aV10000000
p90
aS'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'
p91
as(dp92
S'to_db_name'
p93
(lp94
S'-d'
p95
aS'--to_db_name'
p96
aVorcl12
p97
aS'Oracle 12c database.'
p98
asS'to_passwd'
p99
(lp100
S'-p'
p101
aS'--to_passwd'
p102
aVscott
p103
aS'Oracle 12c user password.'
p104
asS'nls_timestamp_format'
p105
(lp106
S'-m'
p107
aS'--nls_timestamp_format'
p108
aVMM/DD/YYYY HH12:MI:SS PM
p109
aS'nls_timestamp_format for target.'
p110
asS'to_user'
p111
(lp112
S'-u'
p113
aS'--to_user'
p114
aVc##test
p115
aS'Target Oracle 12c db user.'
p116
asS'nls_date_format'
p117
(lp118
S'-e'
p119
aS'--nls_date_format'
p120
aVMM/DD/YYYY HH12:MI:SS
p121
aS'nls_date_format for target.'
p122
asS'nls_timestamp_tz_format'
p123
(lp124
S'-O'
p125
aS'--nls_timestamp_tz_format'
p126
aVMM/DD/YYYY HH12:MI:SS.FF2 TZH:TZM
p127
aS'nls_timestamp_tz_format for target.'
p128
asS'to_table'
p129
(lp130
S'-a'
p131
aS'--to_table'
p132
aVc##test.crime_test
p133
aS'To Oracle table.'
p134
astp135
a.