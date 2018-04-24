#__builtin__  pto, dbkey, dbs
pto[dbkey]['to_user']={'short':'-u','long':'--to_user', 'type':str, 'default':None, 'help':('Target %s db user.' % dbs[dbkey])}
pto[dbkey]['to_passwd']= {'short':'-p','long':'--to_passwd', 'type':str, 'default':None, 'help':'%s user password.' % dbs[dbkey]}
pto[dbkey]['to_db_name']={'short':'-d','long':'--to_db_name', 'type':str, 'default':None, 'help':'%s database.' % dbs[dbkey]}
pto[dbkey]['to_db_server']= {'short': '-s','long':'--to_db_server', 'type':str, 'default':None, 'help':'%s instance name.' % dbs[dbkey]}
pto[dbkey]['to_table']={'short':'-a','long':'--to_table', 'type':str, 'default':None, 'help':'To table.'}
pto[dbkey]['target_client_home']={'short':'-Z','long':'--target_client_home', 'type':str, 'default':None, 'help':'Path to %s client home bin dir.' %  dbs[dbkey]}
pto[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}

