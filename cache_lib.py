import os
from tsql_lib import   appLoc
import cPickle as pickle
from pprint import pprint

def ifCacheExists_(cache_key):
	#pprint (gCache)
	return gCache.has_key(cache_key)

def ifCacheExists(relative_path,  suffix=''):
	#cc= cache_key.split('.')
	cfile_name="%s%s.p" % (relative_path.split('/')[-1], suffix)
	cache_loc= os.path.join(gCacheLoc,relative_path)
	cfile=os.path.join(cache_loc,cfile_name)
	#print 'reading from1:', cfile
	#sys.exit(1)
	if os.path.isfile(cfile):
		print 'cache exists'
		return True
	else: 
		print 'no cache'
		return False
			
def loadCache(cacheLoc, cache_root):
	out={}
	depth =len( cacheLoc.split('\\'))
	for root, dirnames, filenames in os.walk(cacheLoc, topdown=True):

		#dirnames.sort(reverse=True)
		if filenames:
			#print filenames
			sf= root.split('\\')			
			cache_depth= len(sf)-depth
			for fn in filenames:
				#print depth,root,dirnames
				#print filenames
				
				
				cache= os.path.splitext(fn)[0]
				cache_name='%s.%s.%s' % (cache_root,'.'.join(sf[-cache_depth:]),cache)
				cache_loc=os.path.join(cacheLoc,'\\'.join(sf[-cache_depth:]),fn)
				out[str(cache_name)]=str(cache_loc)
	#pprint(out)
	#sys.exit(1)
	out['%s.location' % (cache_root)] =cacheLoc
	return out
def writeToCache(relative_path, cache, suffix=''):
	#print 'CREATING CACHE', cache_key
	cc= relative_path.split('/')
	cfile_name="%s%s.p" % (cc[-1],suffix)
	cache_loc=os.path.join(gCacheLoc,relative_path)
	#print cache_loc,cfile_name
	#sys.exit(1)
	if not os.path.isdir(cache_loc):
		os.makedirs(cache_loc)
	cfile=os.path.join(cache_loc,cfile_name)
	print 'writing to:', cfile
	s=pickle.dump(cache, open( cfile, "wb" ))
	#global gCache
	#gCache=loadCache(gCacheLoc,'global')
	#close(cfile)
	#print s

def readFromCache(relative_path,  suffix=''):
	#cc= cache_key.split('.')
	cfile_name="%s%s.p" % (relative_path.split('/')[-1], suffix)
	cache_loc= os.path.join(gCacheLoc,relative_path)
	#print cache_loc,cfile_name
	#sys.exit(1)
	#assert os.path.isfile(cache_loc), 'Cannot read cache file %s' % cache_loc
	#s=pickle.dump(cache, open( os.path.join(cache_loc,cfile_name), "wb" ))
	cfile=os.path.join(cache_loc,cfile_name)
	print 'reading from3:', cfile
	if os.path.isfile(cfile):
		s = pickle.load( open(cfile, "rb" ) )
		#print s
		return s
	print 'Cache ', cfile, 'does not exists.'
	return {}

	
def writeToCache_0(cache_key, cache):
	#print 'CREATING CACHE', cache_key
	cc= cache_key.split('.')
	cfile_name="%s.p" % cc[-1]
	cache_loc=os.path.join(gCacheLoc,'\\'.join(cc[1:-1]))
	#print cache_loc,cfile_name
	#sys.exit(1)
	if not os.path.isdir(cache_loc):
		os.makedirs(cache_loc)
	cfile=os.path.join(cache_loc,cfile_name)
	s=pickle.dump(cache, open( cfile, "wb" ))
	global gCache
	gCache=loadCache(gCacheLoc,'global')
	#close(cfile)
	#print s
	
#ta=readFromCache(gcache,'tables')

#writeToCache(gTabTreeCache,((2,3)))
#sys.exit(1)

def readFromCache_00(cache_key):
	cc= cache_key.split('.')
	cfile_name="%s.p" % cc[-1]
	cache_loc="%s.p" % os.path.join(gCacheLoc,'\\'.join(cc[1:]))
	#print cache_loc,cfile_name
	#sys.exit(1)
	assert os.path.isfile(cache_loc), 'Cannot read cache file %s' % cache_loc
	#s=pickle.dump(cache, open( os.path.join(cache_loc,cfile_name), "wb" ))
	s = pickle.load( open(cache_loc, "rb" ) )
	return s

gCacheLoc=os.path.join(appLoc,'gcache')
gCache=loadCache(gCacheLoc,'global')