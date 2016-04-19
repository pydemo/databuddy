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
aVC:\u005cUsers\u005calex_buz\u005cDocuments\u005cGitHub\u005cDataBuddy\u005csessions\u005cMy_Sessions\u005cCSV_TimestampFile_to_ORA12C_Table\u005csqlloader.py
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
aI1
aS'QC Debug level.'
p35
asS'copy_vector'
p36
(lp37
S'-w'
p38
aS'--copy_vector'
p39
aS'CSV-ORA12C'
p40
aS'Data copy direction.'
p41
asS'keep_data_file'
p42
(lp43
S'-K'
p44
aS'--keep_data_file'
p45
aI1
aS'Keep data dump.'
p46
asS'time_stamp'
p47
(lp48
S'-Y'
p49
aS'--time_stamp'
p50
aV20160418_230953_903000
p51
aS'Timestamp (log_dir/job_name/timestamp).'
p52
asS'log_dir'
p53
(lp54
S'-M'
p55
aS'--log_dir'
p56
aS'C:\\Temp\\qc_log'
p57
aS'Log destination.'
p58
asS'pool_size'
p59
(lp60
S'-ps'
p61
aS'--pool_size'
p62
aI1
aS'Pool size.'
p63
asS'job_name'
p64
(lp65
S'-B'
p66
aS'--job_name'
p67
aS'qc_job'
p68
aS'Job name (log_dir/job_name).'
p69
asS'host_map'
p70
(lp71
S'-5'
p72
aS'--host_map'
p73
aVC:\u005cUsers\u005calex_buz\u005cDocuments\u005cGitHub\u005cDataBuddy\u005csessions\u005cMy_Sessions\u005cCSV_TimestampFile_to_ORA12C_Table\u005chost_map\u005chost_map.py
p74
aS'Host-to-shard map.'
p75
asa(dp76
S'shard_size_kb'
p77
(lp78
S'-y'
p79
aS'--shard_size_kb'
p80
aV10000000
p81
aS'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'
p82
asS'input_files'
p83
(lp84
S'-i'
p85
aS'--input_files'
p86
aVC:\u005cPython35-32\u005cPROJECTS\u005ccsv2redshift\u005cCrime.csv
p87
aS'Input CSV file(s).'
p88
asa(dp89
S'to_db_name'
p90
(lp91
S'-d'
p92
aS'--to_db_name'
p93
aVorcl12
p94
aS'Oracle 12c database.'
p95
asS'to_passwd'
p96
(lp97
S'-p'
p98
aS'--to_passwd'
p99
aVscott
p100
aS'Oracle 12c user password.'
p101
asS'nls_timestamp_format'
p102
(lp103
S'-m'
p104
aS'--nls_timestamp_format'
p105
aVMM/DD/YYYY HH12:MI:SS PM
p106
aS'nls_timestamp_format for target.'
p107
asS'to_user'
p108
(lp109
S'-u'
p110
aS'--to_user'
p111
aVc##test
p112
aS'Target Oracle 12c db user.'
p113
asS'nls_date_format'
p114
(lp115
S'-e'
p116
aS'--nls_date_format'
p117
aVMM/DD/YYYY HH12:MI:SS
p118
aS'nls_date_format for target.'
p119
asS'nls_timestamp_tz_format'
p120
(lp121
S'-O'
p122
aS'--nls_timestamp_tz_format'
p123
aVMM/DD/YYYY HH12:MI:SS.FF2 TZH:TZM
p124
aS'nls_timestamp_tz_format for target.'
p125
asS'to_table'
p126
(lp127
S'-a'
p128
aS'--to_table'
p129
aVc##test.crime_test
p130
aS'To Oracle table.'
p131
asaa.