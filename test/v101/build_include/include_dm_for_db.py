import sys
from pprint import pprint
e=sys.exit
#_to='3'
#print appname
def getAppTitle(for_db, apptitle, dbs):
	return '%s for %s' % (apptitle, dbs[for_db[0]])
def getAddDescr(dbs,from_dbs,to_dbs):
	return 'Command line tool for '+dbs[self.from_dbs[0]] +' data replication to '+dbs[self.to_dbs[0]] +' database.'			
supported0 = lambda x : x[0] in from_dbs and x[1] in to_dbs

def supported(x,for_db, from_to_dbs):
	#print x,for_db, from_to_dbs, (x[0] in from_to_dbs and x[1] in for_db) or (x[0] in for_db and x[1] in from_to_dbs)
	return (x[0] in from_to_dbs and x[1] in for_db) or (x[0] in for_db and x[1] in from_to_dbs)
def forApp():
	global dbs, from_dbs, to_dbs
	if from_dbs and from_dbs[0] and to_dbs and to_dbs[0]:
		if from_dbs[0] in ['CSV']:
			
			return dbs[to_dbs[0]]
		else:
			return dbs[from_dbs[0]]
	else:
		return ''
def getExeTitle(apptitle, for_db, bin, dbs):
	return '%s %sbit for %s' % (apptitle, bin, dbs[for_db[0]])
def show_default_help(for_db,from_to_dbs,appname, dbs,ff):
	
	#print from_to_dbs
	#print for_db
	cvarg='-h'
	print 'Databases supported (%d):' % (len(from_to_dbs)-len(ff))
	j=1
	
	from_dbs=[d for d in from_to_dbs if d not in ff]
	print from_dbs
	for i in from_dbs:
		if dbs.has_key(i):
			#print i
			print '%d. %s' % (j, dbs[i])
			j +=1
	print ''

	print 'Data formats supported (%d):' % len(ff)
	j=1
	for i in from_to_dbs:
		if i in ff:
			print '%d. %s' % (j, dbs[i])
			j +=1
	print ''

	
	print """For detailed help use one of the options:"""
	if 0:
		assert len(from_to_dbs), 'from_to_dbs are not set.'
		assert len(for_db), 'for_db is not set.'

		print "\nFrom {:s}\n".format((dbs[for_db[0]]+':')[:50]) 
		print (''.join(['\tTo {:20s}: {:s} {:s} {:s}2{:s}\n'.format (dbs[x.upper()],appname, cvarg,for_db[0].lower(),x.lower()) for x in from_to_dbs if '%s%s%s' % (for_db[0].lower(), _to, x.lower())!='csv%scsv' % _to]))
		
		print "To {:s}\n".format((dbs[for_db[0]]+':')[:50]) 
		print (''.join(['\tFrom {:18s}: {:s} {:s} {:s}2{:s}\n'.format (dbs[x.upper()],appname, cvarg,x.lower(),for_db[0].lower()) for x in from_to_dbs if '%s%s%s' % (for_db[0].lower(), _to,  x.lower())!='csv%scsv' % _to and for_db[0].lower()!= x.lower()]))
def show_vector_help(copy_vector,params):
		(from_db, to_db) = copy_vector.split(_to)
		(ufrom_db, uto_db) = copy_vector.upper().split(_to)
		from_args=params['FROM'][ufrom_db]
		to_args=params['TO'][uto_db]
		print '\nSet following command line arguments to copy from %s to %s:\n' % (dbs[ufrom_db], dbs[uto_db])
		#print appname,
		keys=[]
		for key,arg in params['core'].items():
			keys.append(key)
			print arg['short'], key,
		for key,arg in from_args.items():
			keys.append(key)
			print arg['short'], key,
		for key,arg in to_args.items():
			if not key in keys:
				keys.append(key)
				print arg['short'], key,
		print '\n'
		print 'Here:'
		#print keys
		for key in keys:
			if key in params['core'].keys():
				arg=params['core'][key]
				print '(Common) %s [%s]\t%s\t' % (arg['short'],arg['long'],arg['help'])		
			elif key in from_args.keys():
				arg=from_args[key]
				print '(From %s) %s [%s]\t%s\t' % (dbs[ufrom_db],arg['short'],arg['long'],arg['help'])
			else:
				arg=to_args[key]
				print '(To %s) %s [%s]\t%s\t' % (dbs[uto_db],arg['short'],arg['long'],arg['help'])
		
def show_UseCase(ucases,uc,dbs):
	#print uc
	ukey =None
	for c in ucases:
		#print c
		if ucases[c].has_key(uc):			
			ukey =c
	assert ukey, 'Use case %s is not found.'
	#print ukey
	#pprint (ucases[ukey][uc])
	db_from, db_to, descr, details = ucases[ukey][uc]
	print """
************************************
Copy direction: %s->%s
************************************
%s

	""" % (dbs[db_from], dbs[db_to], details)
		
def show_help(for_db,from_to_dbs, dbs, cvarg,copy_vector,params,ucases):
	assert cvarg, 'Help argument [-h] or [--help] is not set'
	assert copy_vector, 'Copy vector [-w] is not set'
	
	if copy_vector.upper() in ('ALL'):
		i = for_db[0]
		print 'From %s:' % dbs[i]
		for vector in ['%s%s%s' % (str(i).lower(),_to, x.lower()) for x in from_to_dbs if '%s%s%s' % (i,_to,  x)!='csv%scsv' % _to]:
			#print vector
			show_vector_help(vector,params)
		print 'To %s:' % dbs[i]
		for vector in ['%s%s%s' % (x.lower(),_to, str(i).lower()) for x in from_to_dbs if '%s%s%s' % (i,_to,  x)!='csv%scsv' % _to]:
			#print vector
			show_vector_help(vector,params)

	elif copy_vector.upper() in ('LIST'):
		cnt=1
		for i in from_to_dbs:
			print 'From %s:' % dbs[i]
			for vector in ['%s%s%s' % (str(i).lower(),_to, x.lower()) for x in from_to_dbs if '%s%s%s' % (i,_to,  x)!='CSV%sCSV' % _to]:
				(ft, to)= vector.upper().split(_to)
				print '\t%s. %s->%s' % (cnt, dbs[ft], dbs[to])
				cnt +=1
	elif copy_vector.upper().startswith('USE'):
		cnt=1
		global appname
		#print ucases.keys()
		uc = copy_vector.split(':')
		

		if len(uc)==1:
			#pprint(ucases[ucases.keys()[0]])
			#print appn
			#if not release:
			#	appname ='python datamule.py'
			for v in ucases.keys():
				print '\nCopy direction: %s->%s\n' % tuple(v.split('_to_'))
				ks=ucases[v].keys()
				ks.sort()
				for k in range(len(ks)):
					print '  %d. %s -h USE:%s' % (cnt,appname, ks[k])
					cnt +=1
		else:
			#print uc
			show_UseCase(ucases,uc[1],dbs)
			#e(0)
			#echo y  | c:\Python27\qc_dist_32\20141222_171211\qc32\qc32.exe -w csv2ora -o 3 -r 3 -t "|" -i c:\Python27\data_migrator_1239\test\v101\data\oracle_shard_0.data -y 10 -g SCOTT/tiger2@orcl -a SCOTT.Timestamp_test_to -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"
	elif copy_vector.upper() in ('FEAT'):
		cnt=1
		i = for_db[0]
		#todbs=list(set([x.split('_')[0] for x in from_to_dbs]))
		feat=[]
	
		for vector in ['%s%s%s' % (str(i).lower(),_to, x.lower()) for x in from_to_dbs if '%s%s%s' % (i,_to,  x)!='CSV%sCSV' % _to]:
			(ft, to)= vector.upper().split(_to)
			if ft in ('CSV'):
				feat.append( 'Load data from "%s file" to "%s"' % ( dbs[ft], dbs[to]))
			elif to in ('CSV'):
				feat.append( 'Extract data from "%s" to "%s file"' % (dbs[ft], dbs[to]))
			else:
				feat.append( 'Copy data from "%s" to "%s"' % (dbs[ft], dbs[to]))
			cnt +=1	
		for vector in ['%s%s%s' % (x.lower(), _to, str(i).lower()) for x in from_to_dbs if '%s%s%s' % (i,_to,  x)!='CSV%sCSV' % _to ]:
			(ft, to)= vector.upper().split(_to)
			if ft in ('CSV'):
				feat.append( 'Load data from "%s file" to "%s"' % ( dbs[ft], dbs[to]))
			elif to in ('CSV'):
				feat.append( 'Extract data from "%s" to "%s file"' % (dbs[ft], dbs[to]))
			else:
				feat.append( 'Copy data from "%s" to "%s"' % (dbs[ft], dbs[to]))
			cnt +=1				
		cnt=1
		for f in sorted(list(set(feat))):
			print '\t%s. %s' % (cnt,f)
			cnt +=1	
	elif copy_vector.upper() in ('ABOUT'):
		"""['CSV', 'DBTAES', 'DBTAWS', 'DBTDE', 'DBTE', 'DBTEC', 'DBTES', 'DBTWS', 
'ORAEXA','INFOB', 'INFOR', 'INFORC', 'MARIA', 'MYSQL', 'ORA11G', 'ORAXE', 'PGRES', 'SLITE',
'SSENT', 'SSEXP', 'SYANY', 'SYASE', 'SYIQ', 'TTEN']"""
		donate=''
		app_descr ={}
		app_descr['ORA11G']=app_descr['PGRES']='Query/Table/Partition/Sub-Partition data migrator for "%s" database.' % dbs[for_db[0]]
		app_descr['SSENT']=app_descr['MYSQL']='Query/Table/Partition data migrator for "%s" database.' % dbs[for_db[0]]
		app_descr['SSEXP']=app_descr['TTEN']=app_descr['SLITE']='Query/Table data migrator for "%s" database.' % dbs[for_db[0]]
		
		
		if free:
			donate="""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!PLEASE, DONATE TO HELP UKRAINIAN PATRIOTS FIGHTING RUSSIAN INVASION.!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

http://euromaidanpress.com/2014/07/04/verified-ways-to-help-the-ukrainian-army/

1. Come back alive:
	Web: http://www.savelife.in.ua/partners.html
	FB:  https://www.facebook.com/groups/backandalive/
	PayPal: zxsk@hotmail.com
	
2. Wings Phoenix:
	Web: http://wings-phoenix.org.ua/en
	PayPal: fenix@mykola.org 

3. ATO Sister of Mercy
	Web: http://alturl.com/qmbhe

4. Army SOS.
	FB: https://www.facebook.com/groups/armia.sos/
	
5. Volunteers' Hundred.
	Western Union: 	recepient Oleksii Savchenko, Kyiv, Ukraine, 
					passport EE321055, armia.sos@gmail.com.
	MoneyGram:  recepient Oleksii Savchenko, Kyiv, Ukraine, 
				passport EE321055, armia.sos@gmail.com.
	LiqPay: transfer to the card 4149 4978 0480 1324, 
			recepient Oleksii Savchenko

6. All-Ukrainian Union "Patriot".
	FB: https://www.facebook.com/groups/PatriotGO/
	PayPal: go.patriot.ua@gmail.com

7. EuroArmyMaydan:
	FB: https://www.facebook.com/groups/EuroArmyMaydan/
	
8. Saving lives in Ukraine
	FB: https://www.facebook.com/SavingLivesinUkraine
	PayPal: savinglivesinukraine@gmail.com

9. Joint Army support project.
	http://kryla.org.ua/

10. Ukrainian Freedom Fund.
	FB: https://www.facebook.com/ukrmilcf
	Donate: http://ukrfreedomfund.org/#slide9

11. Ukrainian American Freedom Foundation.
	Web: http://patriotdefence.org/
	Donate: https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=9KK485RCK7332
	
12. Helping Ukrainian Soldiers.
	https://www.facebook.com/UkieArmyHelp

******************************************************
  Author: Alex Buzunov
Facebook: https://www.facebook.com/buzunov
Hire me: http://www.linkedin.com/in/alexbuz/

			"""		
		print """#
#
#
# "%s" version %s (%sbit)
#
# %s
#
#
#
%s
""" % (getAppTitle(for_db, apptitle, dbs),version, bin, app_descr[for_db[0]],donate)
	else:
		show_vector_help(copy_vector,params)
	
	