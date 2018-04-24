import odbc, sys, dbi
if 0:
	import wxversion
	import wxversion as wv
	wv.select("3.0")
import wx
#import common_utils as cu
#from wx.lib.pubsub import Publisher
from tc_lib import send
#blog= cu.blog

srv={'SMARTU1A':'mapswdbun1-vip.nam.nsroot.net'}
def printerr(err):
	print '#'*60
	print '#'*26,'ERROR!', '#'*26
	print '#'*60
	print err
	print '#'*60
	print '#'*60
	dlg = wx.MessageDialog(None,str(err),
						   'Connect error',
						   wx.OK | wx.ICON_INFORMATION
						   #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
						   )
	dlg.ShowModal()
	dlg.Destroy()
		
	
def query( sql, connect_as, pos=None, limit=100, caller=None):
	#global db
	print connect_as
	(user,db, pwd, host,port) = connect_as
	#(db,user)= ('MRR_BI','MRR_ETL_USER')
	assert sql, 'sql statement is not defined'
	assert db, 'Database is not set'
	assert user, 'User is not set'
	assert host, 'Host is not set'
	assert port, 'Port is not set'
	#if _db: db = _db
	#db1='MRR'
	#blog.log('Connecting to %s as %s ...' % (db, user),(0,0))
	print 'Connecting to %s as %s ...' % (db, user)
	#mapswdbun2-vip.nam.nsroot.net
	cs ='Driver={Microsoft ODBC for Oracle};SERVER=%s:%s/%s;UID=%s;PWD=%s;'  % (host,port, db,user,pwd)
	
	if 0:
		cs ='Driver={Microsoft ODBC for Oracle};SERVER=mapswdbdn1.nam.nsroot.net:11150/%s;UID=%s;PWD=%s;'  % (db,user,pwd)
		if db=='SMARTP_B':
			cs ='Driver={Microsoft ODBC for Oracle};SERVER=mapmwdbpn1-vip.nam.nsroot.net:11150/%s;UID=%s;PWD=%s;'  % (db,user,pwd)
		if db=='SMARTU1A':
			cs ='Driver={Microsoft ODBC for Oracle};SERVER=mapswdbun1-vip.nam.nsroot.net:11150/%s;UID=%s;PWD=%s;'  % (db,user,pwd)		
	print cs
	err=None
	rowcount=None
	headers=[]
	status=0
	out=[]
	#blog.log('Fetching %s...' % (caller[3:]),pos)
	try:
		odb = odbc.odbc(cs)
	except dbi.opError, e:
		print 'dbi.opError'
		status=1
		err=e
	except dbi.progError, e:
		print 'dbi.progError'
		status=1
		err=e
	except dbi.internalError, e:
		print 'dbi.internalError'
		status=1
		err=e
	except dbi.integrityError, e:
		print 'dbi.integrityError'
		status=1
		err=e
	except dbi.warnings, e:
		print 'dbi.warnings',e		
		#status=1
		#err=e
	except dbi.opError, e:
		print 'dbi.opError'
		status=1
		err=e
	else:
		#print 'Undefined odb = odbc.odbc(cs) error.'
		status=0
		#err=e		
		
	if err: 
		printerr(err)
		print status
		#blog.err(str(err),pos)
		#blog.err(str(err),pos)
		#Publisher().sendMessage( "go_up", pos )
		if pos:
			send("go_up", pos)
		
	else:
		cur = odb.cursor()
		#pprint(sql);
		print '='*60
		print (sql)
		print '-'*60
		status=0
		rowcount=0
		
		err=''
		i=1
		
		try:
			status=cur.execute ("%s" % sql) #'SELECT * FROM DUAL'
			
		except dbi.opError, e:
			print 'dbi.opError'
			status=1
			err=e
		except dbi.progError, e:
			print 'dbi.progError'
			status=1
			err=e
		except dbi.internalError, e:
			print 'dbi.internalError'
			status=1
			err=e
		except dbi.integrityError, e:
			print 'dbi.integrityError'
			status=1
			err=e
		except dbi.warnings, e:
			print 'dbi.warnings', e
			#status=1
			#err=e
		except dbi.opError, e:
			print 'dbi.opError'
			status=1
			err=e
		else:
			#print 'Undefined cur.execute() error.'
			status=0
			#err=e

			
		if err: 
			printerr(err)
			print status
			#blog.err(err,pos)
			
		else:
			headers=cur.description
			if headers:

				print headers
				print sql 
				#rs=cur.fetchone()
				#print rs
				#sys.exit(1)
				if 1 or rs:
					if not limit:
						if 0:
							while rs:
								rows=i 
								cols=len(rs)
								#print rs


								i+=1
								#print ''
								out.append(rs)
						rs=cur.fetchall()
						print 'fetched records: ',len(rs)
						#print (rs)
						#print rs[1]
						#sys.exit(1)
						out=rs
					else:	
						while rs and i<limit:
							rows=i 
							cols=len(rs)
							#print rs


							i+=1
							#print ''
							out.append(rs)
							rs=cur.fetchone()					
					rowcount=i-1
				else:
					err='0 records returned.'
			else:
				#del d
				print 'Success status= ',status
				print err
				print cur.error()
				print 
				if status>0:
					print 'Rows affected: %d' % status
	if not status:
		#blog.log('Fetched %d rows from %s.%s' % (len(out), user,db),pos)
		print 'Fetched %d rows from %s.%s' % (len(out), user,db)
	return (status, err, rowcount,headers, out)