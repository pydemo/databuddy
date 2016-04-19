#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['input_files']={'short':'-i','long':'--input_files', 'type':str, 'default':None, 'help':'Input JSON file(s).'}
pfrom[dbkey]['input_dirs']={'short':'-I','long':'--input_dirs', 'type':str, 'default':None, 'help':'Input JSON directory.'}
pfrom[dbkey]['skip_rows']= {'short':'-k','long':'--skip_rows', 	'type':int, 'default':0, 'help':'Header size. Number of rows to skip in input file.'}
pfrom[dbkey]['shard_size_kb']={'short':'-y','long':'--shard_size_kb', 'type':int, 'default':10, 'help':'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'}				
