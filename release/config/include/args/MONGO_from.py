#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['json_query']={'short':'-jsonq','long':'--json_query', 'type':str, 'default':None, 'help':'Inline %s JSON qry.'  % dbs[dbkey]}
pfrom[dbkey]['json_query_file']={'short':'-q','long':'--json_query_file', 'type':str, 'default':None, 'help':'Input file with %s JSON query file.'  % dbs[dbkey]}
pfrom[dbkey]['json_query_dir']={'short':'-Q','long':'--json_query_dir', 'type':str, 'default':None, 'help':'Input dir with %s JSON query files.'  % dbs[dbkey]}
pfrom[dbkey]['from_collection']=  {'short':'-c','long':'--from_collection', 	'type':str, 'default':None, 'help':'From collection.'}
pfrom[dbkey]['from_column_names']=  {'short':'-P','long':'--from_column_names', 	'type':str, 'default':None, 'help':'From column list.'}
pfrom[dbkey]['from_user']= {'short':'-j','long':'--from_user', 	'type':str, 'default':None, 'help':'%s source user.' % dbs[dbkey]}
pfrom[dbkey]['from_passwd']={'short':'-x','long':'--from_passwd', 'type':str, 'default':None, 'help':'%s source user password.' % dbs[dbkey]}			
pfrom[dbkey]['from_db_name']={'short':'-b','long':'--from_db_name', 'type':str, 'default':None, 'help':'%s source database.' % dbs[dbkey]}			
pfrom[dbkey]['from_db_server']={'short':'-n','long':'--from_db_server', 'type':str, 'default':None, 'help':'%s source instance name.' % dbs[dbkey]}
pfrom[dbkey]['from_db_port']={'short':'-z','long':'--from_db_port', 'type':str, 'default':None, 'help':'%s source database port.' % dbs[dbkey]}	
pfrom[dbkey]['header']={'short':'-A','long':'--header', 'type':int, 'default':1, 'help':'Include header to %s extract.' % dbs[dbkey]}	
pfrom[dbkey]['from_skip_rows']= {'short':'-S','long':'--from_skip_rows', 	'type':int, 'default':0, 'help':'Number of rows tto skip in source % stream.'  % dbs[dbkey]}

