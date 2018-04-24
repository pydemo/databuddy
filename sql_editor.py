import wx
import wx.aui
import wx.lib.agw.aui as aui
import  wx.grid             as  gridlib
import sys, re, os
import dbi
import odbc, time, datetime
from pprint import pprint
import images
from tc_lib import sub, send
import types
e = sys.exit
#ddb='MRR_BI'
#duser='MRR_ETL_USER'
from db_utils import query
from common.v101.loaders import import_module
#import config.include.etl.oracle as ora
import __builtin__		
from subprocess import Popen, PIPE
import wx.lib.agw.pybusyinfo as PBI

home= os.path.abspath(os.path.dirname(sys.argv[0]))
print home
#e(0)
editor_file=os.path.join(home, 'include','sql_editor.py')
editor=import_module(editor_file)
	
if __name__ == "__main__":
	"""
	d = showmsg()
	time.sleep(3)
	d = None
	sys.exit(0)
	"""
	import sys
	from wx.lib.mixins.inspection import InspectableApp
	app = InspectableApp(False)
	frame = editor.Main(None, sys.stdout)
	frame.Show(True)
	#import wx.lib.inspection
	#wx.lib.inspection.InspectionTool().Show()
	app.MainLoop()	
