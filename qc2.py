# Title: 	data-buddy
# Description:
#			Session manager for DataMigrator.		
# Environment:
#			Python 2.7 and wxPython 2.8		
#
__author__ = "METRICS TECH"
__copyright__ = None # "Copyright 2015, SequelWorks Inc."
__credits__ = []
__appname__='QC Session Manager'
__license__ = "GPL"
__title__ = "Session Manager for QueryCopy"
__version__ = "0.3.5"
__maintainer__ = "Alex Buzunov"
__email__ = "alexbuzunov@gmail.com"
__github__=None
__status__ = "Development" 


import sys,platform; 
__platform__='32' #platform.architecture()[0]

import wx.lib.inspection
import wx.lib.mixins.inspection
from multiprocessing import freeze_support #Process, Queue, cpu_count, current_process, 
from wx.lib.splitter import MultiSplitterWindow
import wx.lib.agw.flatnotebook as fnb
import wx.lib.mixins.listctrl as listmix

from tc_lib import cml, getPipelineConfig, activeProjName, activeProjLoc, DEFAULT_PERSPECTIVE, projRootLoc, confDirName, configDirLoc,  appLoc

from collections import OrderedDict
from cache_lib import ifCacheExists,readFromCache
import wx.lib.agw.hyperlink as hl
from tc_lib import sub, send
import common_utils as cu
import images
import os, sys, time 
from pprint import pprint
import pprint as pp
import webbrowser
import wx.html 
#from tc_lib import sub, send
from collections import OrderedDict
import imp
from editor_py import PythonEditor
#from py_editor import PythonSTC
import base64
import win32con
import win32gui, win32api
import win32process
import __builtin__
#import webbrowser

import ctypes as ct
from win32con import SW_MINIMIZE, SW_RESTORE
from win32ui import FindWindow, error as ui_err
from time import sleep
import datetime

import threading
from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE

import shutil
import wx.combo

#import yaml
import re
import wx.lib.scrolledpanel


import shlex 
		
__builtin__.copy_vector = None
__builtin__.cvarg = None

#import qc32.common.v101.config as conf
import qc32.config.config as conf
#for d in sorted(conf.dbs):
#	print d,': ',conf.dbs[d]
import argparse

try:
    from agw import ultimatelistctrl as ULC
except ImportError: # if it's not there locally, try the wxPython lib.
    from wx.lib.agw import ultimatelistctrl as ULC


try:
	from agw import flatmenu as FM
	from agw.artmanager import ArtManager, RendererBase, DCSaver
	from agw.fmresources import ControlFocus, ControlPressed
	from agw.fmresources import FM_OPT_SHOW_CUSTOMIZE, FM_OPT_SHOW_TOOLBAR, FM_OPT_MINIBAR
except ImportError: # if it's not there locally, try the wxPython lib.
	import wx.lib.agw.flatmenu as FM
	from wx.lib.agw.artmanager import ArtManager, RendererBase, DCSaver
	from wx.lib.agw.fmresources import ControlFocus, ControlPressed
	from wx.lib.agw.fmresources import FM_OPT_SHOW_CUSTOMIZE, FM_OPT_SHOW_TOOLBAR, FM_OPT_MINIBAR


from qc32.config.include.oracle import target	
from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE

home=os.path.dirname(os.path.abspath(__file__))
app_title='%s %s' % (__title__,__version__)

import __builtin__
__builtin__.home = home
__builtin__.app_title = app_title
__builtin__.__author__ = __author__
__builtin__.__copyright__ = __copyright__
__builtin__.__credits__ = __credits__
__builtin__.__appname__=__appname__
__builtin__.__license__ = __license__
__builtin__.__title__ = __title__
__builtin__.__version__ = __version__
__builtin__.__maintainer__ = __maintainer__
__builtin__.__email__ = __email__
__builtin__.__github__= __github__
__builtin__.__status__ = __status__

from include.main import *

if __name__ == '__main__':
	try:
		_count = int(open("counter").read())
	except IOError:
		_count = 0
	
	freeze_support()	
	
	parser = argparse.ArgumentParser(description=app_title)
	parser.add_argument('-s','--session',default='',type=str,  help='Session file to open')
	args = parser.parse_args()
	default_session=None
	if hasattr(args, 'session') and args.session:
		default_session=args.session
	#pprint(args)
	#e(0)
	class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
		def OnInit(self):
			import images as i
			global imgs
			imgs = i
			self.Init()
			self.frame = DataBuddy(None, -1,title=app_title, size=dimensions['frame'])
			
			#1350,897
			if default_session:
				self.frame.openDefault(default_session)
			self.frame.Show(True)
			#self.frame.Maximize(True)
			self.SetTopWindow(self.frame)
			#print self.frame.GetClientSizeTuple()
			
			return True

	app = MyApp(redirect=False) #=True,filename="applogfile.txt")


	from random import choice
	from sys import maxint

	app.frame.Layout()
	try:
		app.MainLoop()
	except Exception, e:
		traceback.print_exc();
	import atexit
	#atexit.register(savecounter))