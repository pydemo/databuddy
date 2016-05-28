(lp0
VCSV_TimestampFile_to_ORA12C_Table
p1
a(lp2
S'CSV'
p3
aS'ORA12C'
p4
aaVCSV_TimestampFile.ORA12C_Table
p5
a(lp6
(dp7
S'lame_duck'
p8
(lp9
S'-l'
p10
aS'--lame_duck'
p11
aV0
p12
aS'Limit rows (lame duck run).'
p13
asVfield_term
p14
(lp15
S'-t'
p16
aS'--field_term'
p17
aV,
p18
aS'Field terminator.'
p19
asS'num_of_shards'
p20
(lp21
S'-r'
p22
aS'--num_of_shards'
p23
aI1
aS'Number of shards.'
p24
asS'loader_profile'
p25
(lp26
S'-C'
p27
aS'--loader_profile'
p28
aVC:\u005cUsers\u005calex_buz\u005cDocuments\u005cGitHub\u005cDataBuddy\u005csources\u005csessions\u005cMy_Sessions\u005cCSV_TimestampFile_to_ORA12C_Table\u005csqlloader.py
p29
aS'SQL*Loader profile (user defined).'
p30
asS'debug_level'
p31
(lp32
S'-dbg'
p33
aS'--debug_level'
p34
aV1
p35
aS'QC Debug level.'
p36
asS'copy_vector'
p37
(lp38
S'-w'
p39
aS'--copy_vector'
p40
aS'CSV-ORA12C'
p41
aS'Data copy direction.'
p42
asS'keep_data_file'
p43
(lp44
S'-K'
p45
aS'--keep_data_file'
p46
aI1
aS'Keep data dump.'
p47
asS'time_stamp'
p48
(lp49
S'-Y'
p50
aS'--time_stamp'
p51
aV20160419_154424_231000
p52
aS'Timestamp (log_dir/job_name/timestamp).'
p53
asS'log_dir'
p54
(lp55
S'-M'
p56
aS'--log_dir'
p57
aS'C:\\Temp\\qc_log'
p58
aS'Log destination.'
p59
asS'pool_size'
p60
(lp61
S'-ps'
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
asS'host_map'
p71
(lp72
S'-5'
p73
aS'--host_map'
p74
aVC:\u005cUsers\u005calex_buz\u005cDocuments\u005cGitHub\u005cDataBuddy\u005csources\u005csessions\u005cMy_Sessions\u005cCSV_TimestampFile_to_ORA12C_Table\u005chost_map\u005chost_map.py
p75
aS'Host-to-shard map.'
p76
asa(dp77
S'shard_size_kb'
p78
(lp79
S'-y'
p80
aS'--shard_size_kb'
p81
aV10000000
p82
aS'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'
p83
asS'input_files'
p84
(lp85
S'-i'
p86
aS'--input_files'
p87
aVC:\u005cPython35-32\u005cPROJECTS\u005ccsv2redshift\u005cCrime.csv
p88
aS'Input CSV file(s).'
p89
asa(dp90
S'to_db_name'
p91
(lp92
S'-d'
p93
aS'--to_db_name'
p94
aVorcl12
p95
aS'Oracle 12c database.'
p96
asVskip_rows
p97
(lp98
S'-k'
p99
aS'--skip_rows'
p100
aV1
p101
aS'Number of rows to skip in input file.'
p102
asS'to_passwd'
p103
(lp104
S'-p'
p105
aS'--to_passwd'
p106
aVscott
p107
aS'Oracle 12c user password.'
p108
asS'nls_timestamp_format'
p109
(lp110
S'-m'
p111
aS'--nls_timestamp_format'
p112
aVMM/DD/YYYY HH12:MI:SS PM
p113
aS'nls_timestamp_format for target.'
p114
asS'to_user'
p115
(lp116
S'-u'
p117
aS'--to_user'
p118
aVc##test
p119
aS'Target Oracle 12c db user.'
p120
asS'nls_date_format'
p121
(lp122
S'-e'
p123
aS'--nls_date_format'
p124
aVMM/DD/YYYY HH12:MI:SS
p125
aS'nls_date_format for target.'
p126
asS'nls_timestamp_tz_format'
p127
(lp128
S'-O'
p129
aS'--nls_timestamp_tz_format'
p130
aVMM/DD/YYYY HH12:MI:SS.FF2 TZH:TZM
p131
aS'nls_timestamp_tz_format for target.'
p132
asS'to_table'
p133
(lp134
S'-a'
p135
aS'--to_table'
p136
aVc##test.crime_test
p137
aS'To Oracle table.'
p138
asaa.