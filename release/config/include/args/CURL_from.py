#__builtin__  pfrom, dbkey, dbs
pfrom[dbkey]['output']={'short':'-o','long':'--output', 'type':str, 'default':None, 'help':'Write output to <file> instead of stdout.'  }
pfrom[dbkey]['url']={'short':'-url','long':'--url', 'type':str, 'default':None, 'help':'URL to work with.'  }
pfrom[dbkey]['url_list']={'short':'-urls','long':'--url_list', 'type':str, 'default':None, 'help':'List of input URLs.'  }
pfrom[dbkey]['url_files']={'short':'-urlfiles','long':'--url_files', 'type':str, 'default':None, 'help':'Coma separated list of input files containing URLs.'  }
pfrom[dbkey]['url_dirs']={'short':'-urldirs','long':'--url_dirs', 'type':str, 'default':None, 'help':'Coma separated list of input dirs of files containing URLs.'  }
