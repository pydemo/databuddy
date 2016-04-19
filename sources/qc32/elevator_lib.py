from  collections import OrderedDict
def calc_floors(v):
	floors_per_trip=sum([abs(x[0]-x[1]) for x in v])	
	#dummy trip
	reversed_dummy_trip=v[-1:][0][::-1]
	v +=[reversed_dummy_trip]
	#calculating number of floors between trips
	floors_between_trips=sum([abs((v[i][1]-v[i+1][0])) for i in range(len(v)-1)])
	#calculating total floors travelled
	total_floors= floors_per_trip + floors_between_trips
	return total_floors
	
def mode_A(cmds):
	"""Implements Mode A"""
	out=[]
	for k,v in cmds.items():	
		#first trip to initial location
		first_trip=[(int(k),v[0][0])]
		#prepending first trip
		v =first_trip +v
		total_floors_per_line= calc_floors(v)
		#printing trips and total
		out.append( '%s %s (%s)' % (k,' '.join(['%s %s' % tuple(map(abs, x)) for x in v[1:-1]]), total_floors_per_line))
	return out
def breat_trip(trip):
	""" Breaks trip into unidirectional sub-trips:"""
	flag=int(trip[0][0]>trip[0][1])
	out=[]
	out.append(trip[0])
	for i in trip[1:]:
		if flag == int(i[0]>i[1]):
			out.append(i)
		else:
			yield ( flag, out)
			out=[i]
			flag= int(i[0]>i[1])
			
	if out:
		yield (flag, out)

def mode_B(cmds):
	"""Implements Mode B"""
	out=[]
	for k,v in cmds.items():	
		#first trip to initial location
		first_trip=[(int(k),v[0][0])]
		#prepend first trip
		v =first_trip +v
		#first_floor is the end of previous sub trip
		from_floor =-1
		calc=[]
		subtrips=[]
		#process trip ans unidirectional sub-trips
		for i in breat_trip(v):
			flag, trip = i
			#flatten and make dense
			a= list(set([j for subl in trip for j in subl]))
			a.sort(reverse=flag)
			
			if from_floor>0 and from_floor !=a[0]:
				a = [from_floor] +a
			subtrip=[]
			for x in range(len(a)-1):
				subtrip.append( (a[x],a[x+1]))
			calc.append(calc_floors(subtrip))
			subtrips.append(subtrip[:-1])			
			from_floor = a[-1]
		num_of_floors = sum(calc)
		#flatten result
		b= [j for subl in [j for subl in subtrips for j in subl] for j in subl]
		b =[b[0]]+ b+ [b[-1]]
		out.append(' '.join([str(b[x]) for x in range(len(b)-1) if b[x]==b[x+1]])+ '(%s)' % num_of_floors )
	return out
if __name__ == "__main__":
	#Tests
	d=OrderedDict([('6', [(1, 8), (6, 8)])])
	ret= mode_A(d)
	assert ret[0]=='6 1 8 6 8 (16)', 'Test failed.'
	print 'Test OK'
	
	d=OrderedDict([('10', [(8, 1)])])
	ret= mode_A(d)
	assert ret[0]=='10 8 1 (9)', 'Test failed.'
	print 'Test OK'
	
	d=OrderedDict([('9', [(1, 5), (1, 6), (1, 5)])])
	ret= mode_A(d)	
	assert ret[0]=='9 1 5 1 6 1 5 (30)', 'Test failed.'
	print 'Test OK'
	
	d=OrderedDict([('3', [(7, 9), (3, 7), (5, 8), (7, 11), (11, 1)])])
	ret= mode_B(d)	
	assert ret[0]=='3 5 7 8 9 11 1(18)', 'Test failed.'
	print 'Test OK'
