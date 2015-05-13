#__builtin__ args
import sys
from pprint import pprint
e=sys.exit
#
# Define your custom SQL*Loader config
#	
def get_load_config(db_loader_loc,shard_name, row_from, row_to,ctlfn,outfn, datadir):
	dpl_columnarrayrows=10000
	dpl_streamsize=500000
	dpl_readsize=200000
	if_dpl_parallel='TRUE'
	dpl_bindsize=200000
	dpl_skip_index_maintenance='TRUE'
	dpl_skip_unusable_indexes='TRUE'
	if_direct='TRUE'
	loader_errors=10
	ptn=''
	sptn=''
	loadConf=[db_loader_loc, 'control=%s' % ctlfn, 'userid=%s' % args.to_db,
	'DATA=%s' % outfn,
	'COLUMNARRAYROWS=%s' % dpl_columnarrayrows,
	'STREAMSIZE=%s' % dpl_streamsize,'READSIZE=%s' % dpl_readsize,
	'PARALLEL=%s' % if_dpl_parallel,
	'BINDSIZE=%s' % dpl_bindsize, 
	#'UNRECOVERABLE=Y', 
	'SKIP_INDEX_MAINTENANCE=%s' % dpl_skip_index_maintenance, 'SKIP_UNUSABLE_INDEXES=%s' % dpl_skip_unusable_indexes,
	'DIRECT=%s' % if_direct, 	
	'MULTITHREADING=TRUE', 
	#'EXTERNAL_TABLE=EXECUTE',
	'LOG=%s/sqlloader/%s%s_%s.log' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name), 
	'BAD=%s/sqlloader/%s%s_%s.bad' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name),
	'DISCARD=%s/sqlloader/%s%s_%s.dsc' % (datadir,args.to_table, "%s%s" % (ptn,sptn),shard_name),				
	'ERRORS=%s' % loader_errors]
	if row_from:
		loadConf.append('SKIP=%s' % (row_from-1))
	if row_to:
		loadConf.append('LOAD=%s' % (row_to-row_from))
		
	#pprint(loadConf)
	#e(0)
	
	return loadConf	
		
#e(0)