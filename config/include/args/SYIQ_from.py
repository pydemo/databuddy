#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['query_sql_file']={'short':'-q','long':'--query_sql_file', 'type':str, 'default':None, 'help':'Input file with %s query sql.'  % dbs[dbkey]}
pfrom[dbkey]['query_sql_dir']={'short':'-Q','long':'--query_sql_dir', 'type':str, 'default':None, 'help':'Input dir with %s query files sql.'  % dbs[dbkey]}
pfrom[dbkey]['from_table']=  {'short':'-c','long':'--from_table', 	'type':str, 'default':None, 'help':'From table.'}

pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
pfrom[dbkey]['source_client_home']={'short':'-z','long':'--source_client_home', 'type':str, 'default':None, 'help':'Path to %s client home.' % dbs[dbkey]}
pfrom[dbkey]['header']={'short':'-H','long':'--header', 'type':int, 'default':0, 'help':'Include header to %s extract.' % dbs[dbkey]}
