#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}
pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
pfrom[dbkey]['from_DSN_name']={'short':'-b','long':'--from_DSN_name', 'type':str, 'default':None, 'help':'Source server DSN for %s.' % dbs[dbkey]}			
pfrom[dbkey]['nls_date_format']={'short':'-e','long':'--nls_date_format', 'type':str, 'default':'YYYY-MM-DD', 'help':'nls_date_format for source.'}
pfrom[dbkey]['nls_timestamp_format']={'short':'-m','long':'--nls_timestamp_format', 'type':str, 'default':'YYYY-MM-DD HH24.MI.SS.FF', 'help':'nls_timestamp_format for source.'}
pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}