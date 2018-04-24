#__builtin__  pto, dbkey, dbs
pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'Target %s instance name.' % dbs[dbkey]}
pto[dbkey]['to_db_port']= {'short': '-T','long':'--to_db_port', 'type':str, 'default':None, 'help':'Target %s port.' % dbs[dbkey]}
pto[dbkey]['to_collection']={'short':'-a','long':'--to_collection', 'type':str, 'default':None, 'help':'To table.'}
pto[dbkey]['to_column_names']={'short':'-Z','long':'--to_column_names', 'type':str, 'default':None, 'help':'To column list for %s.' %  dbs[dbkey]}
pto[dbkey]['upsert']= {'short':'-G','long':'--upsert', 	'type':int, 'default':0, 'help':'Upsert rows into %s.' %  dbs[dbkey]}
pto[dbkey]['numInsertionWorkers']= {'short':'-numIW','long':'--numInsertionWorkers', 	'type':int, 'default':1, 'help':'Upsert rows into %s.' %  dbs[dbkey]}
