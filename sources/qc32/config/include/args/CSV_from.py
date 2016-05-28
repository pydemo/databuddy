#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['input_files']={'short':'-i','long':'--input_files', 'type':str, 'default':None, 'help':'Input CSV file(s).'}
pfrom[dbkey]['input_dirs']={'short':'-I','long':'--input_dirs', 'type':str, 'default':None, 'help':'Input CSV directory.'}

pfrom[dbkey]['shard_size_kb']={'short':'-y','long':'--shard_size_kb', 'type':int, 'default':10, 'help':'Shard size in KBytes (to partition file and to estimate number of lines in input CSV file).'}				
