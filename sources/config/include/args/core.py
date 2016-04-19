#__builtin__  pcore
pcore['copy_vector']={'short':'-w','long':'--copy_vector', 'type':str, 'default':'-', 'help':'Data copy direction.'}
pcore['pool_size']={'short':'-o','long':'--pool_size', 	'type':int, 'default':1, 'help':'Pool size.'}
pcore['num_of_shards']={'short':'-r','long':'--num_of_shards', 'type':int, 'default':1, 'help':'Number of shards.'}
pcore['field_term']= {'short': '-t','long':'--field_term', 'type':str, 'default':'|', 'help':'Field terminator.'}
pcore['lame_duck']={'short':'-l','long':'--lame_duck', 'type':int, 'default':0, 'help':'Limit rows (lame duck run).'}
pcore['keep_data_file']={'short':'-K','long':'--keep_data_file', 'type':int, 'default':0, 'help':'Keep data dump.'}
pcore['validate']={'short':'-V','long':'--validate', 'type':int, 'default':0, 'help':'Check if source and target objects exist.'}
pcore['truncate_target']={'short':'-U','long':'--truncate_target', 'type':int, 'default':0, 'help':'Truncate target table/partition/subpartition.'}
pcore['ask_to_truncate']={'short':'-E','long':'--ask_to_truncate', 'type':int, 'default':0, 'help':'Ask to truncate.'}
pcore['key_on_exit']={'short':'-X','long':'--key_on_exit', 'type':int, 'default':0, 'help':'Ask for an "Enter" key upon exit.'}
pcore['email_to']={'short':'-L','long':'--email_to', 'type':str, 'default':0, 'help':'Email job status.'}
pcore['log_dir']={'short':'-M','long':'--log_dir', 'type':str, 'default':0, 'help':'Log destination.'}
pcore['default_spool_dir']={'short':'-F','long':'--default_spool_dir', 'type':str, 'default':0, 'help':'Default data dump dir (default_spool_dir/job_name/timestamp).'}
pcore['job_name']={'short':'-B','long':'--job_name', 'type':str, 'default':0, 'help':'Job name (log_dir/job_name).'}
pcore['time_stamp']={'short':'-Y','long':'--time_stamp', 'type':str, 'default':0, 'help':'Timestamp (log_dir/job_name/timestamp).'}
pcore['column_buckets']={'short':'-0','long':'--column_buckets', 'type':int, 'default':0, 'help':'Wide row support.'}
pcore['job_pre_etl']={'short':'-1','long':'--job_pre_etl', 'type':str, 'default':'', 'help':'Path to job level pre-ETL Python script.'}
pcore['shard_pre_etl']={'short':'-2','long':'--shard_pre_etl', 'type':str, 'default':'', 'help':'Path to shard level pre-ETL Python script.'}
pcore['job_post_etl']={'short':'-3','long':'--job_post_etl', 'type':str, 'default':'', 'help':'Job''s post-etl script.'}
pcore['shard_post_etl']={'short':'-4','long':'--shard_post_etl', 'type':str, 'default':'', 'help':'Shard''s post-etl script.'}

pcore['loader_profile']={'short':'-C','long':'--loader_profile', 'type':str, 'default':'', 'help':'SQL*Loader profile (user defined).'}
pcore['host_map']={'short':'-5','long':'--host_map', 'type':str, 'default':'', 'help':'Host-to-shard map.'}
pcore['spool_type']={'short':'-6','long':'--spool_type', 'type':str, 'default':'csv', 'help':'Spool file type (CSV or JSON).'}
pcore['debug_level']={'short':'-dbg','long':'--debug_level', 'type':str, 'default':'', 'help':'QC Debug level.'}
pcore['status_pipe_id']={'short':'-spID','long':'--status_pipe_id', 'type':str, 'default':'0', 'help':'Status reporting pipe ID.'}
#params['core']['arg_8']={'short':'-8','long':'--arg_8', 'type':str, 'default':'', 'help':'Generic string argument 8.'}
#params['core']['arg_9']={'short':'-9','long':'--arg_9', 'type':str, 'default':'', 'help':'Generic string argument 9.'}


