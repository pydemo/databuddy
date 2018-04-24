#elevator.py
import argparse
import os,sys
from pprint import pprint
from  collections import OrderedDict
import elevator_lib as lib
e=sys.exit

def usage():
	print """Usage:
	python elevator.py -f input.txt -m A
	or
	python elevator.py -f input.txt -m B
	
Arguments:
	-f : text file with elevator inputs
		e.g. 9:1-5,1-6,1-5
		
	-m : Calculation mode (A or B)
	"""
#parser config
parser = argparse.ArgumentParser(description='Elevator.')
parser.add_argument('-f','--file_name',type=str,  help='Input file.')
parser.add_argument('-m','--mode',  type=str,  help='Mode (A or B).')
args = parser.parse_args()

if not os.path.isfile(args.file_name):
	usage()
	e(1)
if not args.mode.upper() in ('A', 'B'):
	usage()
	e(1)

cmds=OrderedDict()
fn=args.file_name
#
#parse file and convert each line to ordered dict
# {start_floor:[(from,to),(from,to)...(from,to)])]}
#
with open(fn, 'r') as f:
	for line in f:
		if line.strip():
			floor,cmd=line.strip().split(':')
			assert floor.isdigit(), 'Non numeric floor %s' % floor
			cmds[floor]=[]
			for move in cmd.strip().split(','):
				from_floor,to_floor = move.strip().split('-')
				assert from_floor.isdigit(), 'Non numeric from_floor %s in move %s, floor %s' % (from_floor,move,floor)
				assert to_floor.isdigit(), 'Non numeric to_floor %s in move %s, floor %s' % (to_floor,move,floor)
				cmds[floor].append((int(from_floor),int(to_floor)))

if args.mode.upper() in ('A'):
	print os.linesep.join(lib.mode_A(cmds))
	
elif args.mode.upper() in ('B'):
	print os.linesep.join(lib.mode_B(cmds))