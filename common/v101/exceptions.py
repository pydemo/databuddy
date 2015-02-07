class CopyVectorError(Exception):
	def __init__(self, copy_vector):

		# Call the base class constructor with the parameters it needs
		Exception.__init__(self, 'Unsupported copy vector %s' % copy_vector)

		# Now for your custom code...
		#self.errors = errors
		#print 'Unsupported copy vector %s' % copy_vector
class RowCountError(Exception):
	def __init__(self, rcnt):		
		# Call the base class constructor with the parameters it needs
		Exception.__init__(self, 'Cannot get row count.\n %s' % rcnt)		
class SqlCmdError(Exception):
	def __init__(self, ex):		
		# Call the base class constructor with the parameters it needs
		Exception.__init__(self, 'SQLCMD exception.\n %s' % ex)	