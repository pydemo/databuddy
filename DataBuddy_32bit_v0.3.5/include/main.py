# Title: 	data-buddy
# Description:
#			Session manager for DataMigrator.		
# Environment:
#			Python 2.7 and wxPython 2.8		
#
if 0:
	__author__ = "Alex Buzunov"
	__copyright__ = "Copyright 2015, SequelWorks Inc."
	__credits__ = []
	__appname__='QC Session Manager'
	__license__ = "GPL"
	__title__ = "Session Manager for QueryCopy"
	__version__ = "0.3.5"
	__maintainer__ = "Alex Buzunov"
	__email__ = "alexbuzunov@gmail.com"
	__github__=None
	__status__ = "Development" 	


USE_BUFFERED_DC = 0
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
import os, sys, time, inspect
#from include.v101.host_map import host_map as hmap
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
import pickle
import threading
from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE
#from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE
import shutil
import wx.combo
from wx.lib.wordwrap import wordwrap
import wx.lib.agw.multidirdialog as MDD
#import yaml
import re
import wx.lib.scrolledpanel
import  wx.lib.masked as  masked

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

try:
	from Queue import Queue, Empty
except ImportError:
	from queue import Queue, Empty  # python 3.x
from threading  import Thread
import io											
#import os
import subprocess
#import sys
#import time
#from pprint import pprint
if sys.platform == "win32":
	import msvcrt
	import _subprocess
else:
	import fcntl
e=sys.exit	
ON_POSIX = 'posix' in sys.builtin_module_names

import gc
gc.enable()
print gc.get_count()
#e(0)
				
#from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE
def import_module(filepath):
	class_inst = None
	#expected_class = 'MyClass'

	mod_name,file_ext = os.path.splitext(os.path.split(filepath)[-1])
	assert os.path.isfile(filepath), 'File %s does not exists.' % filepath
	if file_ext.lower() == '.py':
		py_mod = imp.load_source(mod_name, filepath)

	elif file_ext.lower() == '.pyc':
		py_mod = imp.load_compiled(mod_name, filepath)
	return py_mod
########################################################################	
exe=False
exe=True


#print wx.VERSION

blog=cu.blog

tmpl_home=os.path.join(home,'templates')
userhome = os.path.expanduser('~')
session_home=os.path.join(home,'sessions')	
default_tmpl_lib='My_Templates'	
default_sess_lib='My_Sessions'	
transport_home=r'C:\Python27\data_migrator_1239_pscp'
if exe:
	transport_home=os.path.join(home,'qc%d' % int(__platform__[:2]))
if __platform__ in ['32']:
	from qc32.include.v101.host_map import host_map as hmap
	if 0:
		if exe:
			from qc32.include.v101.host_map import host_map as hmap
		else:
			if 0:
				mod_file=os.path.join(transport_home, 'include','v101', 'host_map.py')
				hmap2=import_module(mod_file)
				#hmap2= hmapmod.host_map
				
				from qc32.include.v101.host_map import host_map as hmap
				#print hmap2
				#print hmap
				e(0)
				#os.chdir(transport_home)
				#from include.v101.host_map import host_map as hmap
				#os.chdir(home)
			#import os, sys, inspect
			# realpath() will make your script run, even if you symlink it :)
			#cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
			if transport_home not in sys.path:
				sys.path.insert(0, transport_home)	 
				#from include.v101.host_map import host_map as hmap
				sys.path.pop()
				sys.path.remove(transport_home)
else:
	from qc64.include.v101.host_map import host_map as hmap
	
aa_dir='args_api'
ID_EXIT = wx.NewId()
ID_CREATE = wx.NewId()
ID_ABOUT = wx.NewId()
LOAD_FILE_ID = wx.NewId()
update_cache=True
dBtn='N/A'
tr='qc'

dimensions={'frame':(1290,768), 'common_args':(839,230), 'source_args':(419,270),'target_args':(419,270)}
if 1:
	dim_file=os.path.join(home,'config','dimensions.py')
	assert os.path.isfile(dim_file), 'config/dimentions.py does not exists.'
	dims=import_module(dim_file)
	hasattr(dims, 'dimensions') and dims.dimensions
	dimensions=dims.dimensions

def onExit():
	print 'process exited'
	#print '#'*100
#p = Popen(['start', 'cmd.exe', "/k"]+cfg, stdin=PIPE, shell=True) #stderr=PIPE, stdout=PIPE,


if 0:
	class QuickAddBox(wx.TextCtrl):
		def __init__(self, parent, viewer):
			self.quick_add_text = wx.TextCtrl.__init__(self, parent, -1, '', size=(300,20), style=wx.TE_PROCESS_ENTER)
			self.Bind(wx.EVT_TEXT_ENTER, self.OnPress, self.quick_add_text)

		def OnPress(self, evt):
			print self.quick_add_text.GetValue()
			
			
def popenAndCall(onExit, popenArgs):
	print 'popenAndCall'
	"""
	Runs the given args in a subprocess.Popen, and then calls the function
	onExit when the subprocess completes.
	onExit is a callable object, and popenArgs is a list/tuple of args that 
	would give to subprocess.Popen.
	"""
	def runInThread(onExit, popenArgs):
		#print 'runInThread'
		#proc = subprocess.Popen(*popenArgs)
		proc = Popen(popenArgs , creationflags=CREATE_NEW_CONSOLE)
		out,err=proc.communicate()
		#print out ,err
		proc.wait()
		onExit()
		return
	thread = threading.Thread(target=runInThread, args=(onExit, popenArgs))
	thread.start()
	# returns immediately after the thread starts
	return thread
					
class cls_KeyBdInput(ct.Structure):
    _fields_ = [
        ("wVk", ct.c_ushort),
        ("wScan", ct.c_ushort),
        ("dwFlags", ct.c_ulong),
        ("time", ct.c_ulong),
        ("dwExtraInfo", ct.POINTER(ct.c_ulong) )
    ]
class cls_HardwareInput(ct.Structure):
    _fields_ = [
        ("uMsg", ct.c_ulong),
        ("wParamL", ct.c_short),
        ("wParamH", ct.c_ushort)
    ]

class cls_MouseInput(ct.Structure):
    _fields_ = [
        ("dx", ct.c_long),
        ("dy", ct.c_long),
        ("mouseData", ct.c_ulong),
        ("dwFlags", ct.c_ulong),
        ("time", ct.c_ulong),
        ("dwExtraInfo", ct.POINTER(ct.c_ulong) )
    ]	
class cls_Input_I(ct.Union):
    _fields_ = [
        ("ki", cls_KeyBdInput),
        ("mi", cls_MouseInput),
        ("hi", cls_HardwareInput)
    ]
class cls_Input(ct.Structure):
    _fields_ = [
        ("type", ct.c_ulong),
        ("ii", cls_Input_I)
    ]
def make_input_objects( l_keys ):

	p_ExtraInfo_0 = ct.pointer(ct.c_ulong(0))

	l_inputs = [ ]
	for n_key, n_updown in l_keys:
		ki = cls_KeyBdInput( n_key, 0, n_updown, 0, p_ExtraInfo_0 )
		ii = cls_Input_I()
		ii.ki = ki
		l_inputs.append( ii )

	n_inputs = len(l_inputs)

	l_inputs_2=[]
	for ndx in range( 0, n_inputs ):
		s2 = "(1, l_inputs[%s])" % ndx
		l_inputs_2.append(s2)
	s_inputs = ', '.join(l_inputs_2)


	cls_input_array = cls_Input * n_inputs
	o_input_array = eval( "cls_input_array( %s )" % s_inputs )

	p_input_array = ct.pointer( o_input_array )
	n_size_0 = ct.sizeof( o_input_array[0] )

	# these are the args for user32.SendInput()
	return ( n_inputs, p_input_array, n_size_0 )

	'''It is interesting that o_input_array has gone out of scope
	by the time p_input_array is used, but it works.'''	
		
def send_yes( window1 ):

	#tpl1 = window1.GetWindowPlacement()
	#	window1.ShowWindow(SW_RESTORE)
	#	sleep(0.2)

	#window1.SetForegroundWindow()
	#sleep(0.2)

	#window1.SetFocus()
	#pprint(dir(window1))
	#sleep(0.2)
	# writes "y\n"
	# 0x10 is shift.  note that to repeat a key, as with 4C here, you have to release it after the first press

	t_yes = ( ( 0x79, 0 ), ( 0x0D, 0 ), )
	t_yes = ( ( 0x59, 0 ),  ( 0x0D, 0 ), )
	#print t_yes
	#time.sleep(1)
	l_keys = [ ]
	## l_keys.extend( t_ctrl_o )
	l_keys.extend( t_yes )
	#l_keys.extend( t_ctrl_s )
	t_inputs = make_input_objects( l_keys )
	#print t_inputs
	window1.SetFocus()
	rv = ct.windll.user32.SendInput( *t_inputs )
	#print rv
	#print 'send_input: DONE'
	#if was_min and b_minimize:
	#	sleep(0.3) # if the last input was Save, it may need time to take effect
	#	window1.ShowWindow(SW_MINIMIZE)

	#return rv
def send_no( window1 ):

	#tpl1 = window1.GetWindowPlacement()
	#	window1.ShowWindow(SW_RESTORE)
	#	sleep(0.2)

	#window1.SetForegroundWindow()
	#sleep(0.2)

	#window1.SetFocus()
	#pprint(dir(window1))
	#sleep(0.2)
	# writes "y\n"
	# 0x10 is shift.  note that to repeat a key, as with 4C here, you have to release it after the first press

	#t_yes = ( ( 0x79, 0 ), ( 0x0D, 0 ), )
	t_no = ( ( 0x4e, 0 ),  ( 0x0D, 0 ), )
	#print t_yes
	#time.sleep(1)
	l_keys = [ ]
	## l_keys.extend( t_ctrl_o )
	l_keys.extend( t_no )
	#l_keys.extend( t_ctrl_s )
	t_inputs = make_input_objects( l_keys )
	#print t_inputs
	window1.SetFocus()
	rv = ct.windll.user32.SendInput( *t_inputs )
	#print rv
	#print 'send_input: DONE'
	#if was_min and b_minimize:
	#	sleep(0.3) # if the last input was Save, it may need time to take effect
	#	window1.ShowWindow(SW_MINIMIZE)

	#return rv
	
def find_window( s_app_name ):

    try:
        window1 = FindWindow(  None, s_app_name,)
        return window1
    except ui_err:
        pass
    except:
        raise

    try:
        window1 = FindWindow( s_app_name, None, )
        return window1
    except ui_err:
        return None
    except:
        raise
		


import ctypes

LONG = ctypes.c_long
DWORD = ctypes.c_ulong
ULONG_PTR = ctypes.POINTER(DWORD)
WORD = ctypes.c_ushort

class MOUSEINPUT(ctypes.Structure):
	_fields_ = (('dx', LONG),
				('dy', LONG),
				('mouseData', DWORD),
				('dwFlags', DWORD),
				('time', DWORD),
				('dwExtraInfo', ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
	_fields_ = (('wVk', WORD),
				('wScan', WORD),
				('dwFlags', DWORD),
				('time', DWORD),
				('dwExtraInfo', ULONG_PTR))

class HARDWAREINPUT(ctypes.Structure):
	_fields_ = (('uMsg', DWORD),
				('wParamL', WORD),
				('wParamH', WORD))

class _INPUTunion(ctypes.Union):
	_fields_ = (('mi', MOUSEINPUT),
				('ki', KEYBDINPUT),
				('hi', HARDWAREINPUT))

class INPUT(ctypes.Structure):
	_fields_ = (('type', DWORD),
				('union', _INPUTunion))

def SendInput(*inputs):
	nInputs = len(inputs)
	LPINPUT = INPUT * nInputs
	pInputs = LPINPUT(*inputs)
	cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
	return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARD = 2

def Input(structure):
	if isinstance(structure, MOUSEINPUT):
		return INPUT(INPUT_MOUSE, _INPUTunion(mi=structure))
	if isinstance(structure, KEYBDINPUT):
		return INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure))
	if isinstance(structure, HARDWAREINPUT):
		return INPUT(INPUT_HARDWARE, _INPUTunion(hi=structure))
	raise TypeError('Cannot create INPUT structure!')

WHEEL_DELTA = 120
XBUTTON1 = 0x0001
XBUTTON2 = 0x0002
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_HWHEEL = 0x01000
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_XDOWN = 0x0080
MOUSEEVENTF_XUP = 0x0100

def MouseInput(flags, x, y, data):
	return MOUSEINPUT(x, y, data, flags, 0, None)

VK_LBUTTON = 0x01               # Left mouse button
VK_RBUTTON = 0x02               # Right mouse button
VK_CANCEL = 0x03                # Control-break processing
VK_MBUTTON = 0x04               # Middle mouse button (three-button mouse)
VK_XBUTTON1 = 0x05              # X1 mouse button
VK_XBUTTON2 = 0x06              # X2 mouse button
VK_BACK = 0x08                  # BACKSPACE key
VK_TAB = 0x09                   # TAB key
VK_CLEAR = 0x0C                 # CLEAR key
VK_RETURN = 0x0D                # ENTER key
VK_SHIFT = 0x10                 # SHIFT key
VK_CONTROL = 0x11               # CTRL key
VK_MENU = 0x12                  # ALT key
VK_PAUSE = 0x13                 # PAUSE key
VK_CAPITAL = 0x14               # CAPS LOCK key
VK_KANA = 0x15                  # IME Kana mode
VK_HANGUL = 0x15                # IME Hangul mode
VK_JUNJA = 0x17                 # IME Junja mode
VK_FINAL = 0x18                 # IME final mode
VK_HANJA = 0x19                 # IME Hanja mode
VK_KANJI = 0x19                 # IME Kanji mode
VK_ESCAPE = 0x1B                # ESC key
VK_CONVERT = 0x1C               # IME convert
VK_NONCONVERT = 0x1D            # IME nonconvert
VK_ACCEPT = 0x1E                # IME accept
VK_MODECHANGE = 0x1F            # IME mode change request
VK_SPACE = 0x20                 # SPACEBAR
VK_PRIOR = 0x21                 # PAGE UP key
VK_NEXT = 0x22                  # PAGE DOWN key
VK_END = 0x23                   # END key
VK_HOME = 0x24                  # HOME key
VK_LEFT = 0x25                  # LEFT ARROW key
VK_UP = 0x26                    # UP ARROW key
VK_RIGHT = 0x27                 # RIGHT ARROW key
VK_DOWN = 0x28                  # DOWN ARROW key
VK_SELECT = 0x29                # SELECT key
VK_PRINT = 0x2A                 # PRINT key
VK_EXECUTE = 0x2B               # EXECUTE key
VK_SNAPSHOT = 0x2C              # PRINT SCREEN key
VK_INSERT = 0x2D                # INS key
VK_DELETE = 0x2E                # DEL key
VK_HELP = 0x2F                  # HELP key
VK_LWIN = 0x5B                  # Left Windows key (Natural keyboard)
VK_RWIN = 0x5C                  # Right Windows key (Natural keyboard)
VK_APPS = 0x5D                  # Applications key (Natural keyboard)
VK_SLEEP = 0x5F                 # Computer Sleep key
VK_NUMPAD0 = 0x60               # Numeric keypad 0 key
VK_NUMPAD1 = 0x61               # Numeric keypad 1 key
VK_NUMPAD2 = 0x62               # Numeric keypad 2 key
VK_NUMPAD3 = 0x63               # Numeric keypad 3 key
VK_NUMPAD4 = 0x64               # Numeric keypad 4 key
VK_NUMPAD5 = 0x65               # Numeric keypad 5 key
VK_NUMPAD6 = 0x66               # Numeric keypad 6 key
VK_NUMPAD7 = 0x67               # Numeric keypad 7 key
VK_NUMPAD8 = 0x68               # Numeric keypad 8 key
VK_NUMPAD9 = 0x69               # Numeric keypad 9 key
VK_MULTIPLY = 0x6A              # Multiply key
VK_ADD = 0x6B                   # Add key
VK_SEPARATOR = 0x6C             # Separator key
VK_SUBTRACT = 0x6D              # Subtract key
VK_DECIMAL = 0x6E               # Decimal key
VK_DIVIDE = 0x6F                # Divide key
VK_F1 = 0x70                    # F1 key
VK_F2 = 0x71                    # F2 key
VK_F3 = 0x72                    # F3 key
VK_F4 = 0x73                    # F4 key
VK_F5 = 0x74                    # F5 key
VK_F6 = 0x75                    # F6 key
VK_F7 = 0x76                    # F7 key
VK_F8 = 0x77                    # F8 key
VK_F9 = 0x78                    # F9 key
VK_F10 = 0x79                   # F10 key
VK_F11 = 0x7A                   # F11 key
VK_F12 = 0x7B                   # F12 key
VK_F13 = 0x7C                   # F13 key
VK_F14 = 0x7D                   # F14 key
VK_F15 = 0x7E                   # F15 key
VK_F16 = 0x7F                   # F16 key
VK_F17 = 0x80                   # F17 key
VK_F18 = 0x81                   # F18 key
VK_F19 = 0x82                   # F19 key
VK_F20 = 0x83                   # F20 key
VK_F21 = 0x84                   # F21 key
VK_F22 = 0x85                   # F22 key
VK_F23 = 0x86                   # F23 key
VK_F24 = 0x87                   # F24 key
VK_NUMLOCK = 0x90               # NUM LOCK key
VK_SCROLL = 0x91                # SCROLL LOCK key
VK_LSHIFT = 0xA0                # Left SHIFT key
VK_RSHIFT = 0xA1                # Right SHIFT key
VK_LCONTROL = 0xA2              # Left CONTROL key
VK_RCONTROL = 0xA3              # Right CONTROL key
VK_LMENU = 0xA4                 # Left MENU key
VK_RMENU = 0xA5                 # Right MENU key
VK_BROWSER_BACK = 0xA6          # Browser Back key
VK_BROWSER_FORWARD = 0xA7       # Browser Forward key
VK_BROWSER_REFRESH = 0xA8       # Browser Refresh key
VK_BROWSER_STOP = 0xA9          # Browser Stop key
VK_BROWSER_SEARCH = 0xAA        # Browser Search key
VK_BROWSER_FAVORITES = 0xAB     # Browser Favorites key
VK_BROWSER_HOME = 0xAC          # Browser Start and Home key
VK_VOLUME_MUTE = 0xAD           # Volume Mute key
VK_VOLUME_DOWN = 0xAE           # Volume Down key
VK_VOLUME_UP = 0xAF             # Volume Up key
VK_MEDIA_NEXT_TRACK = 0xB0      # Next Track key
VK_MEDIA_PREV_TRACK = 0xB1      # Previous Track key
VK_MEDIA_STOP = 0xB2            # Stop Media key
VK_MEDIA_PLAY_PAUSE = 0xB3      # Play/Pause Media key
VK_LAUNCH_MAIL = 0xB4           # Start Mail key
VK_LAUNCH_MEDIA_SELECT = 0xB5   # Select Media key
VK_LAUNCH_APP1 = 0xB6           # Start Application 1 key
VK_LAUNCH_APP2 = 0xB7           # Start Application 2 key
VK_OEM_1 = 0xBA                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the ';:' key
VK_OEM_PLUS = 0xBB              # For any country/region, the '+' key
VK_OEM_COMMA = 0xBC             # For any country/region, the ',' key
VK_OEM_MINUS = 0xBD             # For any country/region, the '-' key
VK_OEM_PERIOD = 0xBE            # For any country/region, the '.' key
VK_OEM_2 = 0xBF                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '/?' key
VK_OEM_3 = 0xC0                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '`~' key
VK_OEM_4 = 0xDB                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '[{' key
VK_OEM_5 = 0xDC                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the '\|' key
VK_OEM_6 = 0xDD                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the ']}' key
VK_OEM_7 = 0xDE                 # Used for miscellaneous characters; it can vary by keyboard.
								# For the US standard keyboard, the 'single-quote/double-quote' key
VK_OEM_8 = 0xDF                 # Used for miscellaneous characters; it can vary by keyboard.
VK_OEM_102 = 0xE2               # Either the angle bracket key or the backslash key on the RT 102-key keyboard
VK_PROCESSKEY = 0xE5            # IME PROCESS key
VK_PACKET = 0xE7                # Used to pass Unicode characters as if they were keystrokes. The VK_PACKET key is the low word of a 32-bit Virtual Key value used for non-keyboard input methods. For more information, see Remark in KEYBDINPUT, SendInput, WM_KEYDOWN, and WM_KEYUP
VK_ATTN = 0xF6                  # Attn key
VK_CRSEL = 0xF7                 # CrSel key
VK_EXSEL = 0xF8                 # ExSel key
VK_EREOF = 0xF9                 # Erase EOF key
VK_PLAY = 0xFA                  # Play key
VK_ZOOM = 0xFB                  # Zoom key
VK_PA1 = 0xFD                   # PA1 key
VK_OEM_CLEAR = 0xFE             # Clear key

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP = 0x0002
KEYEVENTF_SCANCODE = 0x0008
KEYEVENTF_UNICODE = 0x0004

KEY_0 = 0x30
KEY_1 = 0x31
KEY_2 = 0x32
KEY_3 = 0x33
KEY_4 = 0x34
KEY_5 = 0x35
KEY_6 = 0x36
KEY_7 = 0x37
KEY_8 = 0x38
KEY_9 = 0x39
KEY_A = 0x41
KEY_B = 0x42
KEY_C = 0x43
KEY_D = 0x44
KEY_E = 0x45
KEY_F = 0x46
KEY_G = 0x47
KEY_H = 0x48
KEY_I = 0x49
KEY_J = 0x4A
KEY_K = 0x4B
KEY_L = 0x4C
KEY_M = 0x4D
KEY_N = 0x4E
KEY_O = 0x4F
KEY_P = 0x50
KEY_Q = 0x51
KEY_R = 0x52
KEY_S = 0x53
KEY_T = 0x54
KEY_U = 0x55
KEY_V = 0x56
KEY_W = 0x57
KEY_X = 0x58
KEY_Y = 0x59
KEY_Z = 0x5A

def KeybdInput(code, flags):
	return KEYBDINPUT(code, code, flags, 0, None)

def HardwareInput(message, parameter):
	return HARDWAREINPUT(message & 0xFFFFFFFF,
						 parameter & 0xFFFF,
						 parameter >> 16 & 0xFFFF)

def Mouse(flags, x=0, y=0, data=0):
	return Input(MouseInput(flags, x, y, data))

def Keyboard(code, flags=0):
	return Input(KeybdInput(code, flags))

def Hardware(message, parameter=0):
	return Input(HardwareInput(message, parameter))

################################################################################

import string

UPPER = frozenset('~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?')
LOWER = frozenset("`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")
ORDER = string.ascii_letters + string.digits + ' \b\r\t'
ALTER = dict(zip('!@#$%^&*()', '1234567890'))
OTHER = {'`': VK_OEM_3,
		 '~': VK_OEM_3,
		 '-': VK_OEM_MINUS,
		 '_': VK_OEM_MINUS,
		 '=': VK_OEM_PLUS,
		 '+': VK_OEM_PLUS,
		 '[': VK_OEM_4,
		 '{': VK_OEM_4,
		 ']': VK_OEM_6,
		 '}': VK_OEM_6,
		 '\\': VK_OEM_5,
		 '|': VK_OEM_5,
		 ';': VK_OEM_1,
		 ':': VK_OEM_1,
		 "'": VK_OEM_7,
		 '"': VK_OEM_7,
		 ',': VK_OEM_COMMA,
		 '<': VK_OEM_COMMA,
		 '.': VK_OEM_PERIOD,
		 '>': VK_OEM_PERIOD,
		 '/': VK_OEM_2,
		 '?': VK_OEM_2}

def keyboard_stream(string):
	mode = False
	for character in string.replace('\r\n', '\r').replace('\n', '\r'):
		if mode and character in LOWER or not mode and character in UPPER:
			yield Keyboard(VK_SHIFT, mode and KEYEVENTF_KEYUP)
			mode = not mode
		character = ALTER.get(character, character)
		if character in ORDER:
			code = ord(character.upper())
		elif character in OTHER:
			code = OTHER[character]
		else:
			continue
			raise ValueError('String is not understood!')
		yield Keyboard(code)
		yield Keyboard(code, KEYEVENTF_KEYUP)
	if mode:
		yield Keyboard(VK_SHIFT, KEYEVENTF_KEYUP)

################################################################################
class bButton ( wx.BitmapButton ):
	''''''
	def __init__ ( self, parent, button, bitmap):
		""""""
		id = wx.NewId ( )
		#imageFile = os.path.join(home,"images/editor_icon_16_2.png")
		#image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		
		wx.BitmapButton.__init__ ( self, parent, id,  bitmap=bitmap,size = (bitmap.GetWidth()+6, bitmap.GetHeight()+6) )
		self.button=button
		(self.whotocall, self.whotonotify, self.msg ) = button
		#self.whotocall = whotocall
		#self.whotonotify = whotonotify
		#self.msg = msg
		wx.EVT_BUTTON ( self, id, self.whotocall )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	#def OnClick ( self, event ):
	#	if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.button[2] )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.button[2] )

################################################################################		
class aTextCtrl ( wx.TextCtrl ):
	''''''
	def __init__ ( self, parent,  button,value, style, size):
		""""""
		id = wx.NewId ( )		
		wx.TextCtrl.__init__(self, parent, id, value=value, style=style, size=size )
		self.button=button
		( self.whotonotify, self.msg ) = button
		#self.whotocall = whotocall
		#self.whotonotify = whotonotify
		#self.msg = msg
		#wx.EVT_BUTTON ( self, id, self.whotocall )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	#def OnClick ( self, event ):
	#	if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.msg )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.msg )

################################################################################		
class aComboBox ( wx.ComboBox ):
	''''''
	def __init__ ( self, parent,  button,value,pos, size,  choices, style):
		""""""
		id = wx.NewId ( )		
		wx.ComboBox.__init__(self, parent, id, pos=pos, value=value, style=style, size=size,choices=choices)
		#panel, 500, sval, (-1, 150), (-1,-1), vals[k], wx.CB_DROPDOWN
		self.button=button
		( self.whotonotify, self.msg ) = button
		#self.whotocall = whotocall
		#self.whotonotify = whotonotify
		#self.msg = msg
		#wx.EVT_BUTTON ( self, id, self.whotocall )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	#def OnClick ( self, event ):
	#	if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.msg )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.msg )

		
################################################################################

#import time, sys
		
class UltListCtrl(ULC.UltimateListCtrl):

	def __init__(self, parent, log):

		ULC.UltimateListCtrl.__init__(self, parent, -1,
									  agwStyle=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES|ULC.ULC_SHOW_TOOLTIPS|ULC.ULC_NO_HEADER|ULC.ULC_SINGLE_SEL|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)

		self.log = log
		self.InsertColumn(0, 'Time')
		self.InsertColumn(1, 'Message')
		#self.SetColumnWidth(0, 50)
		#self.SetColumnWidth(1, 600)
		self.SetColumnWidth(0, 81)
		
		self.SetColumnWidth(0, ULC.ULC_AUTOSIZE_FILL)
		self.SetColumnWidth(1, ULC.ULC_AUTOSIZE_FILL)
		self.SetColumnToolTip(0,"Timestamp")
		self.SetColumnToolTip(1,"Log Message")
		#self.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL))
	
		if 0:
			#self.listCtrl_t.InsertStringItem(0, '/'.join(spath.split('/')[3:5]))
			self.InsertStringItem(0, 'time')
			#self.listCtrl.InsertStringItem(0, prof)
			self.SetStringItem(0, 1, 'test message')		
		if 0:
			self.il = wx.ImageList(16, 16)
			self.il.Add(images.Smiles.GetBitmap())
			self.il.Add(images.core.GetBitmap())
			self.il.Add(images.custom.GetBitmap())
			self.il.Add(images.exit.GetBitmap())
			self.il.Add(images.expansion.GetBitmap())

			self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

			self.InsertColumn(0, "First")
			self.InsertColumn(1, "Second")
			self.InsertColumn(2, "Third")
			self.SetColumnWidth(0, 175)
			self.SetColumnWidth(1, 175)
			self.SetColumnWidth(2, 175)
			self.SetColumnToolTip(0,"First Column Tooltip!")
			self.SetColumnToolTip(1,"Second Column Tooltip!")
			self.SetColumnToolTip(2,"Third Column Tooltip!")

			# After setting the column width you can specify that 
			# this column expands to fill the window. Only one
			# column may be specified.
			self.SetColumnWidth(2, ULC.ULC_AUTOSIZE_FILL)

			self.SetItemCount(50000)
			
			self.attr1 = ULC.UltimateListItemAttr()
			self.attr1.SetBackgroundColour(wx.NamedColour("yellow"))

			self.attr2 = ULC.UltimateListItemAttr()
			self.attr2.SetBackgroundColour(wx.NamedColour("light blue"))

		#self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected)
		#self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)
		#self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected)

		#self.randomLists = [GenerateRandomList(self.il) for i in xrange(5)]  
	def append(self, msg):

		items=self.GetItemCount()
		now=datetime.datetime.now()
		
		#self.listCtrl.InsertStringItem(0, prof)
		#print diR(t
		
		if type(msg) == types.ListType:
			self.appendList(items,now,msg)
		else:
			charge=msg.split(r'\n')
			self.appendList(items,now,charge)
		#self.EnsureVisible(items)
		self._mainWin.MoveToItem(self.GetItemCount()-1)
	def appendErr(self, msg):
		items=self.GetItemCount()
		now=datetime.datetime.now()
		
		#self.listCtrl.InsertStringItem(0, prof)
		#print diR(t
		
		if type(msg) == types.ListType:
			self.appendList(items,now,msg, True)
		else:
			charge=msg.split(r'\n')
			self.appendList(items,now,charge, True)
		#self.EnsureVisible(items)
		self._mainWin.MoveToItem(self.GetItemCount()-1)
	def appendList(self, items,now,charge, if_error=False):
		#print 'UltListCtrl.appendList'
		#pprint(charge)
		if len(charge)>1:
			for m in charge:
				idx=self.InsertStringItem(items, "%02d:%02d:%02d.%02d" % (now.hour,now.minute,now.second,now.microsecond/100))
				self.SetStringItem(idx, 1, m.strip('\n'))
				if if_error:
					item = self.GetItem(idx,1)
					item.SetMask(ULC.ULC_MASK_BACKCOLOUR)
					pink=wx.Colour(255, 168, 168, 255)
					item.SetBackgroundColour(pink) 
					self.SetItem(item)
				items +=1
		else:
			idx=self.InsertStringItem(items, "%02d:%02d:%02d.%02d" % (now.hour,now.minute,now.second,now.microsecond/100))
			#print 'idx=self.InsertStringItem', idx
			msg =charge[0].strip()
			#print 'msg =charge[0].strip()', msg
			if msg:
				s=self.SetStringItem(idx, 1, charge[0].strip())
				#print 's=self.SetStringItem(idx, 1, charge[0].strip())',s
				if if_error:
					item = self.GetItem(idx,1)
					item.SetMask(ULC.ULC_MASK_BACKCOLOUR)
					pink=wx.Colour(255, 168, 168, 255)
					item.SetBackgroundColour(pink)
					self.SetItem(item)
					
	def appendList_(self, items,now,charge, if_error=False):
		if len(charge)==1 and type(charge)==types.ListType and '\n' in charge[0]:
			charge=charge[0].split('\n')
		#pprint(charge)
		
		if len(charge)>1:
			for m in charge:
				self.InsertStringItem(items, "%02d:%02d:%02d.%02d" % (now.hour,now.minute,now.second,now.microsecond/100))
				self.SetStringItem(items, 1, m.strip('\n'))
				if if_error:
					item = self.GetItem(items,1)
					item.SetMask(ULC.ULC_MASK_BACKCOLOUR)
					pink=wx.Colour(255, 168, 168, 255)
					item.SetBackgroundColour(pink)
					self.SetItem(item)
				items +=1
		else:
			self.InsertStringItem(items, "%02d:%02d:%02d.%02d" % (now.hour,now.minute,now.second,now.microsecond/100))
			msg =charge[0].strip('\n')
			#pprint (msg)
			if msg:
				self.SetStringItem(items, 1, msg)
				if if_error:
					item = self.GetItem(items,1)
					item.SetMask(ULC.ULC_MASK_BACKCOLOUR)
					item.SetBackgroundColour('#FAAFBE')
					self.SetItem(item)
			
	def scrollDown(self):
		if self.logList.GetItemCount():
			self.logList._mainWin.MoveToItem(self.logList.GetItemCount()-1)


######################################################################################################
		
class SessionList(wx.ListCtrl):
	def __init__(self, splitter, parent, frame, id,pos, slib_path):
		wx.ListCtrl.__init__(self, splitter, id, style=
										wx.LC_REPORT
										)

		self.parent=parent
		images = [ 'images/arrow_sans_up_16.png', 'images/arrow_sans_down_16.png','images/arrow_sans_up_16.png', \
		'images/Right_Arrow_16.png', 'images/Left_Arrow_16.png', 'images/folder_16.png'  \
		 , 'images/config_16.png','images/database-sql_16.png', 'images/database_share_16.png', \
		 'images/database_connect_16.png','images/user_16.png','images/database_table_16.png', \
		'images/table_select_column_16.png','images/database_red_16.png',
		'images/database_green_16.png',
		'images/database_blue_16.png',
		'images/database_black_16.png','images/file_16.png',]
		self.images=[os.path.join(home,i) for i in images]
		
		#pprint(self.images)
		#e(0)
		self.image_refs={}
		self._bg='#e6f1f5'
		self._imgstart=3
		self.img_offset=0
		self.img_col = 1
		self._imgid=self._imgstart+1
		self.data={}
		self.img={}
		self.current_list=None
		self.connect_type=None
		self.pos=pos
		#slib_path, slib_name
		self.save_to_dir=slib_path #self.getLibPath(slib_name)
		#print self.save_to_dir
		assert os.path.isdir(self.save_to_dir), 'Library does not exists.'
		#	os.makedirs(self.save_to_dir)
		#self.db= OracleDb(self,pos)
		#EVT_SIGNAL(self, self.relaySignal)
		#self.file= FileDir(pos)
		self.il = wx.ImageList(16, 16)
		#self.sm_up = self.il.Add(images.SmallUpArrow.GetBitmap())
		#self.sm_dn = self.il.Add(images.SmallDnArrow.GetBitmap())		
		for i in range(len(self.images)):
			
			img=self.images[i]
			#print img
			self.il.Add(wx.Bitmap(img))
			self.image_refs[img]=i
		self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)	
		#self.setNavlist()		
		self.Bind(wx.EVT_CHAR, self.onKeyPress)	
		#self.Bind(wx.EVT_CHAR_HOOK, self.onKeyPress)
	#def getLibPath(self, slib_name):
	#	userhome = os.path.expanduser('~')
	#	slib_path=os.path.join(userhome,'sessions',slib_name)
	#	return slib_path
	def onKeyPress(self, event):
		#print 'pnl onKeyPress'
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()	
				send('disable_all_for_delete',())
			if kc == 19:
				print 'Ctrl-S 5'
				send('save_args',())				
				#self.Save()
			if	0 and kc == 4:
				print 'Ctrl-D 6'
				selected=tc.GetSelectedItems()
				#print selected
				#if selected:
				#	tc.tryToDelete()

		else:	
			#print 'kc=', kc
			if kc in [127]:
				tc.tryToDelete()
			elif kc in [13,32]:
				send('run_session',())
			event.Skip()
	def SelectAll(self):
		for idx in  range(self.GetItemCount()):
			self.SetItemState(idx, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	def tryToDelete(self):
		#print  'tryToDelete'
		items={}
		data =self.data[self.current_list]
		#pprint(data)
		selected=self.GetSelectedItems()
		#print selected
		names=[]
		for i in selected:
			#print '$$$$$',i
			ii=self.getItemInfo(i)
			#print i, self.sm.list.getItemInfo(i)
			#print data[i]
			key = ii[1] #pprint  (data[i])
			names.append(self.GetItemText(i))
			items[key]=os.path.join(data[i][-2],data[i][-1])
			#del data[i]
		#pprint (names)	
		#pprint (items)		
		msg='Delete these sessions?\n%s' % '\n'.join(names)
		if len(names)==1:
			msg='Delete this session?\n%s' % '\n'.join(names)
		if self.parent.frame.if_yes(msg):
			#print items
			#e(0)
			send('delete_sessions', (items))
			#if len(selected)==1:
			send('disable_all_for_delete',())
			self.parent.frame.btn_delete.Enable(False)
			self.parent.frame.btn_new.Enable(True)	
			
	def GetSelectedItems(self):
		"""    Gets the selected items for the list control.
		Selection is returned as a list of selected indices,
		low to high.
		"""
		selection = []
		index = self.GetFirstSelected()
		selection.append(index)
		while len(selection) != self.GetSelectedItemCount():
			index = self.GetNextSelected(index)
			selection.append(index)

		return selection	
	def onFocus(self, event):
		#print 'got Focus list',self.pos
		#print self.current_list
		#event.skip()
		self.buttons_set=False
	def onKillFocus(self, event):
		#print 'lost Focus list', self.pos	
		#print self.current_list
		#event.skip()	
		self.buttons_set=True
		
	def Populate(self):
		self.Freeze()
		self.current_list='ConfigList'
		#self.setCurrListName(self.root_list, 'forward')
		#self.setConfigList(('configDirLoc',))
		#self.Thaw()
		#self.root_list='ConfigList'
		#self.execList(self.root_list)
		#self.parent.add_nav_hist(self.root_list)
		self.Thaw()			
		
	def setFocus(self, id):
		if  self.GetItemCount():
			self.SetItemState(id, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
	def setFilter(self,value):
		#print(dir(self.parent.filter))
		self.parent.filter.SetValue(value)
	def _onSelect(self, event):
		#self.startIndex=event.m_itemIndex
		#print 'Selected!',event.m_itemIndex
		event.Skip()		

		
		
	def GetSelected(self):
		if self.GetFirstSelected()>-1:
			return self.GetItemText(self.GetFirstSelected())
		return None

	def setListData(self):
		j = 0
		for key,i in self.data[self.current_list].items():
			#print i
			#sys.exit(1)
			if  1:
				
				index=self.InsertStringItem(sys.maxint, str(i[0]))
				for col in range(1,self.GetColumnCount()):
					self.SetStringItem(j, col, str(i[col]))
					#self.SetStringItem(j, 2, str(i[2]))
					#self.SetStringItem(j, 3, str(i[3]) #time.strftime('%Y-%m-%d %H:%M', time.localtime(sec))
					#)
				self.SetItemData(index, key)

				#if i[1] == 'database':
				if 1:
					self.img[key]=self._imgstart+self.img_offset
					self.SetItemImage(index, self.img[key])	
	
				if (j % 2) == 0:
					self.SetItemBackgroundColour(j, self._bg)
				j += 1		
				#sys.exit(1)	
		self.parent.itemDataMap=self.data[self.current_list]
		#listmix.ColumnSorterMixin.__init__(self, self.GetColumnCount())

	def setEnvironmentList(self, vars):
		ConfigList='ORACLE.xml'
		#print configDirLoc,ConfigList
		config_file= '%s.xml' % os.path.join(configDirLoc,ConfigList )
		#print config_file
		#sys.exit(1)
		#e(0)
		#print config_file
		self.InsertColumn(0, 'Name')
		self.InsertColumn(1, 'Created')
		self.InsertColumn(2, 'To_Template')
		self.InsertColumn(3, 'From')		
		self.InsertColumn(4, 'To')
		
		self.InsertColumn(5, 'Type')
		self.InsertColumn(6, 'From_Template')
		#self.InsertColumn(4, 'Desription')

		self.SetColumnWidth(0, 270)
		self.SetColumnWidth(1, 120)
		self.SetColumnWidth(2, 130)
		self.SetColumnWidth(3, 60)
		self.SetColumnWidth(4, 60)
		self.SetColumnWidth(5, 60)
		self.SetColumnWidth(6, 120)

		#self.SetColumnWidth(4, 420)
		self.img_col = 1
		
		#self.il = uListCtrl.PyImageList(22,22)	
		#files = os.listdir('.')
		j = 0
		#self.idx_first=self.InsertStringItem(0, '[..]')
		#self.SetItemImage(0, self._imgstart+3)
		self.set_data()
		#print dbs
		#sys.exit(1)
		#print self.parent
		self.parent.RecreateList(None,(self.parent.list,self.parent.filter))
		#self.parent.list.Thaw()
	def set_data(self):
		#print 'set_data'
		flist=OrderedDict()
		i=0  
		os.chdir(self.save_to_dir)
		#print filter(os.path.isfile,os.listdir(self.save_to_dir))
		#print os.listdir(self.save_to_dir)
		#e(0)
		#print 'dir'
		#pprint(filter(os.path.isfile,os.listdir(self.save_to_dir)))
		
		
		for f in filter(os.path.isfile,os.listdir(self.save_to_dir)):
			#print f
			d= datetime.datetime.fromtimestamp(os.path.getmtime(f))
			dt= d.strftime('%Y-%m-%d %H:%M:%S')
			cv, tmpl,name= f.split(';')
			name=name.split('.')[0]
			#print name
			type='Copy'
			if tmpl.startswith('CSV'):
				type='Load'
			if '.CSV_' in tmpl:
				type='Spool'
			flist[i] = [name.strip(' '),dt,tmpl.split('.')[1],cv.split('.')[0],cv.split('.')[1],type,tmpl.split('.')[0],self.save_to_dir,f]
			i +=1
		#pprint(flist)
		self.data[self.current_list]= flist
		self.parent.itemDataMap=self.data[self.current_list]

	def getList(self):
		#print 'getlist'
		#pprint (self.data[self.current_list])
		return self.data[self.current_list]
	
					
	def setTableList(self, vars):
		self.ClearAll()
		self.setVars(vars)		
		#self.current_list='TableList'
		(user,db,pwd,host,port, object_filter) = self.getConnectInfo()
		#dbs=getTables((db,user),location)
		self.ClearAll()
		self.InsertColumn(0, 'Table')
		self.InsertColumn(1, 'Type')
		self.InsertColumn(2, 'Part')
		self.InsertColumn(3, 'Size, MB', wx.LIST_FORMAT_RIGHT)
		
		self.InsertColumn(4, 'Created')

		self.SetColumnWidth(0, 250)
		self.SetColumnWidth(1, 60)
		self.SetColumnWidth(2, 60)
		self.SetColumnWidth(3, 100)
		self.SetColumnWidth(4, 140)		
		#self.il = uListCtrl.PyImageList(22,22)	
		#files = os.listdir('.')
		j = 0
		#self.idx_first=self.InsertStringItem(0, '[..]')
		#self.SetItemImage(0, self._imgid+7)	
		self.img_offset=8	
		cl = self.parent.getVarsToPath()		
		
		self.data[self.current_list]=self.db.getTables((user,db,pwd,host,port),(self._OwnerList), object_filter, cache_loc=cl)

			
	def getItemInfo(self, idx):
		"""Collect all relevant data of a listitem, and put it in a list"""
		l = []
		#print idx
		l.append(idx) # We need the original index, so it is easier to eventualy delete it
		l.append(self.GetItemData(idx)) # Itemdata
		l.append(self.GetItemText(idx)) # Text first column
		for i in range(1, self.GetColumnCount()): # Possible extra columns
			l.append(self.GetItem(idx, i).GetText())
		return l	

########################################################################

class UltSessionLogger(wx.Panel):
	"""Panel for the Taco deploy xml log panel"""
	def __init__(self, parent, pos, style=1):
		wx.Panel.__init__(self, parent, -1, style=style)
		
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.parent=parent
		self.pos=pos
		#self.panel_id=panel_id
		#self.parentFrame=parent.frame
		#suffix=''
		#self.label = wx.StaticText(self, -1, 'Started code deployment.')
		#self.label.SetLabel("Hello World!")
		#self.label.SetHelpText('Deployment status.')
		self.log=cu.NullLog()
		self.logList = UltListCtrl(self,self.log)
		#print dir(self.logList)

		self.sizer.Add(self.logList, 1, wx.GROW|wx.ALL, 1)

		self.SetSizer(self.sizer)
		#self.sizer.Fit(self)
		#print self.logList._mainWin
		#Publisher().subscribe(self.OnAppendBLog, "append_browser_log")
		#Publisher().subscribe(self.OnAppendBErr, "append_browser_err")
		#sub(self.__OnAppendBLog, "append_browser_log")
		#sub(self.__OnAppendBErr, "append_browser_err")
		
	def Status(self, msg):
		self.label.SetLabel(msg)
		self.logger.AppendText(msg+'\n')
		#print(dir(self.logger))
		#sys.exit(1)
		
	def OnAppendBLog_del(self, evt):
		(msg,pos) = evt.data
		if pos==self.pos:
			self.logList.append(msg)
			
	def __OnAppendBLog(self, data, extra1, extra2=None):
		print '__OnAppendBLog'
		(msg,pos) = data
		if pos==self.pos:
			self.logList.append(msg)
			
	def __OnAppendBErr(self, data, extra1, extra2=None):
		print '__OnAppendBErr'
		(err,pos) = data
		if pos==self.pos:
			self.logList.appendErr(err)				

	def _OnExit(self,e):
		#Publisher().sendMessage( "refresh_list", (None) )
		send("refresh_list", (None))
		self.parentFrame.MakeModal(False)
		self.parentFrame.Close(True)

		
	def OnBackground(self,e):
		print 'OnBackground'
			
########################################################################
		
class SessionListCtrlPanel(wx.Panel, listmix.ColumnSorterMixin):
	def __init__(self, parent, frame, pos, panel_pos, slib_path
	):
		self.ID=wx.NewId()
		wx.Panel.__init__(self, parent, self.ID, style=wx.WANTS_CHARS)
		#self.SetDoubleBuffered(True)
		global app_title
		#self.ulocPanel= wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN, size=(-1,50))
		#wx.BoxSizer(wx.HORIZONTAL)
		self.url_locator={}
		self.find_in_btn={}
		self.nav_hist=[]
		self.curr_hist_id=0
		self._histMenu=None
		self._favMenu=None
		self._popUpMenu = {}
		self._recentMenu = {}
		self.slib=os.path.split(slib_path)[-1]
		(self.row, self.col) =pos
		self.pos=pos
		self.panel_pos=panel_pos
		#print panel_pos
		#sys.exit(1)
		self.sides={'00':'Left','02':'Right'}
		self.status='Welcome to %s!' % app_title
		self.count = {}
		self.root_status="ROOT: Double click on ORACLE to zoom into Table level."
		self.hist_btn=OrderedDict()
		#self.log = log		
		#print (type(parent.Parent))
		tID = wx.NewId()
		self.parent=parent
		self.frame=parent.frame
		#Publisher().subscribe(self.onUpdateLocation, "update_location")
		self.listsplit = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
		self.listsplit.SetOrientation(wx.VERTICAL)	
		if 1:
			sizer = wx.BoxSizer(wx.VERTICAL)
			
			if wx.Platform == "__WXMAC__" and \
				   hasattr(wx.GetApp().GetTopWindow(), "LoadDemo"):
				self.useNative = wx.CheckBox(self, -1, "Use native listctrl")
				self.useNative.SetValue( 
					not wx.SystemOptions.GetOptionInt("mac.listctrl.always_use_generic") )
				self.Bind(wx.EVT_CHECKBOX, self.OnUseNative, self.useNative)
				sizer.Add(self.useNative, 0, wx.ALL | wx.ALIGN_RIGHT, 4)
				
			self.il = wx.ImageList(16, 16)

			self.idx1 = self.il.Add(images.Smiles.GetBitmap())
			self.sm_up = self.il.Add(images.SmallUpArrow.GetBitmap())
			self.sm_dn = self.il.Add(images.SmallDnArrow.GetBitmap())

			self.list = SessionList(self.listsplit, self, frame, -1,self.pos, slib_path)
			

			self.filter =self.getFilter(self,self.list)
			self.filter_history={}
			self.currentItem = 0
		

		if 1:
			#self.btnHome = wx.Button(self, -1, "[.]", style=wx.BU_EXACTFIT, size=(30,20))
			#self.btnUp = wx.Button(self, -1, "[..]", style=wx.BU_EXACTFIT, size=(30,20))
			

			imageFile = os.path.join(home,"images/arrow_back_dgrey_16x2.png")
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			if 0:	
				self.btnFav = wx.Button(self, -1, 'Fav', style=wx.BU_EXACTFIT, size=(30,20))
			#self.btnHist = wx.Button(self, -1, "Hist", style=wx.BU_EXACTFIT, size=(30,20))	
			imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.btn_refresh=wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
			#self.btn_log = wx.Button(self, -1, "Log", size=(25,20))
			#self.btn_refresh = wx.Button(self, -1, "Refresh", size=(30,20)) 
			#self.sPanel.statusbar.Add([self.gauge[pos],self.btn_stop[pos]], 1, wx.EXPAND,1)
			#self.btn_stop[pos].Hide()
			#self.btn_refresh.SetPosition((1,1))
			self.gen_bind(wx.EVT_BUTTON,self.btn_refresh, self.OnBtnRefreshList,(self.pos))
			#self.btnFwd = wx.Button(self, -1, "Forward", style=wx.BU_EXACTFIT)
			navig = wx.BoxSizer(wx.HORIZONTAL)
			
			#navig.Add(self.btnHome, 0, wx.LEFT)
			#navig.Add(self.btnUp, 0, wx.LEFT)
			#navig.Add((5,5), 0, wx.LEFT)
			#navig.Add(self.btn_back, 0, wx.LEFT)
			#navig.Add((2,2), 0, wx.LEFT)
			#navig.Add(self.btn_fwd, 0, wx.LEFT)			
			#navig.Add((8,8), 0, wx.LEFT)
			#navig.Add(self.locator, 1, wx.LEFT)
			#navig.Add(self.btnFwd, 0, wx.LEFT)
			navig.Add(self.filter, 1, wx.EXPAND)
			
			#navig.Add(self.btnHist, 0, wx.LEFT)		
			#navig.Add(self.btnFav, 0, wx.LEFT)
			navig.Add(self.btn_refresh, 0, wx.LEFT)
			

			if 0:
				
				self.p_pos=[(0,0)]
				self.timer={}
				self.timer_xref={}
				if 1:
					for pos in self.p_pos:
						i=wx.NewId()
						self.timer_xref[i]=pos
						self.Bind(wx.EVT_TIMER, lambda event, i=i: self.TimerHandler0(event, the_id=i), id=i)
						self.timer[pos]=wx.Timer(self, id=i)
						#lambda event, i=i: self.Screens(event, the_id=i), id=i
						#self.gen_bind(wx.EVT_TIMER,self, self.TimerHandler,(pos))
						
				#items=[]
				#self.sPanel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN) # ,size=(300, 30)


		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
		self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnItemDeselected)
		self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list)

		self.list.Populate()
		if 1:
		
			sizer = wx.BoxSizer(wx.VERTICAL)
			#sizer.Add(self.locator, 0, wx.EXPAND)
			sizer.Add((2,2), 0, wx.EXPAND)
			#sizer.Add(upsizer, 0, wx.EXPAND)
			#sizer.Add((3,3), 0, wx.EXPAND)
			#sizer.Add(self.url_combo_list, 0, wx.EXPAND)
			sizer.Add(navig, 0, wx.EXPAND)
			#self.log = UltSessionLogger(self.listsplit,self.pos,self.ID)  #EmptyPanel(self.listsplit)
			(width,height) = wx.DisplaySize()
			#print wx.GetApp().GetSize()
			#print (width,height)
			#sys.exit(1)
			self.listsplit.AppendWindow(self.list,height*0.7 )				
			#self.listsplit.AppendWindow(self.log)	
			blog.log('Created %s config list' % (self.sides['%d%d' % self.pos]),self.pos)
			#msplitter.AppendWindow(self.panels[(0,2)],200)
			sizer.Add(self.listsplit, 1, wx.EXPAND,4)
			#sizer.Add(self.list, 1, wx.EXPAND,4)
			#sizer.Add(self.statusbar, 0,wx.EXPAND)
			
			
			
			if 'wxMac' in wx.PlatformInfo:
				sizer.Add((5,5))  # Make sure there is room for the focus ring
			self.SetSizer(sizer)
			#self.SetAutoLayout(True)

		self.list.setEnvironmentList(('configDirLoc','ConfigList',))
		sub(self.onRefreshList, "refresh_list")
		sub(self.OnAddSession, 'add_session')
		sub(self.onHighlightSession, "highlight_session")
		sub(self.onLowlightSession, "lowlight_session")
		sub(self.onDeleteSessions, "delete_sessions")

	def OnBtnRefreshList(self, event, params):
		print 'OnBtnRefreshList'
		self.list.set_data()
		self.RecreateList(None,(self.list,self.filter))
		
	def onHighlightSession(self, data, extra1, extra2=None):
		#print 'onHighlightSession'
		(sname,color) = data
		#print color, color		
		index = self.list.GetFirstSelected()
		if index>-1:
			iname = self.list.GetItemText(index).strip().strip(' ')
			#print '@'*60
			if sname in [iname]:
				#self.list.SetItemTextColour(index, color)
				i = self.list.GetItem(index)
				#print(dir(i))
				i.SetTextColour(color)
				self.list.SetItem(i)
				#print(dir( self.list))
				#e(0)
				#style = self.list.GetSingleStyle()
				#self.list.SetItemTextColour(index, color)
				#f = style.GetFont()
				if 1:
					f = self.list.GetItemFont(index)
					#style.SetTextColour(wx.BLUE)
					f.SetWeight(wx.BOLD)
					#style.SetFont(f)
					#f.SetColor(color)
					#pprint(dir(f))
					self.list.SetItemFont(index, f)
					#self.list.SetItem(i)
					#self.list.SetDefaultStyle(style)
					
					#self.listControl.SetItemTextColour(0, wx.RED)

			else:
				print 'Session name mismatch: [%s] != [%s]' % ( sname, iname)
	def onLowlightSession(self, data, extra1, extra2=None):
		#print 'onLowlightSession'
		(sname) = data		
		index = self.list.GetFirstSelected()
		if index>-1:
			iname = self.list.GetItemText(index)
			#print '@'*60
			if sname in [iname]:
				#i = self.list.GetItem(index)
				#i.SetTextColour(wx.BLACK)
				i = self.list.GetItem(index)
				#print(dir(i))
				i.SetTextColour(wx.BLACK)
				self.list.SetItem(i)
				
				f = self.list.GetItemFont(index)
				f.SetWeight(wx.FONTWEIGHT_NORMAL)
				self.list.SetItemFont(index, f)
				#self.list.SetItem(i)
			else:
				print 'Session name mismatch.', sname, iname
		
	def onDeleteSessions(self,  data, extra1, extra2=None):
		#(items) = data
		#print data
		#for i in items.keys():
			#self.list.DeleteItem(i)
		
		#self.list.DeleteAllItems()
		(items)=data
		for k,v in items.items():
			#print k, v
			sn= v.split(';')[-1].split('.')[0]
			#print sn
			if os.access(v, os.W_OK) and os.path.isfile(v):
				os.remove(v)
				#print 'removing', v, os.path.isfile(v)
				dir=os.path.join(os.path.dirname(v),sn)
				
				if os.access(dir, os.W_OK) and os.path.isdir(dir):
					#print 'removed', v
					shutil.rmtree(dir)
				
		self.list.set_data()
		self.RecreateList(None,(self.list,self.filter))

	def delete_seleted_items_remove(self):
		#print 'OnDeleteButton'
		#print self.list.GetSelectedItemCount()
		#print 
		for i in self.list.GetSelectedItems():
			self.list.DeleteItem(i)
							   
	def onRefreshList(self, data, extra1, extra2=None):
		
		#print 'onRefreshList'
		
		self.list.set_data()
		self.RecreateList(None,(self.list,self.filter))
	def OnAddSession(self, data, extra1, extra2=None):
		(sname,cv,tmpl,dname,fname,lib_name) = data
		#print lib_name	
		if lib_name in [self.slib]:
		
			self.Freeze()
			tmpl1,tmpl2=tmpl.split('.')
			s=[sname.strip(' '),tmpl2,cv[0],cv[1],'Copy',tmpl1,dname,fname]
			#add
			dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			idx= self.addSession(s[:1]+[dt]+s[1:]) 
			#deselect
			index = self.list.GetFirstSelected()
			while index != -1:
				self.list.SetItemState(index, 0, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED)
				index = self.list.GetNextSelected(index)
			#select
			#print 'selecting %s' % idx
			self.list.SetItemState(idx, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED) 
			self.list.EnsureVisible(idx) 
			
			#ss=(sname,tmpl2,cv[0],cv[1],'Copy',tmpl1,dname,fname)
			
			send('open_session',(s))
			self.parent.active_list= self.parent.nb.GetSelection()
			#self.SetItemState(idx, 0, wxLIST_STATE_SELECTED)
			self.Thaw()
			

	def OnUseCache(self, event):
		#print 'use cache', self.pos
		event.Skip()		
	def Status(self, msg):
		pass
		#self.stt.SetLabel(msg)
		
	def OnStopDbRequest(self, event, params):
		( pos) = params
		if pos==self.pos:
			#Publisher().sendMessage( "stop_db_request", (pos) )
			send("stop_db_request", (pos) )
		event.Skip()

	def OnFindInButton(self, event,params):
		(loc_id,loc)=params
		#print (loc_id,loc)
		#print dir(event)
		#btn=event.GetEventObject()
		#print btn.GetPosition()
		#print btn.GetSize()
		#print btn.GetPosition()[0]
		btn = event.GetEventObject()
		#import flat_menu2
		# Create the popup menu
		#self.CreateLongPopupMenu()
		#print 'creating PopupMenu((((((((((((', loc
		self.CreatePopupMenu(loc)

		# Postion the menu:
		# The menu should be positioned at the bottom left corner of the button.
		btnSize = btn.GetSize()

		# btnPt is returned relative to its parent 
		# so, we need to convert it to screen 
		btnPt  = btn.GetPosition()
		btnPt = btn.GetParent().ClientToScreen(btnPt)
		#self._longPopUpMenu.SetOwnerHeight(btnSize.y)
		#self._longPopUpMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
		self._popUpMenu[loc].SetOwnerHeight(btnSize.y)
		self._popUpMenu[loc].Popup(wx.Point(btnPt.x, btnPt.y), self)		

	def CreatePopupMenu(self,loc):

		if self._popUpMenu.has_key(loc):
			#print self.list.data[loc]
			pmenu=FM.FlatMenu()
			self._popUpMenu[loc] = pmenu
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			#subMenu = FM.FlatMenu()
			#subSubMenu = FM.FlatMenu()
			id=wx.ID_ANY
			# Create the menu items
			#print self.pos
			#print loc
			#print self.list.data.keys()
			if loc in self.list.data.keys():
				for key, item in self.list.data[loc].items():
					menuItem = FM.FlatMenuItem(pmenu, 20001+key, '%s' % item[0], "", wx.ITEM_RADIO)
					#print item[0], self.list.nav_list['vars'][loc],  item[0]==self.list.nav_list['vars'][loc]
					pmenu.AppendItem(menuItem)				
					if item[0]==self.list.nav_list['vars'][loc]:
						#pprint(dir(menuItem))
						menuItem.Check(True)
						#subMenu.UpdateItem(menuItem)
						#print menuItem.IsChecked(), menuItem.IsCheckable()
						#menuItem.Enable(False)
					#pmenu.AppendRadioItem(wx.ID_ANY,menuItem)

					#print menuItem.isChecked()
					#print menuItem.IsChecked(), menuItem.IsChecked()
					#menuItem.Enable(True)
					self.Bind(FM.EVT_FLAT_MENU_SELECTED, self.OnMenu, id=20001+key)
					#
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(loc,item[0]))
				
			
	def OnMenu(self, event,params):	
		(loc,item) = params
		#print event.GetEventObject()
		#print(dir(event.GetEventObject()))
		item_id=event.GetId()-20001
		#print item_id
		#self.list.nav_list['vars'][loc]=
		#print self.list., self.list.data[loc][item_id]
		#print  params
		self.list.nav_list['vars'][loc]=item
		self.list.execList(self.list.current_list)
		self._popUpMenu.pop(loc)
		
	def CreatePopupMenu0(self):

		if not self._popUpMenu:
		
			self._popUpMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			subMenu = FM.FlatMenu()
			subSubMenu = FM.FlatMenu()

			# Create the menu items
			menuItem = FM.FlatMenuItem(self._popUpMenu, 20001, "First Menu Item", "", wx.ITEM_CHECK)
			self._popUpMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(self._popUpMenu, 20002, "Sec&ond Menu Item", "", wx.ITEM_CHECK)
			self._popUpMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(self._popUpMenu, wx.ID_ANY, "Checkable-Disabled Item", "", wx.ITEM_CHECK)
			menuItem.Enable(False)
			self._popUpMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(self._popUpMenu, 20003, "Third Menu Item", "", wx.ITEM_CHECK)
			self._popUpMenu.AppendItem(menuItem)

			self._popUpMenu.AppendSeparator()

			# Add sub-menu to main menu
			menuItem = FM.FlatMenuItem(self._popUpMenu, 20004, "Sub-&menu item", "", wx.ITEM_NORMAL, subMenu)
			self._popUpMenu.AppendItem(menuItem)

			# Create the submenu items and add them 
			menuItem = FM.FlatMenuItem(subMenu, 20005, "&Sub-menu Item 1", "", wx.ITEM_NORMAL)
			subMenu.AppendItem(menuItem)
		
			menuItem = FM.FlatMenuItem(subMenu, 20006, "Su&b-menu Item 2", "", wx.ITEM_NORMAL)
			subMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(subMenu, 20007, "Sub-menu Item 3", "", wx.ITEM_NORMAL)
			subMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(subMenu, 20008, "Sub-menu Item 4", "", wx.ITEM_NORMAL)
			subMenu.AppendItem(menuItem)

			# Create the submenu items and add them 
			menuItem = FM.FlatMenuItem(subSubMenu, 20009, "Sub-menu Item 1", "", wx.ITEM_NORMAL)
			subSubMenu.AppendItem(menuItem)
		
			menuItem = FM.FlatMenuItem(subSubMenu, 20010, "Sub-menu Item 2", "", wx.ITEM_NORMAL)
			subSubMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(subSubMenu, 20011, "Sub-menu Item 3", "", wx.ITEM_NORMAL)
			subSubMenu.AppendItem(menuItem)

			menuItem = FM.FlatMenuItem(subSubMenu, 20012, "Sub-menu Item 4", "", wx.ITEM_NORMAL)
			subSubMenu.AppendItem(menuItem)

			# Add sub-menu to submenu menu
			menuItem = FM.FlatMenuItem(subMenu, 20013, "Sub-menu item", "", wx.ITEM_NORMAL, subSubMenu)
			subMenu.AppendItem(menuItem)			
	def CreateLongPopupMenu(self):

		if hasattr(self, "_longPopUpMenu"):
			return

		self._longPopUpMenu = FM.FlatMenu()
		sub = FM.FlatMenu()
		
		#-----------------------------------------------
		# Flat Menu test
		#-----------------------------------------------
		
		for ii in xrange(30):
			if ii == 0:
				menuItem = FM.FlatMenuItem(self._longPopUpMenu, wx.ID_ANY, "Menu Item #%ld"%(ii+1), "", wx.ITEM_NORMAL, sub)
				self._longPopUpMenu.AppendItem(menuItem)

				for k in xrange(5):

					menuItem = FM.FlatMenuItem(sub, wx.ID_ANY, "Sub Menu Item #%ld"%(k+1))
					sub.AppendItem(menuItem)

			else:

				menuItem = FM.FlatMenuItem(self._longPopUpMenu, wx.ID_ANY, "Menu Item #%ld"%(ii+1))
				self._longPopUpMenu.AppendItem(menuItem)
				
	def OnMouseEvent1(self, event):
		self.url_combo_list.Show()
		#self.url_combo_list.Focus()
		self.url_combo_list.Refresh()
		event.Skip()
	def OnItemDeselected(self, evt):
		#print OnItemDeselected
		item = evt.GetItem()
		cnt=self.list.GetSelectedItemCount()
		#print cnt
		if cnt==0:
			send('disable_all',())
			#self.btn_delete.Enable(False)
			#onDisableAllForDelete
			#self.parent.DisableAll()
			#"disable_all_for_delete"
		#print 'GetSelectedItemCount',cnt
			
	def OnItemSelected(self, event):
		##print event.GetItem().GetTextColour()
		#cnt=self.list.GetSelectedItemCount()
		sel= self.list.GetSelectedItems()
		#self.Freeze()
		if len(sel)==1:
			#self.frame.saveArgs()
			#print '---------------', 
			#send('save_args',())
			if self.frame.changed: # or self.frame.output_panel.changed: #or self.frame.editor_panel.Changed():
				if self.frame.if_yes('Save changes to %s?' % (self.frame.session_name)):
					#,fname)=self.frame.saveSession() 
					#send('save_args',())
					#send('open_session',(session))
					(sname,cv,tmpl,dname,fname)=self.parent.frame.saveSession(slib_name=self.parent.getActiveLibName())
				else:
					self.frame.restore_changed_args()
			else:
				if not self.parent.frame.saved:
					(sname,cv,tmpl,dname,fname)=self.parent.frame.saveSession(slib_name=self.parent.getActiveLibName())
			
			#self.currentItem = event.m_itemIndex
			#print self.currentItem
			#idx=self.list.GetFirstSelected()
			#selected idx
			idx=sel[0]
			#pprint(selected)
			self.openSessionByItemId(idx)
		#else:
		#	send('disable_all_for_delete',(cnt))
		#self.Thaw()
		event.Skip()		
	def openSessionByItemId(self, idx):
		#print self.currentItem
		#print 'idx',idx
		ii=self.list.GetItemData(idx)
		s= self.list.getList()[ii]
		session=s[:1]+s[2:]
		#pprint (s)
		#session= [s[0],s[2],s[3],s[4],'%s.%s' % (s[5],s[1]),s[6],s[7]]
		#pprint (session)
		#e(0)
		#print self.frame.session_name
		#print self.frame.session_name,session[0]
		#print 'self.frame.changed', self.frame.changed
		
		if not self.frame.session_name==session[0]:
			if 0 and self.frame.changed: # or self.frame.output_panel.changed: #or self.frame.editor_panel.Changed():
				if self.frame.if_yes('Save changes to %s?' % (self.frame.session_name)):
					#,fname)=self.frame.saveSession() 
					send('save_args',())
					send('open_session',(session))
				else:
					self.frame.restore_changed_args()
					
					send('open_session',(session))
			else:
				#print 'session:'
				#pprint(session)
				send('open_session',(session))
		else:
			send('enable_all',())	
	
		
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
	def __onGaugeStop(self,data, extra1, extra2=None):
		( pos) = data
		if pos==self.pos:		
			#print 'onGaugeStop', pos
			self.gaugeStop(pos)	
			#self.gauge[pos].Hide()
			#self.btn_stop[pos].Hide()			
	def __onGaugeStart(self,data, extra1, extra2=None):
		( pos) = data
		#print '=============================onGaugeStart',pos,self.pos
		if pos==self.pos:		
			#self.sPanel.SetSizer(self.sPanel.statusbar)
			#print 'onGaugeStart',pos
			self.gaugeStart(pos)
			#self.gauge[pos].Show()
			#self.btn_stop[pos].Show()			
		
	def gaugeStart(self,pos):
		#print pos
		#print self.gauge
		#print  'gaugeStart'
		if pos==self.pos:		
			#self.stt.Hide()
			#self.gauge[pos].Show()
			#self.btn_stop[pos].Show()
			self.timer[pos].Start(100)
			self.count[pos] = 0  
	def gaugeStop(self,pos):
		if pos==self.pos:	
			self.timer[pos].Stop()
			self.count[pos] = 0 
			#self.gauge.Freeze()
			#self.gauge[pos].Hide()
			#self.btn_stop[pos].Hide()
			#self.stt.Show()	
			#tmpitem = self.statusbar.GetChildren()
			#print tmpitem
			#self.statusbar.Replace ( 0, tmpitem[2])
			#self.sPanel.SetSizer(self.sPanel.status)			
	def __del__(self):
		for pos in self.panel_pos:
			self.timer[pos].Stop()
	def TimerHandler0(self, event,the_id):
		#(pos)=params
		pos=self.timer_xref[the_id]
		#print 'the_id', the_id,pos
		self.count[pos] = self.count[pos] + 15
		#wx.CallAfter(self.gauge[pos].SetValue, self.count[pos])
		if self.count[pos] >= 180:
			self.count[pos] = 0
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count
		wx.CallAfter(self.gauge[pos].SetValue, self.count[pos])
		
		#self.gauge.Pulse()
		
	def TimerHandler_pos(self, event,params):
		(pos)=params
		self.count = self.count + 15

		if self.count >= 180:
			self.count = 0
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count
		pos=self.panel_pos[0]
		self.gauge[pos].SetValue(self.count)
		#self.gauge.Pulse()
		
	def TimerHandler_(self, event,params):
		(pos)=params
		self.count[pos] = self.count[pos] + 15

		if self.count[pos] >= 180:
			self.count[pos] = 0
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count[pos]
		self.gauge[pos].SetValue(self.count[pos])
		#self.gauge.Pulse()
		
	def onShowProgress(self, evt):
		if 0:
			self.progress_bar.Show()
			self.progress_bar.SetRange(10)
			#print 'in ShowProgress'
			self.progress_bar.SetValue(5)
			#print (dir(self.progress_bar))
		self.gauge.Show()
	def OnClose(self, event):

		#self.ticker.Stop()
		self.Destroy()

	def OnSize1(self, event):
		size = self.GetSize()
		#print 'Size event'
		#self.splitter.SetSashPosition(size.x / 2)
		#self.sb.SetStatusText(os.getcwd())
		event.Skip()


	def OnDoubleClick(self, event):
		global prog
		size =  self.GetSize()
		self.splitter.SetSashPosition(size.x / 2)

		self.statusbar = ESB.EnhancedStatusBar(self, -1)
		self.statusbar.SetSize((-1, 23))
		self.statusbar.SetFieldsCount(7)
		self.SetStatusBar(self.statusbar)        
		self.statusbar.SetStatusWidths([50, 50, 100, 120, 120, 140, -1])

		bmp = wx.ArtProvider_GetBitmap(wx.ART_ERROR,
									   wx.ART_TOOLBAR, (16,16))
		
		upbmp = wx.StaticBitmap(self.statusbar, -1, bmp)

		bmp = wx.ArtProvider_GetBitmap(wx.ART_HELP,
									   wx.ART_TOOLBAR, (16,16))
		
		downbmp = wx.StaticBitmap(self.statusbar, -1, bmp)
		btnmio = wx.Button(self.statusbar, -1, "Push Me!")
		gauge = wx.Gauge(self.statusbar, -1, 50)
		choice = wx.Choice(self.statusbar, -1, size=(100,-1),
						   choices=['Hello', 'World!', 'What', 'A', 'Beautiful', 'Class!'])
		ticker = Ticker(self.statusbar, -1)
		ticker.SetText("Hello World!")
		ticker.SetBackgroundColour(wx.BLUE)
		ticker.SetForegroundColour(wx.NamedColour("YELLOW"))
		ticker.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))
		statictext = wx.StaticText(self.statusbar, -1, "Welcome To %s!" % prog)
		
		self.ticker = ticker
		self.gauge = gauge

		self.count = 0        
		
		statusbarchildren = self.statusbar.GetChildren()
		for widget in statusbarchildren:
			self.statusbar.AddWidget(widget)

		self.Bind(wx.EVT_IDLE, self.IdleHandler)
		self.Bind(wx.EVT_CLOSE, self.OnClose)


	def IdleHandler(self, event):
		
		self.count = self.count + 1

		if self.count >= 100:
			self.count = 0

		self.gauge[pos].SetValue(self.count)
		

		
	def onFileDirEvent(self, evt):
		#print 'onFileDirEvent'
		(st, pos,cache,result) = evt.data
		#print '--onFileDirEvent', st
		#print self.pos,'==',pos
		if st=='done':
			if self.pos==pos:
				#(status, err, rowcount,headers, out) = result
				
				data=result

				self.list.data[self.list.current_list]=data
				self.itemDataMap=self.list.data[self.list.current_list]
				
				self.RecreateList(None,(self.list,self.filter))				
				#self.setListData()
				self.list.Thaw()
				listmix.ColumnSorterMixin.__init__(self, self.list.GetColumnCount())
		if st=='xml_list':
			if self.pos==pos:
				self.list.data[self.list.current_list]=result
				self.itemDataMap=self.list.data[self.list.current_list]
				self.RecreateList(None,(self.list,self.filter))	
		if st=='aborted':
			#print '-----------request aborted',self.pos,pos
			if self.pos==pos:
				#print 'request aborted',pos
				self.gaugeStop(self.pos)	
				self.list.Thaw()
		#if self.pos==pos:
		#	updateCache(cache,self.list.data)
		
	def onRefreshListEvent(self, evt):
		#print 'onRefreshListEvent'
		(st, pos,cache,result) = evt.data
		#print 'onRefreshListEvent', st
		#print self.pos,'==',pos
		if st=='xml_list':
			if self.pos==pos:
				self.list.data[self.list.current_list]=result
				self.itemDataMap=self.list.data[self.list.current_list]
				self.RecreateList(None,(self.list,self.filter))	
		#if self.pos==pos:
		#	updateCache(cache,self.list.data)		


	def OnHome(self, event):
		#print 'Clicked OnHome'
		#Publisher().sendMessage( "go_home", (self.pos) )
		send("go_home", (self.pos))
	def OnUp(self, event):
		#print 'Clicked OnBack'
		#Publisher().sendMessage( "go_up", (self.pos) )
		send("go_up", (self.pos))

	def onForceSearch(self, evt):
		(position, fltr)=evt.data
		if position!=self.pos:
			#print '----------------onForceSearch', position, fltr
			self.filter.SetValue(fltr)
		

		
	def getFilter(self,parent,list):
		#self.treeMap[ttitle] = {}
		self.searchItems={}
		#print _tP
		#tree = TacoTree(parent,images,_tP)
		filter = wx.SearchCtrl(parent, style=wx.TE_PROCESS_ENTER)
		filter.ShowCancelButton(True)
		#filter.Bind(wx.EVT_TEXT, self.RecreateTree)
		self.gen_bind(wx.EVT_TEXT,filter, self.RecreateList,(list,filter))
		#filter.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnSearchCancelBtn)
		self.gen_bind(wx.EVT_SEARCHCTRL_CANCEL_BTN,filter, self.OnSearchCancelBtn,(list, filter))
		self.gen_bind(wx.EVT_TEXT_ENTER,filter, self.OnSearch,(list, filter))
		searchMenu = wx.Menu()
		item = searchMenu.AppendRadioItem(-1, "All")
		#self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
		self.gen_bind(wx.EVT_MENU, item,self.OnSearchMenu,(list, filter))

		item = searchMenu.AppendRadioItem(-1, "Copy")
		#self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
		self.gen_bind(wx.EVT_MENU, item,self.OnSearchMenu,(list, filter))
		item = searchMenu.AppendRadioItem(-1, "Extract")
		#self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
		self.gen_bind(wx.EVT_MENU, item,self.OnSearchMenu,(list, filter))
		item = searchMenu.AppendRadioItem(-1, "Load")
		#self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
		self.gen_bind(wx.EVT_MENU, item,self.OnSearchMenu,(list, filter))
		
		filter.SetMenu(searchMenu)		


		#self.RecreateTree(None, (tree, filter,ttitle,_tP,_tL))
		#tree.SetExpansionState(self.expansionState)
		#tree.Bind(wx.EVT_TREE_ITEM_EXPANDED, self.OnItemExpanded)
		#self.gen_bind(wx.EVT_TREE_ITEM_EXPANDED, tree, self.OnItemExpanded,(tree))
		#tree.Bind(wx.EVT_TREE_ITEM_COLLAPSED, self.OnItemCollapsed)
		#self.gen_bind(wx.EVT_TREE_ITEM_COLLAPSED,tree, self.OnItemCollapsed,(tree))
		#tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged)
		#self.gen_bind(wx.EVT_TREE_SEL_CHANGED, tree,self.OnSelChanged,(tree,filter,ttitle))
		#tree.Bind(wx.EVT_LEFT_DOWN, self.OnTreeLeftDown)
		#self.gen_bind(wx.EVT_LEFT_DOWN, tree,self.OnTreeLeftDown, (ttitle) )
		#self.BuildMenuBar(_tL,ttitle)
		return filter
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)	
	def OnSearchMenu(self, event, tparams):
		(tree, filter)=tparams
		# Catch the search type (name or content)
		searchMenu = filter.GetMenu().GetMenuItems()
		fullSearch = searchMenu[1].IsChecked()
		fltr=filter.GetValue()
		if 1:
			if fullSearch:
				#print 'OnSearchMenu/fullSearch'
				#Publisher().sendMessage( "force_search", (self.pos,fltr) )
				send("force_search", (self.pos,fltr) )
				self.OnSearch(None,tparams)
			else:
				self.RecreateList(None,tparams)

		#self.RecreateList(None,tparams)
			
	def OnSearch(self, event, tf):
		#search in every list
		
		(list, filter) = tf
		fltr = filter.GetValue()
		#print 'OnSearch',fltr, self.searchItems
		self.filter_history[list.current_list]=fltr
		searchItems=self.searchItems
		if not fltr:
			self.RecreateList(None,(list, filter))
			return

		wx.BeginBusyCursor()		
	
		#searchItems=[item for item in list.data.values() if fltr.lower() in str(item[0]).lower()]
	
		self.RecreateList(None,(list, filter)) 
		wx.EndBusyCursor()
		 

	def OnSearchCancelBtn(self, event,tf):
		(list, filter) = tf
		self.filter.SetValue('')
		self.filter_history[list.current_list]=''
		self.OnSearch(event,tf)
		
	def setPanel(self):
		self.list =self.getTree(self.leftPanel[ttitle],ttitle,_tacoPngs,_treeList,xml_projRootLoc)
		self.filter[ttitle] =self.getFilter(self.leftPanel[ttitle],self.tree[ttitle],ttitle,_tacoPngs,_treeList)
		self.RecreateTree(None, (self.tree[ttitle], self.filter[ttitle],ttitle,_tacoPngs,_treeList,'%s/%s' % (user,db)))
		leftBox = wx.BoxSizer(wx.VERTICAL)
		leftBox.Add(self.tree[ttitle], 1, wx.EXPAND)
		#leftBox.Add(wx.StaticText(leftPanel, label = "Filter Files:"), 0, wx.TOP|wx.LEFT, 5)
		leftBox.Add(self.filter[ttitle], 0, wx.EXPAND|wx.ALL, 5)
		if 'wxMac' in wx.PlatformInfo:
			leftBox.Add((5,5))  # Make sure there is room for the focus ring
		self.leftPanel[ttitle].SetSizer(leftBox)
	def addSession(self,session):
		item_mask='%s'
		index=self.list.InsertStringItem(sys.maxint, item_mask % session[0])
		for idx in range(1,len(session)-2):
			self.list.SetStringItem(index, idx, str(session[idx]))
		
		key=len(self.list.data[self.list.current_list])
		self.list.data[self.list.current_list][key]=session
		self.list.SetItemData(index,key)
		imgs= {'default':'images/database_green_16.png', 'DEV':'images/database_green_16.png','PROD':'images/database_red_16.png', \
		'UAT':'images/database_blue_16.png','QA':'images/database_black_16.png'}
		imgs={k:os.path.join(home,v) for k,v in imgs.items()}
		img_type_col_id= self.list.img_col
		img_type = 'DEV'
		img_name=None
		if imgs.has_key(img_type):
			img_name=imgs[img_type]
		else:
			img_name=imgs['default']
		#print img_name
		img_id=self.list.image_refs[img_name]
		self.list.img[key]=img_id
		self.list.SetItemImage(index, self.list.img[key])
		#print 'SetItemImage',index,key,list.img[key]		
		return index
	def getIdFromText(self, item_text):
		for i in range(self.list.GetItemCount()):
			if self.list.GetItemText(i) == item_text:
				return i
		return -1
	def RecreateList(self, evt=None, tf=None):
		# Catch the search type (name or content)
		cl =self.list.current_list
		#print '############# in RecreateList', self.pos,'cl:', cl
		(list, filter) = tf
		fltr = filter.GetValue()
		favs={}
		#print fltr
		#print self.list.current_list, 1
		#btns=self.list.nav_list[self.list.current_list]['hot_keys']
		#Publisher().sendMessage( "set_buttons", (self.list.pos,btns) )
		if 1:
			searchMenu = filter.GetMenu().GetMenuItems()
			fullSearch = searchMenu[1].IsChecked()
			searchItems=self.searchItems
			if evt:
				if fullSearch:
					#print 'RecreateList/fullSearch'
					#Publisher().sendMessage( "force_search", (self.pos,fltr) )
					send("force_search", (self.pos,fltr))
					# Do not`scan all the demo files for every char
					# the user input, use wx.EVT_TEXT_ENTER instead
					#return

			#expansionState = list.GetExpansionState()

			current = None
			#print(dir(list))
			#print list.GetSelectedItemCount()
			if 0:
				item = list.GetSelection()
				if item:
					prnt = list.GetItemParent(item)
					if prnt:
						current = (list.GetItemText(item),
								   list.GetItemText(prnt))
						
			#list.Freeze()
			
			#self.root = list.AddRoot(activeProjName)
			#list.SetItemImage(self.root, 0)
			#list.SetItemPyData(self.root, 0)

			treeFont = list.GetFont()
			catFont = list.GetFont()

			# The old native treectrl on MSW has a bug where it doesn't
			# draw all of the text for an item if the font is larger than
			# the default.  It seems to be clipping the item's label as if
			# it was the size of the same label in the default font.
			if 'wxMSW' not in wx.PlatformInfo or wx.GetApp().GetComCtl32Version() >= 600:
				treeFont.SetPointSize(treeFont.GetPointSize()+2)
				treeFont.SetWeight(wx.BOLD)
				catFont.SetWeight(wx.BOLD)
				
			#list.SetItemFont(self.root, treeFont)
			
			firstChild = None
			selectItem = None
			
			count = 0
			
			#for key, items in list.data.items():
			#items=list.data.values()
			if fltr:
				 self.filter_history[list.current_list]=fltr

			item_mask='%s'
			#print 'RecreateList'
			#print list.data[list.current_list]
			if 1:
				count += 1
				if fltr:
					if 0 and fullSearch:
						items = searchItems[category]
					else:
						keys = [key for key,item in list.data[list.current_list].items() if fltr.lower() in str(item[0]).lower()]
				else:
					keys = [key for key,item in list.data[list.current_list].items()]
				#print keys
				#print list.data[list.current_list].items()
				list.DeleteAllItems()
				if keys:
					#print keys
					j=0
					
					#pprint(list.data[list.current_list])
					for key in keys:
						#print 'key',key
						
						i= list.data[list.current_list][key]
						#print 'i',i
						#e(0)
						if  1:
							index=list.InsertStringItem(sys.maxint, item_mask % i[0])
							for idx in range(1,len(i)-2):
								#print 'idx', idx
								#print i[idx]
								list.SetStringItem(index, idx, str(i[idx]))


							list.SetItemData(index,key)
							
							keycolid=0
							if favs.has_key(i[keycolid]):
								item = list.GetItem(index)
								font = item.GetFont()
								font.SetWeight(wx.FONTWEIGHT_BOLD)
								item.SetFont(font)
								# This does the trick:
								list.SetItem(item)
							

							#if i[1] == 'xml':
							#print list._imgstart,list.img_offset
							imgs= { 'default':'images/database_green_16.png', 
									'DEV':'images/database_green_16.png',
									'PROD':'images/database_red_16.png',
									'UAT':'images/database_blue_16.png',
									'QA':'images/database_black_16.png'}
							imgs={k:os.path.join(home,v) for k,v in imgs.items()}
							img_type_col_id= self.list.img_col
							img_type = i[img_type_col_id]
							img_name=None
							if imgs.has_key(img_type):
								img_name=imgs[img_type]
							else:
								img_name=imgs['default']
							#print img_name
							img_id=self.list.image_refs[img_name]
							list.img[key]=img_id
							list.SetItemImage(index, list.img[key])
							#print 'SetItemImage',index,key,list.img[key]
							if 0:
								if (j % 2) == 0:
									list._bg='#e6f1f5'
									list.SetItemBackgroundColour(index, list._bg)
							j += 1				
					if 0:
						child = list.AppendItem(self.root, category, image=count)
						list.SetItemFont(child, catFont)
						list.SetItemPyData(child, count)
						if not firstChild: firstChild = child
						for childItem in items:
							image = count
							if DoesModifiedExist(childItem):
								image = len(_tP)
							theDemo = list.AppendItem(child, childItem, image=image)
							list.SetItemPyData(theDemo, count)
							self.treeMap[ttitle][childItem] = theDemo
							#if current and (childItem, category) == current:
							#	selectItem = theDemo
							
						

			#print 'list.Thaw()'
			#print (dir(list))
			#print list.pos

			searchItems = {}		
			listmix.ColumnSorterMixin.__init__(self, self.list.GetColumnCount())
			out=''
			max_len=15
			dots=''
			if not out:
				out =self.root_status
			sb=self.status
			if not sb:
				sb=cl
				if not sb:
					sb='Douple click on pipeline file.'

			send( "update_status_bar", (sb,self.pos))
	
	def CreateBackMenu(self):

		if 1:
			#print self.list.data[loc]
			pmenu=FM.FlatMenu()
			self._backMenu = pmenu
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			#subMenu = FM.FlatMenu()
			#subSubMenu = FM.FlatMenu()
			id=wx.ID_ANY
			# Create the menu items
			#(path, loc_to) = self.nav_hist[self.curr_hist_id]
			#relative_path=self.getVarsToPath()
			for id in range(len(self.nav_hist)):
				if id<self.curr_hist_id:
					tup=self.nav_hist[id]
					(loc_to, path)=tup
					#loc_to=self.hist_btn[path]
					itype=wx.ITEM_NORMAL
					if id==self.curr_hist_id:
						itype=wx.ITEM_CHECK
					menuItem = FM.FlatMenuItem(pmenu, wx.ID_ANY, '%s' % ( path), "", itype)
					#print item[0], self.list.nav_list['vars'][loc],  item[0]==self.list.nav_list['vars'][loc]
					pmenu.AppendItem(menuItem)				
					if id==self.curr_hist_id:
						menuItem.Check(True)
						#subMenu.UpdateItem(menuItem)
						#print menuItem.IsChecked(), menuItem.IsCheckable()
						#menuItem.Enable(False)
					#pmenu.AppendRadioItem(wx.ID_ANY,menuItem)

					#print menuItem.isChecked()
					#print menuItem.IsChecked(), menuItem.IsChecked()
					#menuItem.Enable(True)
					#self.Bind(FM.EVT_FLAT_MENU_SELECTED, self.OnMenu, id=20001+key)
					#
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnBackMenu,(id,loc_to,path))		
	def OnBackMenu(self, event, params):
		(id,loc_to,path) = params
		#print event.GetEventObject()
		#print(dir(event.GetEventObject()))
		#item_id=event.GetId()-21001
		#print item_id
		#self.list.nav_list['vars'][loc]=
		#print self.list., self.list.data[loc][item_id]
		#print  params
		#self.list.nav_list['vars'][loc]=item
		#list_to=
		#print (loc_to,path)
		self.curr_hist_id=id
		self.list.initVarsFromPath(path,'/')
		#self.list.clearListVars(loc_to)
		#print '111111111111111	11 cleared to ',loc_to
		self.list.setCurrListName(loc_to, 'reset')		
		self.list.execList(loc_to)
		#self._popUpMenu.pop(loc)
		self.btn_fwd.Enable()	
		if self.curr_hist_id==0:
			self.btn_back.Disable()		
	
	def CreateForwardMenu(self):

		if 1:
			#print self.list.data[loc]
			pmenu=FM.FlatMenu()
			self._fwdMenu = pmenu
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			#subMenu = FM.FlatMenu()
			#subSubMenu = FM.FlatMenu()
			id=wx.ID_ANY
			# Create the menu items
			#(path, loc_to) = self.nav_hist[self.curr_hist_id]
			relative_path=self.getVarsToPath()
			for id in range(len(self.nav_hist)):
				if id>self.curr_hist_id:
					#print id, self.curr_hist_id
					tup=self.nav_hist[id]
					(loc_to, path)=tup
					#print id, self.curr_hist_id
					itype=wx.ITEM_NORMAL
					if id==self.curr_hist_id:

						itype=wx.ITEM_CHECK
					menuItem = FM.FlatMenuItem(pmenu, wx.ID_ANY, '%s' % ( path), "", itype)
					#print item[0], self.list.nav_list['vars'][loc],  item[0]==self.list.nav_list['vars'][loc]
					pmenu.AppendItem(menuItem)				
					if path==relative_path:
						menuItem.Check(True)
						#subMenu.UpdateItem(menuItem)
						#print menuItem.IsChecked(), menuItem.IsCheckable()
						#menuItem.Enable(False)
					#pmenu.AppendRadioItem(wx.ID_ANY,menuItem)

					#print menuItem.isChecked()
					#print menuItem.IsChecked(), menuItem.IsChecked()
					#menuItem.Enable(True)
					#self.Bind(FM.EVT_FLAT_MENU_SELECTED, self.OnMenu, id=20001+key)
					#
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnForwardMenu,(id,loc_to, path))
	def OnForwardMenu(self, event, params):
		(id,loc_to, path) = params
		#print event.GetEventObject()
		#print(dir(event.GetEventObject()))
		#item_id=event.GetId()-21001
		#print item_id
		#self.list.nav_list['vars'][loc]=
		#print self.list., self.list.data[loc][item_id]
		#print  params
		#self.list.nav_list['vars'][loc]=item
		#list_to=
		self.curr_hist_id=id
		#print (loc_to,path)
		self.list.initVarsFromPath(path,'/')
		#self.list.clearListVars(loc_to)
		#print '11111111111111111 cleared to ',loc_to
		self.list.setCurrListName(loc_to, 'reset')		
		self.list.execList(loc_to)
		#self._popUpMenu.pop(loc)
		self.btn_back.Enable()	
		if self.curr_hist_id==(len(self.nav_hist)-1):
			self.btn_fwd.Disable()
	
	def OnFavButton(self, event,params):
		(loc)=params
		#print (loc)
		#print dir(event)
		#btn=event.GetEventObject()
		#print btn.GetPosition()
		#print btn.GetSize()
		#print btn.GetPosition()[0]
		btn = event.GetEventObject()
		#import flat_menu2
		# Create the popup menu
		#self.CreateLongPopupMenu()
		self.CreateFavMenu(loc)

		# Postion the menu:
		# The menu should be positioned at the bottom left corner of the button.
		btnSize = btn.GetSize()

		# btnPt is returned relative to its parent 
		# so, we need to convert it to screen 
		btnPt  = btn.GetPosition()
		btnPt = btn.GetParent().ClientToScreen(btnPt)
		#self._longPopUpMenu.SetOwnerHeight(btnSize.y)
		#self._longPopUpMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
		self._favMenu.SetOwnerHeight(btnSize.y)
		self._favMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)	

	def CreateFavMenu(self,loc):

		if 1 or not self._popUpMenu.has_key(loc):
			#print self.list.data[loc]
			pmenu=FM.FlatMenu()
			self._favMenu = pmenu
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			#subMenu = FM.FlatMenu()
			#subSubMenu = FM.FlatMenu()
			id=wx.ID_ANY
			# Create the menu items
			gsuffix='gfavs%d%d' % self.pos
			gfavs=readFromCache('', gsuffix)	
			#print 'gfavs:', gfavs
			gkeys=gfavs.keys()
			#gkeys=sorted(gkeys,key=lambda path: len(path.split('/'))) #reverse=True
			gkeys.sort()
			#pprint(gkeys)
			#sys.exit(1)
			first=True
			for path in gkeys:	
				items=gfavs[path]
				if not first:
					pmenu.AppendSeparator()
				loc_id=p=path.split(':')[0]
				#loc=self.list.getListFromId(int(loc_id))
				p=path.split(':')[1][5:]
				if p:
					p='(%s)' %p
				ikeys=items.keys()
				ikeys.sort()
				for ikey in ikeys:
					val=items[ikey]
					#print '--item--',ikey, val
					itype=wx.ITEM_NORMAL
					menuItem = FM.FlatMenuItem(pmenu, wx.ID_ANY, '%s %s' % (ikey, p), "", itype)
					pmenu.AppendItem(menuItem)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnFavMenu,(loc_id,'%s/%s' %(val,ikey)))
				first=False

	def OnHistMenu(self, event, params):
		(loc_to,path) = params

		#print (loc_to,path)
		vars=self.list.getVarsFromPath(path,'/')[1:]
		self.list.setNavlist()
		if len(vars)>2:
			conn=self.list.getConnectType(path)
			#print conn
			#print 'before',self.list.nav_list.keys()
			self.list.extendNavlist(conn)
			#print 'after',self.list.nav_list.keys()
				
		self.list.initVarsFromPath(path,'/')
		self.list.setCurrListName(loc_to, 'reset')		
		self.list.execList(loc_to)
		self.add_nav_hist(loc_to)
	def OnFavMenu0(self, event, params):
		(loc_to,path) = params
		if 1:
			#print (loc_to,path)
			self.list.initVarsFromPath(path,'/')
			self.list.setCurrListName(loc_to, 'reset')		
			self.list.execList(loc_to)
			self.add_nav_hist(loc_to)
	def OnFavMenu(self, event, params):
		(loc_id,path) = params
		if 1:
			#print (loc_id,path)
			vars=self.list.getVarsFromPath(path,'/')[1:]
			#print 'new vars:'
			#print vars
			self.list.setNavlist()
			if len(vars)>2:
				conn=self.list.getConnectType(path)
				#print conn
				#print 'before',self.list.nav_list.keys()
				self.list.extendNavlist(conn)
				#print 'after',self.list.nav_list.keys()
			self.list.initVarsFromPath(path,'/')
			loc_to=self.list.getListFromId(int(loc_id))
			self.list.setCurrListName(loc_to, 'reset')	
			self.list.execList(loc_to)
			self.add_nav_hist(loc_to)
	def updateCache(self):
		relative_path='root'
		if update_cache:
			
			vars=self.list.nav_list['vars'].values()[1:]
			if len(vars)>0:
				relative_path='%s/%s'% (relative_path,'/'.join(vars))
			writeToCache(relative_path, self.list.data[self.list.current_list])	
	def SortListItems(self, col=-1, ascending=1):
		pass
	def GetSelection(self):
		row = -1 
		selected_items = [] 
		while 1: 
			row = self.GetNextItem(row, wxLIST_NEXT_ALL, wxLIST_STATE_SELECTED) 
			if row==-1: break 
		selected_items.append(row) 
	def OnUseNative(self, event):
		wx.SystemOptions.SetOptionInt("mac.listctrl.always_use_generic", not event.IsChecked())
		wx.GetApp().GetTopWindow().LoadDemo("ListCtrl")

	def PopulateList(self):
		if 0:
			# for normal, simple columns, you can add them like this:
			self.list.InsertColumn(0, "Artist")
			self.list.InsertColumn(1, "Title", wx.LIST_FORMAT_RIGHT)
			self.list.InsertColumn(2, "Genre")
		else:
			# but since we want images on the column header we have to do it the hard way:
			info = wx.ListItem()
			info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
			info.m_image = -1
			info.m_format = 0
			info.m_text = "Artist"
			self.list.InsertColumnInfo(0, info)

			info.m_format = wx.LIST_FORMAT_RIGHT
			info.m_text = "Title"
			self.list.InsertColumnInfo(1, info)

			info.m_format = 0
			info.m_text = "Genre"
			self.list.InsertColumnInfo(2, info)

		items = musicdata.items()
		for key, data in items:
			index = self.list.InsertImageStringItem(sys.maxint, data[0], self.idx1)
			self.list.SetStringItem(index, 1, data[1])
			self.list.SetStringItem(index, 2, data[2])
			self.list.SetItemData(index, key)

		self.list.SetColumnWidth(0, wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(1, wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(2, 100)

		# show how to select an item
		#self.list.SetItemState(5, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)

		# show how to change the colour of a couple items
		item = self.list.GetItem(1)
		item.SetTextColour(wx.BLUE)
		self.list.SetItem(item)
		item = self.list.GetItem(4)
		item.SetTextColour(wx.RED)
		self.list.SetItem(item)

		self.currentItem = 0


	# Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
	def GetListCtrl(self):
		return self.list

	# Used by the ColumnSorterMixin, see wx/lib/mixins/listctrl.py
	def GetSortImages(self):
		return (self.sm_dn, self.sm_up)


	def OnRightDown(self, event):
		x = event.GetX()
		y = event.GetY()
		#self.log.WriteText("x, y = %s\n" % str((x, y)))
		item, flags = self.list.HitTest((x, y))

		if item != wx.NOT_FOUND and flags & wx.LIST_HITTEST_ONITEM:
			self.list.Select(item)

		event.Skip()


	def getColumnText(self, index, col):
		item = self.list.GetItem(index, col)
		return item.GetText()

		

	def OnItemSelected1(self, event):
		##print event.GetItem().GetTextColour()
		self.currentItem = event.m_itemIndex
		if 0:
			self.log.WriteText("OnItemSelected: %s, %s, %s, %s\n" %
							   (self.currentItem,
								self.list.GetItemText(self.currentItem),
								self.getColumnText(self.currentItem, 1),
								self.getColumnText(self.currentItem, 2)))

		if self.currentItem == 10:
			#self.log.WriteText("OnItemSelected: Veto'd selection\n")
			#event.Veto()  # doesn't work
			# this does
			self.list.SetItemState(10, 0, wx.LIST_STATE_SELECTED)

		event.Skip()


	def OnItemDeselected1(self, evt):
		item = evt.GetItem()
		#print "OnItemDeselected: %d" % evt.m_itemIndex
		#self.log.WriteText("OnItemDeselected: %d" % evt.m_itemIndex)

		# Show how to reselect something we don't want deselected
		if evt.m_itemIndex == 11:
			wx.CallAfter(self.list.SetItemState, 11, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


	def OnItemActivated(self, event):
		self.currentItem = event.m_itemIndex
		#print "OnItemActivated: %s\nTopItem: %s" % (self.list.GetItemText(self.currentItem), self.list.GetTopItem())
		#self.log.WriteText("OnItemActivated: %s\nTopItem: %s" %
		#                   (self.list.GetItemText(self.currentItem), self.list.GetTopItem()))

	def OnBeginEdit(self, event):
		#print "OnBeginEdit"
		#self.log.WriteText("OnBeginEdit")
		event.Allow()

	def OnItemDelete(self, event):
		pass
		#print "OnItemDelete"
		#self.log.WriteText("OnItemDelete\n")

	def OnColClick(self, event):
		#print "OnColClick: %d\n" % event.GetColumn()
		#self.log.WriteText("OnColClick: %d\n" % event.GetColumn())
		#print(dir(self.list))
		#if self.list.idx_first != None:
		#	self.list.DeleteItem(self.list.idx_first)

		event.Skip()
	def OnSortOrderChanged(self):
		#print "OnSortOrderChanged!"
		#self._colSortFlag[self._col]=int(not self._colSortFlag[self._col])
		#pprint(dir(self.list))
		if 1:
			for j in range(len(self.list.data[self.list.current_list])):
				if (j % 2) == 0:
					#self.list._bg='#e6f1f5'
					self.list.SetItemBackgroundColour(j, self.list._bg)
				else:
					self.list.SetItemBackgroundColour(j, '#FFFFFF')
				#j += 1
				
		#self.log.WriteText("OnColClick: %d\n" % event.GetColumn())
		#event.Skip()		

	def OnColRightClick(self, event):
		item = self.list.GetColumn(event.GetColumn())
		#print "OnColRightClick: %d %s\n" % (event.GetColumn(), (item.GetText(), item.GetAlign(), item.GetWidth(), item.GetImage()))
		#self.log.WriteText("OnColRightClick: %d %s\n" %
		#                   (event.GetColumn(), (item.GetText(), item.GetAlign(),
		#                                        item.GetWidth(), item.GetImage())))

	def OnColBeginDrag(self, event):
		print "OnColBeginDrag"
		#self.log.WriteText("OnColBeginDrag\n")
		## Show how to not allow a column to be resized
		#if event.GetColumn() == 0:
		#    event.Veto()


	def OnColDragging(self, event):
		print "OnColDragging"
		#self.log.WriteText("OnColDragging\n")

	def OnColEndDrag(self, event):
		print "OnColEndDrag"
		#self.log.WriteText("OnColEndDrag\n")

	def OnDoubleClick(self, event):
		#print "OnDoubleClick item %s\n" % self.list.GetItemText(self.currentItem)
		#self.log.WriteText("OnDoubleClick item %s\n" % self.list.GetItemText(self.currentItem))
		event.Skip()
	def getSide(self,pos):
		side =None
		id ='%d%d' % pos 
		if self.sides.has_key(id):
			side=self.sides[id]
		return side
	def OnRightClick(self, event):
		#print "OnRightClick %s\n" % self.list.GetItemText(self.currentItem),self.list.GetSelectedItemCount()
		#self.log.WriteText("OnRightClick %s\n" % self.list.GetItemText(self.currentItem))
		#print(dir(self.list))
		#print GetSelectedItemCount
		# only do this part the first time so the events are only bound once
		disabled_favs=False
		if self.list.GetSelectedItemCount()==0:
			disabled_favs =True
		self.show_in={}
		if 1:
			menu = wx.Menu()
			if 1: #not hasattr(self, "add_to_favorites"):
				self.add_to_favorites = wx.NewId()
				self.remove_from_favorites = wx.NewId()
				for sid in ['%d%d' % pos for pos in self.panel_pos if pos!=self.pos ]:
					#print '---ii--',sid, 20100+int(sid)
					self.show_in[sid]=20100+int(sid)
				self.Bind(wx.EVT_MENU, self.OnAddToFavorites, id=self.add_to_favorites)
				self.Bind(wx.EVT_MENU, self.OnRemoveFromFavorites, id=self.remove_from_favorites)
				for sid in ['%d%d' % pos for pos in self.panel_pos if pos!=self.pos ]:
					#self.gen_bind(wx.EVT_MENU,self, self.TimerHandler_pos,(self.panel_pos[0]))
					#self.gen_bind(wx.EVT_MENU,menu, self.OnShowIn,(sid),id=self.show_in[sid])
					self.Bind(wx.EVT_MENU, self.OnShowIn, id=self.show_in[sid])
					self.Bind(wx.EVT_MENU, self.OnShowIn, id=self.show_in[sid]+10000)
					#self.Bind(wx.EVT_MENU, self.OnShowIn, id=self.show_in[sid])
					#menuItem = wx.MenuItem(pmenu, wx.ID_ANY, '%s' % ( label), "", itype)
					#self.gen_bind(wx.EVT_MENU,self.show_in[sid], self.OnShowIn ,(id))	
				if 0:
					self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)
					self.Bind(wx.EVT_MENU, self.OnPopupThree, id=self.popupID3)
					self.Bind(wx.EVT_MENU, self.OnPopupFour, id=self.popupID4)
					self.Bind(wx.EVT_MENU, self.OnPopupFive, id=self.popupID5)
					self.Bind(wx.EVT_MENU, self.OnPopupSix, id=self.popupID6)

			# make a menu
			
			# add some items
			self.add_new_connect = wx.NewId()
			self.delete_connect = wx.NewId()
			self.edit_connect = wx.NewId()
			self.clear_password = wx.NewId()
			if self.list.current_list in ('ConnectList'):
				menu.Append(self.add_new_connect, "Add new connection.")
				self.Bind(wx.EVT_MENU, self.OnAddNewConnection, id=self.add_new_connect)
				menu.Append(self.delete_connect, "Delete connection.")
				self.Bind(wx.EVT_MENU, self.OnDeleteConnection, id=self.delete_connect)
				menu.Append(self.edit_connect, "Edit connection.")
				self.Bind(wx.EVT_MENU, self.OnEditConnection, id=self.edit_connect)
				if disabled_favs:
					menu.Enable(self.delete_connect, False)
				
				menu.Append(self.clear_password, "Clear Password")
				self.Bind(wx.EVT_MENU, self.OnClearPassword, id=self.clear_password)
				if disabled_favs:
					menu.Enable(self.clear_password, False)	
			if self.list.current_list in ('ConfigList','EnvironmentList'):
				menu.Append(self.clear_password, "Clear Passwords")
				self.Bind(wx.EVT_MENU, self.OnClearPasswords, id=self.clear_password)
				if disabled_favs:
					menu.Enable(self.clear_password, False)	
					
					
			menu.Append(self.add_to_favorites, "Add to Favorites.")
			menu.Append(self.remove_from_favorites, "Remove from Favorites.")
			if self.list.current_list in ('TableList','PartitionList','SubPartitionList'):
				gather_stats=wx.NewId()
				menu.Append(gather_stats, "Gather stats.")
				menu.Enable(gather_stats, False)
				copy_ddl=wx.NewId()
				menu.Append(copy_ddl, "Copy DDL.")
				menu.Enable(copy_ddl, False)
				copy_name=wx.NewId()
				menu.Append(copy_name, "Copy name.")
				menu.Enable(copy_name, False)
				
			for pos in [ pos for pos in self.panel_pos if pos!=self.pos and pos !=self.frame.designer_pos ]:
				side= self.getSide(pos)
				sid= '%d%d' % pos 
				#print sid, side, self.panel_pos
				if side:
					menu.Append(self.show_in[sid], "Mirror in %s" % side)
					list=self.getListFromPos(pos)
					pos_connect='test_CSMARTBSER_QA' #'list.parent.getVarsToPath().split('/')[2]
					#db_path=self.getVarsToPath().split('/')[4:]
					#in_url="%s/%s" % (pos_connect, '/'.join(db_path))
					#menu.Append(self.show_in[sid]+10000, "Mirror in %s (%s)" % (side,in_url))
			if disabled_favs:
				menu.Enable(self.add_to_favorites, False)
				menu.Enable(self.remove_from_favorites, False)
			if 0:
				menu.Append(self.popupID1, "FindItem tests")
				menu.Append(self.popupID2, "Iterate Selected")
				menu.Append(self.popupID3, "ClearAll and repopulate")
				menu.Append(self.popupID4, "DeleteAllItems")
				menu.Append(self.popupID5, "GetItem")
				menu.Append(self.popupID6, "Edit")

			# Popup the menu.  If an item is selected then its handler
			# will be called before PopupMenu returns.
			#pprint(dir(menu))
			self.PopupMenu(menu)
			
			menu.Destroy()
	def OnDeleteConnection(self, event):		
		print 'F9 is clicked'
		useMetal = False
		if 'wxMac' in wx.PlatformInfo:
			useMetal = True
		list=self.list #self.frame.getListFromPos(self.pos)
		self.delete_conn = []
		idx = -1
		while True: # find all the selected items and put them in a list
			idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
			if idx == -1:
				break
			self.delete_conn.append(list.getItemInfo(idx))
		#print self.delete_conn		
		dlg = DeleteConnectDialog(self, -1, "Delete Oracle connect.", size=(250, 250),
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=useMetal,
						 )
		dlg.CenterOnScreen()
		# this does not return until the dialog is closed.
		val = dlg.ShowModal()

		if val == wx.ID_OK:
			print "You pressed OK\n"
			#self.log.write("You pressed OK\n")
		else:
			print "You pressed Cancel\n"
			#self.log.write("You pressed Cancel\n")
		table_to=None

		dlg.Destroy()

		
	def OnEditConnection(self, event):		
		print 'F9 is clicked'
		useMetal = False
		if 'wxMac' in wx.PlatformInfo:
			useMetal = True
		list=self.list #self.frame.getListFromPos(self.pos)
		self.delete_conn = []
		idx = -1
		while True: # find all the selected items and put them in a list
			idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
			if idx == -1:
				break
			self.delete_conn.append(list.getItemInfo(idx))
		#print self.delete_conn
		conn_alias=self.delete_conn[0][2].strip('[').strip(']')
		login=(user,db,pwd,host,port) = self.getConnectInfo(conn_alias)
		#print login
		#sys.exit(1)
		#self.list.Freeze()
		dlg = EditOracleConnectDialog(self, -1, "Edit Oracle connect.", size=(450, 450),login=login,
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.SYSTEM_MENU | wx.CAPTION | wx.MAXIMIZE_BOX | wx.FRAME_NO_TASKBAR| wx.FRAME_FLOAT_ON_PARENT | wx.CLIP_CHILDREN,
						 #style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=False,
						 )
		
		dlg.CenterOnScreen()
		val = dlg.Show()

			
		if 0:		
			dlg = DeleteConnectDialog(self, -1, "Delete Oracle connect.", size=(250, 250),
							 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
							 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
							 useMetal=useMetal,
							 )
			dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()

			if val == wx.ID_OK:
				print "You pressed OK\n"
				#self.log.write("You pressed OK\n")
			else:
				print "You pressed Cancel\n"
				#self.log.write("You pressed Cancel\n")
			table_to=None

			dlg.Destroy()
		
	def OnClearPassword(self, event):		
		print 'F9 is clicked'
		useMetal = False
		if 'wxMac' in wx.PlatformInfo:
			useMetal = True
		list=self.list #self.frame.getListFromPos(self.pos)
		self.delete_conn = []
		idx = -1
		while True: # find all the selected items and put them in a list
			idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
			if idx == -1:
				break
			self.delete_conn.append(list.getItemInfo(idx))
		#print self.delete_conn		
		dlg = ClearPasswordDialog(self, -1, "Clear Oracle passwords.", size=(250, 250),
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=useMetal,
						 )
		dlg.CenterOnScreen()
		# this does not return until the dialog is closed.
		val = dlg.ShowModal()

		if val == wx.ID_OK:
			print "You pressed OK\n"
			#self.log.write("You pressed OK\n")
		else:
			print "You pressed Cancel\n"
			#self.log.write("You pressed Cancel\n")
		table_to=None

		dlg.Destroy()

	def OnClearPasswords(self, event):		
		print 'F9 is clicked'
		useMetal = False
		if 'wxMac' in wx.PlatformInfo:
			useMetal = True
		list=self.list #self.frame.getListFromPos(self.pos)
		conf_list = []
		self.delete_conn = []
		idx = -1
		if 0:
			while True: # find all the selected items and put them in a list
				idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
				if idx == -1:
					break
				conf_list.append(list.getItemInfo(idx))
			#print conf_list
			#sys.exit(1)
		cons={}
		if self.list.current_list in ('ConfigList'):
			#get all connects
			conf_list = []
			self.delete_conn = []
			idx = -1
			
			while True: # find all the selected items and put them in a list
				idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
				if idx == -1:
					break
				conf_list.append(list.getItemInfo(idx))
			#print conf_list	
			for crow in conf_list:			
				cfile =crow[2].strip('[').strip(']')		
				config_file= '%s.xml' % os.path.join(configDirLoc, '%s' % cfile)
				#print config_file		
				#get env connects
				env_list = self.list.db.getEnvironments(config_file)
				#print env_list
				#sys.exit(1)
				
				cons[cfile]={}
				for eid, env in env_list.items():
					#print env
					_EnvironmentList=env[0]
					if _EnvironmentList not in cons[cfile]:
						cons[cfile][_EnvironmentList]=[]
					
					#print _EnvironmentList
					con =self.list.db.getConnectList(config_file,_EnvironmentList).values()
					#pprint(con)
					#print cons.items()
					#print con.items()
					#print cons.items()+con.items()
					cons[cfile][_EnvironmentList]=cons[cfile][_EnvironmentList] +con
		if self.list.current_list in ('EnvironmentList'):
			env_list = []
			self.delete_conn = []
			idx = -1
			
			while True: # find all the selected items and put them in a list
				idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
				if idx == -1:
					break
				env_list.append(list.getItemInfo(idx))
			#print env_list
		
			cfile =self.list._ConfigList
			config_file= '%s.xml' % os.path.join(configDirLoc, '%s' % cfile)
			#print config_file		
			#get env connects
			
			cons[cfile]={}
			for env in env_list:
				#print env
				_EnvironmentList=env[2].strip('[').strip(']')
				if _EnvironmentList not in cons[cfile]:
					cons[cfile][_EnvironmentList]=[]
				
				#print _EnvironmentList
				con =self.list.db.getConnectList(config_file,_EnvironmentList).values()
				#pprint(con)
				#print cons.items()
				#print con.items()
				#print cons.items()+con.items()
				cons[cfile][_EnvironmentList]=cons[cfile][_EnvironmentList] +con
		#pprint(cons)
		#sys.exit(1)
		if 0:
			while True: # find all the selected items and put them in a list
				idx = list.GetNextItem(idx, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED)
				if idx == -1:
					break
				self.delete_conn.append(list.getItemInfo(idx))
		#print self.delete_conn		
		dlg = ClearPasswordsDialog(self, -1, "Clear Oracle passwords.", size=(250, 250),
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=useMetal, plist=cons
						 )
		dlg.CenterOnScreen()
		# this does not return until the dialog is closed.
		val = dlg.ShowModal()
		if 0:
			if val == wx.ID_OK:
				print "You pressed OK\n"
				#self.log.write("You pressed OK\n")
			else:
				print "You pressed Cancel\n"
				#self.log.write("You pressed Cancel\n")
			table_to=None

		dlg.Destroy()
		
	def OnAddNewConnection(self, event):
		print str(self.__class__) + ' - OnAddNewConnection'
		index = -1 
		selected_items = [] 
		
		print 'F3 is clicked'
		useMetal = False
		if 'wxMac' in wx.PlatformInfo:
			useMetal = True
			
		dlg = OracleConnectDialog(self, -1, "Add Oracle connect.", size=(450, 450),
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=useMetal,
						 )
		dlg.CenterOnScreen()
		# this does not return until the dialog is closed.
		val = dlg.ShowModal()
		if 0:
			if val == wx.ID_OK:
				self.log.write("You pressed OK\n")
			else:
				self.log.write("You pressed Cancel\n")
		table_to=None

		dlg.Destroy()
		
		if 0:
			while 1: 
				index = self.list.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED) 
				if index==-1: 
					break 
				selected_items.append(index) 
				item = self.list.GetItem(index)
				font = item.GetFont()
				font.SetWeight(wx.FONTWEIGHT_BOLD)
				item.SetFont(font)
				# This does the trick:
				self.list.SetItem(item)

			#print 'si',selected_items
			self.addToFavorites(selected_items)
		
	def OnShowIn(self, event):
		print str(self.__class__) + ' - OnShowIn'
		#print event.GetEventObject().GetLabel(event.GetId())
		#print event.GetId()
		#sys.exit(1)
		#print str(event.GetId()-100)
		#print event.GetId()-20000
		(ignore,row,col) = str(event.GetId()-20000)
		pos_to= (int(row),int(col))
		#print pos_to
		#Publisher().sendMessage( "mirror_list", (self.list.current_list, self.getVarsToPath(), pos_to, self.getSide(self.pos)) )
		send("mirror_list", (self.list.current_list, self.getVarsToPath(), pos_to, self.getSide(self.pos)))
		


	def OnAddToFavorites(self, event):
		print str(self.__class__) + ' - OnAddToFavorites'
		index = -1 
		selected_items = [] 
		while 1: 
			index = self.list.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED) 
			if index==-1: 
				break 
			selected_items.append(index) 
			item = self.list.GetItem(index)
			font = item.GetFont()
			font.SetWeight(wx.FONTWEIGHT_BOLD)
			item.SetFont(font)
			# This does the trick:
			self.list.SetItem(item)

		#print 'si',selected_items
		self.addToFavorites(selected_items)

	def OnRemoveFromFavorites(self, event):
		print str(self.__class__) + ' - OnRemoveFromFavorites'
		index = -1 
		selected_items = [] 
		while 1: 
			index = self.list.GetNextItem(index, wx.LIST_NEXT_ALL, wx.LIST_STATE_SELECTED) 
			if index==-1: 
				break 
			selected_items.append(index) 
			item = self.list.GetItem(index)
			font = item.GetFont()
			font.SetWeight(wx.FONTWEIGHT_NORMAL)
			item.SetFont(font)
			# This does the trick:
			self.list.SetItem(item)

		#print 'si',selected_items
		self.removeFromFavorites(selected_items)

		

	
	def addToFavorites(self, ids):	
		pass
	def removeFromFavorites(self, ids):	
		relative_path= self.getVarsToPath()
		fav_path= self.getVarsToFavPath()
		#print fav_path
		if 0:
			suffix='_favs%d%d' % self.pos
			favs=readFromCache(relative_path, suffix)
			#pprint (self.list.data)
			#print 'old favs:', favs
			for id in ids:
				#print 'removing:', self.list.data[self.list.current_list][id][0]
				if favs.has_key(self.list.data[self.list.current_list][id][0]):
					favs.pop(self.list.data[self.list.current_list][id][0])
			#print favs
			writeToCache(relative_path, favs, suffix)
		gsuffix='gfavs%d%d' % self.pos
		gfavs=readFromCache('', gsuffix)	
		#print 'old gfavs:', gfavs
		#print ids
		#for key, items in gfavs.items():			
			#print key,relative_path
			#print items
		fav_key='%d:%s' % (len(relative_path.split('/')),fav_path)
		if gfavs.has_key(fav_key):
			#pprint(dir(gfavs[ relative_path]))
			for id in ids:
				#print id,  self.list.data[self.list.current_list][id][0]
				#print gfavs[ relative_path].index(self.list.data[self.list.current_list][id][0])
				#print 'before', gfavs[fav_key]
				pop_val=self.list.data[self.list.current_list][id][0]
				if gfavs[fav_key].has_key(pop_val):
					gfavs[fav_key].pop(pop_val)
				#print 'after', gfavs[fav_key]
			#gfavs[relative_path].append(self.list.data[self.list.current_list][id][0])
			#print 'new global favs:',gfavs
			writeToCache('', gfavs, gsuffix)		
		
		
	def OnPopupTwo(self, event):
		#self.log.WriteText("Selected items:\n")
		index = self.list.GetFirstSelected()

		while index != -1:
			#print "      %s: %s\n" % (self.list.GetItemText(index), self.getColumnText(index, 1))
			#self.log.WriteText("      %s: %s\n" % (self.list.GetItemText(index), self.getColumnText(index, 1)))
			index = self.list.GetNextSelected(index)

	def OnPopupThree(self, event):
		#print "Popup three\n"
		#self.log.WriteText("Popup three\n")
		self.list.ClearAll()
		wx.CallAfter(self.PopulateList)

	def OnPopupFour(self, event):
		self.list.DeleteAllItems()

	def OnPopupFive(self, event):
		item = self.list.GetItem(self.currentItem)
		#print item.m_text, item.m_itemId, self.list.GetItemData(self.currentItem)

	def OnPopupSix(self, event):
		self.list.EditLabel(self.currentItem)	

########################################################################
class TabPanelOne(wx.Panel):
    """
    A simple wx.Panel class
    """
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """"""
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        txtOne = wx.TextCtrl(self, wx.ID_ANY, "")
        txtTwo = wx.TextCtrl(self, wx.ID_ANY, "")
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(txtOne, 0, wx.ALL, 5)
        sizer.Add(txtTwo, 0, wx.ALL, 5)
 
        self.SetSizer(sizer)		
########################################################################
class SessionListCtrlPanelManager(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent,frame, pos, panel_pos, sess_dir):
		""""""

		wx.Panel.__init__(self, parent,  id=wx.NewId())

		self.pos=pos
		self.panel_pos=panel_pos

		self.parent=parent
		self.frame=frame
		self.createRightClickMenu()
		self.nb = fnb.FlatNotebook(self, -1, size=(-1,-1), agwStyle=fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_SMART_TABS) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
		#userhome = os.path.expanduser('~')
		#sess_dir=os.path.join(userhome,'sessions')		
		default_slib_name='My_Sessions'
		self.slib_name=default_slib_name
		self.home_dir=sess_dir
		default_slib=os.path.join(self.home_dir,default_slib_name)
		#del self.lists
		self.lists={}
		self.slps={}
		if os.path.isdir(default_slib):
			slp=SessionListCtrlPanel(self,frame, pos,self.panel_pos, slib_path=default_slib)
			self.slps[default_slib_name]=slp
			self.list=slp.list
			self.nb.AddPage(slp,'')
			self.nb.SetPageText(0, default_slib_name)
			self.lists[default_slib_name]=slp.list
		
		dirs=[o for o in os.listdir(self.home_dir) if os.path.isdir(os.path.join(self.home_dir,o)) and o not in ['My_Sessions']]
		#pprint(dirs)
		#e(0)
		
		for i in range(len(dirs)):
			d=dirs[i]
			slp=SessionListCtrlPanel(self,frame, pos,self.panel_pos, slib_path=os.path.join(self.home_dir,d))
			self.slps[d]=slp
			self.lists[d]=slp.list
			self.list=slp.list
			self.nb.AddPage(slp,'')
			self.nb.SetPageText(self.nb.GetPageCount()-1, d)
		#tmpl=SessionListCtrlPanel(self,pos,self.panel_pos)
		#self.nb.AddPage(tmpl,'Templates')
		#self.active_list=0
		self.nb.SetSelection(0)
		
		self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.onTabChanged, self.nb)
		#self.nb.EnableTab(0,False)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.nb, 1, wx.GROW|wx.EXPAND|wx.ALL, 0)
		self.SetSizer(self.sizer)
		#self.SetAutoLayout(True)
		self._newPageCounter=0
		self.nb.SetRightClickMenu(self._rmenu)

		if 1:
			
			MENU_SELECT_GRADIENT_COLOR_FROM = wx.NewId()
			MENU_SELECT_GRADIENT_COLOR_TO = wx.NewId()
			MENU_SELECT_GRADIENT_COLOR_BORDER = wx.NewId()
			MENU_SET_ACTIVE_TEXT_COLOR = wx.NewId()
			MENU_SET_ACTIVE_TAB_COLOR = wx.NewId()
			MENU_SET_TAB_AREA_COLOR = wx.NewId()
			MENU_SELECT_NONACTIVE_TEXT_COLOR = wx.NewId()

			eventid = MENU_SET_TAB_AREA_COLOR
			red=wx.Colour(255, 0, 0, 255)
			blue=wx.Colour(0, 128, 255, 255)
			green= wx.Colour(0, 128, 0, 255)
			light_yellow=wx.Colour(255, 255, 128, 255)		
			light_green=wx.Colour(128, 255, 128, 255)
			light_blue=wx.Colour(128, 255, 255, 255)
			_TAB_AREA_COLOR=red			
			if pos==(0,0):
				_TAB_AREA_COLOR=light_blue
			elif pos==(0,1):
				_TAB_AREA_COLOR=light_yellow
			elif pos==(0,2):
				_TAB_AREA_COLOR=light_green

			if 1: #dlg.ShowModal() == wx.ID_OK:
				if eventid == MENU_SELECT_GRADIENT_COLOR_BORDER:
					self.nb.SetGradientColourBorder(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_GRADIENT_COLOR_FROM:
					self.nb.SetGradientColourFrom(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_GRADIENT_COLOR_TO:
					self.nb.SetGradientColourTo(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_ACTIVE_TEXT_COLOR:
					#print 'colour----------------------------',dlg.GetColourData().GetColour()
					self.nb.SetActiveTabTextColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_NONACTIVE_TEXT_COLOR:
					self.nb.SetNonActiveTabTextColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_ACTIVE_TAB_COLOR:
					self.nb.SetActiveTabColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_TAB_AREA_COLOR:
					#col = dlg.GetColourData().GetColour()
					#print 'colour----------------------------', col, type(col)
					self.nb.SetTabAreaColour(_TAB_AREA_COLOR)
	#----------------------------------------------------------------------
	def getActiveLibName(self):
		return self.nb.GetPageText(self.nb.GetSelection())	
	def onTabChanged(self, evt):
		#print str(self.__class__) +' - onTabChanged'
		#send('disable_all',())
		self.setTab()
	def setTab(self):
		self.slib_name=self.getActiveLibName()
		#
		#print slib_name
		#list=self.lists[slib_name]
		selected= self.lists[self.slib_name].GetSelected()
		#print selected
		#sel= self.lists[slib_name].GetSelectedItems()
		#print sel
		if selected:
			sel= self.lists[self.slib_name].GetSelectedItems()
			self.lists[self.slib_name].parent.openSessionByItemId(sel[0])
			self.frame.setLibHome(self.slib_name)
		else:
			send('disable_all',())
		#else:
		#	send('enable_all',())
		if 0:
			if self.nb_tab:
				self.btn_clearall.Enable(False)
			else:
				self.btn_clearall.Enable(True)
			#self.updateCommand(self.nb_tab)	
			
	def createRightClickMenu(self):
		"""
		Based on method from flatnotebook demo
		"""
		
		self._rmenu = wx.Menu()
		item = wx.MenuItem(self._rmenu, wx.ID_ANY, 
						   "Close Tab\tCtrl+F4", 
						   "Close Tab")
		item2 = wx.MenuItem(self._rmenu, wx.ID_ANY, 
						   "New Session Library\tCtrl+F5", 
						   "New Session Library")
		#item3 = wx.MenuItem(self._rmenu, wx.ID_ANY, 
		#				   "Open\tCtrl+F6", 
		#				   "Open")						   
		self.Bind(wx.EVT_MENU, self.onDeletePage, item)
		self.Bind(wx.EVT_MENU, self.onAddPage, item2)
		#self.Bind(wx.EVT_MENU, self.onOpenPage, item3)
		self._rmenu.AppendItem(item)
		self._rmenu.AppendItem(item2)
		#self._rmenu.AppendItem(item3)
	#----------------------------------------------------------------------
	def onAddPage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It adds a new page to the notebook
		"""
		slib_name='Sessions_2'
		if 1:
			dlg = NewSessionLibraryDialog(self, -1, "New session library.", size=(-1, -1),				
				 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
				 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
				 useMetal=False
				 )
			#dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			#print wx.ID_OK, ID_EXIT, val
			if val == wx.ID_OK:
				(slib_name)= dlg.getLibName()
		caption = slib_name
		self.Freeze()
		page=self.createPage(caption)
		self.list=page.list
		self.lists[caption]=page.list
		self.nb.AddPage(page, caption, True)
		self.Thaw()
		self._newPageCounter = self._newPageCounter + 1
	#----------------------------------------------------------------------
	def onOpenPage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It adds a new page to the notebook
		"""
		caption = "New Session Library"
		self.Freeze()
		page=self.createPage(caption)
		self.list=page.list
		self.nb.AddPage(page, caption, True)
		self.Thaw()
		self._newPageCounter = self._newPageCounter + 1 
	#----------------------------------------------------------------------
	def createPage(self, caption):
		"""
		Creates a notebook page from one of three
		panels at random and returns the new page
		"""
		#panel_list = [TabPanelOne(self.nb)]
		slib_path= os.path.join(self.home_dir, caption)
		if not os.path.isdir(slib_path):
			os.makedirs(slib_path)
		page=SessionListCtrlPanel(self,self.frame, self.pos,self.panel_pos, slib_path=slib_path)
		#page = TabPanelOne(self.nb)
		#page = panel_list[0]
		#page = obj.TabPanel(self.nb)
		return page
 
	#----------------------------------------------------------------------
	def onDeletePage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It removes a page from the notebook
		"""
		self.nb.DeletePage(self.nb.GetSelection())	
########################################################################
class TemplateListCtrlPanelManager(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent,frame, pos, panel_pos, sess_dir):
		""""""

		wx.Panel.__init__(self, parent,  id=wx.NewId())

		self.pos=pos
		self.panel_pos=panel_pos

		self.parent=parent
		self.frame=frame
		self.createRightClickMenu()
		self.nb = fnb.FlatNotebook(self, -1, size=(-1,-1), agwStyle=fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_SMART_TABS) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
		#userhome = os.path.expanduser('~')
		#sess_dir=os.path.join(userhome,'sessions')	
		self.home_dir=sess_dir		
		default_templates_name='My_Templates'
		default_slib=os.path.join(self.home_dir,default_templates_name)
		self.lists={}
		self.slps={}
		if os.path.isdir(os.path.join(self.home_dir, default_slib)):
			slp=SessionListCtrlPanel(self,frame, pos,self.panel_pos, slib_path=default_slib)
			self.slps[default_templates_name]=slp
			self.list=slp.list
			self.nb.AddPage(slp,'')
			self.nb.SetPageText(0, default_templates_name)
			self.lists[default_templates_name]=slp.list
		
		dirs=[o for o in os.listdir(self.home_dir) if os.path.isdir(os.path.join(self.home_dir,o)) and o not in ['My_Templates']]
		#pprint(dirs)
		#e(0)
		
		for i in range(len(dirs)):
			d=dirs[i]
			slp=SessionListCtrlPanel(self,frame, pos,self.panel_pos, slib_path=os.path.join(self.home_dir,d))
			self.slps[default_templates_name]=slp
			self.lists[d]=slp.list
			self.list=slp.list
			self.nb.AddPage(slp,'')
			self.nb.SetPageText(self.nb.GetPageCount()-1, d)
		#tmpl=SessionListCtrlPanel(self,pos,self.panel_pos)
		#self.nb.AddPage(tmpl,'Templates')
		#self.active_list=0
		self.nb.SetSelection(0)
		
		self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.onTabChanged, self.nb)
		#self.nb.EnableTab(0,False)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.nb, 1, wx.GROW|wx.EXPAND|wx.ALL, 0)
		self.SetSizer(self.sizer)
		#self.SetAutoLayout(True)
		self._newPageCounter=0
		self.nb.SetRightClickMenu(self._rmenu)

		if 1:
			
			MENU_SELECT_GRADIENT_COLOR_FROM = wx.NewId()
			MENU_SELECT_GRADIENT_COLOR_TO = wx.NewId()
			MENU_SELECT_GRADIENT_COLOR_BORDER = wx.NewId()
			MENU_SET_ACTIVE_TEXT_COLOR = wx.NewId()
			MENU_SET_ACTIVE_TAB_COLOR = wx.NewId()
			MENU_SET_TAB_AREA_COLOR = wx.NewId()
			MENU_SELECT_NONACTIVE_TEXT_COLOR = wx.NewId()

			eventid = MENU_SET_TAB_AREA_COLOR
			red=wx.Colour(255, 0, 0, 255)
			blue=wx.Colour(0, 128, 255, 255)
			green= wx.Colour(0, 128, 0, 255)
			light_yellow=wx.Colour(255, 255, 128, 255)		
			light_green=wx.Colour(128, 255, 128, 255)
			light_blue=wx.Colour(128, 255, 255, 255)
			_TAB_AREA_COLOR=red			
			if pos==(0,0):
				_TAB_AREA_COLOR=light_blue
			elif pos==(0,1):
				_TAB_AREA_COLOR=light_yellow
			elif pos==(0,2):
				_TAB_AREA_COLOR=light_green

			if 1: #dlg.ShowModal() == wx.ID_OK:
				if eventid == MENU_SELECT_GRADIENT_COLOR_BORDER:
					self.nb.SetGradientColourBorder(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_GRADIENT_COLOR_FROM:
					self.nb.SetGradientColourFrom(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_GRADIENT_COLOR_TO:
					self.nb.SetGradientColourTo(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_ACTIVE_TEXT_COLOR:
					#print 'colour----------------------------',dlg.GetColourData().GetColour()
					self.nb.SetActiveTabTextColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SELECT_NONACTIVE_TEXT_COLOR:
					self.nb.SetNonActiveTabTextColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_ACTIVE_TAB_COLOR:
					self.nb.SetActiveTabColour(dlg.GetColourData().GetColour())
				elif eventid == MENU_SET_TAB_AREA_COLOR:
					#col = dlg.GetColourData().GetColour()
					#print 'colour----------------------------', col, type(col)
					self.nb.SetTabAreaColour(_TAB_AREA_COLOR)
	#----------------------------------------------------------------------
	def getActiveLibName(self):
		return self.nb.GetPageText(self.nb.GetSelection())	
	def onTabChanged(self, evt):
		#print str(self.__class__) +' - onTabChanged'
		self.setTab()
	def setTab(self):
		#send('disable_all',())
		slib_name=self.getActiveLibName()
		#print slib_name
		#list=self.lists[slib_name]
		selected= self.lists[slib_name].GetSelected()
		#print selected
		#sel= self.lists[slib_name].GetSelectedItems()
		#print sel
		if selected:
			sel= self.lists[slib_name].GetSelectedItems()
			self.lists[slib_name].parent.openSessionByItemId(sel[0])
			self.frame.setLibHome(self.slib_name)
		else:
			send('disable_all',())
		#else:
		#	send('enable_all',())
		if 0:
			if self.nb_tab:
				self.btn_clearall.Enable(False)
			else:
				self.btn_clearall.Enable(True)
			#self.updateCommand(self.nb_tab)

			
	def createRightClickMenu(self):
		"""
		Based on method from flatnotebook demo
		"""
		
		self._rmenu = wx.Menu()
		item = wx.MenuItem(self._rmenu, wx.ID_ANY, 
						   "Close Tab\tCtrl+F4", 
						   "Close Tab")
		item2 = wx.MenuItem(self._rmenu, wx.ID_ANY, 
						   "New Template Library\tCtrl+F5", 
						   "New Template Library")
		#item3 = wx.MenuItem(self._rmenu, wx.ID_ANY, 
		#				   "Open\tCtrl+F6", 
		#				   "Open")						   
		self.Bind(wx.EVT_MENU, self.onDeletePage, item)
		self.Bind(wx.EVT_MENU, self.onAddPage, item2)
		#self.Bind(wx.EVT_MENU, self.onOpenPage, item3)
		self._rmenu.AppendItem(item)
		self._rmenu.AppendItem(item2)
		#self._rmenu.AppendItem(item3)
	#----------------------------------------------------------------------
	def onAddPage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It adds a new page to the notebook
		"""
		slib_name='Sessions_2'
		if 1:
			dlg = NewTemplateLibraryDialog(self, -1, "New template library.", size=(-1, -1),				
				 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
				 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
				 useMetal=False
				 )
			#dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			#print wx.ID_OK, ID_EXIT, val
			if val == wx.ID_OK:
				(slib_name)= dlg.getLibName()
		caption = slib_name
		self.Freeze()
		
		page=self.createPage(caption)
		self.list=page.list
		self.lists[caption]=page.list
		self.nb.AddPage(page, caption, True)
		self.Thaw()
		self._newPageCounter = self._newPageCounter + 1
	#----------------------------------------------------------------------
	def onOpenPage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It adds a new page to the notebook
		"""
		caption = "New Session Library"
		self.Freeze()
		page=self.createPage(caption)
		self.list=page.list
		
		self.nb.AddPage(page, caption, True)
		self.Thaw()
		self._newPageCounter = self._newPageCounter + 1 
	#----------------------------------------------------------------------
	def createPage(self, caption):
		"""
		Creates a notebook page from one of three
		panels at random and returns the new page
		"""
		#panel_list = [TabPanelOne(self.nb)]
		slib_path= os.path.join(self.home_dir, caption)
		os.makedirs(slib_path)
		page=SessionListCtrlPanel(self,self.frame, self.pos,self.panel_pos, slib_path=slib_path)
		#page = TabPanelOne(self.nb)
		#page = panel_list[0]
		#page = obj.TabPanel(self.nb)
		return page
 
	#----------------------------------------------------------------------
	def onDeletePage(self, event):
		"""
		This method is based on the flatnotebook demo
 
		It removes a page from the notebook
		"""
		self.nb.DeletePage(self.nb.GetSelection())	
		
def textentry(self, event):
	dlg = wx.TextEntryDialog(self, 'Enter some text','Text Entry')
	dlg.SetValue("Default")
	if dlg.ShowModal() == wx.ID_OK:
		self.SetStatusText('You entered: %s\n' % dlg.GetValue())
	dlg.Destroy()	
def message(self, event):
	dlg = wx.MessageDialog(self, 'To save one life is as if you have saved the world.', 'Talmud', wx.OK|wx.ICON_INFORMATION)
	dlg.ShowModal()
	dlg.Destroy()
def singlechoice(self, event):
	sins = ['Greed', 'Lust', 'Gluttony', 'Pride', 'Sloth', 'Envy', 'Wrath']
	dlg = wx.SingleChoiceDialog(self, 'Seven deadly sins', 'Which one?', sins, wx.CHOICEDLG_STYLE)
	if dlg.ShowModal() == wx.ID_OK:
		self.SetStatusText('You chose: %s\n' % dlg.GetStringSelection())
	dlg.Destroy()
def opendir(self, event):
	dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
	if dlg.ShowModal() == wx.ID_OK:
		self.SetStatusText('You selected: %s\n' % dlg.GetPath())
	dlg.Destroy()
class ConfigTree(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 350))

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		vbox = wx.BoxSizer(wx.VERTICAL)
		panel1 = wx.Panel(self, -1)
		panel2 = wx.Panel(self, -1)

		self.tree = wx.TreeCtrl(panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
		root = self.tree.AddRoot('Programmer')
		os = self.tree.AppendItem(root, 'Operating Systems')
		pl = self.tree.AppendItem(root, 'Programming Languages')
		tk = self.tree.AppendItem(root, 'Toolkits')
		self.tree.AppendItem(os, 'Linux')
		self.tree.AppendItem(os, 'FreeBSD')
		self.tree.AppendItem(os, 'OpenBSD')
		self.tree.AppendItem(os, 'NetBSD')
		self.tree.AppendItem(os, 'Solaris')
		cl = self.tree.AppendItem(pl, 'Compiled languages')
		sl = self.tree.AppendItem(pl, 'Scripting languages')
		self.tree.AppendItem(cl, 'Java')
		self.tree.AppendItem(cl, 'C++')
		self.tree.AppendItem(cl, 'C')
		self.tree.AppendItem(cl, 'Pascal')
		self.tree.AppendItem(sl, 'Python')
		self.tree.AppendItem(sl, 'Ruby')
		self.tree.AppendItem(sl, 'Tcl')
		self.tree.AppendItem(sl, 'PHP')
		self.tree.AppendItem(tk, 'Qt')
		self.tree.AppendItem(tk, 'MFC')
		self.tree.AppendItem(tk, 'wxPython')
		self.tree.AppendItem(tk, 'GTK+')
		self.tree.AppendItem(tk, 'Swing')
		self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)
		self.display = wx.StaticText(panel2, -1, '',(10,10), style=wx.ALIGN_CENTRE)
		vbox.Add(self.tree, 1, wx.EXPAND)
		hbox.Add(panel1, 1, wx.EXPAND)
		hbox.Add(panel2, 1, wx.EXPAND)
		panel1.SetSizer(vbox)
		self.SetSizer(hbox)
		self.Centre()

	def OnSelChanged(self, event):
		item =  event.GetItem()
		self.display.SetLabel(self.tree.GetItemText(item))
class CheckListBoxComboPopup(wx.CheckListBox, wx.combo.ComboPopup):
  
    def __init__(self, values):
        self.values = values
        self.PostCreate(wx.PreCheckListBox())
        wx.combo.ComboPopup.__init__(self)
  
    def Create(self, parent):
        wx.CheckListBox.Create(self, parent)
        self.InsertItems(self.values, 0)
        return True
  
    def GetControl(self):
        return self
  
    def OnPopup(self):
        combo = self.GetCombo()
        value = map(string.strip, combo.GetValue().split('|'))
        if value == ['']: value = []
        self.ignored = []
        for i in value:
            try:
                self.Check(self.values.index(i))
            except ValueError:
                # Try to find equal
                if self.equal.has_key(i):
                    self.Check(self.values.index(self.equal[i]))
                else:
                    logger.warning('unknown flag: %s: ignored.', i)
                    self.ignored.append(i)
  
        wx.combo.ComboPopup.OnPopup(self)
  
    def OnDismiss(self):
        combo = self.GetCombo()
        value = []
        for i in range(self.GetCount()):
            if self.IsChecked(i):
                value.append(self.values[i])
        # Add ignored flags
        value.extend(self.ignored)
        strValue = '|'.join(value)
        if combo.GetValue() != strValue:
            combo.SetValue(strValue)
            Presenter.setApplied(False)
  
        wx.combo.ComboPopup.OnDismiss(self)
class NewSessionDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size,data,  values_source,defaults, slib='My_Sessions',pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		wx.Dialog.__init__(self, None, -1, title, 	style=wx.DEFAULT_DIALOG_STYLE|wx.THICK_FRAME|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL)
  
		self.parent=parent
		self.data=data
		self.slib=slib
		self.values_source=values_source
		self.def_cv,self.def_tmpl=(None,None)
		self.tobjects=['All', 'Query', 'Table', 'Partition', 'Subpartition', 'Whitespace', 'Header', 'WideRows', 'NamedFile','List']
		self.fobjects=['File', 'Dir']			
		if defaults:
			self.def_cv=defaults[0] #default copy_vector if any

			self.def_tmpl=defaults[1].split('.') #default templates if any
		#print defaults
		#pprint(data)
		#print  '#'*40
		#print self.def_cv
		#self._popUpMenu = None
		#self.recent=[]
		if 0:
			pre = wx.PreDialog()
			pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
			pre.Create(parent, ID, title, pos, size, style)
		
			# This next step is the most important, it turns this Python
			# object into the real wrapper of the dialog (instead of pre)
			# as far as the wxPython extension is concerned.
			self.PostCreate(pre)

			# This extra style can be set after the UI object has been created.
			if 'wxMac' in wx.PlatformInfo and useMetal:
				self.SetExtraStyle(wx.DIALOG_EX_METAL)


		# Now continue with the normal construction of the dialog
		# contents
		#self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.tc_tables={}
		self.shards_btn={}
		self.tmpl={}
		self.copy_vector=[None,None]
		self.userhome = os.path.expanduser('~')
		self.recent_fname= os.path.join(self.userhome,'recent.p')
		self.recent=[]
		self._defMenu=None
		#self.s_default=None
		#self.t_default=None		
		self.default_db=self.parent.aconf['defaults']['default_db']
		#print self.parent.aconf
		if os.path.isfile(self.recent_fname):
			self.recent=self.readRecent()

		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(1, 4)			
			
			text1 = wx.StaticText(self, label="Session name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			#self.tc_sname = wx.TextCtrl(self,size=(400,23))
			self.tc_sname = masked.TextCtrl(self, -1, "",
										mask         = maskText[1],
										excludeChars = maskText[2],
										formatcodes  = maskText[3],
										includeChars = "_0123456789",
										validRegex   = maskText[4],
										validRange   = maskText[5],
										choices      = maskText[6],
										choiceRequired = False,
										defaultValue = maskText[7])			
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			self.tc_sname.Bind(wx.EVT_CHAR, self.onKeyPress)
			namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			icon = wx.StaticBitmap(self, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))


		
			#namesizer.Add((3,3),0)
			namesizer.Add(icon, pos=(0, 3), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)
			sizer.Add(namesizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.EXPAND, 5)

			
		line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)  
		sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)			
		if 1: #Source tmpl
			self.listCtrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_VRULES|wx.LC_HRULES)
			self.listCtrl.InsertColumn(0, 'Source Template')	
			if 0:
				self.listCtrl.InsertColumn(1, 'Type')		
				self.listCtrl.InsertColumn(2, 'Database')		
				self.listCtrl.InsertColumn(3, 'Object')
				self.listCtrl.InsertColumn(4, 'Limit')
				self.listCtrl.InsertColumn(5, 'Header')
				self.listCtrl.InsertColumn(6, 'Sharded')
				self.listCtrl.InsertColumn(7, 'Parallel')
			
			self.listCtrl.SetColumnWidth(0, 320)
			if 0:
				self.listCtrl.SetColumnWidth(1, 40)
				self.listCtrl.SetColumnWidth(2, 80)
				self.listCtrl.SetColumnWidth(3, 50)
				self.listCtrl.SetColumnWidth(4, 50)
				self.listCtrl.SetColumnWidth(5, 50)
				self.listCtrl.SetColumnWidth(6, 60)
				self.listCtrl.SetColumnWidth(7, 50)
			#copy_vector='ORA11G2ORA11G'
			
			
		if 1: #Target tmpl
			self.targlistCtrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT|wx.LC_VRULES|wx.LC_HRULES)
			self.targlistCtrl.InsertColumn(0, 'Target Template')	
			if 0:
				self.targlistCtrl.InsertColumn(1, 'Type')		
				self.targlistCtrl.InsertColumn(2, 'Database')		
				self.targlistCtrl.InsertColumn(3, 'Object')
				self.targlistCtrl.InsertColumn(4, 'Limit')
				self.targlistCtrl.InsertColumn(5, 'Header')
				self.targlistCtrl.InsertColumn(6, 'Sharded')
				self.targlistCtrl.InsertColumn(7, 'Parallel')
			
			self.targlistCtrl.SetColumnWidth(0, 320)
			if 0:
				self.targlistCtrl.SetColumnWidth(1, 40)
				self.targlistCtrl.SetColumnWidth(2, 80)
				self.targlistCtrl.SetColumnWidth(3, 50)
				self.targlistCtrl.SetColumnWidth(4, 50)
				self.targlistCtrl.SetColumnWidth(5, 50)
				self.targlistCtrl.SetColumnWidth(6, 60)
				self.targlistCtrl.SetColumnWidth(7, 50)
			if 0:
				self.plist={'ORA_Table':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Table_NoClient':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Table_TruncateTarget':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Table_TruncateTarget_NoClient':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Partition':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Partition_TruncateTarget':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Subpartition':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),
				'ORA_Subpartition_TruncateTarget':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),}
				for t, details in sorted(self.plist.items()):
					self.targlistCtrl.InsertStringItem(0, t)
					if 0:
						for i in range(len(details)):
							self.targlistCtrl.SetStringItem(0, i+1, details[i])		
		#self.listCtrl.Select(0)
		#button4 = wx.Button(self, ID_EXIT, "Test")
		
		if 0:
			sb = wx.StaticBox(self, label='Type')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			boxsizer.Add(wx.RadioButton(self, label="Copy",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=5)
			boxsizer.Add(wx.RadioButton(self, label="Extract"), flag=wx.LEFT|wx.TOP, border=5)
			boxsizer.Add(wx.RadioButton(self, label="Load"), flag=wx.LEFT|wx.TOP, border=5)
			if 0:
				rb=wx.RadioButton(self, label="FTP")
				boxsizer.Add(rb, flag=wx.LEFT|wx.TOP, border=5)
				rb.Enable(False)
				rb=wx.RadioButton(self, label="Pipe")
				boxsizer.Add(rb, flag=wx.LEFT|wx.TOP, border=5)
				rb.Enable(False)			
			#sizer.Add(boxsizer, pos=(2, 0), span=(1, 2), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)
		if 1: #Vector
			sb = wx.StaticBox(self, label='Copy Vector')
			vboxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			#rb_v=wx.RadioButton(panel, label="ora2ora",style=wx.RB_GROUP)
			lbl='Start(%s)' % self.default_db
			#print self.def_cv
			if self.def_cv and self.def_cv[0] and self.def_cv[1]:
				#print self.def_cv
				self.copy_vector=self.def_cv	
				#self.reset_lbl()
				#lbl='-'. join (self.copy_vector)
			#else:
			if 0:
				if self.s_default:
					self.copy_vector[0] = self.s_default
					#lbl='-'. join ([self.s_default,'???'])
					self.reset_lbl()
				if self.t_default:
					self.copy_vector[1] = self.t_default
					#lbl='-'. join (['???', self.t_default])
					self.reset_lbl()

				
				
			#if self.def_cv:
			#	#lbl='%s->%s' % (conf.dbs[self.def_cv[0]], conf.dbs[self.def_cv[1]])
				
			#	self.copy_vector=[self.def_cv[0].upper(), self.def_cv[1].upper()]
			
			self.b_vector = wx.Button(self, label=lbl,size=(100,35))
			#if self.def_cv:
				#self.set_vector_btn(self.def_cv[0], self.def_cv[1])
				
			#b_vector.Enable(True)
			vboxsizer.Add(self.b_vector, flag=wx.LEFT|wx.TOP, border=0)
			#self.b_vector.Bind(wx.EVT_BUTTON, self.OnCVClicked)
			self.b_vector.Bind(wx.EVT_BUTTON, self.OnShowPopup) # EVT_CONTEXT_MENU
			if 1:
				imageFile = os.path.join(home,"images/arrow_down_24.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				m_default = wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#tc[sn]['source'][0]
				m_default.SetName('host_map')
				m_default.Bind(wx.EVT_BUTTON, self.OnSetDefaultsMenu)
				vboxsizer.Add(m_default, flag=wx.LEFT|wx.TOP, border=0)
				
		self.optsizer = wx.BoxSizer(wx.HORIZONTAL)	
		#optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)		
		#optsizer.Add((3,3),0)
		self.optsizer.Add(vboxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)		
		#optsizer.Add((3,3),0)
		#optsizer.Add((5,5),1, wx.EXPAND)
		#optsizer.Add(button4, 0 , wx.RIGHT)
		sizer.Add(self.optsizer, 0, wx.EXPAND|wx.ALL|wx.GROW, 1)	
		listsizer = wx.BoxSizer(wx.HORIZONTAL)	
		listsizer.Add(self.listCtrl, 1 , wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)	
		listsizer.Add(self.targlistCtrl, 1 , wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)		
		sizer.Add(listsizer, 1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
		self.rbs={}
		if 1:
			sb = wx.StaticBox(self, label="Source Template")
			self.rb_boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)

			so=self.tobjects+self.fobjects
			self.s_rb={}
			style=0 
			bucket=8
			fgs=wx.GridBagSizer(2, 2) 
			for i in range(len(so)):
				rbname=so[i]
				if not i:
					style=wx.RB_GROUP
				else:
					style=0
				rb=wx.RadioButton(self, label=rbname,style=style)
				rb.SetName=rbname
				rb.Enable(False)
				rb.Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
				fgs.Add(rb, pos=(i/bucket,i%bucket), flag=wx.LEFT, border=0)
				self.s_rb[rbname]=rb
				if 0:
					self.s_rb[rbname]=wx.RadioButton(self, label=rbname,style=style)
					self.s_rb[rbname].SetName=rbname
					self.rb_boxsizer.Add(self.s_rb[rbname], flag=wx.LEFT|wx.TOP, border=0)
					self.s_rb[rbname].Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
					self.s_rb[rbname].Enable(False)
			self.rb_boxsizer.Add(fgs, flag=wx.LEFT|wx.TOP, border=1)
			self.optsizer.Add(self.rb_boxsizer, 0 , wx.LEFT,0)	
		if 0:
			sb = wx.StaticBox(self, label="Target Object")
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			#boxsizer.Add(wx.RadioButton(self, label="Query",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=5)
			#boxsizer.Add(wx.RadioButton(self, label="Table",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=5)
			#boxsizer.Add(wx.RadioButton(self, label="Partition"), flag=wx.LEFT|wx.TOP, border=5)
			#boxsizer.Add(wx.RadioButton(self, label="Sub-Partition"), flag=wx.LEFT|wx.TOP, border=5)
			
			so=['Table', 'Partition', 'Sub-Partition']
			t_rb={}
			style=0
			for i in range(len(so)):
				rbname=so[i]
				if not i:
					style=wx.RB_GROUP
				else:
					style=0
				t_rb[rbname]=wx.RadioButton(self, label=rbname,style=style)
				boxsizer.Add(t_rb[rbname], flag=wx.LEFT|wx.TOP, border=5)
				t_rb[rbname].Bind(wx.EVT_RADIOBUTTON, self.onTargetObjButton)

				
			self.optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)	
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		if 1:
			sb = wx.StaticBox(self, label='Arguments source')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.rb_use_templates=wx.RadioButton(self, label="Templates",style=wx.RB_GROUP)
			boxsizer.Add(self.rb_use_templates, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_set_manually=wx.RadioButton(self, label="Generic")
			self.rb_set_manually.Enable(True)
			boxsizer.Add(self.rb_set_manually, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_use_templates.Bind(wx.EVT_RADIOBUTTON, self.onUseRbButton)
			self.rb_set_manually.Bind(wx.EVT_RADIOBUTTON, self.onUseRbButton)
			btnsizer.Add(boxsizer, 0 , wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND)
		if 0: #checkbox
			sb = wx.StaticBox(self, label='Source Values')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			#self.rb_use_templates=wx.RadioButton(self, label="Templates",style=wx.RB_GROUP)
			self.values = ['test1','test2']
			popup = CheckListBoxComboPopup(self.values)
			self.combo = wx.combo.ComboCtrl(self, size=(220,-1))
			self.combo.SetPopupControl(popup)
			boxsizer.Add(self.combo, 1, wx.ALL, 0)
			self.combo.Bind(wx.EVT_TEXT, self.OnChange)
			#self.combo.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
			btnsizer.Add(boxsizer, 0 , wx.TOP|wx.BOTTOM|wx.LEFT)
		if 1:
			if self.values_source:
				lbl='Reuse "%s" Values' % self.values_source
				sb = wx.StaticBox(self, label=lbl)
				boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)			
				self.rb_r0=wx.CheckBox(self, label='Common')
				self.rb_r1=wx.CheckBox(self, label='Source+Target')
				#self.rb_r2=wx.CheckBox(self, label='Target')
				self.rb_r0.Enable(True)
				self.rb_r0.SetValue(False)
				self.rb_r1.Enable(True)
				self.rb_r1.SetValue(True)
				#self.rb_r2.Enable(True)
				#self.rb_r2.SetValue(False)
				boxsizer.Add(self.rb_r0, flag=wx.LEFT|wx.TOP, border=5)
				boxsizer.Add(self.rb_r1, flag=wx.LEFT|wx.TOP, border=5)
				#boxsizer.Add(self.rb_r2, flag=wx.LEFT|wx.TOP, border=5)
				
				btnsizer.Add(boxsizer, 0 , wx.TOP|wx.BOTTOM|wx.LEFT|wx.EXPAND)			
		#self.test = wx.Button(self, wx.NewId(), 'Test')
		if 1:
			#btnsizer = wx.BoxSizer(wx.HORIZONTAL)
			#st_tlib = wx.StaticText(self, label="Session library:")
			#namesizer.Add(st_tlib, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)			
			sb = wx.StaticBox(self, label='Session Library')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			libs=self.getSessionLibNames()
			#print libs
			#e(0)
			self.cb_tname= wx.ComboBox(self, id=wx.NewId(), value=self.slib, choices=libs, size=(100,30), style=0, name='tmpl_lib')
			boxsizer.Add(self.cb_tname, flag=wx.LEFT|wx.TOP, border=1)
			#namesizer.Add(self.cb_tname, pos=(1, 1),  flag=wx.TOP|wx.ALIGN_LEFT|wx.BOTTOM, border=10)
			btnsizer.Add(boxsizer, 0 , wx.TOP|wx.LEFT)	
		self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		self.create_btn.Enable(False)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		#btnsizer.Add(self.test, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		#self.test.Bind(wx.EVT_BUTTON, self.OnTest)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)


		self.SetSizer(sizer)
		#sizer.Fit(self)
		#self.SetSize((600,400))
		(x,y) = self.parent.GetScreenPositionTuple()
		(l,w) =self.parent.GetClientSizeTuple()
		dl,dw= size
		self.SetDimensions(x+(l-dl)/2, y+(w-dw)/2, dl,dw)
		self.i=0 #menu counter
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSrcTmplSelected, self.listCtrl)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnTargTmplSelected, self.targlistCtrl)
		self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnTargTmplDeselected, self.targlistCtrl)
		self.api_args=None
		self.changed=False
		if 1:
			apidir= os.path.join(home,aa_dir)
			#print apidir
			self.api_from = [ f.upper() for f in os.listdir(apidir) if os.path.isdir(os.path.join(apidir,f)) and f not in conf.ff] # and f not in conf.dt]
			#print self.api_from
			#print conf.ff
			#print conf.dt
			#e(0)
			self.api2= list(set(conf.dbfam.values()))
			self.api2.sort()
			#print self.api2
			#e(0)
			self.api_menu={}
			if 0:
				for m in self.api_from:
					#print m
					
					if not self.api_menu.has_key(m[:2]):
						self.api_menu[m[:2]]=[]
					self.api_menu[m[:2]].append(m)
			for m in self.api_from:
				k=conf.dbfam[m]
				assert m in conf.dbfam.keys(), '"%s: is not defined in dbfam' % m
				if not self.api_menu.has_key(k):
					self.api_menu[k]=[]
				self.api_menu[k].append(m)
			#pprint (self.api_menu)
			#e(0)
			#print pprint(self.api_menu)

			
		if self.copy_vector and self.copy_vector[0] and self.copy_vector[1]:
			#print self.def_cv
			#self.copy_vector=self.def_cv
			self.refresh_src_list()
			sname=''
			for i in range(self.listCtrl.GetItemCount()):
				if self.listCtrl.GetItemText(i) in [self.def_tmpl[0]]:
					self.listCtrl.SetItemState(i, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
					self.listCtrl.EnsureVisible(i)
					sname=self.def_tmpl[0]
			for i in range(self.targlistCtrl.GetItemCount()):
				if self.targlistCtrl.GetItemText(i) in [self.def_tmpl[1]]:
					self.targlistCtrl.SetItemState(i, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)
					self.targlistCtrl.EnsureVisible(i)
					sname='%s_to_%s' % (sname,self.def_tmpl[1])
			self.setDefaultName(sname)
			a,b = self.copy_vector
			if 1:
				if a.startswith('CSV'):
					for n in self.tobjects:
						self.s_rb[n].Enable(False)
					for n in self.fobjects:
						self.s_rb[n].Enable(True)
				elif b.startswith('CSV'):
					for n in self.tobjects:
						self.s_rb[n].Enable(True)
					for n in self.fobjects:
						self.s_rb[n].Enable(True)
				else:
					for n in self.tobjects:
						self.s_rb[n].Enable(True)
					for n in self.fobjects:
						self.s_rb[n].Enable(True)
				
			#self.rb_boxsizer.Enable(True)
		#old_size = self.GetSize()
		self.Layout()
		self.Fit()
		self.SetSize((-1,size[1]))
		self.recentMenu=None
		self.max_recent=10
		self.highlight=['ORA11G']
		self._cvMenu=None
		#print gc.get_count()
		#self.popupmenu=None
		
	
	def createNativeCVMenu(self):
		if not self.recentMenu:
			self.recentMenu = wx.Menu()
		#else:
		#	self.recentMenu.Clear()

		if not self._cvMenu:
			self._cvMenu = wx.Menu()
			if 1: #len(self.recent):
				#self.i +=1
				#menuItem = FM.FlatMenuItem(self._cvMenu, 20005, 'Recent', '', wx.ITEM_NORMAL, self.recentMenu)
				#menu1 = wx.Menu()
				
				#item = self._cvMenu.Append(-1, 'Recent')
				#self._cvMenu.AppendItem(menuItem)
				if self.recent:
					for r in reversed(self.recent):
						(a,b)=r
						a=a.upper()
						b=b.upper()
						self.i +=1
						#Menu1 = FM.FlatMenu()
						#menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
						item = self.recentMenu.Append(wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]))
						self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(a,b))
						#self.recentMenu.AppendItem(menuItem)
			self._cvMenu.AppendMenu(wx.NewId(),'Recent',self.recentMenu)
			#self._cvMenu.AppendSeparator()
			
			if 1:
				k=self.default_db #self.api2[0]
				#print self.api2
				#e(0)
				m=self._cvMenu
				for sm in self.api_menu[k]:
					if len(self.api_menu[k])>0:
						self.i +=1
						self.create_Menu2_short_2(m,sm)
						
					else:
						k2= self.api2[0]
						if 1:
							self.i +=1
							self.create_Menu4_2(m,self.api_menu[k2][0],from_db=sm, from_to='To 2 ')
						

						m.AppendSeparator()
						for sm in conf.ff:
							#self.i +=1
							#Menu1 = FM.FlatMenu()
							#menuItem = FM.FlatMenuItem(m, wx.NewId(), 'To %s' % sm, '', wx.ITEM_NORMAL)
							#m.AppendItem(menuItem)		
							item = m.Append(wx.NewId(), 'To %s' % sm)							
							self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(k,sm))	
			if 1: #From other dbs
				self._cvMenu.AppendSeparator()
				Menu1_2 = wx.Menu()
				#menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From other DB', '', wx.ITEM_NORMAL, Menu1_2)
				#self._cvMenu.AppendItem(menuItem)
				self._cvMenu.AppendMenu(wx.NewId(),'From other DB',Menu1_2)
				self.from_other_db_Menu_2(Menu1_2)
				#e(0)
			self._cvMenu.AppendSeparator()
			if 1: #From Web/CURL
				#self._cvMenu.AppendSeparator()
				Menu2_2 = wx.Menu()
				#menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From other DB', '', wx.ITEM_NORMAL, Menu1_2)
				#self._cvMenu.AppendItem(menuItem)
				self._cvMenu.AppendMenu(wx.NewId(),'From Web',Menu2_2)
				self.from_web_Menu_2(Menu2_2)
				Menu2_2.AppendSeparator()
				for k2 in self.api2:
					self.i +=1
					if self.api_menu.has_key(k2): 
						#print k2, len(self.api_menu[k2])
						if len(self.api_menu[k2])>1:
							#print 1
							self.create_Menu3_2(Menu2_2,k2,from_db='CURL',from_to='From Web to')
						else:
							#print 2,self.api_menu[k2][0]
							self.create_Menu4_2(Menu2_2,self.api_menu[k2][0],from_db='CURL',from_to='From Web to')				
				#e(0)				
			self._cvMenu.AppendSeparator()	
			for sm in conf.ff:
				#self.i +=1
				Menu1 = wx.Menu()
				#menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From %s' % sm, '', wx.ITEM_NORMAL, Menu1)
				#self._cvMenu.AppendItem(menuItem)	
				self._cvMenu.AppendMenu(wx.NewId(),'From %s' % sm,Menu1)
				#pprint (self.api_menu)
				for k2 in self.api2:
					self.i +=1
					if self.api_menu.has_key(k2): 
						#print k2, len(self.api_menu[k2])
						if len(self.api_menu[k2])>1:
							#print 1
							self.create_Menu3_2(Menu1,k2,from_db=sm)
						else:
							#print 2,self.api_menu[k2][0]
							self.create_Menu4_2(Menu1,self.api_menu[k2][0],from_db=sm)
						
				
		else:
			#pprint(dir(self.recentMenu))
			#self.recentMenu.Clear()
			if self.recent:
				for r in reversed(self.recent):
					(a,b)=r
					a=a.upper()
					b=b.upper()
					self.i +=1
					#Menu1 = FM.FlatMenu()
					#menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
					#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
					#self.recentMenu.AppendItem(menuItem)
					item = self.recentMenu.Append(wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]))
					self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(a,b))					
	def create_Menu3_2(self,Menu2,k2,from_db, from_to='To'):
		#print from_db, k2
		#from_to='To_%s_%s' %(from_db,k2)
		self.i +=1
		Menu3 = wx.Menu()
		#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), "%s %s" % (from_to, k2), "", wx.ITEM_NORMAL, Menu3)
		#Menu2.AppendItem(menuItem)
		Menu2.AppendMenu(wx.NewId(),"%s %s" % (from_to, k2),Menu3)
		#if not k2 in ['OR']:
		#	menuItem.Enable(False)
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4_2(Menu3,sm2,from_db,from_to)
		if 0 and  from_db not in conf.ff:
			Menu2.AppendSeparator()
			for s in conf.ff:
				self.i +=1
				#Menu1 = FM.FlatMenu()
				#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
				item=Menu2.Append(wx.NewId(), 'To %s' % s)
				self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(k2,s))
				#Menu2.AppendItem(menuItem)	
					
	def from_other_db_Menu_2(self,Menu):
		for k in  [x for x in self.api_menu.keys() if x not in conf.tt+conf.dt]:
			#print k
			if k not in [self.default_db]:
			
				Menu1 = wx.Menu()
				#menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				#Menu.AppendItem(menuItem)
				Menu.AppendMenu(wx.NewId(),k,Menu1)
				#print self.api_menu[k]
				for k2 in self.api_menu[k]:
					#self.create_Menu3(Menu1,k2,from_db=k)
					
					#print from_db, k2
					#from_to='To_%s_%s' %(from_db,k2)
					#self.i +=1
					Menu2 = wx.Menu()
					#menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), "From %s" % ( k2), "", wx.ITEM_NORMAL, Menu2)
					#Menu1.AppendItem(menuItem)
					Menu1.AppendMenu(wx.NewId(),"From %s" % ( conf.dbs[k2]),Menu2)
					#if not k2 in ['OR']:
					#	menuItem.Enable(False)
					for sm2 in self.api_menu[self.default_db]:
						#self.i +=1
						self.create_Menu4_2(Menu2,sm2,k2,from_to='To')
		Menu.AppendSeparator()
		for k in  conf.tt:
			#print k
			if k not in [self.default_db]:
			
				Menu1 = wx.Menu()
				#menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				#Menu.AppendItem(menuItem)
				Menu.AppendMenu(wx.NewId(),k,Menu1)
				#print self.api_menu[k]
				for k2 in self.api_menu[k]:
					#self.create_Menu3(Menu1,k2,from_db=k)
					
					#print from_db, k2
					#from_to='To_%s_%s' %(from_db,k2)
					#self.i +=1
					Menu2 = wx.Menu()
					#menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), "From %s" % ( k2), "", wx.ITEM_NORMAL, Menu2)
					#Menu1.AppendItem(menuItem)
					Menu1.AppendMenu(wx.NewId(),"From %s" % ( conf.dbs[k2]),Menu2)
					#if not k2 in ['OR']:
					#	menuItem.Enable(False)
					for sm2 in self.api_menu[self.default_db]:
						#self.i +=1
						self.create_Menu4_2(Menu2,sm2,k2,from_to='To')
		Menu.AppendSeparator()
		for k in  conf.dt:
			#print k
			if k not in [self.default_db]:
			
				Menu1 = wx.Menu()
				#menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				#Menu.AppendItem(menuItem)
				Menu.AppendMenu(wx.NewId(),k,Menu1)
				#print self.api_menu[k]
				for k2 in self.api_menu[k]:
					#self.create_Menu3(Menu1,k2,from_db=k)
					
					#print from_db, k2
					#from_to='To_%s_%s' %(from_db,k2)
					#self.i +=1
					Menu2 = wx.Menu()
					#menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), "From %s" % ( k2), "", wx.ITEM_NORMAL, Menu2)
					#Menu1.AppendItem(menuItem)
					Menu1.AppendMenu(wx.NewId(),"From %s" % ( conf.dbs[k2]),Menu2)
					#if not k2 in ['OR']:
					#	menuItem.Enable(False)
					for sm2 in self.api_menu[self.default_db]:
						#self.i +=1
						self.create_Menu4_2(Menu2,sm2,k2,from_to='To')						
	def from_web_Menu_2(self,Menu2):
			for w in conf.dt:
				for s in conf.ff[:-1]:
					self.i +=1
					#Menu1 = FM.FlatMenu()
					#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
					item=Menu2.Append(wx.NewId(), '%s To %s' % (w,s))
					self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(w,s))
					#Menu2.AppendItem(menuItem)	
				
	def create_Menu2_short_2(self,Menu1,sm, from_to='From'):
		#self.i +=1
		Menu2 = wx.Menu()
		if 0:
			if sm in self.api_menu[self.default_db]:
				imageFile = os.path.join(home,"images/database_green_16.png")
				if sm in self.highlight:
					imageFile = os.path.join(home,"images/database_red_16.png")
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				item = Menu2.Append(wx.NewId(),  '%s %s' % (from_to, conf.dbs[sm]) )
				#menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2,context_bmp)
			else:
				item = Menu2.Append(wx.NewId(),  '%s %s' % (from_to, conf.dbs[sm]) )
				#menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2)
			
		Menu1.AppendMenu(wx.NewId(),'%s %s' % (from_to, conf.dbs[sm]) ,Menu2)
		#Menu1.AppendItem(menuItem)
		

			
		k2=self.default_db
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4_2(Menu2,sm2,sm,'To')
		if 1: #To other dbs
			Menu2.AppendSeparator()
			Menu3 = wx.Menu()
			#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To other DB', '', wx.ITEM_NORMAL, Menu3)
			#Menu2.AppendItem(menuItem)
			Menu2.AppendMenu(wx.NewId(), 'To other DB' ,Menu3)
			self.to_other_db_Menu_2(Menu3,sm)

		#append to_csv
		Menu2.AppendSeparator()
		for s in conf.tt:
			#self.i +=1
			#Menu1 = FM.FlatMenu()
			#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
			item = Menu2.Append(wx.NewId(),  'To %s' % s )
			self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(sm,s))
			#Menu2.AppendItem(menuItem)
		Menu2.AppendSeparator()
		for s in conf.dt:
			#self.i +=1
			#Menu1 = FM.FlatMenu()
			#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
			item = Menu2.Append(wx.NewId(),  'To %s' % s )
			self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(sm,s))
			#Menu2.AppendItem(menuItem)	
		#append to_csv
		Menu2.AppendSeparator()
		for s in conf.ff:
			#self.i +=1
			#Menu1 = FM.FlatMenu()
			#menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
			item = Menu2.Append(wx.NewId(),  'To %s' % s )
			self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(sm,s))
			#Menu2.AppendItem(menuItem)					

	def create_Menu4_2(self,Menu3,sm2,from_db, from_to='To'):
		#self.i +=1
		#print sm2, from_db
		#imageFile = os.path.join(home,"images/database_grey_16.png")
		if 0:
			if sm2 in self.api_menu[self.default_db]:
				imageFile = os.path.join(home,"images/database_green_16.png")
				if sm2 in self.highlight:
					imageFile = os.path.join(home,"images/database_red_16.png")
				assert os.path.isfile(imageFile), 'image file does not exists\n%s' % imageFile
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				
				menuItem = FM.FlatMenuItem(Menu3, wx.NewId(), "%s %s" % (from_to, conf.dbs[sm2]) , "", wx.ITEM_NORMAL, None,context_bmp)
			else:
				menuItem = FM.FlatMenuItem(Menu3, wx.NewId(), "%s %s" % (from_to, conf.dbs[sm2]) , "", wx.ITEM_NORMAL)
			#menuItem.SetFont(wx.Font(10, wx.SWISS, wx.ITALIC, wx.BOLD, False, "Courier New"))
			#menuItem.SetTextColour(wx.RED)
			#pprint(dir(menuItem))
		item=Menu3.Append(wx.NewId(),'%s %s' % (from_to, conf.dbs[sm2]))
		self.gen_bind(wx.EVT_MENU,item, self.OnMenu,(from_db,sm2))
		#Menu3.AppendItem(menuItem)
	def to_other_db_Menu_2(self,Menu,from_db):
		for k in [x for x in self.api_menu.keys() if x not in conf.tt+conf.dt]:
			#print k
			if k not in [self.default_db]:
				Menu1 = wx.Menu()
				#menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				#Menu.AppendItem(menuItem)
				Menu.AppendMenu(wx.NewId(), k ,Menu1)
				for k2 in self.api_menu[k]:
					#for sm2 in self.api_menu[self.default_db]:
					#self.i +=1
					self.create_Menu4_2(Menu1,k2,from_db,from_to='To')
				
		
	def CreatePopupMenu2(self):
		if not self.recentMenu:
			self.recentMenu = FM.FlatMenu()
		else:
			self.recentMenu.Clear()

		if not self._cvMenu:
		
			self._cvMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------
			dbf={'OR':'Oracle', 'SS':'SQLServer', 'MA':'MariaDB', 'MY': 'MySQL', 'PG':'PostgreSQL', 'DB':'DB2', 'TT':'TimesTen', 'SL':'SQLite', 'IN':'Informix', 'SY':'Sybase','MO':'Mongo'}
			self.i=0
			if 1: #len(self.recent):
				self.i +=1
				menuItem = FM.FlatMenuItem(self._cvMenu, 20005, 'Recent', '', wx.ITEM_NORMAL, self.recentMenu)
				self._cvMenu.AppendItem(menuItem)
				if self.recent:
					for r in reversed(self.recent):
						(a,b)=r
						a=a.upper()
						b=b.upper()
						self.i +=1
						#Menu1 = FM.FlatMenu()
						menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
						self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
						self.recentMenu.AppendItem(menuItem)
					
				self._cvMenu.AppendSeparator()
			if 0 and len(self.api2)>1:
				for k in self.api2:
					self.i +=1
					Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From %s' % k, '', wx.ITEM_NORMAL, Menu1)
					self._cvMenu.AppendItem(menuItem)
					#if not k in ['OR']:
					#	menuItem.Enable(False)
					#print k
					#pprint (self.api_menu)
					e(0)
					for sm in self.api_menu[k]:
						if 1 or len(self.api_menu[k])>1:
							self.i +=1
							self.create_Menu2(Menu1,sm,dbf)
							
						else:
							for k2 in self.api2:
								self.i +=1
								if len(self.api_menu[k2])>1:
									self.create_Menu3(Menu1,k2,from_db=sm,from_to='To')
								else:
									self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm, from_to='To')
							Menu1.AppendSeparator()
							for sm in conf.ff:
								self.i +=1
								#Menu1 = FM.FlatMenu()
								menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), 'To %s' % sm, '', wx.ITEM_NORMAL)
								Menu1.AppendItem(menuItem)									
								self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(dbf[k],sm))
			#else:
			if 1:
				k=self.default_db #self.api2[0]
				#print self.api2
				#e(0)
				Menu1=self._cvMenu
				for sm in self.api_menu[k]:
					if 1  or len(self.api_menu[k])>1:
						self.i +=1
						self.create_Menu2_short(Menu1,sm,dbf)
						
					else:
						k2= self.api2[0]
						if 1:
							self.i +=1
							self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm, from_to='To 2 ')
						

						Menu1.AppendSeparator()
						for sm in conf.ff:
							self.i +=1
							#Menu1 = FM.FlatMenu()
							menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), 'To %s' % sm, '', wx.ITEM_NORMAL)
							Menu1.AppendItem(menuItem)									
							self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(k,sm))	
			if 1: #From other dbs
				self._cvMenu.AppendSeparator()
				Menu1_2 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From other DB', '', wx.ITEM_NORMAL, Menu1_2)
				self._cvMenu.AppendItem(menuItem)
				self.from_other_db_Menu(Menu1_2)
				#e(0)
			self._cvMenu.AppendSeparator()	
			for sm in conf.ff:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From %s' % sm, '', wx.ITEM_NORMAL, Menu1)
				self._cvMenu.AppendItem(menuItem)	
				#pprint (self.api_menu)
				for k2 in self.api2:
					self.i +=1
					if self.api_menu.has_key(k2): 					
						if len(self.api_menu[k2])>1:
							self.create_Menu3(Menu1,k2,from_db=sm)
						else:
							self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm)
						
				
		else:
			#pprint(dir(self.recentMenu))
			#self.recentMenu.Clear()
			if self.recent:
				for r in reversed(self.recent):
					(a,b)=r
					a=a.upper()
					b=b.upper()
					self.i +=1
					#Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
					self.recentMenu.AppendItem(menuItem)
		#print gc.get_count()		
	def OnShowPopup(self, event):
		btn = event.GetEventObject()
		btnSize = btn.GetSize()
		pos =  btn.GetPosition()
		btnPt = btn.GetScreenPosition()
		btnPt = self.ScreenToClient(btnPt)
		btnPt = btnPt.x, btnPt.y + btnSize.y
		if not self._cvMenu:
			self.createNativeCVMenu()
		self.PopupMenu(self._cvMenu, btnPt)
				
		

	def OnPopupItemSelected(self, event):
		item = self._cvMenu.FindItemById(event.GetId())
		text = item.GetText()
		wx.MessageBox("You selected item '%s'" % text)
		
	def reset_lbl(self):
		#pprint(self.copy_vector)
		lbl='Start(%s)' % self.default_db
		self.b_vector.SetLabel(lbl)
	def OnSetDefaultsMenu(self, event):
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()
		#print 1
		if 1:
			# Create the popup menu
			self.CreateDefaultsMenu()
			btnSize = btn.GetSize()
			
			btnPt = btn.GetPosition()
			#print '1 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			#print '2 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			#print 'btnSize.y', btnSize.y
			self._defMenu.SetOwnerHeight(btnSize.y)
			#print 'btnPt.x, btnPt.y', btnPt.x, btnPt.y
			self._defMenu.Popup(wx.Point(btnPt.x, btnPt.y+50), self)
			mpsn=self._defMenu.GetScreenPosition()
			#print 'mpsn', mpsn
			#adjust
			if btnPt.y<mpsn[1]:
				self._defMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
			#print self._hmMenu.ClientToScreen(mpsn)
			#print	dir(self._hmMenu)

		
	def CreateDefaultsMenu(self):
		if not self._defMenu:
		
			self._defMenu = FM.FlatMenu()
			#pprint(conf.dbfam)
			if 1:
				self.i +=1
				#self._defMenu.AppendSeparator()
				imageFile = os.path.join(home,'images','Right_Arrow_16.png')
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._defMenu, wx.NewId(), 'Set default db', '', wx.ITEM_NORMAL, Menu1, context_bmp)
				#print self.args_panel.hm.host_map_loc				
				#if not is_default:					
				#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
				menuItem.Enable(True)
				self._defMenu.AppendItem(menuItem)
				dbfam= list(set([conf.dbfam[x] for x in conf.dbfam.keys()]))				
				letters= list(set([x[0] for x in dbfam]))				
				for ch in letters:
					imageFile = os.path.join(home,'images','Right_Arrow_16.png')
					context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
					Menu2 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), ch, '', wx.ITEM_NORMAL, Menu2, context_bmp)
					#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
					menuItem.Enable(True)
					Menu1.AppendItem(menuItem)
					for db in [x for x in dbfam if x.startswith(ch)]:
						imageFile = os.path.join(home,'images','database_green_16.png')
						context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)						
						menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), db, '', wx.ITEM_NORMAL, None, context_bmp)
						self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSetDefaultDb,(db,))
						menuItem.Enable(True)
						Menu2.AppendItem(menuItem)
						
						
			if 0:
				self.i +=1
				#self._defMenu.AppendSeparator()
				imageFile = os.path.join(home,'images','Right_Arrow_16.png')
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._defMenu, wx.NewId(), 'Set "Source" default db', '', wx.ITEM_NORMAL, Menu1, context_bmp)
				#print self.args_panel.hm.host_map_loc				
				#if not is_default:					
				#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
				menuItem.Enable(True)
				self._defMenu.AppendItem(menuItem)
				letters= list(set([x[0] for x in conf.dbs.keys() if x not in conf.ff]))				
				for ch in letters:
					imageFile = os.path.join(home,'images','Right_Arrow_16.png')
					context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
					Menu2 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), ch, '', wx.ITEM_NORMAL, Menu2, context_bmp)
					#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
					menuItem.Enable(True)
					Menu1.AppendItem(menuItem)
					for db in [x for x in conf.dbs.keys() if x not in conf.ff and x.startswith(ch)]:
						imageFile = os.path.join(home,'images','database_green_16.png')
						context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)						
						menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), conf.dbs[db], '', wx.ITEM_NORMAL, None, context_bmp)
						self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSetSourceDefault,(db,))
						menuItem.Enable(True)
						Menu2.AppendItem(menuItem)
						
					
				
				#else:
				#	menuItem.Enable(False)
				if 0:
					imageFile = os.path.join(home,'images','Right_Arrow_16.png')
					context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
					Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._defMenu, wx.NewId(), 'Set "Target" default db', '', wx.ITEM_NORMAL, Menu1, context_bmp)
					#print self.args_panel.hm.host_map_loc				
					#if not is_default:					
					#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
					menuItem.Enable(True)
					#else:
					#	menuItem.Enable(False)
					self._defMenu.AppendItem(menuItem)	
					letters= list(set([x[0] for x in conf.dbs.keys() if x not in conf.ff]))				
					for ch in letters:
						imageFile = os.path.join(home,'images','Right_Arrow_16.png')
						context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
						Menu2 = FM.FlatMenu()
						menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), ch, '', wx.ITEM_NORMAL, Menu2, context_bmp)
						#self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
						menuItem.Enable(True)
						Menu1.AppendItem(menuItem)
						for db in [x for x in conf.dbs.keys() if x not in conf.ff and x.startswith(ch)]:
							imageFile = os.path.join(home,'images','database_green_16.png')
							context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)						
							menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), conf.dbs[db], '', wx.ITEM_NORMAL, None, context_bmp)
							self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSetTargetDefault,(db,))
							menuItem.Enable(True)
							Menu2.AppendItem(menuItem)
						
	def OnSetDefaultDb(self, event, params): 
		[db] = params
		#print db
		self.default_db = db
		self.parent.aconf['defaults']['default_db']=db
		#self.copy_vector[0] = self.s_default
		#lbl='-'. join (['???', self.t_default])
		self.reset_lbl()		
		send('set_bar_status', (0,'Default DB is set to "%s" ' % db))
		#self._popUpMenu.Clear()
		#self.recentMenu.Clear()
		#print (dir(self._popUpMenu))
		del self._cvMenu
		del self.recentMenu
		del self._defMenu
		self._cvMenu=None
		self.recentMenu=None
		self._defMenu=None
		#self._cvMenu=None
		#self.recentMenu=None
	def OnSetTargetDefault_(self, event, params): 
		[db] = params
		self.t_default=db
		self.copy_vector[1] = self.t_default
		self.reset_lbl()		
		send('set_bar_status', (0,'Target default DB is set to "%s" ' % db))

	def getSessionLibNames(self):
		global session_home
		libs= [d for d in os.listdir(session_home) if os.path.isdir(os.path.join(session_home,d))]
		return libs		
	def setDefaultName(self, sname):
		if not self.changed:
			self.tc_sname.SetValue(sname.strip().strip(' ').replace(' ',''))
	def onKeyPress(self, event):
		#print str(self.__class__) + " - onKeyPress"
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()				
			if	kc == 4:
				print 'Ctrl-D 1'
				self.parent.tryToDelete()
		else:
			if kc<123 and not (kc == wx.WXK_SPACE): #(kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				#self.parent.btn_save.Enable(True)
				#self.parent.changed=True
				#print 'changed'
				if not self.changed:
					self.changed=True
		
		event.Skip()
		
		
	def OnTest(self,e):
		[cn, slib, cv, tmpl, args, reuse] = self.getConfig()		
		#print len(args)	
		#pprint(args[2])
		#pprint(self.api_args[tmpl][0])
	def OnChange(self, evt):
		# ComboCtrl still generates events in SetValue
		if self.freeze: return
		Presenter.setApplied(False)
		evt.Skip() 			
	def onSourceValues(self, evt):
		print 'onSourceValues'
	def getConfig(self):
		tmpl=self.get_template()
		reuse=None
		slib=self.cb_tname.GetValue()
		#print(self.api_args['default'])
		if self.values_source:
			reuse=(self.rb_r0.GetValue(),self.rb_r1.GetValue() ) #,self.rb_r2.GetValue())
		if tmpl in ['generic.generic']:
			default_args=self.api_args['default']
			#print self.copy_vector
			default_args[0]['copy_vector'][2]=conf._to.join(self.copy_vector)
			return [self.getSessionName(), slib, self.copy_vector, tmpl, default_args, reuse]
		else:
			return [self.getSessionName(), slib, self.copy_vector, tmpl, self.api_args[tmpl], reuse]
	def getSessionName(self):
		return self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
	def onSourceObjButton(self, event): 
		""" 
		Source object filter
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
		if label in ('All'):
			label=''
		self.refresh_src_list(label)
		#print btn
	def onTargetObjButton(self, event): 
		""" 
		Target object filter
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
		
	def onUseRbButton(self, event): 
		""" 
		Use type
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
		if 'GENERIC' in label.upper():
			self.create_btn.Enable(True)
			self.targlistCtrl.Enable(False)
			self.listCtrl.Enable(False)
			self.setDefaultName('')
			#self.tc_sname.SetValue('')
			
			so=self.tobjects+self.fobjects
			for s in so:
				self.s_rb[s].Enable(False)
			
		else:
			self.targlistCtrl.Enable(True)
			self.listCtrl.Enable(True)
			sname=self.get_template().replace('.','_to_')
			#print 'sname',sname
			self.setDefaultName(sname)
			#self.tc_sname.SetValue(sname)
			#self.tc_sname.SetValue('')
			
			so=self.tobjects+self.fobjects
			for s in so:
				self.s_rb[s].Enable(True)
				
			#print 'targlistCtrl',self.targlistCtrl.GetFirstSelected()
			if self.targlistCtrl.GetFirstSelected()<0:
				self.create_btn.Enable(False)
			else:
				#print 'listCtrl', self.listCtrl.GetFirstSelected()
				if self.listCtrl.GetFirstSelected()<0:
					self.create_btn.Enable(False)

			
	def refresh_src_list(self, filter=None):
		self.Freeze()
		print gc.get_count()
		assert self.copy_vector, 'copy_vector is not set.'
		self.listCtrl.ClearAll()
		self.listCtrl.InsertColumn(0, 'Source Template')
		self.listCtrl.SetColumnWidth(0, 320)
		self.targlistCtrl.ClearAll()
		self.targlistCtrl.InsertColumn(0, 'Target Template')	
		self.targlistCtrl.SetColumnWidth(0, 320)	
		self.tmpl={}
		from_to = self.copy_vector
		api_home=os.path.join(home,aa_dir)
		from_home=os.path.join(api_home,from_to[0])
		#to_home=os.path.join(from_home,from_to[1])
		assert os.path.isdir(from_home), '"From" args_api %s does not exists in %s' % (from_to[0],api_home)
		api_file=os.path.join(from_home,'%s-%s.py' % tuple(from_to))
		#print api_file
		assert os.path.isfile(api_file), 'api_file %s does not exists.' % (api_file)
		#from os import listdir
		#from os.path import isfile, join
		#apifiles = { f for f in os.listdir(to_home) if os.path.isfile(os.path.join(to_home,f)) and 'default' not in f }
		apimod=import_module(api_file)
		self.api_args=apimod.aa
		for f in self.api_args: 
			#print f
			if f not in ('default'):
				(t_from,t_to) = f.split('.')
				if not self.tmpl.has_key(t_from): self.tmpl[t_from]=[]
				self.tmpl[t_from].append(t_to)
		#pprint(tmpl)
		#self.plist={'ORA_QueryFile':('Copy','Oracle 11G','Table','Yes','Yes','Yes','Yes'),}
		self.fcounts={}
		for flt in self.tobjects:
			self.fcounts[flt]=0
		for flt in self.fobjects:
			self.fcounts[flt]=0
		if filter:
			filter=filter.split('(')[0]
		for t in sorted(self.tmpl.keys(),reverse=True):
			#t=t.split('(')[0]
			if filter:
				if filter in t:
					self.listCtrl.InsertStringItem(0, t)

			else:
				self.listCtrl.InsertStringItem(0, t)
				for flt in self.tobjects:
					if flt.upper() in t.upper():
						self.fcounts[flt] +=1
				for flt in self.fobjects:
					if flt.upper() in t.upper():
						self.fcounts[flt] +=1
		self.create_btn.Enable(False)
		#pprint (self.fcounts)
		if not filter:
			for k, v in self.fcounts.items():
				#print v
				if v:
					self.s_rb[k].SetLabel("%s(%s)" % (k, v))
		self.optsizer.Layout()
		#self.optsizer.Refresh()
		self.Thaw()
		print gc.get_count()
	def OnSrcTmplSelected(self,event):
		#print str(self.__class__) + " - OnItemSelected"
		currentItem = event.m_itemIndex
		self.targlistCtrl.ClearAll()
		src_val=self.listCtrl.GetItem(itemId=currentItem, col=0).GetText()
		#self.list_ctrl.GetItem(itemId=currentItem, col=0).GetText()
        #    print item
		self.targlistCtrl.InsertColumn(0, 'Target Template')	
		self.targlistCtrl.SetColumnWidth(0, 320)
		#print src_val
		#print self.tmpl[src_val]
		for t in sorted(self.tmpl[src_val],reverse=True):
			self.targlistCtrl.InsertStringItem(0, t)
		self.create_btn.Enable(False)
		#print currentItem
		if currentItem>-1:
			#print 'setting name',currentItem
			sname=self.get_template().replace('.','_to_')
			#print 'sname',sname
			self.setDefaultName(sname)
			#self.tc_sname.SetValue(sname)
		event.Skip()
	def get_template(self):
		trg_tmpl=None
		if self.rb_set_manually.GetValue():
			return 'generic.generic'
		else:
			src_tmpl=self.listCtrl.GetItemText(self.listCtrl.GetFirstSelected())
			if self.targlistCtrl.GetFirstSelected()>-1:
				trg_tmpl=self.targlistCtrl.GetItemText(self.targlistCtrl.GetFirstSelected())
			return '%s.%s' % (src_tmpl, trg_tmpl)
	def OnTargTmplSelected(self,event):
		#print str(self.__class__) + " - OnItemSelected"
		currentItem = event.m_itemIndex
		self.create_btn.Enable(True)
		if 0:
			if not self.dirty:
				self.dirty = True
				wx.CallAfter(self.Cleanup)
		if currentItem>-1:	
			sname=self.get_template().replace('.','_to_')
			self.setDefaultName(sname)		
			#self.tc_sname.SetValue()
		event.Skip()
		
	def OnTargTmplDeselected(self,event):
		#print str(self.__class__) + " - OnItemDeselected"
		self.create_btn.Enable(False)
		#if currentItem>-1:
		#	self.tc_sname.SetValue(self.get_template().replace('.',''))
		event.Skip()	
	def onMouseOver(self, event):
		print "mouse over"
		for item in range(self.list_ctrl.GetItemCount()):
			 self.list_ctrl.SetItemBackgroundColour(item,wx.NullColor)
		x = event.GetX()
		y = event.GetY()
		item, flags = self.list_ctrl.HitTest((x, y))
		self.list_ctrl.SetItemBackgroundColour(item,wx.RED)
		#self.list_ctrl.RefreshItems(0,2)
		event.Skip()

	def onMouseLeave(self, event):
		print "mouse leave"
		for item in range(self.list_ctrl.GetItemCount()):
			 self.list_ctrl.SetItemBackgroundColour(item,wx.NullColor)
		#self.list_ctrl.RefreshItems(0,2)
		event.Skip()
	

	def OnExit(self,e):
		#print 'self.recent'
		#self.Close(True)
		#self.Destroy()
		#return

		#print 'OnExit'
		#print gc.get_count()
		self.writeRecent()
		#del self._cvMenu
		#del self.recentMenu
		#del self._defMenu
		#self._cvMenu=None
		#self.recentMenu=None
		#self._defMenu=None	
		items=[]
		
		#print self._cvMenu.GetAllItems(self._cvMenu,items)
		#print items	
		#print self._cvMenu.FindItem(2005,self._cvMenu)
		if 0 and self._cvMenu:
			self._cvMenu.DestroyChildren()
			self._cvMenu.DissociateHandle()
			#itm=self._cvMenu.FindItem(2005)
			
			#self._cvMenu.Destroy(itm)
			#self._cvMenu.
			del self._cvMenu
		#print self.mem()
		#print gc.get_count()
		#gc.collect()
		self._cvMenu=None
		e.Skip()
	def writeRecent(self):
		#print 'writeRecent'
		#print self.recent
		if self.recent:
			if len(self.recent)>self.max_recent:
				self.recent.pop(0)
			import pickle
			
			pickle.dump(self.recent, open( self.recent_fname, "wb" ) )
	def readRecent(self):
		#print 'readRecent'
		import pickle
		self.recent = pickle.load( open( self.recent_fname, "rb" ) )
		#print self.recent
		if not self.recent:
			self.recent=[]
		return self.recent
	def OnCreate(self,e):
		#print 'OnCreate'
		#self._cvMenu.Clear()
		#del self._cvMenu
		#del self.recentMenu
		#del self._defMenu
		#self._cvMenu=None
		#self.recentMenu=None
		#self._defMenu=None
		gc.collect()		
		libname=self.cb_tname.GetValue()
		sname=self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
		if not sname:
			self.Warn('Enter session name.')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(libname,sname):
			self.Warn('Duplicate session name.','OnCreate')
			self.tc_sname.SetFocus()

		else:
		
			self.writeRecent()
		
			e.Skip()

	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self, slib, sname):
		#print 'if_duplicate_name', slib, sname
		sfile_loc=os.path.join(session_home,slib,sname)
		#print session_home,slib,sname
		#print sfile_loc, os.path.isdir(sfile_loc)

		return os.path.isdir(sfile_loc)
	def OnCVClicked_0(self, event):
		#print self.recent
		#e(0)
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()

		# Create the popup menu
		self.CreatePopupMenu()

		# Position the menu:
		# The menu should be positioned at the bottom left corner of the button.
		btnSize = btn.GetSize()
		btnPt = btn.GetPosition()

		# Since the btnPt (button position) is in client coordinates, 
		# and the menu coordinates is relative to screen we convert
		# the coords
		btnPt = btn.GetParent().ClientToScreen(btnPt)

		# A nice feature with the Popup menu, is the ability to provide an 
		# object that we wish to handle the menu events, in this case we
		# pass 'self'
		# if we wish the menu to appear under the button, we provide its height
		self._cvMenu.SetOwnerHeight(btnSize.y)
		self._cvMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
	def OnCVClicked(self, event):
		#print self.recent
		#e(0)
		# Demonstrate using the wxFlatMenu without a menu bar
		print gc.get_count()
		gc.collect()
		btn = event.GetEventObject()
		if 1:
			# Create the popup menu
			self.CreatePopupMenu()
			btnSize = btn.GetSize()
			
			btnPt = btn.GetPosition()
			#print '1 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			#print '2 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			#print 'btnSize.y', btnSize.y
			self._cvMenu.SetOwnerHeight(btnSize.y)
			#print 'btnPt.x, btnPt.y', btnPt.x, btnPt.y
			self._cvMenu.Popup(wx.Point(btnPt.x, btnPt.y+50), self)
			mpsn=self._cvMenu.GetScreenPosition()
			#print 'mpsn', mpsn
			#adjust
			if btnPt.y<mpsn[1]:
				self._cvMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
			
	def CreatePopupMenu(self):
		if not self.recentMenu:
			self.recentMenu = FM.FlatMenu()
		else:
			self.recentMenu.Clear()

		if not self._cvMenu:
		
			self._cvMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------
			dbf={'OR':'Oracle', 'SS':'SQLServer', 'MA':'MariaDB', 'MY': 'MySQL', 'PG':'PostgreSQL', 'DB':'DB2', 'TT':'TimesTen', 'SL':'SQLite', 'IN':'Informix', 'SY':'Sybase','MO':'Mongo'}
			self.i=0
			if 1: #len(self.recent):
				self.i +=1
				menuItem = FM.FlatMenuItem(self._cvMenu, 20005, 'Recent', '', wx.ITEM_NORMAL, self.recentMenu)
				self._cvMenu.AppendItem(menuItem)
				if self.recent:
					for r in reversed(self.recent):
						(a,b)=r
						a=a.upper()
						b=b.upper()
						self.i +=1
						#Menu1 = FM.FlatMenu()
						menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
						self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
						self.recentMenu.AppendItem(menuItem)
					
				self._cvMenu.AppendSeparator()
			if 0 and len(self.api2)>1:
				for k in self.api2:
					self.i +=1
					Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From %s' % k, '', wx.ITEM_NORMAL, Menu1)
					self._cvMenu.AppendItem(menuItem)
					#if not k in ['OR']:
					#	menuItem.Enable(False)
					#print k
					#pprint (self.api_menu)
					e(0)
					for sm in self.api_menu[k]:
						if 1 or len(self.api_menu[k])>1:
							self.i +=1
							self.create_Menu2(Menu1,sm,dbf)
							
						else:
							for k2 in self.api2:
								self.i +=1
								if len(self.api_menu[k2])>1:
									self.create_Menu3(Menu1,k2,from_db=sm,from_to='To')
								else:
									self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm, from_to='To')
							Menu1.AppendSeparator()
							for sm in conf.ff:
								self.i +=1
								#Menu1 = FM.FlatMenu()
								menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), 'To %s' % sm, '', wx.ITEM_NORMAL)
								Menu1.AppendItem(menuItem)									
								self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(dbf[k],sm))
			#else:
			if 1:
				k=self.default_db #self.api2[0]
				#print self.api2
				#e(0)
				Menu1=self._cvMenu
				for sm in self.api_menu[k]:
					if 1  or len(self.api_menu[k])>1:
						self.i +=1
						self.create_Menu2_short(Menu1,sm,dbf)
						
					else:
						k2= self.api2[0]
						if 1:
							self.i +=1
							self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm, from_to='To 2 ')
						

						Menu1.AppendSeparator()
						for sm in conf.ff:
							self.i +=1
							#Menu1 = FM.FlatMenu()
							menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), 'To %s' % sm, '', wx.ITEM_NORMAL)
							Menu1.AppendItem(menuItem)									
							self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(k,sm))	
			if 1: #From other dbs
				self._cvMenu.AppendSeparator()
				Menu1_2 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From other DB', '', wx.ITEM_NORMAL, Menu1_2)
				self._cvMenu.AppendItem(menuItem)
				self.from_other_db_Menu(Menu1_2)
				#e(0)
			self._cvMenu.AppendSeparator()	
			for sm in conf.ff:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._cvMenu, wx.NewId(), 'From %s' % sm, '', wx.ITEM_NORMAL, Menu1)
				self._cvMenu.AppendItem(menuItem)	
				#pprint (self.api_menu)
				for k2 in self.api2:
					self.i +=1
					if self.api_menu.has_key(k2): 					
						if len(self.api_menu[k2])>1:
							self.create_Menu3(Menu1,k2,from_db=sm)
						else:
							self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm)
						
				
		else:
			#pprint(dir(self.recentMenu))
			#self.recentMenu.Clear()
			if self.recent:
				for r in reversed(self.recent):
					(a,b)=r
					a=a.upper()
					b=b.upper()
					self.i +=1
					#Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self.recentMenu, wx.NewId(), '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
					self.recentMenu.AppendItem(menuItem)
		print gc.get_count()
	def from_other_db_Menu(self,Menu):
		for k in self.api_menu.keys():
			#print k
			if k not in [self.default_db]:
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				Menu.AppendItem(menuItem)
				for k2 in [x for x in self.api_menu[k] if x not in conf.tt+conf.dt]:
					#self.create_Menu3(Menu1,k2,from_db=k)
					print k2
					#print from_db, k2
					#from_to='To_%s_%s' %(from_db,k2)
					self.i +=1
					Menu2 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), "From %s" % ( k2), "", wx.ITEM_NORMAL, Menu2)
					Menu1.AppendItem(menuItem)
					#if not k2 in ['OR']:
					#	menuItem.Enable(False)
					for sm2 in self.api_menu[self.default_db]:
						#self.i +=1
						self.create_Menu4(Menu2,sm2,k2,from_to='To')
				
	def to_other_db_Menu(self,Menu,from_db):
		for k in self.api_menu.keys():
			#print k
			if k not in [self.default_db]:
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(Menu, wx.NewId(), k, "", wx.ITEM_NORMAL, Menu1)
				Menu.AppendItem(menuItem)
				for k2 in self.api_menu[k]:
					#for sm2 in self.api_menu[self.default_db]:
					#self.i +=1
					self.create_Menu4(Menu1,k2,from_db,from_to='To')
						

	def create_Menu2(self,Menu1,sm,dbf, from_to='From'):
		self.i +=1
		Menu2 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2)
		Menu1.AppendItem(menuItem)
		#self.set_sub_submenu(subSubMenu,1, 'CSV')
		
		for k2 in self.api2:
			self.i +=1
			if len(self.api_menu[k2])>1:
				self.create_Menu3(Menu2,k2,from_db=sm)
			else:
				self.create_Menu4(Menu2,self.api_menu[k2][0],from_db=sm)
		#append to_csv
		Menu2.AppendSeparator()
		for s in conf.ff:
			self.i +=1
			#Menu1 = FM.FlatMenu()
			menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
			self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(sm,s))
			Menu2.AppendItem(menuItem)	
	def create_Menu2_short(self,Menu1,sm,dbf, from_to='From'):
		self.i +=1
		Menu2 = FM.FlatMenu()
		if sm in self.api_menu[self.default_db]:
			imageFile = os.path.join(home,"images/database_green_16.png")
			if sm in self.highlight:
				imageFile = os.path.join(home,"images/database_red_16.png")
			context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
		
			menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2,context_bmp)
		else:
			menuItem = FM.FlatMenuItem(Menu1, wx.NewId(), '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2)
			
		
		Menu1.AppendItem(menuItem)
		

			
		k2=self.default_db
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4(Menu2,sm2,sm,'To')
		if 1: #To other dbs
			Menu2.AppendSeparator()
			Menu3 = FM.FlatMenu()
			menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To other DB', '', wx.ITEM_NORMAL, Menu3)
			Menu2.AppendItem(menuItem)
			self.to_other_db_Menu(Menu3,sm)
		#append to_csv
		Menu2.AppendSeparator()
		for s in conf.ff:
			self.i +=1
			#Menu1 = FM.FlatMenu()
			menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
			self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(sm,s))
			Menu2.AppendItem(menuItem)	
	
	def create_Menu3(self,Menu2,k2,from_db, from_to='To'):
		#print from_db, k2
		#from_to='To_%s_%s' %(from_db,k2)
		self.i +=1
		Menu3 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), "%s %s" % (from_to, k2), "", wx.ITEM_NORMAL, Menu3)
		Menu2.AppendItem(menuItem)
		#if not k2 in ['OR']:
		#	menuItem.Enable(False)
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4(Menu3,sm2,from_db,from_to)
		if 0 and  from_db not in conf.ff:
			Menu2.AppendSeparator()
			for s in conf.ff:
				self.i +=1
				#Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(Menu2, wx.NewId(), 'To %s' % s, '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(k2,s))
				Menu2.AppendItem(menuItem)	
			
			

	def create_Menu4(self,Menu3,sm2,from_db, from_to='To'):
		self.i +=1
		#print sm2, from_db
		#imageFile = os.path.join(home,"images/database_grey_16.png")
		if sm2 in self.api_menu[self.default_db]:
			imageFile = os.path.join(home,"images/database_green_16.png")
			if sm2 in self.highlight:
				imageFile = os.path.join(home,"images/database_red_16.png")
			assert os.path.isfile(imageFile), 'image file does not exists\n%s' % imageFile
			context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
			
			menuItem = FM.FlatMenuItem(Menu3, wx.NewId(), "%s %s" % (from_to, conf.dbs[sm2]) , "", wx.ITEM_NORMAL, None,context_bmp)
		else:
			menuItem = FM.FlatMenuItem(Menu3, wx.NewId(), "%s %s" % (from_to, conf.dbs[sm2]) , "", wx.ITEM_NORMAL)
		#menuItem.SetFont(wx.Font(10, wx.SWISS, wx.ITALIC, wx.BOLD, False, "Courier New"))
		#menuItem.SetTextColour(wx.RED)
		#pprint(dir(menuItem))
		self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(from_db,sm2))
		Menu3.AppendItem(menuItem)
			

	def set_vector_btn(self,a,b):	
		#print a,b
		lbl='%s->%s' % (a,b)
		self.b_vector.SetLabel(lbl.lower())
		self.copy_vector=[a.upper(),b.upper()]
		self.refresh_src_list()

	def OnMenu(self, event, params):
		(a,b) = params
		a=a.upper()
		b=b.upper()
		if (a,b) not in self.recent:
			self.recent.append((a,b))
		else:
			#print dir(self.recent)
			self.recent.remove((a,b))
			self.recent.append((a,b))
		self.writeRecent()
		#print '###########', self.recent
		self.set_vector_btn(a,b)
		self.create_btn.Enable(False)
		#print a,b
		if a.startswith('CSV'):
			for n in self.tobjects:
				self.s_rb[n].Enable(False)
			for n in self.fobjects:
				self.s_rb[n].Enable(True)
		elif b.startswith('CSV'):
			for n in self.tobjects:
				self.s_rb[n].Enable(True)
			for n in self.fobjects:
				self.s_rb[n].Enable(True)
		else:
			for n in self.tobjects:
				self.s_rb[n].Enable(True)
			for n in self.fobjects:
				self.s_rb[n].Enable(True)
			
		
		
		


	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

###################################################################################################
class NewSessionLibraryDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size, pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent

		#print defaults
		#pprint(data)
		self._popUpMenu = None
		#self.recent=[]
		pre = wx.PreDialog()
		pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
		pre.Create(parent, ID, title, pos, size, style)
	
		# This next step is the most important, it turns this Python
		# object into the real wrapper of the dialog (instead of pre)
		# as far as the wxPython extension is concerned.
		self.PostCreate(pre)

		# This extra style can be set after the UI object has been created.
		if 'wxMac' in wx.PlatformInfo and useMetal:
			self.SetExtraStyle(wx.DIALOG_EX_METAL)


		# Now continue with the normal construction of the dialog
		# contents
		#self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.userhome = os.path.expanduser('~')
		self.session_dir=session_home		
		self.changed=False
		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(1, 4)			
			
			text1 = wx.StaticText(self, label="Library name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			#self.tc_sname = wx.TextCtrl(self,size=(400,23))
			self.tc_sname = masked.TextCtrl(self, -1, "",
										mask         = maskLibName[1],
										excludeChars = maskLibName[2],
										formatcodes  = maskLibName[3],
										includeChars = "_0123456789",
										validRegex   = maskLibName[4],
										validRange   = maskLibName[5],
										choices      = maskLibName[6],
										choiceRequired = False,
										defaultValue = maskLibName[7])			
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			self.tc_sname.Bind(wx.EVT_CHAR, self.onKeyPress)
			#namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			#icon = wx.StaticBitmap(self, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))
			#namesizer.Add((3,3),0)
			#namesizer.Add(icon, pos=(0, 3), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)
			sizer.Add(namesizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		self.create_btn.Enable(False)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		#btnsizer.Add(self.test, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		#self.test.Bind(wx.EVT_BUTTON, self.OnTest)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer(sizer)
			

		self.Layout()
		self.Fit()
		#self.SetSize((-1,size[1]))
	def setDefaultName(self, sname):
		if not self.changed:
			self.tc_sname.SetValue(sname.strip().strip(' ').replace(' ',''))
	def onKeyPress(self, event):
		#print str(self.__class__) + " - onKeyPress"
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()				
			if	kc == 4:
				print 'Ctrl-D 1'
				self.parent.tryToDelete()
		else:
			if kc<123 and not (kc == wx.WXK_SPACE): #(kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.create_btn.Enable(True)
				#self.parent.changed=True
				#print 'changed'
				if not self.changed:
					self.changed=True
		
		event.Skip()
		
		
	def OnTest(self,e):
		[cn, cv, tmpl, args, reuse] = self.getConfig()		
		#print len(args)	
		#pprint(args[2])
		#pprint(self.api_args[tmpl][0])

	def getLibName(self):
		return self.tc_sname.GetValue().strip().strip(' ').replace(' ','')

	def OnExit(self,e):	
		pass
		e.Skip()

	def OnCreate(self,e):
		#print 'OnCreate'
		
		sname=self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
		if not sname:
			self.Warn('Enter session library name.', 'OnCreate')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(sname):
			self.Warn('Duplicate session library name.', 'OnCreate')
			self.tc_sname.SetFocus()

		else:
		
			#self.writeRecent()
		
			e.Skip()

	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,name):
		dir = os.path.join(self.session_dir, self.getLibName())
		if os.path.isdir(dir):
			return True
		else:
			return False

		

	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

		

###################################################################################################
class NewTemplateLibraryDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size, pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent

		#print defaults
		#pprint(data)
		self._popUpMenu = None
		#self.recent=[]
		pre = wx.PreDialog()
		pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
		pre.Create(parent, ID, title, pos, size, style)
	
		# This next step is the most important, it turns this Python
		# object into the real wrapper of the dialog (instead of pre)
		# as far as the wxPython extension is concerned.
		self.PostCreate(pre)

		# This extra style can be set after the UI object has been created.
		if 'wxMac' in wx.PlatformInfo and useMetal:
			self.SetExtraStyle(wx.DIALOG_EX_METAL)


		# Now continue with the normal construction of the dialog
		# contents
		#self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		sizer = wx.BoxSizer(wx.VERTICAL)
		#self.userhome = os.path.expanduser('~')
		self.home_dir=os.path.join(home,'sessions')		
		self.changed=False
		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(1, 4)			
			
			text1 = wx.StaticText(self, label="Library name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			#self.tc_sname = wx.TextCtrl(self,size=(400,23))
			self.tc_sname = masked.TextCtrl(self, -1, "",
										mask         = maskLibName[1],
										excludeChars = maskLibName[2],
										formatcodes  = maskLibName[3],
										includeChars = "_0123456789",
										validRegex   = maskLibName[4],
										validRange   = maskLibName[5],
										choices      = maskLibName[6],
										choiceRequired = False,
										defaultValue = maskLibName[7])			
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			self.tc_sname.Bind(wx.EVT_CHAR, self.onKeyPress)
			#namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			#icon = wx.StaticBitmap(self, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))
			#namesizer.Add((3,3),0)
			#namesizer.Add(icon, pos=(0, 3), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)
			sizer.Add(namesizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		self.create_btn.Enable(False)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		#btnsizer.Add(self.test, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		#self.test.Bind(wx.EVT_BUTTON, self.OnTest)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer(sizer)
			

		self.Layout()
		self.Fit()
		#self.SetSize((-1,size[1]))
	def setDefaultName(self, sname):
		if not self.changed:
			self.tc_sname.SetValue(sname.strip().strip(' ').replace(' ',''))
	def onKeyPress(self, event):
		#print str(self.__class__) + " - onKeyPress"
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()				
			if	kc == 4:
				print 'Ctrl-D 1'
				self.parent.tryToDelete()
		else:
			if kc<123 and not (kc == wx.WXK_SPACE): #(kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.create_btn.Enable(True)
				#self.parent.changed=True
				#print 'changed'
				if not self.changed:
					self.changed=True
		
		event.Skip()
		
		
	def OnTest(self,e):
		[cn, cv, tmpl, args, reuse] = self.getConfig()		
		#print len(args)	
		#pprint(args[2])
		#pprint(self.api_args[tmpl][0])

	def getLibName(self):
		return self.tc_sname.GetValue().strip().strip(' ').replace(' ','')

	def OnExit(self,e):	
		pass
		e.Skip()

	def OnCreate(self,e):
		#print 'OnCreate'
		
		sname=self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
		if not sname:
			self.Warn('Enter template library name.')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(sname):
			self.Warn('Duplicate template library name.')
			self.tc_sname.SetFocus()

		else:
		
			#self.writeRecent()
		
			e.Skip()

	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,name):
		dir = os.path.join(self.home_dir, self.getLibName())
		if os.path.isdir(dir):
			return True
		else:
			return False

		

	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

		


###################################################################################################

class Args(object):
	def __init__(self, args_dict):
		for name, value in args_dict.items():
			#print name, value[2]
			setattr(Args, name, value[2])
			#self.__dict__[name] = value[2]

		
class pnl_args(wx.Panel):
	"""Arguments"""
	
	def __init__(self, parent, copy_vector,tmpl,the_id,args_api,size, style):
		wx.Panel.__init__(self, parent, -1, size=size, style=style)
		#self.frame=frame
		global home
		ID_TC_MODE = wx.NewId()
		ID_RUN_AT = wx.NewId()
		self.parent=parent
		#self.SetSizer(sizer)
		#sizer.Fit(self)
		self.args_vbox = wx.BoxSizer(wx.VERTICAL)
		self.args_hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.args_api=args_api
		self.the_id=the_id
		self.cargs,self.fargs,self.targs=args_api
		self.copy_vector=copy_vector
		self.tmpl=tmpl
		self.obj={}
		self.checks={}
		#self.changed=False
		self.tc_length=180
		self.tfile={'target':os.path.join(home,'test','test_connnect','Target_connect_test_for_oracle.sql'),
		'source':os.path.join(home,'test','test_connnect','Source_connect_test_for_oracle.sql')}
		self.disabled=['copy_vector', 'time_stamp','keep_data_file', 'job_pre_etl','thread_pre_etl','loader_profile', 'host_map']
		#self.Freeze()
		if 0: #Src Timer
			i=wx.NewId()			
			self.Bind(wx.EVT_TIMER, lambda event, i=i: self.src_TimerHandler(event, the_id=i), id=i)
			
			self.src_timer=wx.Timer(self, id=i)
		if 0: #Src Timer
			i=wx.NewId()			
			self.Bind(wx.EVT_TIMER, lambda event, i=i: self.trg_TimerHandler(event, the_id=i), id=i)
			
			self.trg_timer=wx.Timer(self, id=i)	
			
		if 1: #Common
			#self.core_args_panel = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.core_args_panel = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=dimensions['common_args'], pos=(0,0), style=wx.SIMPLE_BORDER)
			self.core_args_panel.SetVirtualSize((500, 500))
			self.core_args_panel.SetScrollRate(20,20)
			self.setCommonArgs(self.core_args_panel)
			
			#self.sb_common = wx.StaticBox(self, label="Common")
			boxsizer = wx.BoxSizer( wx.VERTICAL)
			if 1:
				hboxsizer = wx.BoxSizer( wx.HORIZONTAL)
				#btn_ctl=wx.Button(self, label='Test', size=(-1,30))
				#txt=wx.TextCtrl(self,value='Source Args')
				#self.s_boxsizer.Add(txt, flag=wx.LEFT|wx.TOP, border=5)
				stxt=wx.StaticText(self, label='Common Args:',size=(-1,20) )
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
				stxt.SetFont(font)
				hboxsizer.Add(stxt, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				hboxsizer.Add((20,-1), flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				self.st_type = wx.StaticText(self, label="n/a",size=(-1,19))
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
				self.st_type.SetFont(font)				
				hboxsizer.Add(self.st_type, 1, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)

				#hboxsizer.Add((20,-1), flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				
				self.st_copy_vector = wx.StaticText(self, label='{:s}'.format('n/a'),size=(-1,19))
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
				self.st_copy_vector.SetFont(font)				
				hboxsizer.Add(self.st_copy_vector, 1, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				self.cb_all_args=wx.CheckBox(self, label="all args")				
				self.cb_all_args.Bind(wx.EVT_CHECKBOX, self.OnShowAllArgs)
				self.cb_all_args.SetValue(False)	
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
				self.cb_all_args.SetFont(font)				
				hboxsizer.Add(self.cb_all_args, 1, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM|wx.GROW|wx.ALL|wx.EXPAND, border=3)
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				r_button=wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))				
				hboxsizer.Add(r_button, 0, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				r_button.Bind(wx.EVT_BUTTON, self.OnRefreshArgLists)  
					
		
				boxsizer.Add(hboxsizer, 1, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM|wx.GROW|wx.ALL|wx.EXPAND, border=1)				
				#self.boxsizer.Add(self.from_args_panel, flag=wx.LEFT|wx.TOP, border=1)
			boxsizer.Add(self.core_args_panel, flag=wx.LEFT|wx.TOP, border=1)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_vbox.Add(boxsizer,0,  border=1)
		if 1: #Source
			#self.from_args_panel = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.from_args_panel = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=dimensions['source_args'], pos=(0,0), style=wx.SIMPLE_BORDER)
			
			#self.p_sql.SetBackgroundColour('#FFFFFF')
			#bSizer = wx.BoxSizer( wx.VERTICAL )
			#self.from_args_panel.fgs4=wx.GridBagSizer(3, 10)
				
			self.setSourceArgs(self.from_args_panel)
			#self.from_args_panel.SetAutoLayout(1)
			#self.from_args_panel.SetupScrolling()
			self.buttons = {
				'open_source_args_list':[self.OnEditSpoolerArglist, self.OnMessage, 'Open spooler argument list.'],
				'open_target_args_list':[self.OnEditLoaderArglist, self.OnMessage, 'Open loader argument list.'],
				#( 'Cancel', self.CancelClicked, self.OnMessage, 'Cancel button text', ),
				#( 'Re-invert', self.ReinvertClicked, self.OnMessage, 'Re-invert button text', ),
				#( 'Exit', self.ExitClicked, self.OnMessage, 'Exit button text', ),
				}			
			
			lbl='Source'
			if self.parent.getCopyVector()[0]:
				lbl="Source (%s)" % conf.dbs[self.parent.getCopyVector()[0]]
			if 0:	
				self.sb_from = wx.StaticBox(self, label=lbl)
				self.s_boxsizer = wx.StaticBoxSizer(self.sb_from, wx.VERTICAL)
				self.s_boxsizer.Add(self.from_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			else:
				self.s_boxsizer = wx.BoxSizer(wx.VERTICAL)
				#btn_ctl=wx.Button(self, label='Test', size=(-1,30))
				#txt=wx.TextCtrl(self,value='Source Args')
				#self.s_boxsizer.Add(txt, flag=wx.LEFT|wx.TOP, border=5)
				hboxsizer = wx.BoxSizer( wx.HORIZONTAL)
				stxt=wx.StaticText(self, label='Source Args:',size=(-1,20) )
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
				"""
				family can be:

				wx.DECORATIVE, wx.DEFAULT,wx.MODERN, wx.ROMAN, wx.SCRIPT or wx.SWISS.
				style can be:

				wx.NORMAL, wx.SLANT or wx.ITALIC.
				weight can be:

				wx.NORMAL, wx.LIGHT, or wx.BOLD		
				"""
				stxt.SetFont(font)
				hboxsizer.Add(stxt, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				hboxsizer.Add((20,-1), flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				self.st_sourcet = wx.StaticText(self, label='n/a',size=(-1,20))
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
				self.st_sourcet.SetFont(font)
				hboxsizer.Add(self.st_sourcet, 1, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				hboxsizer.Add((20,20), 0, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				#previous = None
				imageFile = os.path.join(home,"images/editor_icon_16_2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#for button in self.buttons [ 0 : len ( self.buttons ) -Bottom ]:
				if 1:
					button=self.buttons['open_source_args_list']
					oneButton = bButton ( self, button, image1)
					if 0:
						lc = wx.LayoutConstraints ( )
						lc.left.SameAs ( self, wx.Left, 5 )
						lc.right.SameAs ( self, wx.Right, 5 )
						lc.height.AsIs ( )
						if previous: lc.top.SameAs ( previous, wx.Bottom, 5 )
						else: lc.top.SameAs ( self, wx.Top, 5 )
						oneButton.SetConstraints ( lc )
						previous = oneButton
			
				#btn=self.parent.getEditButton(self)
				#btn.Bind(wx.EVT_BUTTON, self.OnEditSpoolerArglist)
				hboxsizer.Add(oneButton, 0, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT, border=1)
				self.s_boxsizer.Add(hboxsizer,0, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				self.s_boxsizer.Add(self.from_args_panel, flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				if not self.copy_vector[0][:3] in conf.ff:
					if 0:
						self.tc_0test=wx.StaticText(self, label='NOT TESTED')
						self.fgs.Add(self.tc_0test, pos=(i, 0), flag=wx.ALIGN_RIGHT|wx.TOP|wx.BOTTOM, border=1)
					tcbox = wx.BoxSizer(wx.HORIZONTAL)
					lbl='Test connect'
					sn=self.parent.getSessionName()
					#tc=self.parent.testconn
					btn=wx.Button(self, label=lbl, style=wx.BU_EXACTFIT)	
					#tc[sn]['source'][0]
					tcbox.Add(btn, flag=wx.LEFT|wx.TOP, border=1)
					imageFile = os.path.join(home,"images/editor_icon_16_2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					bitbtn = wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))

					bitbtn.Bind(wx.EVT_BUTTON, self.OnEditTestConnectSQL)
					bitbtn.SetName('source')
					tcbox.Add(bitbtn, flag=wx.LEFT|wx.TOP, border=1)
					#self.fgs.Add(tcbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					btn.SetName('source')
					btn.Bind(wx.EVT_BUTTON, self.OnTestConnect)
					self.s_boxsizer.Add(tcbox, flag=wx.LEFT|wx.TOP, border=1)
					if 1:
						#btn_sqp=wx.Button(panel, label=lbl, style=wx.BU_EXACTFIT)	
						imageFile = os.path.join(home,"images/exec_16.png")
						image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
						btn_sqp = wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))

				
						#tc[sn]['source'][0]
						btn_sqp.SetName('source_sqp')
						btn_sqp.Bind(wx.EVT_BUTTON, self.OnOpenSqlPlusMenu)
						tcbox.Add(btn_sqp, flag=wx.LEFT|wx.TOP, border=1)
						
					if self.parent.btn.has_key(self.the_id[0]) and self.parent.counters.has_key(self.the_id[0]) and self.parent.counters[self.the_id[0]]>0:
						btn.Enable(False)
						lbl='Closing in %d' % (self.parent.closing_in-self.parent.counters[self.the_id[0]])
						btn.SetLabel('%s: %s' % (sn,lbl))
						self.parent.btn[self.the_id[0]]=btn
					else:
						pass
						#print 'conter is not set'				
			#pprint(dir(self.sb_from))
			#e(0)
			self.args_hbox.Add(self.s_boxsizer, 0, border=1)
		if 1: #Target pnl
			#self.to_args_panel = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.to_args_panel = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=dimensions['target_args'], pos=(0,0), style=wx.SIMPLE_BORDER)
			self.setTargetArgs(self.to_args_panel)
			lbl='Target'
			if self.parent.getCopyVector()[1]:
				lbl="Target (%s)" % conf.dbs[self.parent.getCopyVector()[1]]
			#sb_from = wx.StaticBox(self, label=lbl)
			boxsizer = wx.BoxSizer( wx.VERTICAL)
			if 1:
				#btn_ctl=wx.Button(self, label='Test', size=(-1,30))
				#txt=wx.TextCtrl(self,value='Source Args')
				#self.s_boxsizer.Add(txt, flag=wx.LEFT|wx.TOP, border=5)
				hboxsizer = wx.BoxSizer( wx.HORIZONTAL)
				stxt=wx.StaticText(self, label='Target Args:',size=(-1,20) )
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)
				stxt.SetFont(font)
				hboxsizer.Add(stxt, flag=wx.LEFT|wx.TOP, border=1)
				hboxsizer.Add((20,-1), flag=wx.LEFT|wx.BOTTOM|wx.ALIGN_BOTTOM, border=1)
				self.st_targett = wx.StaticText(self, label='{:s}'.format('n/a'),size=(-1,20))
				font = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
				self.st_targett.SetFont(font)
				hboxsizer.Add(self.st_targett, flag=wx.LEFT|wx.TOP, border=1)
				hboxsizer.Add((20,20), 0, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT, border=1)
				if 1:
					imageFile = os.path.join(home,"images/editor_icon_16_2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					button=self.buttons['open_target_args_list']
					oneButton = bButton ( self, button, image1)
					hboxsizer.Add(oneButton, 0, flag=wx.RIGHT|wx.BOTTOM|wx.ALIGN_RIGHT, border=1)
				if 0:
					btn=self.parent.getEditButton(self)
					btn.Bind(wx.EVT_BUTTON, self.OnEditLoaderArglist)
				
				boxsizer.Add(hboxsizer, flag=wx.LEFT|wx.TOP, border=1)
				
			boxsizer.Add(self.to_args_panel, flag=wx.LEFT|wx.TOP, border=1)
			if not self.copy_vector[1].upper()[:3] in conf.ff:	
				if 0:
					self.tc_1test=wx.StaticText(self, label='NOT TESTED')
					self.fgs.Add(self.tc_1test, pos=(i, 0), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=1)

				lbl="Test connect"			

				sn=self.parent.getSessionName()
				#tc=self.parent.testconn
				tcbox = wx.BoxSizer(wx.HORIZONTAL)
				
				sn=self.parent.getSessionName()
				#tc=self.parent.testconn
				btn=wx.Button(self, label=lbl, style=wx.BU_EXACTFIT)	
				#tc[sn]['source'][0]
				btn.SetName('target')
				btn.Bind(wx.EVT_BUTTON, self.OnTestConnect)
				tcbox.Add(btn, flag=wx.LEFT|wx.TOP, border=1)
				imageFile = os.path.join(home,"images/editor_icon_16_2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				bitbtn = wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))

				bitbtn.Bind(wx.EVT_BUTTON, self.OnEditTestConnectSQL)
				bitbtn.SetName('target')
				tcbox.Add(bitbtn, flag=wx.LEFT|wx.TOP, border=1)	
							
				if 1:
					#btn_sqp=wx.Button(self, label=lbl, style=wx.BU_EXACTFIT)	
					imageFile = os.path.join(home,"images/exec_16.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					btn_sqp = wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
					
					#tc[sn]['source'][0]
					btn_sqp.SetName('target_sqp')
					btn_sqp.Bind(wx.EVT_BUTTON, self.OnOpenSqlPlusMenu)
					tcbox.Add(btn_sqp, flag=wx.LEFT|wx.TOP, border=1)
				


				#panel.fgs.Add(tcbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)

				id=self.the_id[1]
				if self.parent.btn.has_key(id) and self.parent.counters[id]>0:
					btn.Enable(False)
					lbl='Closing in %d' % (self.parent.closing_in-self.parent.counters[id])
					btn.SetLabel('%s: %s' % (sn,lbl))
					self.parent.btn[id]=btn
				
			if 1:
				#print self.copy_vector
				#e(0)
				self.output_panel = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
				self.setLoaderButtons(self.output_panel)
			
				tcbox.Add(self.output_panel, flag=wx.LEFT|wx.TOP, border=1)
				#self.sqldr_btns=(btn_ctl,btn_log,btn_discard,btn_bad)
			boxsizer.Add(tcbox, flag=wx.LEFT|wx.TOP, border=1)	
			
			self.args_hbox.Add(boxsizer, 0,  border=1)
			
		if 0: #Source
			
			panel_from = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)

			fgs = wx.FlexGridSizer(3, 2, 9, 5)
			ttl=['From table','From database','nls_date_format','nls_timestamp_format','nls_timestamp_tz_format','Client home']
			l=[wx.StaticText(panel_from, label="%s:" % t) for t in ttl]

			p=[wx.TextCtrl(panel_from) for t in ttl]
			#pprint(dir(fgs))
			for lid in range(len(l)):
				fgs.AddMany([(l[lid]), (p[lid], 1, wx.EXPAND|wx.TOP)])
	
			#fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author), 
			#	(tc2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])

			#fgs.AddGrowableRow(2, 1)
			#fgs.AddGrowableCol(1, 1)

			hbox.Add(fgs, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)	
			panel_from.SetSizer(hbox)
			sb_from = wx.StaticBox(self, label="Source")
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(panel_from, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_hbox.Add(boxsizer, 0, border=5)

		
		if 0: #Target
			panel_from = wx.Panel(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)

			fgs = wx.FlexGridSizer(3, 2, 9, 5)

			ttl=['To database','To table','To partition','nls_date_format','nls_timestamp_format','nls_timestamp_tz_format','Client home']
			l=[wx.StaticText(panel_from, label="%s:" % t) for t in ttl]

			p=[wx.TextCtrl(panel_from) for t in ttl]
			#pprint(dir(fgs))
			for lid in range(len(l)):
				fgs.AddMany([(l[lid]), (p[lid], 1, wx.EXPAND|wx.TOP)])
	
			#fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author), 
			#	(tc2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])

			#fgs.AddGrowableRow(2, 1)
			#fgs.AddGrowableCol(1, 1)

			hbox.Add(fgs, flag=wx.ALL|wx.EXPAND)	
			panel_from.SetSizer(hbox)
			sb_from = wx.StaticBox(self, label="Target")
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(panel_from, flag=wx.LEFT|wx.TOP)
			#sizer.Add(boxsizer, pos=(3, 3),  flag=wx.TOP|wx.EXPAND, border=5)
			self.args_hbox.Add(boxsizer, 0, border=5)
		self.args_vbox.Add(self.args_hbox,0)
		self.SetSizer(self.args_vbox)
		#self.args_vbox.Layout()
		#self.Fit()	
		#self.Fit()
		#sub(self.OnCloseExec, "close_exec")
		self.src_count=0
		self.trg_count=0
		self.sldr_btns=None
		#enable keep/show dump
		if not (self.copy_vector[0].startswith('CSV') or self.copy_vector[0].startswith('CSV')):
			self.parent.enableKeepDump()
		#self.Refresh()
		#self.Fit()
		#self.Layout()
		#self.Thaw()
			
		self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
		
		#self.checks={}
		sub(self.onSetLoaderProfile, "set_loader_profile")
		sub(self.onSetEtlLoc, 'set_etl_loc')
		sub(self.onSetHostMap, "set_hostmap")
		#sub(self.onSetEtlEditorProfile, "set_etl_editor_profile")
		sub(self.onDisableUnusedArgs, 'disable_unused_args')
		
		self.hm=None
		if not self.hm:
			default_hostmap_dir = os.path.join(transport_home, 'config','host_map')
			default_hostmap_loc = os.path.join(default_hostmap_dir, self.parent.default_hm_file)
			#print default_hostmap_loc
			self.set_hm(self.parent.get_default_cv(),default_hostmap_loc )
			
	def set_hm(self,copy_vector, hm_file_loc):
		#hm_type='default'
		
		#new_hostmap_loc=self.parent.args_panel.CreateNewSessionHostMap(hostmap_loc)
		#if new_hostmap_loc not in [hostmap_loc]:
		#	self.obj[k][1].SetValue(new_hostmap_loc)
		#e(0)
		#print conf._to.join(self.copy_vector)
		#print transport_home,default_hostmap_loc
		#print copy_vector, hm_file_loc
		self.hm = hmap(copy_vector, hm_file_loc)
		#pprint(dir(self.hm))
		am= self.hm.get_active_mapping()
		#print am
		self.parent.set_bar_status(2,am)
		#send('set_bar_status', (2,am))
		
	def OnMessage ( self, on, msg ) :
		if not on : msg = ""
		self.parent.SetStatusText ( msg )
			
	def OnEditSpoolerArglist(self, evt):
		#print 'OnEditLoader'
		#print home
		
		#print self.parent.copy_vector
		from_db,to_db=self.parent.copy_vector
		spooler_args= os.path.join(conf.abspath,'config', 'include', 'args', '%s_from.py' %from_db )
		assert os.path.isfile(spooler_args), 'Spooler argument list file is not defined at\n%s' % spooler_args
		#tc = evt.GetEventObject()
		webbrowser.open(spooler_args)
	def OnEditLoaderArglist(self, evt):
		from_db,to_db=self.parent.copy_vector
		loader_args= os.path.join(conf.abspath,'config', 'include', 'args', '%s_to.py' %from_db )
		assert os.path.isfile(loader_args), 'Loader argument list file is not defined at\n%s' % loader_args
		#tc = evt.GetEventObject()
		webbrowser.open(loader_args)		

		
	def OnRefreshArgLists(self, e):
		#sender = e.GetEventObject()
		#isChecked = sender.GetValue()
		#print isChecked
		self.setCommonArgs(self.core_args_panel)
		self.setSourceArgs(self.from_args_panel)		
		self.setTargetArgs(self.to_args_panel)		
		#k=sender.GetName() 		
	def OnShowAllArgs(self, e):
		sender = e.GetEventObject()
		isChecked = sender.GetValue()
		#print isChecked
		self.setCommonArgs(self.core_args_panel)
		self.setSourceArgs(self.from_args_panel)		
		self.setTargetArgs(self.to_args_panel)		
		#k=sender.GetName() 
		
	def CreateNewSessionHostMap(self, hostmap_loc):
		#print 'CreateNewSessionHostMap', hostmap_loc
		#e(0)
		#hostmap_loc=obj.GetValue()
		#print 'existing hostmap: %s' % hostmap_loc
		hostmap_name=os.path.basename(hostmap_loc)
		
		
		
		
		session_dir=self.getSessionDir()
		if not os.path.isdir(session_dir):
			os.makedirs(session_dir)
		session_hostmap_loc=os.path.join(session_dir,hostmap_name)
		#print session_hostmap_loc
		#print self.parent.save_to_dir
		if 0 and os.path.isfile(session_hostmap_loc):
			pass
			#print 'session host map already exists'

		else:
		
			os.chdir(home)
			if 0:
				if hostmap_loc.startswith(r'.'):
					#relative
					real_hostmap_loc=os.path.join(transport_home,hostmap_loc[2:])
					#real_hostmap_loc=os.path.realpath(hostmap_loc)
				else:
					real_hostmap_loc=os.path.realpath(hostmap_loc)
				#from os.path import relpath
				hostmap_home= os.path.join(transport_home, 'config','host_map')
				#print 'real_hostmap_loc', real_hostmap_loc
				#print 'hostmap_home' , hostmap_home
				hm_rel_path = os.path.relpath (real_hostmap_loc,hostmap_home)
				#print 'hm_rel_path', hm_rel_path
				#e(0)
				assert os.path.isfile(real_hostmap_loc), 'host_map template does not exists at\n%s' % real_hostmap_loc
				#print real_hostmap_loc
				#print session_hostmap_loc
			if 1:
				hostmap_home= os.path.join(transport_home, 'config','host_map')
				real_hostmap_loc = os.path.join(hostmap_home, self.parent.default_hm_file)				
				hm_rel_path = os.path.relpath (real_hostmap_loc,hostmap_home)
				hostmap_name=os.path.basename(self.parent.default_hm_file)
				#print '#'*60
				#print self.parent.default_hm_file
				#print real_hostmap_loc
			session_hostmap_dir= os.path.join(session_dir,'host_map',os.path.dirname(hm_rel_path))
			#print 'session_hostmap_dir', session_hostmap_dir
			if not os.path.isdir(session_hostmap_dir):
				os.makedirs(session_hostmap_dir)
			session_hostmap_loc=os.path.join(session_hostmap_dir,hostmap_name)
			#print 'session_hostmap_loc', session_hostmap_loc
			if not os.path.isfile(session_hostmap_loc):
				shutil.copyfile(real_hostmap_loc,session_hostmap_loc)
			#obj.SetValue(session_hostmap_loc)
			#self.Save()
			#print 'created new session_hostmap at \n%s' % session_hostmap_loc
			send('set_hostmap', (session_hostmap_loc))
		#print session_hostmap_loc
		#e(0)
		return session_hostmap_loc	
	def CreateNewSessionLoaderProfile(self, loader_loc):
		#print 'CreateNewSessionHostMap', hostmap_loc
		#e(0)
		#hostmap_loc=obj.GetValue()
		#print 'existing hostmap: %s' % hostmap_loc
		loader_name=os.path.basename(loader_loc)
		session_dir=self.getSessionDir()
		if not os.path.isdir(session_dir):
			os.makedirs(session_dir)
		session_loader_loc=os.path.join(session_dir,loader_name)
		#print session_hostmap_loc
		#print self.parent.save_to_dir
		if os.path.isfile(session_loader_loc):
			pass
			#print 'session host map already exists'

		else:
			os.chdir(home)
			if loader_loc.startswith(r'.'):
				#relative
				real_loader_loc=os.path.join(transport_home,loader_loc)
			else:
				real_loader_loc=os.path.realpath(loader_loc)
			assert os.path.isfile(real_loader_loc), 'sqlloader template does not exists at\n%s' % real_loader_loc
			#print real_hostmap_loc
			#print session_hostmap_loc
			shutil.copyfile(real_loader_loc,session_loader_loc)
			#obj.SetValue(session_hostmap_loc)
			#self.Save()
			#print 'created new session_hostmap at \n%s' % session_hostmap_loc
		send('set_loader_profile', (session_loader_loc))
		#print session_hostmap_loc
		#e(0)
		#return session_loader_loc	
		
	def getSessionDir(self):
		session_dir=os.path.join(self.parent.save_to_dir,self.parent.getSessionName())
		return session_dir		
	def onSetHostMap(self, data, extra1, extra2=None):
		(hostmap_loc)=data
		k='host_map'
		if self.obj.has_key(k):
			self.obj[k][1].SetValue(hostmap_loc)
		#send('save_args',())		
	def onSetLoaderProfile(self, data, extra1, extra2=None):
		(profile_loc)=data
		k='loader_profile'
		#print self.obj.keys()
		if self.obj.has_key(k):
			self.obj[k][1].SetValue(profile_loc)
		#send('save_args',())
	def onSetEtlLoc(self, data, extra1, extra2=None):
		(etl_loc,k)=data
		#print etl_loc,k
		#k='loader_profile'
		#print self.obj.keys()
		if self.obj.has_key(k):
			self.obj[k][1].SetValue(etl_loc)
		#send('save_args',())
		
	def onSetEtlEditorProfile_(self, data, extra1, extra2=None):
		(etl_loc,k)=data
		#print 'onSetEtlEditorProfile',k
		#print etl_loc
		#k='loader_profile'
		#print self.obj.keys()
		if self.obj.has_key(k):
			self.obj[k][1].SetValue(etl_loc)
		#send('save_args',())	
	def onKey(self, evt):
		if evt.GetKeyCode() == wx.WXK_DOWN:
			print "Down key pressed"
		else:
			evt.Skip()			
	def onRemoveWidget(self, event):
		""""""
		if self.widgetSizer.GetChildren():
			self.widgetSizer.Hide(self.number_of_buttons-1)
			self.widgetSizer.Remove(self.number_of_buttons-1)
			self.number_of_buttons -= 1
			self.frame.fSizer.Layout()
			#self.frame.Fit()
	def setLoaderButtons(self, panel):
		#print self.copy_vector[1].upper(),self.copy_vector[1].upper().startswith('ORA')
		ora=self.copy_vector[1].upper().startswith('ORA')
		if 1: #self.copy_vector[1].upper().startswith('ORA'):
			empty=False
			#self.obj={}
			if not hasattr(panel, 'hbox'):
				empty=True
				#sb_from = wx.StaticBox(panel, label='Output')
				
				panel.hbox = wx.BoxSizer( wx.HORIZONTAL)
			#if hasattr(panel, 'fgs'):
			else:
				#pprint(dir(panel.hbox))
				l=len(list(panel.hbox.GetChildren()))
				for i in range(l):
					#c=panel.fgs.GetChildren()[i]
					#	print c.Destroy()
					#panel.fgs.Destroy()
					#print i,l, l-i
					l= len(list(panel.hbox.GetChildren()))
					panel.hbox.Hide(l-1)
					panel.hbox.Remove(l-1)
				
			#hbox = wx.BoxSizer(wx.HORIZONTAL)
			#panel.fgs = wx.GridBagSizer(2, 10)
			
			#sql_boxsizer = wx.StaticBoxSizer(sb_from, wx.HORIZONTAL)
			btn_ctl=wx.Button(panel, label='Control0', size=(-1,30))
			panel.hbox.Add(btn_ctl, flag=wx.LEFT|wx.TOP, border=2)
			#btn_ctl.Bind(wx.EVT_BUTTON, self.OnFileOpen)
			self.gen_bind(wx.EVT_BUTTON,btn_ctl, self.OnFileOpen,('ctl'))
			btn_log=wx.Button(panel, label='Log0', size=(42,30))
			panel.hbox.Add(btn_log, flag=wx.LEFT|wx.TOP, border=2)
			self.gen_bind(wx.EVT_BUTTON,btn_log, self.OnFileOpen,('log'))
			btn_discard=wx.Button(panel, label='Discard0', style=wx.BU_EXACTFIT)
			panel.hbox.Add(btn_discard, flag=wx.LEFT|wx.TOP, border=2)
			self.gen_bind(wx.EVT_BUTTON,btn_discard, self.OnFileOpen,('dsc'))
			btn_bad=wx.Button(panel, label='Bad0', style=wx.BU_EXACTFIT)
			panel.hbox.Add(btn_bad, flag=wx.LEFT|wx.TOP, border=2)
			self.gen_bind(wx.EVT_BUTTON,btn_bad, self.OnFileOpen,('bad'))				
			#boxsizer.Add(sql_boxsizer, flag=wx.LEFT|wx.TOP, border=5)
			
			#self.btn_sqlldr_open.Enable(True)
			imageFile = os.path.join(home,"images/folder_icon_16.png")
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			
			if hasattr(self, 'btn_sqlldr_open') and self.btn_sqlldr_open:
				self.btn_sqlldr_open.Destroy()		
			self.btn_sqlldr_open=wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
			panel.hbox.Add(self.btn_sqlldr_open, flag=wx.LEFT|wx.TOP, border=2)
			self.gen_bind(wx.EVT_BUTTON,self.btn_sqlldr_open, self.OnShowSqlLdrDir, ())
			
			self.sqldr_btns=(btn_ctl,btn_log,btn_discard,btn_bad,self.btn_sqlldr_open)


			#panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			if empty:
				#pass
				panel.SetSizer(panel.hbox)
				#pprint(dir(panel.fgs))
				#for c in panel.fgs.GetChildren():
				#	print c.Destroy()

					
			if not ora:
				panel.Hide()
			else:
				panel.Show()
			panel.hbox.Layout()
			#panel.Fit()
		
	def OnShowSqlLdrDir(self, evt,params):
		#print 'OnShowSqlLdrDir'
		#[dir_obj] = params
		#dir_loc= dir_obj.GetValue()
		sqldr_dir=os.path.join(self.getLogDir(),'sqlloader')
		if not os.path.isdir(sqldr_dir):
			msg='SQL*Loader dir\n%s\ndoes not exists.' % sqldr_dir
			self.parent.Warn(msg)
		else:
			#print 'exists'
			#file_loc 
			self.parent.ShowLocation(sqldr_dir)			
	def setTargetArgs(self, panel):
		empty=False
		panel.Freeze()
		#self.obj={}
		if not hasattr(panel, 'hbox'):
			empty=True
			panel.hbox = wx.BoxSizer(wx.HORIZONTAL)
		if hasattr(panel, 'fgs'):
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
			#panel.fgs.Destroy()
			panel.hbox.Hide(0)
			panel.hbox.Remove(0)
			
		#hbox = wx.BoxSizer(wx.HORIZONTAL)
		panel.fgs = wx.GridBagSizer(2, 30)
		i=0
		#args_dict={}
		#args_dict.update(self.cargs)
		#args_dict.update(self.fargs)
		args_dict = dict(self.cargs, **self.fargs)
		#pprint (args_dict.keys())
		
		args=Args(args_dict)
		#print self.targs.keys()
		#print args
		#print args.copy_vector
		#e(0)
		#print conf._to
		import __builtin__
		__builtin__.args = args
		__builtin__._to = conf._to
		uargs = import_module(os.path.join(conf.abspath,'config','user_conf.py'))
		(_,to_tmpl)=self.tmpl.split('.')
		if 0 and to_tmpl in ['CSV_Default']:
			lbl=''
			default=wx.StaticText(panel, label=lbl)
			panel.fgs.Add(default, pos=(0, 0), span=(1,2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			#e(0)
		#tkeys=[k for k in self.targs.keys() if not self.obj.has_key(k)]
		#tkeys=[k for k in self.targs.keys() ]
		#print tkeys
		#e(0)
		dbkey=self.copy_vector[1]
		panel.unused_from_args={} #self.targs
		#pprint(all_from_args)
		if dbkey:
			
			imp_file = os.path.join(transport_home,'config','include','args','%s_to.py' % dbkey)
			#print imp_file
			assert os.path.isfile(imp_file), imp_file
			pto={}
			pto[dbkey]=OrderedDict()
			import __builtin__
			__builtin__.pto = pto
			__builtin__.dbkey = dbkey
			__builtin__.dbs = conf.dbs			
			import_module(imp_file)
			#from_args=self.fargs.keys()
			#all_from_args=[] #pfrom[dbkey].items() #.keys()
			
			for k,v in pto[dbkey].items():
				#print k
				#print v				
				if not self.checks.has_key(k):
					#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					if self.targs.has_key(k):
						cb = wx.CheckBox(panel, label='', size=(20,20))

						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb
						cb.SetValue(True)					
					elif self.show_unused():
						cb = wx.CheckBox(panel, label='', size=(20,20))
						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb
						panel.unused_from_args[k]=(v['short'],v['long'],'',v['help'])
						#self.checks[k]=cb
						cb.SetValue(False)
		#print len(all_from_args)
		#show used args
		#for k,v in sorted(self.fargs.items()):
		items=[(k,self.targs[k] ) for k in self.targs if k not in self.fargs.keys()]
		#pprint(items)
		#e(0)
		self.tcs = {
			'open_source_args_list':[None, self.OnMessage, 'Open spooler argument list.'],
			'open_target_args_list':[self.OnEditLoaderArglist, self.OnMessage, 'Open loader argument list.'],
			#( 'Cancel', self.CancelClicked, self.OnMessage, 'Cancel button text', ),
			#( 'Re-invert', self.ReinvertClicked, self.OnMessage, 'Re-invert button text', ),
			#( 'Exit', self.ExitClicked, self.OnMessage, 'Exit button text', ),
			}		
		for k,v in sorted(panel.unused_from_args.items()+items):	
			atc= [ self.OnMessage, v[3]]
			#for k in sorted(tkeys):
			#v=self.targs[k]
			#print v
			#print i
			short,long,val,desc=v
			sval=str(val).strip('"')
			style=0
			
			if k in ['to_passwd']:
				style=wx.TE_PASSWORD
			length=self.tc_length
			if k in ['to_dir', 'target_client_home','to_file']:
				length=160
			#if k in ['to_file']:
			#	length=148					
			if k in ['to_passwd']:
				length=160
				self.obj[k]= [wx.StaticText(panel, label=k)]
			else:
				#print k
				#e(0)
				tc= aTextCtrl(panel,atc,value=sval, style=style, size=(length,22))
				#wx.TextCtrl(panel,value=sval, style=style, size=(length,22))
				self.obj[k]= [wx.StaticText(panel, label=k), tc]
			panel.fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			if self.checks and not self.checks[k].GetValue():
				self.obj[k][0].Enable(False)			
			
			if k in ['to_file']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				
				#global home
				dir =home
				#print sval
				if os.path.isdir(sval):
					dir=sval
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputFile,[self.obj[k][1]])
				#floc=None
				#if os.path.isdir(sval):
				#floc=sval
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputFile,[self.obj[k][1]])
				
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				self.add_tc(panel, (1,2,3), k, i)
				if 0:
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)				
			elif k in ['to_dir', 'target_client_home']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				#global home
				#dir =home
				#print sval
				#if os.path.isdir(sval):
				#	dir=sval
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputDir,[self.obj[k][1],k])
				
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				self.add_tc(panel, (1,2,3), k, i)
				if 0:
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			elif k in ['to_passwd']:
				self.obj[k].append(None)
				self.obj[k].append(None)
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k][2]=wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#global home
				dir =home
				#print sval
				if os.path.isdir(sval):
					dir=sval
				
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				pwd_panel = wx.Panel(panel, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
				self.tc_p1=aTextCtrl(pwd_panel,atc,value=sval, style=0, size=(length,22))
				self.tc_p1.SetName(k)
				self.tc_p1.Hide()
				self.tc_p2=aTextCtrl(pwd_panel,atc,value=sval, style=style, size=(length,22))
				self.tc_p2.SetName(k)
				self.tc_p2.Show()
				self.trg_hide_show=[self.tc_p1, self.tc_p2]
				self.obj[k][1]=self.tc_p2
				if self.checks.has_key(k):
					bbox.Add(self.checks[k], 0, flag=wx.ALIGN_CENTER, border=0)					 
				bbox.Add(pwd_panel, 0, flag=wx.ALIGN_CENTER, border=5)	
			
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
				self.tc_p1.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
				self.tc_p2.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnPassword,[self.trg_hide_show])
				#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p1, self.OnPassword,[self.obj[k]])
				#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p2, self.OnPassword,[self.obj[k]])
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			else:
				self.add_tc(panel, (1,), k, i)
			i+=1
			self.obj[k][1].SetName(k)
			self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
			#self.Bind(wx.EVT_TEXT_ENTER, self.f_EVT_TEXT_ENTER,id=self.obj[k][1].GetId()) 
			#show unused args
			#if self.checks.has_key(k):
			#	print [arg for arg in all_from_args if arg not in from_args]
			#	e(0)

		#hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		panel.Thaw()
		panel.SetupScrolling()
		panel.SetAutoLayout(1)
		
		if 0 and not self.copy_vector[1][:3] in conf.ff:	
			if 0:
				self.tc_1test=wx.StaticText(panel, label='NOT TESTED')
				panel.fgs.Add(self.tc_1test, pos=(i, 0), flag=wx.ALIGN_RIGHT|wx.RIGHT, border=1)

			lbl="Test connect"			

			sn=self.parent.getSessionName()
			#tc=self.parent.testconn
			tcbox = wx.BoxSizer(wx.HORIZONTAL)
			
			sn=self.parent.getSessionName()
			#tc=self.parent.testconn
			btn=wx.Button(panel, label=lbl, style=wx.BU_EXACTFIT)	
			#tc[sn]['source'][0]
			btn.SetName('target')
			btn.Bind(wx.EVT_BUTTON, self.OnTestConnect)
			tcbox.Add(btn, flag=wx.LEFT|wx.TOP, border=5)
			imageFile = os.path.join(home,"images/editor_icon_16_2.png")
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			bitbtn = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))

			bitbtn.Bind(wx.EVT_BUTTON, self.OnEditTestConnectSQL)
			bitbtn.SetName('target')
			tcbox.Add(bitbtn, flag=wx.LEFT|wx.TOP, border=5)			
			if 1:
				#btn_sqp=wx.Button(panel, label=lbl, style=wx.BU_EXACTFIT)	
				imageFile = os.path.join(home,"images/exec_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				btn_sqp = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#tc[sn]['source'][0]
				btn_sqp.SetName('target_sqp')
				btn_sqp.Bind(wx.EVT_BUTTON, self.OnOpenSqlPlusMenu)
				tcbox.Add(btn_sqp, flag=wx.LEFT|wx.TOP, border=5)
			


			panel.fgs.Add(tcbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)

			id=self.the_id[1]
			if self.parent.btn.has_key(id) and self.parent.counters[id]>0:
				btn.Enable(False)
				lbl='Closing in %d' % (self.parent.closing_in-self.parent.counters[id])
				btn.SetLabel('%s: %s' % (sn,lbl))
				self.parent.btn[id]=btn

				
			#fgs.Add(btn, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			
		#hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		#panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		if empty:			
			panel.SetSizer(panel.hbox)
			#pprint(dir(panel.fgs))
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
		panel.hbox.Layout()
		#panel.Fit()
	def OnTest(self, evt):
		print 'test1'


	def onDisableUnusedArgs(self, data, extra1, extra2=None):
		#print 'onDisableUnusedArgs'	
		#usedkeys=self.fargs.keys()
		for k, v in self.checks.items():
			if not v.GetValue():
				self.obj[k][0].Enable(False)
				self.obj[k][1].Enable(False)
			else:
				self.obj[k][0].Enable(True)
				self.obj[k][1].Enable(True)
				
		#panel.hbox.Layout()
	def setSourceArgs(self, panel):	
		empty=False
		panel.Freeze()
		#self.obj={}
		if not hasattr(panel, 'hbox'):
			empty=True
			panel.hbox = wx.BoxSizer(wx.HORIZONTAL)
		if hasattr(panel, 'fgs'):
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
			#panel.fgs.Destroy()
			panel.hbox.Hide(0)
			panel.hbox.Remove(0)
		#else:
		#panel.fgs = wx.GridBagSizer(10, 3)
	
		#hbox = wx.BoxSizer(wx.HORIZONTAL)
		panel.fgs = wx.GridBagSizer(2, 30)
		i=0
		#pprint(self.fargs.items())
		#print len(self.fargs.items())
		
		dbkey=self.copy_vector[0]
		panel.unused_from_args={} #self.fargs
		#pprint(all_from_args)
		#(_,self.fargs,self.targs)=self.parent.unobfuscate([None,self.fargs,self.targs])
		if dbkey:
			
			imp_file = os.path.join(transport_home,'config','include','args','%s_from.py' % dbkey)
			#print imp_file
			assert os.path.isfile(imp_file), imp_file
			pfrom={}
			pfrom[dbkey]=OrderedDict()
			import __builtin__
			__builtin__.pfrom = pfrom
			__builtin__.dbkey = dbkey
			__builtin__.dbs = conf.dbs			
			import_module(imp_file)
			#from_args=self.fargs.keys()
			#all_from_args=[] #pfrom[dbkey].items() #.keys()
			#print self.fargs.keys()
			for k,v in pfrom[dbkey].items():
				#print k
				#print v['help']
				if 1:
					if self.fargs.has_key(k):
						cb = wx.CheckBox(panel, label='', size=(20,20))

						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb
						cb.SetValue(True)					
					elif self.show_unused():
						cb = wx.CheckBox(panel, label='', size=(20,20))

						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb					
						#print '---------adding ------', k
						panel.unused_from_args[k]=(v['short'],v['long'],'',v['help'])
						cb.SetValue(False)
		#print len(all_from_args)
		#show used args
		#for k,v in sorted(self.fargs.items()):
		vals={'header':['0','1'],'skip_rows':['0','1']}

		for k,v in sorted(panel.unused_from_args.items()+self.fargs.items()):
			atc= [ self.OnMessage, v[3]]
			#all_from_args
			#print k
			#print i
			#print v
			short,long,val,desc=v
			sval=str(val).strip('"')
			style=wx.TE_PROCESS_ENTER
			if k in ['from_passwd']:
				style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER
			length=self.tc_length
			if k in ['query_sql_file','query_sql_dir', 'input_dirs','input_files', 'source_client_home']:
				length=self.tc_length-20
			if k in ['from_passwd']:
				length=self.tc_length-20
				self.obj[k]= [wx.StaticText(panel, label=k)]
			else:
				tx=wx.StaticText(panel, label=k)
				#tx.Enable(False)
				if k not in ['header','skip_rows']:
					#tc=wx.TextCtrl(panel,value=sval, style=style, size=(length,-1))
					tc=aTextCtrl(panel,atc,value=sval, style=style, size=(length,22))
					tc.Disable()				
					#tc=wx.TextCtrl(panel,value=sval, style=style, size=(length,22))
					#tc.Disable()
					self.obj[k]= [tx, tc]
				
			panel.fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			if self.checks and self.checks.has_key(k) and not self.checks[k].GetValue():
				self.obj[k][0].Enable(False)
			#print dir(panel.fgs)
			#print panel.fgs.Rows
			#print i
			if k in ['header','skip_rows']:
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				#bbox = wx.BoxSizer(wx.HORIZONTAL)
				#self.add_tc(panel, (1,),  k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				#dbg=self.obj[k][1].GetValue()
				#del self.obj[k][1]
				#print self.obj[k][1]
				#e(0)
				self.obj[k][1] = aComboBox(panel, atc , sval, (-1, 150), (-1,-1), vals[k], wx.CB_DROPDOWN)
				self.add_tc(panel, (1,),  k, i)
				#panel.fgs.Add(self.obj[k][1], pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	\
			elif k in ['input_files','url_files','output']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				

				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnInputFiles,[self.obj[k][1]])
				
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				
				bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.add_tc(panel, (1,2), k, i)				
				#panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	

						
			elif k in ['query_sql_file']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				
				#global home
				hdir =home
				#print sval
				ffile=sval.split(';')[0]
				if os.path.isfile(ffile):
					hdir=os.path.dirname(ffile) 
				#print sval
				#print dir
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnQuerySqlFile,[self.obj[k][1],hdir])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				
				imageFile = os.path.join(home,"images/editor_icon_16_2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				bitbtn = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				#bitbtn.Bind(wx.EVT_BUTTON, self.OnEditSQL)
				self.gen_bind(wx.EVT_BUTTON,bitbtn, self.parent.OnEditSQL,(self.obj[k][1]))
				self.obj[k].append(bitbtn)
				self.add_tc(panel, (1,2,3), k, i)
				if 0:
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(bitbtn, 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
			elif k in ['query_sql_dir', 'input_dirs', 'source_client_home','url_dirs']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnInputDir,[self.obj[k][1],k])
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				self.add_tc(panel, (1,2,3), k, i)
				if 0:
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			elif k in ['from_passwd']:
				self.obj[k].append(None)
				self.obj[k].append(None)
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k][2]=wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#global home
				hdir =home
				#print sval
				if os.path.isdir(sval):
					hdir=sval
				
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				pwd_panel = wx.Panel(panel, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
				self.tc_p1=aTextCtrl(pwd_panel,atc,value=sval, style=0, size=(length,22))
				self.tc_p1.SetName(k)
				self.tc_p1.Hide()
				self.tc_p2=aTextCtrl(pwd_panel,atc,value=sval, style=style, size=(length,22))
				self.tc_p2.SetName(k)
				self.tc_p2.Show()
				self.src_hide_show=[self.tc_p1, self.tc_p2]
				self.obj[k][1]=self.tc_p2
				if self.checks.has_key(k):
					bbox.Add(self.checks[k], 0, flag=wx.ALIGN_CENTER, border=0)
				bbox.Add(pwd_panel, 0, flag=wx.ALIGN_CENTER, border=0)	
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
				self.tc_p1.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
				self.tc_p2.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnPassword,[self.src_hide_show])
				#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p1, self.OnPassword,[self.obj[k]])
				#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p2, self.OnPassword,[self.obj[k]])
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			else:
				self.add_tc(panel, (1,), k, i)
				if 0:
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					#if not hasattr(self, 'checks'):
					#	self.checks={}
					if self.checks.has_key(k):

						bbox.Add(self.checks[k], 0, flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT|wx.BOTTOM, border=0)
						if not self.checks[k].GetValue():
							self.obj[k][1].Enable(False)
							self.obj[k][0].Enable(False)
							#self.obj[k][2].Enable(False)
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=0)	
					#print k
					panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					#panel.fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			i+=1
			self.obj[k][1].SetName(k)
			self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
			#self.Bind(wx.EVT_TEXT_ENTER, self.f_EVT_TEXT_ENTER,id=self.obj[k][1].GetId()) 
			#show unused args
			#if self.checks.has_key(k):
			#	print [arg for arg in all_from_args if arg not in from_args]
			#	e(0)

		#hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)
		panel.Thaw()		
		panel.SetupScrolling()
		panel.SetAutoLayout(1)
		if empty:			
			panel.SetSizer(panel.hbox)
			#pprint(dir(panel.fgs))
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
		panel.hbox.Layout()
		#panel.Fit()	
		#print len(self.checks), len(self.obj)
		#pprint(sorted(self.obj.keys()))
		#from_args_panel.SetSizer(hbox)
		#print self.obj['from_passwd'][1].GetValue()
	def onArgCheck(self, e):

		sender = e.GetEventObject()
		isChecked = sender.GetValue()
		k=sender.GetName() 
		#print k
		if isChecked:
			#print 'checked', k			
			self.obj[k][0].Enable(True)
			self.obj[k][1].Enable(True)
			self.checks[k].SetValue(True)
			self.changed=True
			if self.core_args_panel.unused_from_args.has_key(k):
				#print self.core_args_panel.unused_from_args[k]
				self.obj[k][1].SetValue(self.core_args_panel.unused_from_args[k][2])
				self.cargs[k]=self.core_args_panel.unused_from_args[k]
				del self.core_args_panel.unused_from_args[k]
				#print self.cargs[k]
			elif self.from_args_panel.unused_from_args.has_key(k):
				#print self.core_args_panel.unused_from_args[k]
				self.obj[k][1].SetValue(self.from_args_panel.unused_from_args[k][2])
				self.fargs[k]=self.from_args_panel.unused_from_args[k]
				del self.from_args_panel.unused_from_args[k]
				#print self.cargs[k]
			elif self.to_args_panel.unused_from_args.has_key(k):
				#print self.core_args_panel.unused_from_args[k]
				self.obj[k][1].SetValue(self.to_args_panel.unused_from_args[k][2])
				self.targs[k]=self.to_args_panel.unused_from_args[k]
				del self.to_args_panel.unused_from_args[k]
				#print self.cargs[k]
			else:
				assert 1==2, 'Unknown key "%s"' % k
		else: 
			#print 'un-checked'
			self.obj[k][0].Enable(False)
			self.obj[k][1].Enable(False)
			self.checks[k].SetValue(False)
			self.changed=True
			if self.cargs.has_key(k):
				self.core_args_panel.unused_from_args[k] = self.cargs[k]
				del self.cargs[k]
				#print self.core_args_panel.unused_from_args[k]
			elif self.fargs.has_key(k):
				self.from_args_panel.unused_from_args[k] = self.fargs[k]
				del self.fargs[k]
				#print self.core_args_panel.unused_from_args[k]
			elif self.targs.has_key(k):
				self.to_args_panel.unused_from_args[k] = self.targs[k]
				del self.targs[k]
				#print self.core_args_panel.unused_from_args[k]
			else:
				assert 1==2, 'Unknown key "%s"' % k
			send('save_args',())
	def setCommonArgs_0(self, panel):
		empty=False
		#self.obj={}
		if not hasattr(panel, 'hbox'):
			empty=True
			panel.hbox = wx.BoxSizer(wx.HORIZONTAL)
		if hasattr(panel, 'fgs'):
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
			#panel.fgs.Destroy()
			panel.hbox.Hide(0)
			panel.hbox.Remove(0)
		#else:
		panel.fgs = wx.GridBagSizer(10, 3)
		#sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
		#sizer.Add(tc0, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
		#fgs = wx.FlexGridSizer(3, 4, 9, 20)
		#ttl=['Copy vector','Pool size','Num of shards','Field terminator','Truncate target']
		#pprint(dir(fgs))
		
		i=0
		#pprint(self.cargs.items())
		#e(0)
		length=120
		for k,v in sorted(self.cargs.items()):
			if k in ['default_spool_dir','log_dir']:
				length=100
			elif k in ['time_stamp']:
				length=150
			else:
				length=120
			#print k,v
			short,long,val,desc=v
			row=i%6
			#col=(i-i%2)
			bucket=6
			col=i/bucket*2
			#print 'row',row, 'col', col
			self.obj[k]= [wx.StaticText(panel, label=k), wx.TextCtrl(panel,value=str(val).strip('"'), size=(length,22))]
			self.obj[k][1].SetName(k)
			self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
			
			panel.fgs.Add(self.obj[k][0], pos=(i%bucket, col), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			
			if k in ['default_spool_dir']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 0:
					imageFile = os.path.join(home,"images/folder_icon_16.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputDir,[self.obj[k][1],k])
				#self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				
				bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)	
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			elif k in ['log_dir']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 1:
					imageFile = os.path.join(home,"images/folder_icon_16.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputDir,[self.obj[k][1],k])
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				
				bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)					
			elif k in ['job_pre_etl','thread_pre_etl','loader_profile', 'host_map']:
				if 0:
					imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 1:
					imageFile = os.path.join(home,"images/editor_icon_16_2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				
				#self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnSetFile,[self.obj[k][1],'Set %s' % k])
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnEditPreEtlFile,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				
				bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
				
			else:
				panel.fgs.Add(self.obj[k][1], pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			
			if k in self.disabled:
				#print k, self.obj[k][1], self.obj[k][1].Name
				if  self.obj.has_key(k):
					self.obj[k][1].Enable(False)
			#pprint(dir)
			#pprint (self.disabled)
			#e(0)
			i+=1
		panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		if empty:			
			panel.SetSizer(panel.hbox)
			#pprint(dir(panel.fgs))
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
		panel.hbox.Layout()
		#panel.Fit()		
		#return core_args_panel
	def show_unused(self):
		return self.cb_all_args.GetValue()
	def setCommonArgs(self, panel):	
		empty=False
		
		panel.Freeze()
		#self.obj={}
		if not hasattr(panel, 'hbox'):
			empty=True
			panel.hbox = wx.BoxSizer(wx.HORIZONTAL)
		if hasattr(panel, 'fgs'):
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
			#panel.fgs.Destroy()
			panel.hbox.Hide(0)
			del panel.fgs
			panel.hbox.Remove(0)
		#else:
		#panel.fgs = wx.GridBagSizer(10, 3)
	
		#hbox = wx.BoxSizer(wx.HORIZONTAL)
		#panel.fgs = wx.GridBagSizer(4, 40)
		panel.fgs = wx.GridBagSizer(2, 8)
		i=0
		#pprint(self.fargs.items())
		#print len(self.fargs.items())
		
		dbkey=self.copy_vector[0].upper()
		panel.unused_from_args={}#self.cargs
		#pprint(all_from_args)
		#print len(self.cargs),len(self.fargs),len(self.targs)
		if dbkey:
			
			imp_file = os.path.join(transport_home,'config','include','args','core.py')
			#print imp_file
			assert os.path.isfile(imp_file), imp_file
			#pcore={}
			pcore=OrderedDict()
			import __builtin__
			__builtin__.pcore = pcore
			#__builtin__.dbkey = dbkey
			#__builtin__.dbs = conf.dbs			
			import_module(imp_file)
			#from_args=self.fargs.keys()
			#all_from_args=[] #pfrom[dbkey].items() #.keys()
			#pprint(pcore[dbkey].keys())
			#pprint (pcore)
			for k,v in pcore.items():
				#print k
				#print v				
				if 1:					
					if self.cargs.has_key(k):
						cb = wx.CheckBox(panel, label='', size=(20,-1))

						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb
						cb.SetValue(True)					
					elif self.show_unused():
						cb = wx.CheckBox(panel, label='', size=(20,20))

						cb.SetName(k)
						cb.Bind(wx.EVT_CHECKBOX, self.onArgCheck)
						#panel.fgs.Add(cb,  pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.checks[k]=cb						
						panel.unused_from_args[k]=(v['short'],v['long'],'',v['help'])
						#self.checks[k]=cb
						cb.SetValue(False)
		#print len(all_from_args)
		#show used args
		#for k,v in sorted(self.fargs.items()):
		#pprint(all_from_args.keys())
		#print len(self.cargs),len(self.fargs),len(self.targs)
		#all_from_args=[]
		#all_from_args=self.cargs.items()+extra_from_args.items()
		vals={'debug_level':['1','2','4'], 'num_of_shards':['1','2','3','4','5','10','15','20'],'pool_size':['1','2','3','4','5','10','15','20'],
		'spool_type':['csv','json'],'keep_data_file':['0','1'],'lame_duck':['0','10','100','1000','10000','100000'], 'field_term':['|','^',',','|^']}
		for k,v in sorted(self.cargs.items()+panel.unused_from_args.items()):
			atc= [ self.OnMessage, v[3]]
			#all_from_args
			#print k
			#print i
			#print v
			short,long,val,desc=v
			sval=str(val).strip('"')
			style=wx.TE_PROCESS_ENTER
			#length=self.tc_length
			if k in ['default_spool_dir','log_dir','time_stamp']:
				length=self.tc_length-20
			#elif k in ['time_stamp']:
			#	length=self.tc_length
			else:
				length=self.tc_length
				#print k,v
			short,long,val,desc=v
			#blen=8
			#row=i%blen
			#col=(i-i%2)
			bucket=8
			col=i/bucket*2
			tx=wx.StaticText(panel, label=k, size=(-1,-1))
			tx.Enable(True)
			tc=None
			if k not in ['debug_level','num_of_shards','pool_size','keep_data_file','spool_type','lame_duck', 'field_term']:
				tc=aTextCtrl(panel,atc,value=sval, style=style, size=(length,-1))
				tc.Disable()
			self.obj[k]= [tx, tc]
				
			#panel.fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			#print 'common',i%bucket, col
			panel.fgs.Add(self.obj[k][0], pos=(i%bucket, col), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			if self.checks and not self.checks[k].GetValue():
				self.obj[k][0].Enable(False)
			#print dir(panel.fgs)
			#print panel.fgs.Rows
			#print i
			if k in ['default_spool_dir']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				#print self.obj[k]
				#print len(self.obj[k])
				
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 0:
					imageFile = os.path.join(home,"images/folder_icon_16.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputDir,[self.obj[k][1],k])
				#self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				self.add_tc(panel,(1,2), k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)	
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				#print 'common',i%bucket, col+1				
				#panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			elif k in ['log_dir']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 1:
					imageFile = os.path.join(home,"images/folder_icon_16.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputDir,[self.obj[k][1],k])
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][3], self.OnShowOutputDir,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				#bbox = wx.BoxSizer(wx.HORIZONTAL)
				self.add_tc(panel, (1,2,3),  k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				#panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
			elif k in ['time_stamp']:
				
				imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				
				self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnResetTimestamp)
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				#bbox = wx.BoxSizer(wx.HORIZONTAL)
				self.add_tc(panel, (1,2),  k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				#panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			elif k in ['debug_level', 'num_of_shards', 'pool_size', 'keep_data_file','spool_type','lame_duck', 'field_term']:
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				#bbox = wx.BoxSizer(wx.HORIZONTAL)
				#self.add_tc(panel, (1,),  k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				#dbg=self.obj[k][1].GetValue()
				#del self.obj[k][1]
				#print self.obj[k][1]
				#e(0)
				self.obj[k][1] = aComboBox(panel, atc, sval, (-1, 150), (-1,-1), vals[k], wx.CB_DROPDOWN)
				self.add_tc(panel, (1,),  k, i,bucket,col)
				#panel.fgs.Add(self.obj[k][1], pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)				
			elif k in ['job_pre_etl','thread_pre_etl','loader_profile', 'host_map']:
				if 0:
					imageFile = os.path.join(home,"images/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if 1:
					imageFile = os.path.join(home,"images/editor_icon_16_2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.obj[k].append(wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))

				
				
				
				#self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnSetFile,[self.obj[k][1],'Set %s' % k])
				self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnEditPreEtlFile,[self.obj[k][1]])
				#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
				#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
				bbox = wx.BoxSizer(wx.HORIZONTAL)
				self.add_tc(panel, (1,2), k, i,bucket,col)
				#bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
				#bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)
				#bbox.Add(self.obj[k][3], 0, flag=wx.ALIGN_CENTER, border=5)						
				#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
				#panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
				
			#else:
			#	panel.fgs.Add(self.obj[k][1], pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			else:
				#if not hasattr(self, 'checks'):
				#	self.checks={}
				self.add_tc(panel, (1,), k, i,bucket,col)
			
			if k in self.disabled:
				#print k, self.obj[k][1], self.obj[k][1].Name
				if  self.obj.has_key(k):
					self.obj[k][1].Enable(False)

					
				#panel.fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			i+=1
			self.obj[k][1].SetName(k)
			self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
			#self.Bind(wx.EVT_TEXT_ENTER, self.f_EVT_TEXT_ENTER,id=self.obj[k][1].GetId()) 
			#show unused args
			#if self.checks.has_key(k):
			#	print [arg for arg in all_from_args if arg not in from_args]
			#	e(0)

		#hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		panel.hbox.Add(panel.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
		panel.Thaw()
		panel.SetupScrolling()
		panel.SetAutoLayout(1)
		if empty:			
			panel.SetSizer(panel.hbox)
			#pprint(dir(panel.fgs))
			#for c in panel.fgs.GetChildren():
			#	print c.Destroy()
		panel.hbox.Layout()
		#panel.Fit()	
		#print len(self.checks), len(self.obj)
		#pprint(sorted(self.obj.keys()))
		#from_args_panel.SetSizer(hbox)
	def OnResetTimestamp(self, evt):
		#print 'OnResetTimestamp'
		#[ts_obj,title] = params
		self.parent.updateTimeStamp()
		
	def add_tc(self, panel, oids, k, i, bucket=None,col=None):
		bbox = wx.BoxSizer(wx.HORIZONTAL)	
		
		if self.checks.has_key(k):
			bbox.Add(self.checks[k], 0, flag=wx.ALIGN_CENTER|wx.TOP|wx.LEFT|wx.BOTTOM, border=0)
			if not self.checks[k].GetValue():
				for oid in oids:
					self.obj[k][oid].Enable(False)
			else:
				for oid in oids:
					self.obj[k][oid].Enable(True)
				#self.obj[k][1].Enable(False)
				#self.obj[k][0].Enable(False)
				#self.obj[k][2].Enable(False)
		for oid in oids:
			#print k,oid
			bbox.Add(self.obj[k][oid], 0, flag=wx.ALIGN_CENTER, border=0)	
		#print k
		#panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
		if bucket:
			panel.fgs.Add(bbox, pos=(i%bucket, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
		else:
			panel.fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
		
	def OnEditPyFile(self, evt,params):
		print 'OnEditPyFile'
		[file_obj] = params
		val =file_obj.GetValue()
		#import os
		#print val
		fname =os.path.realpath(val)
		#print fname
		
		assert os.path.isfile(fname), 'File does not exists\n%s' % fname
		#webbrowser.open(fname)
		import os
		os.startfile(fname)		
	def OnEditPreEtlFile(self, evt,params):
		#print 'OnEditPreEtlFile'
		import os
		[file_obj] = params
		val =file_obj.GetValue()
		#print val
		#import os
		os.chdir(home)
		fname =os.path.realpath(val)
		#print fname
		assert os.path.isfile(fname), 'File does not exists\n%s' % fname
		#webbrowser.open(fname)
		
		os.startfile(fname)
		#file_to_open = "c:\path\to\file.txt"
		#os.system ('cmd /c "notepad.exe %s"' % fname)
		#os.system(r'start "%s" cmd.exe  /k "%s"' % (title, cmd))
		#How to open python file in default editor from Python script
		if 0:
			import os
			import subprocess

			DEFAULT_EDITOR = 'notepad.exe' # backup, if not defined in environment vars

			#path = os.path.abspath(os.path.expanduser(__file__))
			editor = os.environ.get('EDITOR', DEFAULT_EDITOR)
			#print editor
			subprocess.call([editor, fname])
		if 0:
			import ctypes

			shell32 = ctypes.windll.shell32
			#file = 'somedocument.doc'

			shell32.ShellExecuteA(0,"open",fname,0,0,5)
		if 0:
			import win32com.shell.shell as shell
			shell.ShellExecuteEx(fmask = win32com.shell.shellcon.SEE_MASK_NOASYNC, lpVerb='edit', lpFile=fname)
		
	def load_session(self,copy_vector,tmpl,the_id,args):
		#print 'open_session args_panel'
		#(self.copy_vector,self.tmpl,self.the_id,(self.cargs,self.fargs,self.targs))
		#self.args=args
		del self.cargs
		del self.fargs
		del self.targs
		(self.cargs,self.fargs,self.targs)=args
		#print len(self.cargs),len(self.fargs),len(self.targs)
		#self.args=args_api
		self.the_id=the_id
		#self.cargs,self.fargs,self.targs=self.args
		self.copy_vector=copy_vector
		self.tmpl=tmpl
		#self.core_args_panel.Destroy()
		if self.obj:
			for o,v in self.obj.items():
				#del v
				for c in v:
					if  'BitmapButton' in str(type(c)):
						#print str(type(c))
						c.Destroy()
						#print(dir(c))
					else:				
						c.Destroy()
		#print ''
		self.obj={}
		del self.checks
		self.checks={}
		self.setCommonArgs(self.core_args_panel)
		#pprint(self.obj.keys())
		#print len(self.cargs),len(self.fargs),len(self.targs)
		#e(0)
		self.setSourceArgs(self.from_args_panel)
		#pprint(self.obj.keys())
		self.setTargetArgs(self.to_args_panel)
		#pprint(self.obj.keys())
		self.setLoaderButtons(self.output_panel)
		#print len(self.cargs),len(self.fargs),len(self.targs)
		self.buttons['open_source_args_list'][2]='Open spooler argument list for "%s".' % self.copy_vector[0]
		self.buttons['open_target_args_list'][2]='Open loader argument list for "%s".' % self.copy_vector[1]
		k='host_map'
		
		if self.obj.has_key(k):
			hostmap_loc = self.obj[k][1].GetValue().strip()
			#print 'hm:', hostmap_loc
			new_hostmap_loc=self.parent.args_panel.CreateNewSessionHostMap(hostmap_loc)
			#print 'hm:', new_hostmap_loc
			#if new_hostmap_loc not in [hostmap_loc]:
			self.obj[k][1].SetValue(new_hostmap_loc)
			#print 'set to', new_hostmap_loc
			#e(0)
			#print conf._to.join(self.copy_vector)
			self.set_hm(self.copy_vector, new_hostmap_loc)
			if 0:
				self.hm = hmap(self.copy_vector,new_hostmap_loc)						
				am= self.hm.get_active_mapping()
				self.parent.set_bar_status(2,am)
			del self.parent._hmMenu
			self.parent._hmMenu=None
		else:
			print 'no host_map'
		
		k='loader_profile'
		#e(0)
		#pprint(self.args)
		#assert self.obj.has_key(k), 'loader profile ./config/sqlloader.py is not defined for this session.'
		if self.obj.has_key(k) and self.checks[k].GetValue():
			loader_loc = self.obj[k][1].GetValue().strip()
			self.parent.args_panel.CreateNewSessionLoaderProfile(loader_loc)
			#e(0)
			#if new_hostmap_loc not in [loader_loc]:
			#	self.obj[k][1].SetValue(new_loader_loc)
			#print new_hostmap_loc
			#print loader_loc
			#e(0)
			#print conf._to.join(self.copy_vector)
			
			#self.hm = hmap(self.copy_vector,new_hostmap_loc)						
			#am= self.hm.get_active_mapping()
			#self.parent.set_bar_status(2,am)
			#self.parent._hmMenu=None
		#else:
			#print 'no host_map'			
		k='keep_data_file'
		if self.obj.has_key(k):
			val=self.obj[k][1].GetValue().strip()
			send('set_keep_data_file',(val))
		self.etl_name=['job_pre_etl', 'job_post_etl', 'thread_pre_etl', 'thread_post_etl']		
		#self.etl_file_loc={}
		#default_etl=self.etl_name[0]
		self.etl_file_name={x:'%s.py' % x for x in self.etl_name}		
		#self.default_etl_file_loc={x:os.path.join(transport_home,  os.path.join('config','etl',self.etl_file_name[x])) for x in self.etl_name}		
		#self.etl={}		
		#self.etl_loc={}		
			
		k='job_pre_etl'
		#e(0)
		#pprint(self.args)
		#assert self.obj.has_key(k), 'loader profile ./config/sqlloader.py is not defined for this session.'
		#print '#'*60
		#print '#'*60
		if self.obj.has_key(k):
			pre_etl_loc = self.obj[k][1].GetValue().strip()
			#print pre_etl_loc
			self.CreateNewSessionEtlFile(pre_etl_loc,k)
			
		if 0:
			if 0:
				k='job_pre_etl'
				etl_names=['job_pre_etl', 'job_post_etl', 'thread_pre_etl', 'thread_post_etl']
				#print self.args_panel.obj.keys()
				etl_file_loc={} #{x:None for x in k}
				for k in etl_names:
					if self.obj.has_key(k):			
						etl_file_loc[k]=self.obj[k][1].GetValue()
				#print self.obj.keys()
				#if self.obj.has_key(k):			
			k='job_pre_etl'
			#session_etl_file=self.parent.editor_panel.getSessionEtlFileLoc(k)
			#if 
			#print 'test', self.obj.has_key(k)
			#pprint(self.obj.keys())
			self.parent.etl_loc={}
			#self.parent.editor_panel.etl_changed=False

		self.parent.output_panel.setOutputArgs()		
		#self.sb_from.Layout()
		#self.sb_from.Fit()
		self.s_boxsizer.Layout()
		#self.s_boxsizer.Fit(self)
		#self.args_hbox.Layout()
		#self.Fit()	
		self.args_vbox.Layout()
		#self.Fit()	
		self._sMenu = None #source popup menu
		self._tMenu = None #target popup menu
		self._saMenu = None #save as popup menu
		self.T=False
		self.Q=False
		#print '###############exiting open_session args_panel'
		#print len(self.cargs),len(self.fargs),len(self.targs)
	def getSessionEtlFileLoc(self,k):
		session_loc=os.path.join(self.parent.save_to_dir,self.parent.getSessionName(),'etl', self.etl_file_name[k])
		return session_loc
	def CreateNewSessionEtlFile(self, etl_loc,k ): 
		session_etl_loc=self.getSessionEtlFileLoc(k)
		os.chdir(home)
		real_etl_loc=etl_loc
		if real_etl_loc.startswith(r'.'):
			#relative
			real_etl_loc=os.path.join(home,real_etl_loc)
		
		real_etl_loc=os.path.realpath(real_etl_loc)
				
		if os.path.isfile(session_etl_loc):
			#print 'session file exists'
			pass
		else:			
			#print profile_loc
			#print session_loc
			dir=os.path.dirname(session_etl_loc)
			if not os.path.isdir(dir):
				os.makedirs(dir)
			shutil.copyfile(real_etl_loc,session_etl_loc)
		send('set_etl_loc', (session_etl_loc,k))
		#print session_etl_loc
		return session_etl_loc
		if 0:
			loader_name=os.path.basename(loader_loc)
			session_dir=self.getSessionDir()
			if not os.path.isdir(session_dir):
				os.makedirs(session_dir)
			session_loader_loc=os.path.join(session_dir,loader_name)
			#print session_hostmap_loc
			#print self.parent.save_to_dir
			if os.path.isfile(session_loader_loc):
				pass
				#print 'session host map already exists'

			else:
				os.chdir(home)
				if loader_loc.startswith(r'.'):
					#relative
					real_loader_loc=os.path.join(transport_home,loader_loc)
				else:
					real_loader_loc=os.path.realpath(loader_loc)
				assert os.path.isfile(real_loader_loc), 'sqlloader template does not exists at\n%s' % real_loader_loc
				#print real_hostmap_loc
				#print session_hostmap_loc
				shutil.copyfile(real_loader_loc,session_loader_loc)
				#obj.SetValue(session_hostmap_loc)
				#self.Save()
				#print 'created new session_hostmap at \n%s' % session_hostmap_loc
				send('set_loader_profile', (session_loader_loc))

			
	def OnEditTestConnectSQL(self, evt):
		#print 'OnEditTestConnectSQL'
		#import webbrowser		
		#(ftype) = params
		#sqldr_dir=os.path.join(self.getLogDir(),'sqlloader')
		#print sqldr_dir
		#fname=self.getSqlLoaderFileName()
		#ctl_fname=os.path.join(sqldr_dir,'%s.%s' % (fname,ftype) )
		#print self.tfile
		tc = evt.GetEventObject()
		webbrowser.open(self.tfile[tc.Name])

		
	def f_EVT_TEXT_ENTER(self, evt):
		print 'f_EVT_TEXT_ENTER'
	def OnFileOpen(self, evt,params):
		#import webbrowser
		(ftype) = params
		sqldr_dir=os.path.join(self.getLogDir(),'sqlloader')
		#print sqldr_dir
		fname=self.getSqlLoaderFileName()
		ctl_fname=os.path.join(sqldr_dir,'%s.%s' % (fname,ftype) )
		webbrowser.open(ctl_fname)

	def getLogDir(self):
		job_dir=self.obj['log_dir'][1].GetValue()
		job_name=self.obj['job_name'][1].GetValue()
		
		time_stamp=self.parent.ts 
		if self.obj.has_key('time_stamp'):
			time_stamp=self.obj['time_stamp'][1].GetValue()
		return os.path.join(job_dir, job_name,time_stamp)
	
	def disableSqlLoaderButtons(self):
		if hasattr(self, 'sqldr_btns'):
			for btn in self.sqldr_btns:
				btn.Enable(False)
	def getSqlLoaderFileName(self):
		sldr_file=''
		if 1:			
			#if self.fargs.has_key('query_sql_file') and self.fargs['query_sql_file'][2]:
			#	qfn, qfx = os.path.splitext(os.path.basename(self.fargs['query_sql_file'][2]))
			#	sldr_file='%s_Shard-0' % (qfn)
			if self.targs.has_key('to_table') and self.targs['to_table'][2]:
				sldr_file='%s_Shard-0' % (self.targs['to_table'][2])
				if 0:
					if self.fargs.has_key('from_sub_partition') and self.fargs['from_sub_partition'][2]:
						sldr_file='%s_%s_Shard-0' % (self.fargs['from_table'][2],self.fargs['from_sub_partition'][2])

					elif self.fargs.has_key('from_partition') and self.fargs['from_partition'][2]:
						sldr_file='%s_%s_Shard-0' % (self.fargs['from_table'][2],self.fargs['from_partition.replace'][2]('(','_').replace(')','_'))
			
		return sldr_file
	def enableSqlLoaderButtons(self):	
		if hasattr(self, 'sqldr_btns') and self.sqldr_btns:
			(ctl, log, dsc, bad, open) = self.sqldr_btns
			sqldr_dir=os.path.join(self.getLogDir(),'sqlloader')
			#print sqldr_dir
			fname=self.getSqlLoaderFileName()
			#print '#'*60
			#print fname
			#print '#'*60
			ctl_fname=os.path.join(sqldr_dir,'%s.ctl' % fname )
			
			if os.path.isfile(ctl_fname):
				ctl.Enable(True)
			else:
				ctl.Enable(False)
			log_fname=os.path.join(sqldr_dir,'%s.log' % fname )
			if os.path.isfile(log_fname):
				log.Enable(True)		
			else:
				log.Enable(False)
			dsc_fname=os.path.join(sqldr_dir,'%s.dsc' % fname )
			if os.path.isfile(dsc_fname):
				dsc.Enable(True)
			else:
				dsc.Enable(False)
			bad_fname=os.path.join(sqldr_dir,'%s.bad' % fname )
			if os.path.isfile(bad_fname):
				bad.Enable(True)			
			else:
				bad.Enable(False)
			ld=os.path.isdir(self.getLogDir())
			if (self.parent.last_log_dir.has_key(self.parent.session_name) and self.parent.last_log_dir[self.parent.session_name]) or ld:
				open.Enable(True)
			else:
				open.Enable(False)
	def src_TimerHandler(self, event,the_id):
		#print  'the_id', the_id
		self.src_count = self.src_count + 1
		msg= 'Closing in %d' % (5-self.src_count)
		hwnd= self.get_hwnds_for_pid (self.src_p.pid)
		if not hwnd or self.src_count >= 5:
			self.close_exec(self.src_p)
			self.src_count = 0
			self.src_timer.Stop()
			self.src_btn.Enable(True)
			self.src_btn.SetLabel('Test connect')
		else:			
			self.src_btn.SetLabel(msg)
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count
		
		#self.gauge.SetValue(self.count)
		#self.gauge.Pulse()	
	def trg_TimerHandler(self, event,the_id):
		#print  'the_id', the_id
		self.trg_count = self.trg_count + 1
		msg= 'Closing in %d' % (5-self.trg_count)
		hwnd= self.get_hwnds_for_pid (self.trg_p.pid)
		if not hwnd or self.trg_count >= 5:
			self.close_exec(self.trg_p)
			self.trg_count = 0
			self.trg_timer.Stop()
			self.trg_btn.Enable(True)
			self.trg_btn.SetLabel('Test connect')
		else:			
			self.trg_btn.SetLabel(msg)		



	
	def OnOpenSqlPlusMenu(self, event):
		print 'OnOpenSqlPlusMenu'
		#print self.recent
		#e(0)
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()
		#print 
		#print btn.Name
		if btn.Name.startswith('source'):
			# Create the popup menu
			self.CreatePopupMenuS()
			btnSize = btn.GetSize()
			btnPt = btn.GetPosition()
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			self._sMenu.SetOwnerHeight(btnSize.y)
			self._sMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)	
		elif btn.Name.startswith('target'):
			# Create the popup menu
			self.CreatePopupMenuT()
			btnSize = btn.GetSize()
			btnPt = btn.GetPosition()
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			self._tMenu.SetOwnerHeight(btnSize.y)
			self._tMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)	
		else:
			assert 1==2, 'btn.Name is not set.'
		
	def CreatePopupMenuS(self):

		if not self._sMenu:
			print 'not self._sMenu'
			self._sMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			
			#dbf={'OR':'Oracle', 'SS':'SQLServer', 'MA':'MariaDB', 'MY': 'MySQL', 'PG':'PostgreSQL', 'DB':'DB2', 'TT':'TimesTen', 'SL':'SQLite', 'IN':'Informix', 'SY':'Sybase'}
			tname=''
			qfile=''
			query=''			
			if self.obj.has_key('from_table'): # or self.obj.has_key('from_table_list'):
				tname=self.obj['from_table'][1].GetValue()
				self.T=True
			if self.obj.has_key('query_sql_file'): # or self.obj.has_key('query_sql_dir'):
				qfile=self.obj['query_sql_file'][1].GetValue()				
				
				if not os.path.isfile(qfile):
					qfile=''
					self.Q=False
				else:
					query=open(qfile,'r').read().strip().strip(';')
					self.Q=True
				
			mitems={0:'Open SQL*Plus'}
			if tname:
				mitems={0:'Open SQL*Plus', 1: 'count(*)', 2:'DESCRIBE %s' % tname}
			if query:
				mitems={0:'Open SQL*Plus', 1: 'count(*)'}

			self.i=0
			if self.T:
				for k,v in mitems.items():
					self.i +=1
					self.recentMenu = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._sMenu, wx.NewId(), v, '', wx.ITEM_NORMAL)
					self._sMenu.AppendItem(menuItem)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSqpMenu,(True,k,tname))
					if k==0 and tname:
						self._sMenu.AppendSeparator()
			elif self.Q:
				for k,v in mitems.items():
					self.i +=1
					self.recentMenu = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._sMenu, wx.NewId(), v, '', wx.ITEM_NORMAL)
					self._sMenu.AppendItem(menuItem)
					
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSqpMenu,(True,k, query))
					if k==0 and tname:
						self._sMenu.AppendSeparator()
			else:
				for k,v in mitems.items():
					self.i +=1
					self.recentMenu = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._sMenu, wx.NewId(), v, '', wx.ITEM_NORMAL)
					self._sMenu.AppendItem(menuItem)
					
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSqpMenu,(True,k, query))
					if k==0 and tname:
						self._sMenu.AppendSeparator()			
						
	def CreatePopupMenuT(self):

		if not self._tMenu:
		
			self._tMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			
			#dbf={'OR':'Oracle', 'SS':'SQLServer', 'MA':'MariaDB', 'MY': 'MySQL', 'PG':'PostgreSQL', 'DB':'DB2', 'TT':'TimesTen', 'SL':'SQLite', 'IN':'Informix', 'SY':'Sybase'}
			tname=''

			if self.obj.has_key('to_table'):
				tname=self.obj['to_table'][1].GetValue()
			self.T=True
			mitems={0:'Open SQL*Plus'}
			if tname:
				mitems={0:'Open SQL*Plus', 1: 'count(*)', 2:'DESCRIBE %s' % tname}
			self.i=0
			#print '-'*20, self.recent
			if self.T:
				for k,v in mitems.items():
					self.i +=1
					self.recentMenu = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self._tMenu, wx.NewId(), v, '', wx.ITEM_NORMAL)
					self._tMenu.AppendItem(menuItem)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSqpMenu,(False,k, tname))
					if k==0 and tname:
						self._tMenu.AppendSeparator()

			
				
					
	def OnSqpMenu(self, event,params):	
		(source, id, tname) = params
		if id==0:
			self.OpenSqlPlus(source)
		if id==1:
			self.OpenCountStar(source, tname)
		if id==2:
			self.OpenDescribe(source, tname)
	def OpenSqlPlus(self, source):
		client_loc=''
		login=''
		
		ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
		title='SQL*Plus/%s' % ts
		#self.hm.local_source_client_home, self.hm.local_target_client_home 
		if source:
			#assert self.obj.has_key('source_client_home')
			client_loc=self.hm.local_source_client_home #self.obj['source_client_home'][1].GetValue()
			assert self.obj.has_key('from_user')
			assert self.obj.has_key('from_passwd')
			assert self.obj.has_key('from_db_name')
			login='%s/%s@%s' % (self.obj['from_user'][1].GetValue(),self.obj['from_passwd'][1].GetValue(),self.obj['from_db_name'][1].GetValue())
			title='%s/source' % title
		else:
			#assert self.obj.has_key('target_client_home')
			assert self.obj.has_key('to_user')
			assert self.obj.has_key('to_passwd')
			assert self.obj.has_key('to_db_name')
			login='%s/%s@%s' % (self.obj['to_user'][1].GetValue(),self.obj['to_passwd'][1].GetValue(),self.obj['to_db_name'][1].GetValue())
			client_loc=self.hm.local_target_client_home  #self.obj['target_client_home'][1].GetValue()
			title='%s/target' % title
		
		cfg=[os.path.join(client_loc,'sqlplus.exe'),login]
		#pprint(cfg)
		#e(0)
		p = Popen(cfg, creationflags=CREATE_NEW_CONSOLE) #stderr=PIPE, stdout=PIPE,

		if 1:
			hwnd=None
			while not hwnd:
				hwnd=self.get_hwnds_for_pid(p.pid)
			
			win32gui.SetWindowText (hwnd[0], title)
								
		window1 = find_window( title )
		(x,y) = self.GetScreenPositionTuple()
		(l,w) =self.GetClientSizeTuple()
		dl,dw= self.GetSize()
		window1.SetWindowPos(0, (x/2,y/2,dl,dw),0)	
		return window1
	def OpenCountStar(self, source, q):
		window1=self.OpenSqlPlus( source)
		q='SELECT COUNT(*) FROM (%s);\n' % q
		self.send_str( window1, q)
	def OpenDescribe(self, source, q):
		window1=self.OpenSqlPlus( source)
		q='DESCRIBE %s;\n' % q
		self.send_str( window1, q)		
		
	def send_str(self, window, q):		
		window.SetFocus()
		if 1:
			#time.sleep(5)
			for event in keyboard_stream(q):
				#print event
				SendInput(event)
				#time.sleep(0.1)
				rv = ct.windll.user32.SendInput( event )
		
	def get_hwnds_for_pid (self, pid):
		def callback (hwnd, hwnds):
			if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
				_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
				if found_pid == pid:
					hwnds.append (hwnd)
			return True

		hwnds = []
		win32gui.EnumWindows (callback, hwnds)
		#print hwnds
		return hwnds	
	def OnTestConnect(self, evt):
		print 'OnTestConnect'
		
		
		#print r'start "%s" cmd.exe  /k "%s"' % (title, cmd)
		#os.system(r'start "%s" cmd.exe  /k "%s"' % (title, cmd))
		tc = evt.GetEventObject()
		
		#print title
		cmd=None
		title='Connection test'
		spooler=None
		path_to_db_client=None
		
		#print self.hm
		#print self.hm.local_source_client_home, self.hm.local_target_client_home 
		if tc.Name=='source':
			spooler=conf.dbtools['SPOOLER'][self.copy_vector[0]]
			path_to_db_client=self.hm.local_source_client_home #self.obj['source_client_home'][1].GetValue()
			title='%s (%s) connection test.' % (conf.dbs[self.copy_vector[0]],tc.Name)
			tspooler=os.path.join(path_to_db_client,spooler )
			cmd=r"'%s' %s/%s@%s @'%s'" % (
			tspooler, #spooler location
			self.obj['from_user'][1].GetValue(), #db user
			self.obj['from_passwd'][1].GetValue(), #pwd
			self.obj['from_db_name'][1].GetValue(), #pwd
			self.tfile[tc.Name]
			)
			#print cmd
		if tc.Name=='target':
			spooler=conf.dbtools['SPOOLER'][self.copy_vector[1]]
			path_to_db_client=self.hm.local_target_client_home #self.obj['target_client_home'][1].GetValue()
			title='%s (%s) connection test.' % (conf.dbs[self.copy_vector[1]],tc.Name)
			tspooler=os.path.join(path_to_db_client,spooler )
			cmd=r"'%s' %s/%s@%s @'%s'" % (
			tspooler, #spooler location
			self.obj['to_user'][1].GetValue(), #db user
			self.obj['to_passwd'][1].GetValue(), #pwd
			self.obj['to_db_name'][1].GetValue(), #pwd
			self.tfile[tc.Name]
			)
		#print cmd
		assert cmd, 'command is not set'
		if not os.path.isfile(os.path.join(path_to_db_client,spooler)):
			self.parent.Warn('"%s" does not exists at "%s".' % (spooler,path_to_db_client))
		else:
			#evt.Skip()
			#cmd=r'cmd.exe  /k %s' % ( cmd)
			#cmd=r'%s' % ( cmd)
			#print cmd
			
			cfg=[]
			if 1:
				import shlex 
				#cmd2=''.join(cmd.split('^\n'))
				#print cmd
				cfg=shlex.split(cmd)
				#pprint(cfg)
			if 1:
				#pprint(cfg)
				p = Popen(cfg, creationflags=CREATE_NEW_CONSOLE)
			hwnd=None
			while not hwnd:
				hwnd=self.get_hwnds_for_pid(p.pid)
			#print hwnd
			#pprint(dir(win32gui))
			win32gui.SetWindowText (hwnd[0], title)
			

			(x,y) = self.parent.GetScreenPositionTuple()
			(l,w) =self.parent.GetClientSizeTuple()
			dl,dw= self.parent.GetSize()
			#print dl,dw
			tc.Enable(False)
			if tc.Name=='source':
				#print x+(l-dl)/2, y+(w-dw)/2, dl,dw
				#self.SetDimensions(x+(l-dl)/2, y+(w-dw)/2, dl,dw)
				win32gui.SetWindowPos (hwnd[0],  0, x/2,y/2, 750, 400, 0)
				#self.src_p=p
				#self.src_btn=tc
				#self.timers={}
				#self.counters={}
				#self.th={}
				#self.the_id=None
				the_id=self.the_id[0]
				self.parent.btn[the_id]=tc
				sn=self.parent.getSessionName()
				self.parent.p[the_id]=p
				#self.parent.q.append([sn,self.the_id])
				btn=None
				#if tc:
				#	btn=tc
				#self.parent.Bind(wx.EVT_TIMER, lambda event, i=the_id: self.parent.th[the_id] (event, the_id), id=the_id)
				self.parent.timers[the_id].Start(1000)
			if tc.Name=='target':
				#print x+(l-dl)/2, y+(w-dw)/2, dl,dw
				#self.SetDimensions(x+(l-dl)/2, y+(w-dw)/2, dl,dw)
				win32gui.SetWindowPos (hwnd[0],  0, x+l/2,y/2, 750, 400, 0)		
				#win32gui.SetWindowPos (hwnd[0],  win32con.HWND_TOPMOST,500,100, 750, 400, 0)
				#self.src_p=p
				#self.src_btn=tc
				#self.timers={}
				#self.counters={}
				#self.th={}
				#self.the_id=None
				the_id=self.the_id[1]
				self.parent.btn[the_id]=tc
				sn=self.parent.getSessionName()
				self.parent.p[the_id]=p
				#self.parent.q.append([sn,self.the_id])
				#win32gui.ShowWindow(firefox[0], win32con.SW_MINIMIZE)
				btn=None
				#if tc:
				#	btn=tc
				#self.parent.Bind(wx.EVT_TIMER, lambda event, i=the_id: self.parent.th[the_id] (event, the_id), id=the_id)
				self.parent.timers[the_id].Start(1000)

	
			#self.timer.Stop()
			
			#send('close_exec', p)
			#wnd = subprocess.Popen ([cmd], shell=True)
		
	def get_hwnds_for_pid (self, pid):
		def callback (hwnd, hwnds):
			if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
				_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
				if found_pid == pid:
					hwnds.append (hwnd)
			return True

		hwnds = []
		win32gui.EnumWindows (callback, hwnds)
		#print hwnds
		return hwnds
	def close_exec(self,p):

		if 1:
			#import subprocess
			#import time
			#notepad = subprocess.Popen ([r"notepad.exe"])
			#
			# sleep to give the window time to appear
			#
			#time.sleep (5)

			for hwnd in self.get_hwnds_for_pid (p.pid):
				#print hwnd, "=>", win32gui.GetWindowText (hwnd)
				#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
				win32gui.SendMessage (hwnd, win32con.WM_CLOSE, 0, 0)	
		
	def OnDirButton(self, event):
		print 'OnDirButton'
	def onKeyPress(self, event):
		#print 'pnl onKeyPress'
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()	
			if kc == 19:
				print 'Ctrl-S'
				send('save_args',())				
				#self.Save()
			if	kc == 4:
				print 'Ctrl-D 2'
				self.parent.tryToDelete()
		else:		
			if kc<123: #not (kc = wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.parent.btn_save.Enable(True)
				#self.parent.changed=True
				if not tc.Name in self.parent.changed:
					self.parent.changed.append(tc.Name)		
		event.Skip()
		#return

			
	def ClearAll(self):
		for k in self.obj:
			if k not in self.disabled:
				if  self.obj.has_key(k):
					self.obj[k][1].SetValue('')
	def DisableAll(self):
		for k in self.obj:
			if k not in self.disabled:
				for i in range(len( self.obj[k])):
					if  self.obj.has_key(k):
						self.obj[k][i].Enable(False)
		self.disableSqlLoaderButtons()
	def EnableAll(self):
		for k in self.obj:
			if k not in self.disabled and self.checks[k].GetValue():
				for i in range(len( self.obj[k])):
					if  self.obj.has_key(k):
						self.obj[k][i].Enable(True)		
	def getArgs(self):
		#print 'getArgs'
		#print len(self.cargs)
		for k in self.cargs:
			assert self.obj.has_key(k), 'cargs "%s" is not set' % k
			val=self.obj[k][1].GetValue().strip()
			self.cargs[k]=list(self.cargs[k])
			if str(self.cargs[k][2]).strip('"') not in [val]:
				#print 'cargs "%s" value changed' % k, str(self.cargs[k][2]),'-->' ,val
				self.cargs[k][2]=val
			#,self.fargs,self.targs=self.args
		for k in self.fargs:
			assert self.obj.has_key(k), 'fargs "%s" is not set' % k
			val=self.obj[k][1].GetValue().strip()
			#print self.fargs[k]
			self.fargs[k]=list(self.fargs[k])
			#if k in ['from_passwd']:
			#	#base64.b64decode("cGFzc3dvcmQ=")
			#	self.targs[k][2]=base64.b64encode(val)
			if 1: #else:
				#print val, k
				#print self.fargs[k][2].strip('"')
				#print val
				#e(0)
				if str(self.fargs[k][2]).strip('"') not in [val]:
					#print 'fargs "%s" value changed' % k, str(self.fargs[k][2]),'-->' ,val
					self.fargs[k][2]=val		
		for k in self.targs:
			assert self.obj.has_key(k), 'targs "%s" is not set' % k
			val=self.obj[k][1].GetValue().strip()
			self.targs[k]=list(self.targs[k])
			#if k in ['to_passwd']:
			#	#import base64
			#	self.targs[k][2]=base64.b64encode(val)
			if 1: #else:			
				if str(self.targs[k][2]).strip('"') not in [val]:
					#print 'targs "%s" value changed' % k, str(self.targs[k][2]),'-->' ,val
					self.targs[k][2]=val
		#save to file
		#print len(self.cargs)
		return [self.cargs, self.fargs, self.targs]
	def OnPwdFocus (self, evt):
		#print 'OnPwdFocus'
		#(objArr)=params
		#print 'OnPwdFocus'
		tc = evt.GetEventObject()
		#print tc.Name
		#print self.obj[tc.Name][1].GetValue()
		self.obj[tc.Name][1]=tc
		evt.Skip()
		
	def OnPassword(self, evt,params):
		#print 'OnPassword'
		[flip] =params

		for tc in flip:
			#print tc
			if tc.IsShown():
				[a,b]=flip
				if tc==flip[0]:
					if a.GetValue()<>b.GetValue():
						b.SetValue(a.GetValue())
				else:
					if a.GetValue()<>b.GetValue():
						a.SetValue(b.GetValue())
					
				tc.Hide()
			else:
				tc.Show()
		evt.Skip()	
		#pprint(dir(self.src_hide_show[0]))		
	def OnInputDir(self, evt,params):
		print 'OnInputDir'
		[dir_obj,title] = params
		dir =dir_obj.GetValue()
		if 1: #dirtype in ['input_dirs']:
			import wx.lib.agw.multidirdialog as MDD
			dlg = MDD.MultiDirDialog(None, title=title, defaultPath=dir,
							 agwStyle=MDD.DD_MULTIPLE|MDD.DD_DIR_MUST_EXIST)

			if dlg.ShowModal() != wx.ID_OK:
				print("You Cancelled The Dialog!")
				dlg.Destroy()
				return

			paths = dlg.GetPaths()
			#for indx, path in enumerate(paths):
			#	print("Path %d: %s"%(indx+1, path))
			
			dlg.Destroy()
			self.set_dirs(dir_obj, paths)
			#print dir
	def OnSetFile(self, evt, params):
		[file_obj,title] = params
		 
		
		val =file_obj.GetValue()
		fname =os.path.realpath(val)
		dir= os.path.dirname(fname)
	
		dlg = wx.FileDialog(self, title, dir, "",
                                       "*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) #wx.FD_MULTIPLE|
		if dlg.ShowModal() != wx.ID_OK:
			print("You Cancelled The Dialogue!")
			dlg.Destroy()
			return
		files = dlg.GetPaths()
		for indx, path in enumerate(files):
				print("File %d: %s"%(indx+1, path))
		#pprint files
		dlg.Destroy()
		fname=files[0]
		assert os.path.isfile(fname)
		file_obj.SetValue(fname)
		if not file_obj.Name in self.parent.changed:
			self.parent.changed.append(file_obj.Name)
		send('value_changed',())
		send('show_nb_tab',(1,fname))
		
	def OnOutputDir(self, evt,params):
		#print 'OnOutputDir'
		[dir_obj,title] = params
		 
		
		val =dir_obj.GetValue()
		loc =os.path.realpath(val)
		dir= os.path.dirname(loc)
		#print dir
		if 1: #dirtype in ['input_dirs']:
			
			dlg = MDD.MultiDirDialog(None, title=title, defaultPath=dir, agwStyle=MDD.DD_NEW_DIR_BUTTON)

			if dlg.ShowModal() != wx.ID_OK:
				print("You Cancelled The Dialog!")
				dlg.Destroy()
				return

			paths = dlg.GetPaths()
			#for indx, path in enumerate(paths):
			#	print("Path %d: %s"%(indx+1, path))
			
			dlg.Destroy()
			self.set_dirs(dir_obj, paths)
			#print paths			
	def OnInputFiles_del(self, evt,params):
		#print 'OnInputDir'
		[dir_obj,dir] = params
		if 1: #dirtype in ['input_dirs']:
			import wx.lib.agw.multidirdialog as MDD
			dlg = MDD.MultiFileDialog(None, title="Choose CVS files:", defaultPath=dir,
							 agwStyle=MDD.DD_MULTIPLE|MDD.DD_DIR_MUST_EXIST)

			if dlg.ShowModal() != wx.ID_OK:
				print("You Cancelled The Dialog!")
				dlg.Destroy()
				return

			paths = dlg.GetPaths()
			#for indx, path in enumerate(paths):
			#	print("Path %d: %s"%(indx+1, path))
			
			dlg.Destroy()
			self.set_dirs(dir_obj, paths)
			#print dir
		#OnQuerySqlFile	
	def OnQuerySqlFile(self, evt,params):
		#print 'OnQuerySqlFile'
		[file_obj,dir] = params
		dlg = wx.FileDialog(self, "Choose SQL file", dir, "",
                                       "*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) #wx.FD_MULTIPLE|
		if dlg.ShowModal() != wx.ID_OK:
			print("You Cancelled The Dialogue!")
			dlg.Destroy()
			return
		files = dlg.GetPaths()
		for indx, path in enumerate(files):
				print("File %d: %s"%(indx+1, path))
		#pprint files
		dlg.Destroy()
		self.set_files(file_obj, files)

		
	def OnInputFiles(self, evt,params):
		#print 'OnInputDir'
		[files_obj] = params
		files=files_obj.GetValue()
		dirname=os.path.dirname(files.split(';')[0])
		dlg = wx.FileDialog(self, "Choose input CSV files", dirname, "",
                                       "*.*", wx.FD_OPEN | wx.FD_MULTIPLE|wx.FD_FILE_MUST_EXIST)
		if dlg.ShowModal() != wx.ID_OK:
			print("You Cancelled The Dialogue!")
			dlg.Destroy()
			return
		files = dlg.GetPaths()
		for indx, path in enumerate(files):
				print("File %d: %s"%(indx+1, path))
		#pprint files
		dlg.Destroy()
		self.set_files(files_obj, files)
			
	def OnShowOutputFile(self, evt,params):
		#print 'OnOutputFile'
		[file_obj] = params
		file_loc= file_obj.GetValue()
		if not os.path.isfile(file_loc):
			msg='Output file\n%s\ndoes not exists.' % file_loc
			self.parent.Warn(msg)
		else:
			#print 'exists'
			#file_loc 
			self.parent.ShowLocation(file_loc)
			
	def OnShowOutputDir(self, evt,params):
		#print 'OnOutputFile'
		[dir_obj] = params
		dir_loc= dir_obj.GetValue()
		if not os.path.isdir(dir_loc):
			msg='Output dir\n%s\ndoes not exists.' % dir_loc
			self.parent.Warn(msg)
		else:
			#print 'exists'
			#file_loc 
			self.parent.ShowLocation(dir_loc)
			
	def OnOutputFile(self, evt,params):
		#print 'OnInputDir'
		[file_obj] = params
		dir=os.path.dirname(file_obj.GetValue())
		dlg = wx.FileDialog(self, "Choose output CSV file", dir, "",
                                       "*.*", wx.FD_OPEN)
		if dlg.ShowModal() != wx.ID_OK:
			print("You Cancelled The Dialogue!")
			dlg.Destroy()
			return
		file = dlg.GetPath()
		dlg.Destroy()
		file_obj.SetValue(file)	
	def set_files(self, file_obj, files):
		path=[]
		#clean-up
		for file in files:
			if file.startswith('OS '):
				path.append(file.strip('OS ').replace('(','').replace(')',''))
			else:
				path.append(file)
		
		file_obj.SetValue(';'.join(path))
	def set_dirs(self, dir_obj, dirs):
		#print 'set_dirs'
		path=[]
		#clean-up
		for dir in dirs:
			split_test=os.path.splitdrive(dir)
			#pprint (split_test)
			if not split_test[0]: #mailformed path
				sp=split_test[1].split(':)\\')
				#print sp
				newdir='\\'.join(['%s:' % sp[0].split(' ')[-1].strip('('),sp[1]])
				#print newdir
				path.append(newdir)
			else:
				path.append(dir)
			#if dir.startswith('OS '):
			#	path.append(dir.strip('OS ').replace('(','').replace(')',''))
			#else:
			#	path.append(dir)
		
		dir_obj.SetValue(';'.join(path))
		
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
		
	def get_cmd(self,transport):
		cmd=self.get_cmd_line_new(transport, passwords=False)
		lexer=shlex.shlex(cmd)
		lexer.quotes = '"'
		lexer.whitespace_split = True
		lexer.commenters = ''
		cfg = list(lexer)
		out=['%s ^' % cfg[0]]
		for i in xrange(1,len(cfg),2):
			#print i,cfg[i],cfg[i+1]
			#print cfg[i]
			out.append('%s %s ^' % (cfg[i],cfg[i+1]))
		return ('\n'.join(out)).strip('^')

	def get_cmd_line(self,transport):
		cmd='%s' % transport #'python  C:\Python27\data_migrator_1239\datamule.py' #
		for k, v in sorted(self.cargs.items()):
			#print k,v
			short,long,val,desc=v
			cmd='%s %s "%s"' % (cmd, short,self.obj[k][1].GetValue().strip())
		for k, v in sorted(self.fargs.items()):
			#print k,v
			short,long,val,desc=v
			val=self.obj[k][1].GetValue().strip()
			if 0 and 'passwd' in long: 
				val= base64.b64decode(val)
			cmd='%s %s "%s"' % (cmd, short,val)
			#print cmd
		for k, v in sorted(self.targs.items()):
			#print k,v
			short,long,val,tesc=v
			val=self.obj[k][1].GetValue().strip()
			if 0 and 'passwd' in long: 
				#pprint (val)
				val= base64.b64decode(val)
			cmd='%s %s "%s"' % (cmd, short,val)			
		return cmd
	def get_cmd_line_new(self,transport, passwords=True):
		cmd='%s' % transport #'python  C:\Python27\data_migrator_1239\datamule.py' #
		for k, v in self.cargs.items():
			#print k, self.parent.if_send_email()
			#print k,v
			short,long,val,desc=v
			value=self.obj[k][1].GetValue().strip()
			#if not value.isdigit() and short not in ['-w']:
			#	value='"%s"' % value
			if value and value.strip('"') and value.strip(' ') :
				#print long, long.strip('--') in ['email_to'] and self.parent.if_send_email()
				if long.strip('--') in ['email_to']:
					if self.parent.if_send_email():
						cmd=r'%s %s %s' % (cmd, short,value)
				else:
					cmd=r'%s %s %s' % (cmd, short,value)
		#print cmd
		filter=[]
		if not passwords:
			filter=['to_passwd', 'from_passwd']
		keys =[k for k in self.fargs.keys() if k not in filter]
		for k in keys:
			#print k
			v= self.fargs[k]
			short,long,val,desc=v
			value=self.obj[k][1].GetValue().strip()
			if not value.isdigit() and ' ' in value:
				value='"%s"' % value
			if value and value.strip('"')  and value.strip(' '):
				cmd=r'%s %s %s' % (cmd, short,value)
		filter=[]
		if not passwords:
			filter=['to_passwd', 'from_passwd']
		keys =[k for k in self.targs.keys() if k not in filter]				
		for k in keys:
			#print k
			v= self.targs[k]
			short,long,val,tesc=v
			value=self.obj[k][1].GetValue().strip()
			if (not value.isdigit() and ' ' in value):
				value='"%s"' % value
			if value and value.strip('"')  and value.strip(' '):
				cmd=r'%s %s %s' % (cmd, short,value)			
		return cmd	
		
class DummyStaticText(object): 
	def __init__(self, value, boo=True):		
		self.value=value
		self.enabled=boo
	def SetLabel(self,value):
		self.value=value
	def GetLabel(self):
		return value
	def Enable(self,boo):
		self.enabled=boo
		
class DummyTextControl(object): 
	def __init__(self, value, boo=True):		
		self.value=value
		self.enabled=boo
	def SetValue(self,value):
		self.value=value
	def GetValue(self):
		return self.value
	def Enable(self,boo):
		self.enabled=boo	

maskText = ["Session Name", "C{90}", " ", 'F_', '^[a-zA-Z0-9_]+', '', '', '']
maskLibName = ["Session Name", "C{40}", " ", 'F_', '^[a-zA-Z0-9_]+', '', '', '']
#maskText = ["Session Name", "C{90}", " ", 'F_', '^[a-zA-Z0-9_]+', '', '', '']

########################################################################
class pnl_output(wx.Panel):
	"""
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent, profile_loc, style):
		""""""
		wx.Panel.__init__(self, parent, id=wx.NewId(), style=style)
		self.parent=parent
		self.param={}
		self.Prepare()

	def Prepare(self):
		self.initPanel()

	def getSessionLoc(self):
		session_loc=os.path.join(self.parent.save_to_dir,self.parent.getSessionName(),'loader', self.pname)
		return session_loc
		
	def onKeyPress(self, event):
		
		tc = event.GetEventObject()
		kc = event.GetKeyCode()

		event.Skip()		
	def initPanel(self):

				
		if 0:
			self.sb_sql = wx.StaticBox(self, label="SQL Log")
			self.vbox4 = wx.StaticBoxSizer(self.sb_sql, wx.VERTICAL)
			
			#self.p_sql = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,400), pos=(0,28), style=wx.SIMPLE_BORDER)
			self.p_sql = wx.lib.scrolledpanel.ScrolledPanel(self,-1,  pos=(0,28), style=wx.SIMPLE_BORDER)
			self.p_sql.SetupScrolling()
			self.p_sql.SetBackgroundColour('#FFFFFF')
			self.sql={}	
			self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
		if 0:
			self.sb_data = wx.StaticBox(self, label="Data Spool")
			self.vbox_dump = wx.StaticBoxSizer(self.sb_data, wx.VERTICAL)
			
			#self.p_sql = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(screenWidth,400), pos=(0,28), style=wx.SIMPLE_BORDER)
			self.p_dump = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(397,170), pos=(0,28), )
			self.p_dump.SetupScrolling()
			self.p_dump.SetBackgroundColour('#FFFFFF')
			self.sql={}	
			self.vbox_dump.Add(self.p_dump, flag=wx.LEFT|wx.TOP, border=5)

		self.setOutputArgs()
		self.afgs = wx.GridBagSizer(3, 2)
		self.afgs.Add(self.btnsizer, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
		self.afgs.Add(self.vbox_alog, pos=(0, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
		self.afgs.Add(self.vbox4, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
		self.afgs.Add(self.vbox_dump, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
		self.afgs.Add(self.vbox_ldr, pos=(1, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)		
		self.SetSizer(self.afgs)

				
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
	def setOutputArgs(self):
		args_panel=self.parent.args_panel
		if hasattr(self, 'out') and self.out:
			for o,v in self.out.items():
				#del v
				for c in v:
					if  'BitmapButton' in str(type(c)):
						#print 'out', str(type(c))
						c.Destroy()
						#print(dir(c))
					else:				
						c.Destroy()
		#print ''		
		self.out={}
		if not hasattr(self, 'btnsizer'):
			self.btnsizer = wx.BoxSizer(wx.VERTICAL)
			
		else:
			self.btnsizer.Hide(0)
			self.btnsizer.Remove(0)
		fgs=wx.GridBagSizer(3, 4) 
		length=287
		#fgs={}
		
		log_items={'log_dir':'App Log','default_spool_dir':'Data Spool','sql_log_dir':'SQL log','sqloader_log_dir':'SQL*Loader log'}
		 
		i=0	
		
		
		x='log_dir'
		val=''
		if args_panel.obj.has_key(x):			
			#val=args_panel.obj[x][1].GetValue()
			val=self.parent.getLogDir()
		if 1:
			items={x:val}
			for k,v in items.items():
				#fgs[k] = wx.GridBagSizer(2, 1)
				self.out[k]= [wx.StaticText(self, label=log_items[k]), wx.TextCtrl(self,value=v, size=(length,22))]
				fgs.Add(self.out[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.out[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.out[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.out[k].append(wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if args_panel.obj.has_key(k):
					self.gen_bind(wx.EVT_BUTTON,self.out[k][2], self.OnShowDir,[self.out[k][1]])								
				else:
					self.out[k][2].Enable(False)
				fgs.Add(self.out[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
				i +=1
		x='sql_log_dir'
		val=''
		if args_panel.obj.has_key('log_dir'):			
			#val=args_panel.obj[x][1].GetValue()
			val=os.path.join(self.parent.getLogDir(), 'sql')
		if 1:
			items={x:val}
			for k,v in items.items():
				#fgs[k] = wx.GridBagSizer(2, 1)
				self.out[k]= [wx.StaticText(self, label=log_items[k]), wx.TextCtrl(self,value=v, size=(length,22))]
				fgs.Add(self.out[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.out[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.out[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.out[k].append(wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				#if args_panel.obj.has_key(k):
				self.gen_bind(wx.EVT_BUTTON,self.out[k][2], self.OnShowDir,[self.out[k][1]])								
				#else:
				#self.out[k][2].Enable(False)
				fgs.Add(self.out[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				i +=1			

		x='default_spool_dir'
		val=''
		if args_panel.obj.has_key(x):	
			#val=args_panel.obj[x][1].GetValue()
			val=self.parent.getDumpDir()
		if 1:
			items={x:val}
			#items={'default_spool_dir':'test2'}
			for k,v in items.items():
				#fgs[k] = wx.GridBagSizer(2, 1)
				self.out[k]= [wx.StaticText(self, label=log_items[k]), wx.TextCtrl(self,value=v, size=(length,22))]
				fgs.Add(self.out[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.out[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.out[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.out[k].append(wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				if args_panel.obj.has_key(k):
					self.gen_bind(wx.EVT_BUTTON,self.out[k][2], self.OnShowDir,[self.out[k][1]])							
				else:
					self.out[k][2].Enable(False)
				fgs.Add(self.out[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				i +=1

		if 1:		
			val=''
			if args_panel.obj.has_key('log_dir'):	
				#val=args_panel.obj[x][1].GetValue()
				val=os.path.join(self.parent.getLogDir(), 'sqlloader')
				
			items={'sqloader_log_dir':val}
			for k,v in items.items():
				#fgs[k] = wx.GridBagSizer(2, 1)
				self.out[k]= [wx.StaticText(self, label=log_items[k]), wx.TextCtrl(self,value=v, size=(length,22))]
				fgs.Add(self.out[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.out[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.out[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
				imageFile = os.path.join(home,"images/folder_icon_16.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.out[k].append(wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
				#if args_panel.obj.has_key(k):
				self.gen_bind(wx.EVT_BUTTON,self.out[k][2], self.OnShowDir,[self.out[k][1]])				
				#else:
				#self.out[k][2].Enable(False)
				fgs.Add(self.out[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				i +=1
			if 1:
				btn=wx.Button(self, label='Refresh', style=wx.BU_EXACTFIT)	
				#tc[sn]['source'][0]
				btn.SetName('Refresh')
				fgs.Add(wx.StaticText(self, label=''), pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(btn, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				btn.Bind(wx.EVT_BUTTON, self.OnRefreshOutput)	
				i+=1
			self.sb_d3 = wx.StaticBox(self, label="Logs")
			vbox3 = wx.StaticBoxSizer(self.sb_d3, wx.VERTICAL)
			vbox3.Add(fgs, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			self.btnsizer.Add(vbox3, flag=wx.LEFT|wx.TOP, border=0)
			
		if 1: #App log
			length=255
			if hasattr(self, 'alog') and self.alog:
				for o,v in self.alog.items():
					#del v
					for c in v:
						if  'BitmapButton' in str(type(c)):
							#print 'alog', str(type(c))
							c.Destroy()
							#print(dir(c))
						else:				
							c.Destroy()
			#print ''
		
			self.alog={}	
			if not hasattr(self, 'vbox_alog'):
				#empty=True
				self.sb_alog = wx.StaticBox(self, label="App log")
				self.vbox_alog = wx.StaticBoxSizer(self.sb_alog, wx.VERTICAL)
			else:
				self.vbox_alog.Hide(0)
				self.vbox_alog.Remove(0)
			
			if 1: #not hasattr(self, 'p_dump'):
				self.p_alog = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(397,133), pos=(0,28)) #, style=wx.SIMPLE_BORDER)
				self.p_alog.SetupScrolling()
				#self.p_sql.SetBackgroundColour('#FFFFFF')
				#bSizer = wx.BoxSizer( wx.VERTICAL )
				self.p_alog.fgs4=wx.GridBagSizer(3, 10)
			
			#self.p_sql.fgs4=wx.GridBagSizer(1, 10)
			#self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
			i=0
			#self.dump={}	
			if args_panel.obj.has_key('log_dir'):
				alogdir=self.parent.getLogDir()
				if os.path.isdir(alogdir):
					files=[d for d in os.listdir(alogdir) if os.path.isfile(os.path.join(alogdir,d))]
					for k in files:
						#print k
						lbl=''
						if 1:
							lbl='Log file'
						self.alog[k]= [wx.StaticText(self.p_alog, label=lbl), wx.TextCtrl(self.p_alog,value=k,pos=(60,i*20), size=(length,22))]
						self.p_alog.fgs4.Add(self.alog[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.p_alog.fgs4.Add(self.alog[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.alog[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
						
						imageFile = os.path.join(home,"images/editor_icon_16_2.png")
						image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
						self.alog[k].append(wx.BitmapButton(self.p_alog, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
						self.p_alog.fgs4.Add(self.alog[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.gen_bind(wx.EVT_BUTTON,self.alog[k][2], self.OnEditSqlFile,[os.path.join(alogdir,k)])
								
						
						i +=1
						#self.p_sql.SetSizer( bSizer )
						self.p_alog.SetSizer( self.p_alog.fgs4 )
			self.vbox_alog.Add(self.p_alog, flag=wx.LEFT|wx.TOP, border=5)
			#self.tc_sloc.SetValue(self.getSessionLoc())
			#self.tc_sloc.SetSize((len(self.profile_loc)*5.5,23))
			#self.btnsizer.Layout()
			self.vbox_alog.Layout()
			#self.h_sizer.Layout()
			
				
		if 1:
			if hasattr(self, 'sql') and self.sql:
				for o,v in self.sql.items():
					#del v
					for c in v:
						if  'BitmapButton' in str(type(c)):
							#print 'sql', str(type(c))
							c.Destroy()
							#print(dir(c))
						else:				
							c.Destroy()		
			self.sql={}	
			length=255
			#self.obj={}
			if not hasattr(self, 'vbox4'):
				self.sb_sql = wx.StaticBox(self, label="SQL Log")
				self.vbox4 = wx.StaticBoxSizer(self.sb_sql, wx.VERTICAL)
			else:
				self.vbox4.Hide(0)
				self.vbox4.Remove(0)
				
			if 1: #not hasattr(self, 'p_sql'):
				self.p_sql = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(397,205), pos=(0,28)) #, style=wx.SIMPLE_BORDER)
				self.p_sql.SetupScrolling()
				#self.p_sql.SetBackgroundColour('#FFFFFF')
				#bSizer = wx.BoxSizer( wx.VERTICAL )
				self.p_sql.fgs4=wx.GridBagSizer(3, 10)
			
			#self.p_sql.fgs4=wx.GridBagSizer(1, 10)
			#self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
			i=0		
			#print 'profile:',self.profile_loc
			
			if self.parent.args_panel.obj.has_key('log_dir'):
				#e(0)
				sqldir=os.path.join(self.parent.getLogDir(),'sql')	
				
				if os.path.isdir(sqldir):
					files=[d for d in os.listdir(sqldir) if os.path.isfile(os.path.join(sqldir,d))]
					for k in files:
						#print k
						lbl=''
						if 'query_columns' in k:
							lbl='Query columns'
						elif 'table_columns' in k:
							lbl='Table columns'
						elif 'table_spool' in k:
							lbl='Table spool'						
						elif 'truncate_partition' in k:
							lbl='Truncate part'
						elif 'truncate_sub_partition' in k:
							lbl='Truncate sub-part'
						elif 'truncate_table' in k:
							lbl='Truncate table'						
						elif 'query_spool' in k:
							
							#print k
							regexp1=re.compile(r'.*_(\d+)\.sql')
							m= re.match(regexp1, k)
							sid=''
							#print sid
							if m:
								lbl='Query spool (%s)' % m.groups()[0]
						else:						
							#print k
							regexp1=re.compile(r'.*\.(\d+)\.sql')
							m= re.match(regexp1, k)
							sid=''
							#print sid
							if m:
								lbl='Data load (%s)' % m.groups()[0]
						self.sql[k]= [wx.StaticText(self.p_sql, label=lbl), wx.TextCtrl(self.p_sql,value=k,pos=(60,i*20), size=(length,22))]
						self.p_sql.fgs4.Add(self.sql[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.p_sql.fgs4.Add(self.sql[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.sql[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
						
						imageFile = os.path.join(home,"images/editor_icon_16_2.png")
						image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
						self.sql[k].append(wx.BitmapButton(self.p_sql, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
						self.p_sql.fgs4.Add(self.sql[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.gen_bind(wx.EVT_BUTTON,self.sql[k][2], self.OnEditSqlFile,[os.path.join(sqldir,k)])
								
						
						i +=1
						#self.p_sql.SetSizer( bSizer )
						self.p_sql.SetSizer( self.p_sql.fgs4 )
			self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
			#self.tc_sloc.SetValue(self.getSessionLoc())
			#self.tc_sloc.SetSize((len(self.profile_loc)*5.5,23))
			#self.btnsizer.Layout()
			self.vbox4.Layout()
			#self.h_sizer.Layout()
					#self.param={}
		if 1:
			length=255
			self.dump={}	
			if not hasattr(self, 'vbox_dump'):
				#empty=True
				self.sb_data = wx.StaticBox(self, label="Data Spool")
				self.vbox_dump = wx.StaticBoxSizer(self.sb_data, wx.VERTICAL)
			else:
				self.vbox_dump.Hide(0)
				self.vbox_dump.Remove(0)
			
			if 1: #not hasattr(self, 'p_dump'):
				self.p_dump = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(397,155), pos=(0,28)) #, style=wx.SIMPLE_BORDER)
				self.p_dump.SetupScrolling()
				#self.p_sql.SetBackgroundColour('#FFFFFF')
				#bSizer = wx.BoxSizer( wx.VERTICAL )
				self.p_dump.fgs4=wx.GridBagSizer(3, 10)
			
			#self.p_sql.fgs4=wx.GridBagSizer(1, 10)
			#self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
			i=0
			if hasattr(self, 'dump') and self.dump:
				for o,v in self.dump.items():
					#del v
					for c in v:
						if  'BitmapButton' in str(type(c)):
							#print 'dump', str(type(c))
							c.Destroy()
							#print(dir(c))
						else:				
							c.Destroy()
						
			self.dump={}	
			k='default_spool_dir'
			if args_panel.obj.has_key(k) and args_panel.checks[k].GetValue():
				dumpdir=self.parent.getDumpDir()
				#print args_panel.obj.has_key('default_spool_dir')
				#print dumpdir
				#os.path.isdir(dumpdir):
				files=[d for d in os.listdir(dumpdir) if os.path.isfile(os.path.join(dumpdir,d))]
				for k in files:
					#print k
					lbl=''
					if 1:
						regexp1=re.compile(r'.*_(\d+)\.')
						m= re.match(regexp1, k)
						sid=''
						#print sid
						if m:
							lbl='Query %s' % m.groups()[0]
					self.dump[k]= [wx.StaticText(self.p_dump, label=lbl), wx.TextCtrl(self.p_dump,value=k,pos=(60,i*20), size=(length,22))]
					self.p_dump.fgs4.Add(self.dump[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					self.p_dump.fgs4.Add(self.dump[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					self.dump[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
					
					imageFile = os.path.join(home,"images/editor_icon_16_2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					self.dump[k].append(wx.BitmapButton(self.p_dump, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
					self.p_dump.fgs4.Add(self.dump[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					self.gen_bind(wx.EVT_BUTTON,self.dump[k][2], self.OnEditSqlFile,[os.path.join(dumpdir,k)])
							
					
					i +=1
					#self.p_sql.SetSizer( bSizer )
					self.p_dump.SetSizer( self.p_dump.fgs4 )
			self.vbox_dump.Add(self.p_dump, flag=wx.LEFT|wx.TOP, border=5)
			#self.tc_sloc.SetValue(self.getSessionLoc())
			#self.tc_sloc.SetSize((len(self.profile_loc)*5.5,23))
			#self.btnsizer.Layout()
			self.vbox_dump.Layout()
			#self.h_sizer.Layout()
		if 1: #SQL*Loader log
			length=255
			if hasattr(self, 'ldr') and self.ldr:
				for o,v in self.ldr.items():
					#del v
					for c in v:
						if  'BitmapButton' in str(type(c)):
							#print 'ldr', str(type(c))
							c.Destroy()
							#print(dir(c))
						else:				
							c.Destroy()			
			self.ldr={}	
			if not hasattr(self, 'vbox_ldr'):
				#empty=True
				self.sb_ldr = wx.StaticBox(self, label="SQL*Loader log")
				self.vbox_ldr = wx.StaticBoxSizer(self.sb_ldr, wx.VERTICAL)
			else:
				self.vbox_ldr.Hide(0)
				self.vbox_ldr.Remove(0)
			
			if 1: #not hasattr(self, 'p_dump'):
				self.p_ldr = wx.lib.scrolledpanel.ScrolledPanel(self,-1, size=(397,205), pos=(0,28)) #, style=wx.SIMPLE_BORDER)
				self.p_ldr.SetupScrolling()
				#self.p_sql.SetBackgroundColour('#FFFFFF')
				#bSizer = wx.BoxSizer( wx.VERTICAL )
				self.p_ldr.fgs4=wx.GridBagSizer(3, 10)
			
			#self.p_sql.fgs4=wx.GridBagSizer(1, 10)
			#self.vbox4.Add(self.p_sql, flag=wx.LEFT|wx.TOP, border=5)
			i=0
			#self.dump={}	
			if args_panel.obj.has_key('log_dir'):
				ldrdir=os.path.join(self.parent.getLogDir(), 'sqlloader')
				if os.path.isdir(ldrdir):
					files=[d for d in os.listdir(ldrdir) if os.path.isfile(os.path.join(ldrdir,d))]
					for k in files:
						#print k
						lbl=''
						if 1:
							regexp1=re.compile(r'.*(\d+)\.(\w+)')
							m= re.match(regexp1, k)
							sid=''
							#print sid
							if m:
								lbl='%s (%s)' % (m.groups()[1], m.groups()[0])
						self.ldr[k]= [wx.StaticText(self.p_ldr, label=lbl), wx.TextCtrl(self.p_ldr,value=k,pos=(60,i*20), size=(length,22))]
						self.p_ldr.fgs4.Add(self.ldr[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.p_ldr.fgs4.Add(self.ldr[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.ldr[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
						
						imageFile = os.path.join(home,"images/editor_icon_16_2.png")
						image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
						self.ldr[k].append(wx.BitmapButton(self.p_ldr, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
						self.p_ldr.fgs4.Add(self.ldr[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
						self.gen_bind(wx.EVT_BUTTON,self.ldr[k][2], self.OnEditSqlFile,[os.path.join(ldrdir,k)])
								
						
						i +=1
						#self.p_sql.SetSizer( bSizer )
						self.p_ldr.SetSizer( self.p_ldr.fgs4 )
			self.vbox_ldr.Add(self.p_ldr, flag=wx.LEFT|wx.TOP, border=5)
			#self.tc_sloc.SetValue(self.getSessionLoc())
			#self.tc_sloc.SetSize((len(self.profile_loc)*5.5,23))
			#self.btnsizer.Layout()
			self.vbox_ldr.Layout()
			#self.h_sizer.Layout()
			
		if hasattr(self, 'afgs'):
			
			#self.afgs.Refresh()
			self.afgs.Layout()
			#OnRefreshOutput
	def OnRefreshOutput(self, evt):
		self.setOutputArgs()
	def OnShowDir(self, evt,params):
		#print 'OnShowDir'
		[dir_obj] = params
		dir_loc= dir_obj.GetValue()
		if not os.path.isdir(dir_loc):
			msg='Output dir\n%s\ndoes not exists.' % dir_loc
			self.parent.Warn(msg)
		else:
			#print 'exists'
			#file_loc 
			self.parent.ShowLocation(dir_loc)
			
	def OnEditSqlFile(self, evt,params):
		#print 'OnEditSqlFile'		
		(file_loc,) = params
		#print file_loc
		#val =file_obj.GetValue()
		#print val
		#import os
		os.chdir(home)
		fname =os.path.realpath(file_loc)
		#print fname
		assert os.path.isfile(fname), 'File does not exists\n%s' % fname
		#webbrowser.open(fname)
		
		os.startfile(fname)
		
	def setOutputArgs2(self):		
		#print str(self.__class__) + ' - setOutputArgs'
		items= ['log_dir','default_spool_dir']
		for x in items:
			val=''
			
			args_panel=self.parent.args_panel
			if args_panel.obj.has_key(x):
				if x in ['default_spool_dir']:
					val=self.parent.getDumpDir()
				elif x in ['log_dir']:
					val=self.parent.getLogDir()
			self.out[x][1].SetValue(val)
			if os.path.isdir(val):
				self.out[x][1].Enable(True)
			else:
				self.out[x][1].Enable(False)
		
		val=os.path.join(self.parent.getLogDir(),'sql')
		x='sql_log_dir'
		self.out[x][1].SetValue(val)
		#args_panel=self.parent.args_panel
		
		
		val=os.path.join(self.parent.getLogDir(),'sqlloader')
		x='sqloader_log_dir'
		args_panel=self.parent.args_panel
		self.out[x][1].SetValue(val)	
		sqldir=os.path.join(self.parent.getLogDir(),'sql')		
		if 1:
			#self.param={}
			length=220
			#self.obj={}
			if not hasattr(self, 'vbox4'):
				empty=True
				self.vbox4 = wx.BoxSizer(wx.VERTICAL)
			if hasattr(self, 'fgs4'):
				#for c in panel.fgs.GetChildren():
				#	print c.Destroy()
				#panel.fgs.Destroy()
				self.vbox4.Hide(0)
				self.vbox4.Remove(0)
			else:
				self.fgs4=wx.GridBagSizer(1, 10) 
			i=0		
			#print 'profile:',self.profile_loc
			if os.path.isdir(sqldir):
				files=[d for d in os.listdir(sqldir) if os.path.isfile(os.path.join(sqldir,d))]
				for k in files:
					#print k
					lbl=''
					if 'query_columns' in k:
						lbl='Query columns'
					elif 'table_columns' in k:
						lbl='Table columns'
					elif 'table_spool' in k:
						lbl='Table spool'						
					elif 'truncate_partition' in k:
						lbl='Truncate partition'
					elif 'truncate_sub_partition' in k:
						lbl='Truncate sub-partition'
					elif 'truncate_table' in k:
						lbl='Truncate table'						
					elif 'query_spool' in k:
						
						#print k
						regexp1=re.compile(r'.*_(\d+)\.sql')
						m= re.match(regexp1, k)
						sid=''
						#print sid
						if m:
							lbl='Query spool (Shard-%s)' % m.groups()[0]
					else:						
						#print k
						regexp1=re.compile(r'.*\.(\d+)\.sql')
						m= re.match(regexp1, k)
						sid=''
						#print sid
						if m:
							lbl='Data load (Shard-%s)' % m.groups()[0]
							
					self.sql[k]= [wx.StaticText(self, label=lbl), wx.TextCtrl(self,value=k, size=(length,22))]
					self.fgs4.Add(self.sql[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					self.fgs4.Add(self.sql[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
					self.sql[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
					i +=1
			self.vbox4.Add(self.fgs4, flag=wx.LEFT|wx.TOP, border=5)
			#self.tc_sloc.SetValue(self.getSessionLoc())
			#self.tc_sloc.SetSize((len(self.profile_loc)*5.5,23))
			#self.btnsizer.Layout()
			self.vbox4.Layout()
			self.h_sizer.Layout()			

########################################################################
class etl_file(object):
	"""
	Editor config
  
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent):
		""""""
		#wx.Panel.__init__(self, parent, id=wx.NewId(), style=style)
		self.parent=parent
		#self.frame=frame
		self.etl_name=['job_pre_etl', 'job_post_etl', 'thread_pre_etl', 'thread_post_etl']
		#print self.args_panel.obj.keys()
		self.etl_file_loc={}

		self.changed=False
		#self.etlname={}
		default_etl=self.etl_name[0]
		self.etl_file_name={x:'%s.py' % x for x in self.etl_name}		
		self.default_etl_file_loc={x:os.path.join(transport_home,  os.path.join('config','etl',self.etl_file_name[x])) for x in self.etl_name}
		#self.etl_loc={}
		self.etl={}
		#self.changed=False
		self.etl_loc={}		
		self.Prepare()
		#sub(self.onValueChanged, "value_changed")

	def Prepare(self):
		#e(0)
		self.SetEtlEditor()
		self.initEtlEditor()
		#self.initPanel()
		
	def SetEtlEditor(self):
		self.etl_loc={}
		self.etl_file_loc={}
		if 1:
			 #{x:None for x in k}
			for k in self.etl_name:
				if self.parent.args_panel.obj.has_key(k):			
					self.etl_file_loc[k]=self.parent.args_panel.obj[k][1].GetValue().strip()
		#pprint (self.etl_file_loc)
		#e(0)
		for k in self.etl_name:
			if not self.etl_file_loc.has_key(k):
				if os.path.isfile(self.default_etl_file_loc[k]):
					self.etl_loc[k] = self.default_etl_file_loc[k]
					#print 'default etl file'
			else:
				
				if self.etl_file_loc[k].startswith('.'):
					#print self.etl_file_loc[k]
					os.chdir(home)
					tmpl_loc=os.path.realpath(self.etl_file_loc[k])
					assert os.path.isfile(tmpl_loc), 'JOB-PRE-ETL template is missing\n%s' % tmpl_loc
					self.etl_loc[k]= tmpl_loc
					#print 'template etl file'
					#e(0)
				else:
					if not os.path.isfile(self.etl_file_loc[k]):
						self.etl_loc[k] = self.default_etl_file_loc[k]
						#print 'test etl file, session file missing'
				#self.etl_loc[k]= os.path.join(home,self.etl_file_loc[k])
				#print self.etl_loc[k]
				#print 'test etl file'

	def initEtlEditor(self):	
		#print 'initEtlEditor'
		#pprint(self.etl_loc)
		for k in self.etl_name:
			session_loc=self.getSessionEtlFileLoc(k)
			dn=os.path.dirname(session_loc)
			#print dn
			#print self.etl_loc
			#e(0)
			
			if not os.path.isdir(dn):
				os.makedirs(dn)
			if not os.path.isfile(session_loc):
				self.etl_loc[k]=self.CreateNewSessionEtlFile(self.etl_loc[k],k)
			else: 
				self.etl_loc[k]=session_loc
			
			#print self.etl[k]
			send('set_etl_editor_profile', (self.etl_loc[k],k))
	def getSessionEtlFileLoc(self,k):
		session_loc=os.path.join(self.parent.save_to_dir,self.parent.getSessionName(),'etl', self.etl_file_name[k])
		return session_loc
	def CreateNewSessionEtlFile(self, etl_loc,k ): 
		session_loc=self.getSessionEtlFileLoc(k)
		if os.path.isfile(session_loc):
			#print 'session file exists'
			pass
		else:			
			#print profile_loc
			#print session_loc
			dir=os.path.dirname(session_loc)
			if not os.path.isdir(dir):
				os.makedirs(dir)
			shutil.copyfile(etl_loc,session_loc)
		return session_loc


	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
	def setEditor(self,etl_name):		
		#e(0)
		#print 'setEditor', etl_name, self.etl_loc
		if not self.etl_loc:
			self.Prepare()
		else:
			self.initEtlEditor()	
		
class MessageBox(wx.Dialog):
    def __init__(self, parent, title):
        wx.Dialog.__init__(self, parent, title=title)
        text = wx.TextCtrl(self, style=wx.TE_READONLY|wx.BORDER_NONE)
        text.SetValue("Hi hi hi")
        text.SetBackgroundColour(wx.SystemSettings.GetColour(4))
        self.ShowModal()
        self.Destroy()

###################################################################################################
class SaveAsDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size, saveas_name='',pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent

		#print defaults
		#pprint(data)
		self._popUpMenu = None
		#self.recent=[]
		pre = wx.PreDialog()
		pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
		pre.Create(parent, ID, title, pos, size, style)
	
		# This next step is the most important, it turns this Python
		# object into the real wrapper of the dialog (instead of pre)
		# as far as the wxPython extension is concerned.
		self.PostCreate(pre)

		# This extra style can be set after the UI object has been created.
		if 'wxMac' in wx.PlatformInfo and useMetal:
			self.SetExtraStyle(wx.DIALOG_EX_METAL)


		# Now continue with the normal construction of the dialog
		# contents
		#self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.userhome = os.path.expanduser('~')
		self.session_dir=session_home		
		self.changed=False
		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(2, 4)			
			
			text1 = wx.StaticText(self, label="Session Name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			#self.tc_sname = wx.TextCtrl(self,size=(400,23))
			self.tc_sname = masked.TextCtrl(self, -1, saveas_name,
										mask         = maskText[1],
										excludeChars = maskText[2],
										formatcodes  = maskText[3],
										includeChars = "_0123456789",
										validRegex   = maskText[4],
										validRange   = maskText[5],
										choices      = maskText[6],
										choiceRequired = False,
										defaultValue = maskText[7])			
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			self.tc_sname.Bind(wx.EVT_CHAR, self.onKeyPress)
			#namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			#icon = wx.StaticBitmap(self, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))
			#namesizer.Add((3,3),0)
			#namesizer.Add(icon, pos=(0, 3), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)
			sizer.Add(namesizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
			st_tlib = wx.StaticText(self, label="Session library:")
			namesizer.Add(st_tlib, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			libs=self.getSessionLibNames()
			#print libs
			#e(0)
			self.cb_tname= wx.ComboBox(self, id=wx.NewId(), value='My_Sessions', choices=libs, size=(100,30), style=0, name='tmpl_lib')
			namesizer.Add(self.cb_tname, pos=(1, 1),  flag=wx.TOP|wx.ALIGN_LEFT|wx.BOTTOM, border=10)

			
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		self.create_btn = wx.Button(self, wx.ID_OK, 'Save')
		self.create_btn.Enable(True)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		#btnsizer.Add(self.test, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((30,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		#self.test.Bind(wx.EVT_BUTTON, self.OnTest)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer(sizer)
			

		self.Layout()
		self.Fit()
		#self.SetSize((-1,size[1]))
	def setDefaultName(self, sname):
		if not self.changed:
			self.tc_sname.SetValue(sname.strip().strip(' ').replace(' ',''))
	def onKeyPress(self, event):
		#print str(self.__class__) + " - onKeyPress"
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()				
			if	kc == 4:
				print 'Ctrl-D 1'
				self.parent.tryToDelete()
		else:
			if kc<123 and not (kc == wx.WXK_SPACE): #(kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.create_btn.Enable(True)
				#self.parent.changed=True
				#print 'changed'
				if not self.changed:
					self.changed=True
		
		event.Skip()
		
		
	def OnTest(self,e):
		[cn, cv, tmpl, args, reuse] = self.getConfig()		
		#print len(args)	
		#pprint(args[2])
		#pprint(self.api_args[tmpl][0])

	def getNewSessionName(self):
		return self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
	def getNewSessionInfo(self):
		return (self.getNewSessionName(),self.cb_tname.GetValue().strip().strip(' '))
	def OnExit(self,e):	
		pass
		e.Skip()

	def OnCreate(self,e):
		#print 'OnCreate'
		
		sname=self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
		if not sname:
			self.Warn('Enter session library name.', 'OnCreate')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(sname):
			self.Warn('Duplicate session library name.', 'OnCreate')
			self.tc_sname.SetFocus()

		else:
		
			#self.writeRecent()
		
			e.Skip()

	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,name):
		dir = os.path.join(self.session_dir, self.getNewSessionName())
		if os.path.isdir(dir):
			return True
		else:
			return False

		

	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)
	def getSessionLibNames(self):
		global session_home
		libs= [d for d in os.listdir(session_home) if os.path.isdir(os.path.join(session_home,d))]
		return libs
###################################################################################################
class SaveAsTemplateDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size, saveas_name='',pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent

		#print defaults
		#pprint(data)
		self._popUpMenu = None
		#self.recent=[]
		pre = wx.PreDialog()
		pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
		pre.Create(parent, ID, title, pos, size, style)
	
		# This next step is the most important, it turns this Python
		# object into the real wrapper of the dialog (instead of pre)
		# as far as the wxPython extension is concerned.
		self.PostCreate(pre)

		# This extra style can be set after the UI object has been created.
		if 'wxMac' in wx.PlatformInfo and useMetal:
			self.SetExtraStyle(wx.DIALOG_EX_METAL)


		# Now continue with the normal construction of the dialog
		# contents
		#self.create_btn = wx.Button(self, wx.ID_OK, 'Create')
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.userhome = os.path.expanduser('~')
		self.session_dir=session_home		
		self.changed=False
		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(2, 4)			
			
			text1 = wx.StaticText(self, label="Template Name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			#self.tc_sname = wx.TextCtrl(self,size=(400,23))
			self.tc_sname = masked.TextCtrl(self, -1, saveas_name,
										mask         = maskText[1],
										excludeChars = maskText[2],
										formatcodes  = maskText[3],
										includeChars = "_0123456789",
										validRegex   = maskText[4],
										validRange   = maskText[5],
										choices      = maskText[6],
										choiceRequired = False,
										defaultValue = maskText[7])			
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			self.tc_sname.Bind(wx.EVT_CHAR, self.onKeyPress)
			#namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			#icon = wx.StaticBitmap(self, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))
			#namesizer.Add((3,3),0)
			#namesizer.Add(icon, pos=(0, 3), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)
			sizer.Add(namesizer, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.EXPAND, 5)
			st_tlib = wx.StaticText(self, label="Template library:")
			namesizer.Add(st_tlib, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			libs=self.getTmplLibNames()
			#print libs
			#e(0)
			self.cb_tname= wx.ComboBox(self, id=wx.NewId(), value='My_Templates', choices=libs, size=(100,30), style=0, name='tmpl_lib')
			namesizer.Add(self.cb_tname, pos=(1, 1),  flag=wx.TOP|wx.ALIGN_LEFT|wx.BOTTOM, border=10)
		 
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		self.create_btn = wx.Button(self, wx.ID_OK, 'Save')
		self.create_btn.Enable(True)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		#btnsizer.Add(self.test, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		#self.test.Bind(wx.EVT_BUTTON, self.OnTest)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)
		
		self.SetSizer(sizer)
			

		self.Layout()
		self.Fit()
		#self.SetSize((-1,size[1]))
	def getTmplLibNames(self):
		#tmpl_home
		libs= [d for d in os.listdir(tmpl_home) if os.path.isdir(os.path.join(tmpl_home,d))]
		return libs
	def setDefaultName(self, sname):
		if not self.changed:
			self.tc_sname.SetValue(sname.strip().strip(' ').replace(' ',''))
	def onKeyPress(self, event):
		#print str(self.__class__) + " - onKeyPress"
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()				
			if	kc == 4:
				print 'Ctrl-D 1'
				self.parent.tryToDelete()
		else:
			if kc<123 and not (kc == wx.WXK_SPACE): #(kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.create_btn.Enable(True)
				#self.parent.changed=True
				#print 'changed'
				if not self.changed:
					self.changed=True
		
		event.Skip()
		
		
	def OnTest(self,e):
		[cn, cv, tmpl, args, reuse] = self.getConfig()		
		#print len(args)	
		#pprint(args[2])
		#pprint(self.api_args[tmpl][0])

	def getTemplateInfo(self):
		tlib=self.cb_tname.GetValue().strip().strip(' ').replace(' ','')
		return (self.tc_sname.GetValue().strip().strip(' ').replace(' ',''), tlib)

	def OnExit(self,e):	
		pass
		e.Skip()

	def OnCreate(self,e):
		#print 'OnCreate'
		
		tname=self.tc_sname.GetValue().strip().strip(' ').replace(' ','')
		tlib=self.cb_tname.GetValue().strip().strip(' ').replace(' ','')
		if not tname:
			self.Warn('Enter session library name.', 'OnCreate')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(tname,tlib):
			self.Warn('Duplicate session library name.', 'OnCreate')
			self.tc_sname.SetFocus()

		else:
		
			#self.writeRecent()
		
			e.Skip()

	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self, tname, tlib):
		dir = os.path.join(tmpl_home, tlib, tname)
		return os.path.isdir(dir)
			

		

	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

		
		
###################################################################################################
class DataBuddy(wx.Frame):
	def __init__(self, parent, id, title, size, aconf):
		global tr,maskText
		#wx.Frame.__init__(self, parent, -1, title)
		#super(DataBuddy, self).__init__(parent, title=title , size=(900, 565))
		global app_title, home
		wx.Frame.__init__(self, None, wx.ID_ANY, title=app_title, size=size)
		self.SetIcon(images.Mondrian.GetIcon())
		wx.SystemOptions_SetOption("msw.remap", "0")
		#self.SetTitle("FlatMenu wxPython Demo ;-D")
		self.aconf=aconf
		#if _hasAUI:
		#	self._mgr = AuiManager()
		#	self._mgr.SetManagedWindow(self)		
		self._vectMenu=None
		#self._popUpMenu = None
		#self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
		#self.splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
		#s=self.splitter
		#self.splitter.SetMinimumPaneSize(50)
		#panel layout
		self.panel_pos=[(0,i) for i in range(3)]
		#print self.panel_pos
		self.panel = wx.Panel(self, size=(935,-1),style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		panel=self.panel
		self.panel.sizer = wx.GridBagSizer(3, 4)
		self.sizer=self.panel.sizer
		self.home=home
		self.sids={}
		self.changed=[]
		self.copy_vector=['','']
		self.tmpl='n/a.n/a'
		self.the_id=[None,None,None]
		self.btn={}
		self.timers={}
		self.counters={}
		self.th={}
		self.btn={}
		self.p={}
		self.hwnd={}
		self.elapsed={}
		self.q={}
		self.s={}
		self.saved=True
		self.default_hm_file=self.get_default_hm_file()
		self.closing_in=6
		(self.cargs,self.fargs,self.targs)=(None, None, None)
		#userhome = os.path.expanduser('~')		
		#self.sess_home=os.path.join(userhome,'sessions')
		self.S=True
		self.bT=False
		self.setLibHome(default_sess_lib)
		#self.save_to_dir=os.path.join(session_home,'My_Sessions')
		#if not os.path.isdir(self.save_to_dir):
		#	os.makedirs(self.save_to_dir)
		platform=__platform__[:2]
		self.transport=os.path.join(self.home,r'%s%s\%s%s.exe' % (tr,platform,tr,platform))
		#self.args_panel =  dummy_args(panel,style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		#path_to_default_session=os.path.join(self.sdir,self.fname)
		#default_session=self.get_session_args(path_to_default_session)
		from include.default_args import default_args
		(self.cargs,self.fargs,self.targs)=default_args
		
		self.nb_tab=0
		self.cmd=''
		self.default_session=None
		
		#self.cmd=self.args_panel.get_cmd(self.transport)
		if 1:
			self.st_session_name = wx.StaticText(panel, label="Session name:")
			self.sizer.Add(self.st_session_name, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			self.session_name=None
			#self.tc_session_name = wx.TextCtrl(panel,value='n/a')
			self.tc_session_name = masked.TextCtrl(panel, -1, "",
										mask         = maskText[1],
										excludeChars = maskText[2],
										formatcodes  = maskText[3],
										includeChars = "_0123456789",
										validRegex   = maskText[4],
										validRange   = maskText[5],
										choices      = maskText[6],
										choiceRequired = False,
										defaultValue = maskText[7])
												
			self.tc_session_name.SetName('session_name')
			self.tc_session_name.Bind(wx.EVT_CHAR, self.onKeyPress)
			self.tc_session_name.Enable(False)
			self.sizer.Add(self.tc_session_name, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			#
			if 1:
				imageFile = os.path.join(home,'images','exec.png')
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				btn = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))			
				self.sizer.Add(btn, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=5)
				btn.Bind(wx.EVT_BUTTON, self.OnMainMenu)
				btn.SetName('menu')
			
			else:
				icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap(os.path.join(home,'images','exec.png')))
				self.sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=5)
		if 0:
			line = wx.StaticLine(panel)
			self.sizer.Add(line, pos=(1, 0), span=(1, 5), 
				flag=wx.EXPAND|wx.BOTTOM, border=0)
		#self.panel1 = wx.Panel(panel, wx.ID_ANY, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		#self.panel1.boxsizer1 =  wx.BoxSizer(wx.HORIZONTAL)
		if 0: #Type
			sb = wx.StaticBox(self.panel1, label='Type')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_type = wx.StaticText(self.panel1, label="n/a")
			boxsizer.Add(self.st_type, flag=wx.LEFT|wx.TOP, border=5)
			self.panel1.boxsizer1.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=5)	
			#sizer.Add(boxsizer, pos=(2, 0),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
		if 0: #Vector
			sb = wx.StaticBox(self.panel1, label='Vector')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_copy_vector = wx.StaticText(self.panel1, label='{:s}'.format('n/a'))
			boxsizer.Add(self.st_copy_vector, flag=wx.LEFT|wx.TOP, border=5)
			self.panel1.boxsizer1.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=5)	
			#sizer.Add(boxsizer, pos=(2, 1),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
		if 0: #Vector
			sb = wx.StaticBox(self.panel1, label='Source template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_sourcet = wx.StaticText(self.panel1, label='n/a')
			boxsizer.Add(self.st_sourcet, flag=wx.LEFT|wx.TOP, border=5)
			self.panel1.boxsizer1.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=5)	
			#sizer.Add(boxsizer, pos=(2, 2),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))	
		if 0: #Vector
			sb = wx.StaticBox(self.panel1, label='Target template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_targett = wx.StaticText(self.panel1, label='{:s}'.format('n/a'))
			boxsizer.Add(self.st_targett, flag=wx.LEFT|wx.TOP, border=5)
			self.panel1.boxsizer1.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=5)	
		#self.panel1.SetSizer(self.panel1.boxsizer1)
		#self.refreshType()
		#self.sizer.Add(self.panel1, pos=(2, 0), span=(1,4),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))				
		#print self.copy_vector
		if 1:
			self.statusbar = self.CreateStatusBar(3, wx.ST_SIZEGRIP)
			#self.statusbar.SetStatusWidths([-3, -3])
			self.statusbar.SetStatusText(os.getcwd(), 0)
			self.statusbar.SetStatusText("Welcome To %s!" % app_title, 1)
			#self.statusbar.SetStatusText('', 2)		
		self.args_panel= pnl_args(self,self.copy_vector,self.tmpl,self.the_id,(self.cargs,self.fargs,self.targs),size=(-1,-1),style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		#self.preetl='not set'
		if 1:
			
			self.nb = fnb.FlatNotebook(panel, -1, agwStyle=fnb.FNB_NO_TAB_FOCUS|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS|fnb.FNB_NODRAG) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
			#print(dir(self.nb))
			self.nb.AddPage(self.args_panel, 'Arguments')
			self.nb.EnableTab(0,False)
			#self.OpenLoaderTab()
			#if self.nb
			k='loader_profile'
			#print self.args_panel.obj.keys()
			loader_profile=None
			if self.args_panel.obj.has_key(k):			
				loader_profile=self.args_panel.obj[k][1].GetValue().strip()
			#print loader_profile
			#e(0)
			self.output_panel = pnl_output(self, loader_profile, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.nb.AddPage(self.output_panel, 'Output' )
			self.nb.EnableTab(1,False)			
			self.nb.SetSelection(self.nb_tab)
			if 0:
				etl_names=['job_pre_etl', 'job_post_etl', 'thread_pre_etl', 'thread_post_etl']
				#print self.args_panel.obj.keys()
				etl_file_loc={} #{x:None for x in k}
				for k in etl_names:
					if self.args_panel.obj.has_key(k):			
						etl_file_loc[k]=self.args_panel.obj[k][1].GetValue().strip()

				#print editor_profile
				
			#self.editor_panel = pnl_editor(self, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.etl_file = etl_file(self)
			#self.nb.AddPage(self.editor_panel, 'JOB-PRE-ETL')	
			#self.nb.EnableTab(2,False)					
			#print(dir(self.nb))
			
			
			#print type(self.nb.GetPage(1))
			self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.onTabChanged, self.nb)
				
			self.sizer.Add(self.nb, pos=(1, 0), span=(1, 4), flag=wx.GROW|wx.EXPAND|wx.ALL, border=0)
		if 1:
			fgs = wx.FlexGridSizer(20, 1)

			#l=[wx.StaticText(panel_from, label="Title"), wx.StaticText(panel_from, label="Author"),wx.StaticText(panel_from, label="Review")]

			#p=[wx.TextCtrl(panel_from), wx.TextCtrl(panel_from), wx.TextCtrl(panel_from)]
			#pprint(dir(fgs))
			self.btn_new=wx.Button(panel, label='New', size=(90,40))
			self.btn_new.Enable(True)
			self.btn_delete=wx.Button(panel, label="Delete", size=(90,40))
			self.btn_delete.Enable(False)
			self.btn_clearall=wx.Button(panel, label="Clear All",size=(60,-1))
			self.btn_clearall.Enable(False)
			self.btn_save=wx.Button(panel, label="Save", size=(60,40))
			self.btn_save.Enable(False)			
			s_sizer =  wx.BoxSizer(wx.HORIZONTAL)	
			if 1:
							
				s_sizer.Add(self.btn_save,0,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=0)
				#self.btn_run.Enable(False)	
				#btn_sqp=wx.Button(panel, label=lbl, style=wx.BU_EXACTFIT)	
				imageFile = os.path.join(home,"images/arrow_down_24.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.save_as = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#tc[sn]['source'][0]
				self.save_as.SetName('save_as')
				self.save_as.Bind(wx.EVT_BUTTON, self.OnSaveAsMenu)
				#tcbox.Add(btn_sqp, flag=wx.LEFT|wx.TOP, border=5)
				s_sizer.Add(self.save_as,0,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=0)
			#self.host_map = wx.Button(panel, label=' ', size=(30,30))
			#self.host_map.Enable(False)
			#hm_sizer.Add(self.host_map,0,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=0)
			#self.sizer.Add(s_sizer, pos=(9, 3), span=(1, 1), flag=wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
			
			#self.btn_log=wx.Button(panel, label="Log")
			#self.btn_log.Enable(False)	
			if 1:
				sb = wx.StaticBox(panel, label='Post-etl Email')

				boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
				self.send_email=wx.CheckBox(panel, label="Send email")
				boxsizer.Add(self.send_email, flag=wx.LEFT|wx.TOP, border=5)
				self.send_email.Bind(wx.EVT_CHECKBOX, self.OnChangeEmailYesNo)
				self.send_email.SetValue(False)		
				
				#print(dir(cb))
				#self.sizer.Add(boxsizer, pos=(4, 0),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
			if 1:
				sb = wx.StaticBox(panel, label='On Run')

				or_boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)

				self.auto_save=wx.CheckBox(panel, label="Auto-save")
				or_boxsizer.Add(self.auto_save, flag=wx.LEFT|wx.TOP, border=5)
				self.auto_save.SetValue(True)
				#self.confirm_run=wx.CheckBox(panel, label='Confirm run')
				#boxsizer.Add(self.confirm_run, flag=wx.LEFT|wx.TOP, border=5)
				#self.confirm_run.SetValue(True)
				
				#print(dir(cb))
				#self.sizer.Add(boxsizer, pos=(4, 1),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)	
			if 1:
				sb = wx.StaticBox(panel, label='Data dump')
				dd_boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
				self.keep_dump=wx.CheckBox(panel, label="Keep")
				self.keep_dump.SetName('keep_data_file')
				dd_boxsizer.Add(self.keep_dump, flag=wx.LEFT|wx.TOP, border=5)
				self.keep_dump.Bind(wx.EVT_CHECKBOX, self.OnKeepDump)
				if self.args_panel.cargs.has_key('keep_data_file') and self.args_panel.cargs['keep_data_file'][2] in ['1']:
					self.keep_dump.SetValue(True)
				else:
					self.keep_dump.SetValue(False)	
				#self.keep_dump.Enable(False)
				if 1:
					self.btn_show_dump = wx.Button(panel, label='Show', size=(36,22))
					self.btn_show_dump.SetName('spool')
					self.btn_show_dump.Bind(wx.EVT_BUTTON, self.onShowDump)
					self.btn_show_dump.Enable(False)
					dd_boxsizer.Add(self.btn_show_dump, flag=wx.LEFT|wx.TOP, border=0)
				
			if 1:
				sb = wx.StaticBox(panel, label='Confirmation')
				c_boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
				self.confirm_run=wx.CheckBox(panel, label="? run")
				c_boxsizer.Add(self.confirm_run, flag=wx.LEFT|wx.TOP, border=5)
				self.confirm_run.SetValue(True)			
				self.confirm_truncate=wx.CheckBox(panel, label="? truncate")
				self.confirm_truncate.SetName('truncate_target')
				c_boxsizer.Add(self.confirm_truncate, flag=wx.LEFT|wx.TOP, border=5)
				#self.confirm_truncate.Bind(wx.EVT_CHECKBOX, self.OnConfirmTruncate)
				self.enableConfirmTruncate()		
			fgs.AddMany([((-1,37),0),(self.btn_new, 0),(self.btn_delete, 0),wx.StaticText(panel, label=' '),(self.btn_clearall, 0),wx.StaticText(panel, label=' \n'),(s_sizer, 0),
			((-1,37),0),(boxsizer,0),(or_boxsizer,0),(dd_boxsizer,0),(c_boxsizer,0),])
			self.btn_new.Bind(wx.EVT_BUTTON, self.OnNewButton)	
			self.btn_delete.Bind(wx.EVT_BUTTON, self.OnDeleteButton)	
			self.btn_clearall.Bind(wx.EVT_BUTTON, self.OnClearAllButton)	
			self.btn_save.Bind(wx.EVT_BUTTON, self.OnSaveButton)
			#button1 = wx.Button(panel, label="New")
			#sizer.Add(button1, pos=(3, 5), flag=wx.TOP|wx.RIGHT, border=5)

			#button2 = wx.Button(panel, label="Delete")
			#sizer.Add(button2, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
			self.sizer.Add(fgs, pos=(1, 4), flag=wx.TOP|wx.RIGHT, border=1)
		if 0:
			sb = wx.StaticBox(panel, label='Post-etl Email')

			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.send_email=wx.CheckBox(panel, label="Send email")
			boxsizer.Add(self.send_email, flag=wx.LEFT|wx.TOP, border=5)
			self.send_email.Bind(wx.EVT_CHECKBOX, self.OnChangeEmailYesNo)
			self.send_email.SetValue(False)		
			
			#print(dir(cb))
			self.sizer.Add(boxsizer, pos=(4, 0),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
		if 0:
			sb = wx.StaticBox(panel, label='On Run')

			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)

			self.auto_save=wx.CheckBox(panel, label="Auto-save")
			boxsizer.Add(self.auto_save, flag=wx.LEFT|wx.TOP, border=5)
			self.auto_save.SetValue(True)
			#self.confirm_run=wx.CheckBox(panel, label='Confirm run')
			#boxsizer.Add(self.confirm_run, flag=wx.LEFT|wx.TOP, border=5)
			#self.confirm_run.SetValue(True)
			
			#print(dir(cb))
			self.sizer.Add(boxsizer, pos=(4, 1),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)		
		boxsizer2 =  wx.BoxSizer(wx.HORIZONTAL)
		if 0:
			sb = wx.StaticBox(panel, label='Temporary data dump')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.keep_dump=wx.CheckBox(panel, label="Keep")
			self.keep_dump.SetName('keep_data_file')
			boxsizer.Add(self.keep_dump, flag=wx.LEFT|wx.TOP, border=5)
			self.keep_dump.Bind(wx.EVT_CHECKBOX, self.OnKeepDump)
			if self.args_panel.cargs.has_key('keep_data_file') and self.args_panel.cargs['keep_data_file'][2] in ['1']:
				self.keep_dump.SetValue(True)
			else:
				self.keep_dump.SetValue(False)	
			#self.keep_dump.Enable(False)
			if 1:
				self.btn_show_dump = wx.Button(panel, label='Show', size=(70,20))
				self.btn_show_dump.SetName('spool')
				self.btn_show_dump.Bind(wx.EVT_BUTTON, self.onShowDump)
				self.btn_show_dump.Enable(False)
				boxsizer.Add(self.btn_show_dump, flag=wx.LEFT|wx.TOP, border=0)
			
			#e(0)
			#print(dir(cb))
			#sizer.Add(boxsizer, pos=(8, 2),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
			boxsizer2.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=5)
		if 0:
			sb = wx.StaticBox(panel, label='Confirmation')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.confirm_run=wx.CheckBox(panel, label="Confirm run")
			boxsizer.Add(self.confirm_run, flag=wx.LEFT|wx.TOP, border=5)
			self.confirm_run.SetValue(True)			
			self.confirm_truncate=wx.CheckBox(panel, label="Confirm truncate")
			self.confirm_truncate.SetName('truncate_target')
			boxsizer.Add(self.confirm_truncate, flag=wx.LEFT|wx.TOP, border=5)
			#self.confirm_truncate.Bind(wx.EVT_CHECKBOX, self.OnConfirmTruncate)
			self.enableConfirmTruncate()
			#else:
			#	if self.args_panel.cargs.has_key('truncate_target') and self.args_panel.cargs['truncate_target'][2] in [1,'1']:
			#		self.confirm_truncate.SetValue(True)	
			#		self.confirm_truncate.Enable(True)

			#sizer.Add(boxsizer, pos=(8, 3),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
			boxsizer2.Add(boxsizer, flag=wx.LEFT|wx.TOP, border=1)
		#self.sizer.Add(boxsizer2, pos=(4, 2),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
		self.last_log_dir={}
		bs_log = wx.BoxSizer(wx.HORIZONTAL)
		#aboutBtn = wx.Button(panel, ID_ABOUT, 'About', style=wx.BU_EXACTFIT, size=(-1,25))
		#bs_log.Add(aboutBtn,flag=wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=1)
		
		self.btn_log = wx.Button(panel, label='Log', size=(-1,27))
		bs_log.Add(self.btn_log,flag=wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=1)
		self.sizer.Add(bs_log, pos=(2, 0), flag=wx.LEFT|wx.BOTTOM, border=1)
		
		if (self.last_log_dir.has_key(self.session_name) and self.last_log_dir[self.session_name]):
			self.btn_log.Enable(True)
		else:
			self.btn_log.Enable(False)
		self.btn_log.Bind(wx.EVT_BUTTON, self.OnButtonShowLog)

		self.btn_show = wx.Button(panel, label='Show in Folder', size=(-1,27))
		self.btn_show.Bind(wx.EVT_BUTTON, self.OnButtonShowInFolder)
		self.sizer.Add(self.btn_show, pos=(2, 1),flag=wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=1)
		self.btn_show.Enable(False)
		
		if 1:
			
			self.btn_run = wx.Button(panel, label='Run', size=(110,35))
			#self.btn_run = wx.ToggleButton(panel, -1, label='Run', size=(110,30))
			self.c_ok='#00FF7F'
			self.c_failed='#FF0000'
			self.c_default=(240, 240, 240, 255)
			self.btn_run.SetName('run')
			#print self.btn_run.GetBackgroundColour()
			#(240, 240, 240, 255)
			self.btn_run.SetBackgroundColour(self.c_default) 
			self.btn_run.Bind(wx.EVT_BUTTON, self.OnButtonRun)
			hm_sizer =  wx.BoxSizer(wx.HORIZONTAL)	
			hm_sizer.Add((175,-1))
			hm_sizer.Add(self.btn_run,0,wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=0)
			self.btn_run.Enable(False)	
					
			if 1:
				#btn_sqp=wx.Button(panel, label=lbl, style=wx.BU_EXACTFIT)	
				imageFile = os.path.join(home,"images/arrow_down_24.png")
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				host_map = wx.BitmapButton(panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				
				#tc[sn]['source'][0]
				host_map.SetName('host_map')
				host_map.Bind(wx.EVT_BUTTON, self.OnOpenHostMapMenu)
				#tcbox.Add(btn_sqp, flag=wx.LEFT|wx.TOP, border=5)
				hm_sizer.Add(host_map,0,wx.TOP, border=0)
			#self.host_map = wx.Button(panel, label=' ', size=(30,30))
			#self.host_map.Enable(False)
			#hm_sizer.Add(self.host_map,0,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=0)
			self.sizer.Add(hm_sizer, pos=(2, 3),   flag=wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_RIGHT, border=1)
		button5 = wx.Button(panel, ID_EXIT, label="Cancel",size=(90,35))
		#self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutBtn)
		self.sizer.Add(button5, pos=(2, 4), span=(1, 1), flag=wx.TOP|wx.BOTTOM, border=1)
		
		#sizer.AddGrowableCol(2)
		self.sizer.AddGrowableRow(1)
		#self.sizer.AddGrowableRow(3)
				
		if 1:
			self.panel2 = wx.Panel(self, wx.ID_ANY, size=(-1,-1), style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			panel2=self.panel2
			vsizer =  wx.BoxSizer(wx.VERTICAL)
			#wx.BoxSizer(wx.VERTICAL)
			#if 1:
				#self.splitter.SetOrientation(wx.VERTICAL)
			userhome = os.path.expanduser('~')
			sess_dir=session_home	
			self.sm=SessionListCtrlPanelManager(panel2,self,(0,0),self.panel_pos,sess_dir)
			if 1:
			
				self.snb = fnb.FlatNotebook(panel2, -1, size=(-1,-1), agwStyle=fnb.FNB_BOTTOM|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_SMART_TABS|fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
				snb=self.snb
				snb.AddPage(self.sm,'')
				snb.SetPageText(0, 'Sessions')
				if 1:
					#self.tm= wx.Panel(self, wx.ID_ANY, style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
					#userhome = os.path.expanduser('~')
					tmpl_dir=os.path.join(home,'templates')	
					#print tmpl_dir
					#e(0)
					self.tm=TemplateListCtrlPanelManager(panel2,self,(0,0),self.panel_pos,tmpl_dir)
					#self.tm= SessionListCtrlPanelManager(panel2,self,(0,0),self.panel_pos)
					snb.AddPage(self.tm,'')
					snb.SetPageText(1, 'Templates')
				
				snb.SetSelection(0)
				self.Bind(fnb.EVT_FLATNOTEBOOK_PAGE_CHANGED, self.onLibTypeChanged, self.snb)
		
			self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
			vsizer.Add(snb,1,wx.EXPAND|wx.GROW|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
			self.data =self.sm.list.data[self.sm.list.current_list]

			#self.vsizer.Add(self.sizer,pos=(0,1),flag=wx.EXPAND)
			
			

			#self.log=cu.NullLog()
			#self.sizer = wx.BoxSizer(wx.VERTICAL)
			self.hsizer.Add(panel2,1,wx.EXPAND, border=5)
			#self.hsizer.Add((5,5),0,wx.EXPAND)
			self.hsizer.Add(panel,0,wx.EXPAND,border=5)
			#self.sizer.Add((5,5),0,wx.EXPAND)
			#self.SetSizer(self.sizer)
			self.SetSizer(self.hsizer)

			#size = wx.DisplaySize()
			#print size
			#e(0)
			#self.SetSize((size[0]/3,size[1]/2))
			self.count = {}
			#self.sb = self.CreateStatusBar()
			#self.sb.SetStatusText(os.getcwd())
			self.Bind(wx.EVT_BUTTON, self.OnExit, id=ID_EXIT)
			#self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutBtn)
			#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
			panel2.SetSizer(vsizer)
		
		self.Bind(wx.EVT_MENU, self.loadFile, id=LOAD_FILE_ID)
		accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('O'), LOAD_FILE_ID )])
		self.SetAcceleratorTable(accel_tbl)		
		panel.SetSizer(self.sizer)
		sub(self.onTransportLoc, "set_transport_location")
		sub(self.onNewSession, "create_new_session")
		sub(self.onOpenSession, "open_session")
		sub(self.onValueChanged, "value_changed")
		sub(self.onDisableAllForDelete, "disable_all_for_delete")
		sub(self.onDisableAll, "disable_all")
		sub(self.onEnableAll, "enable_all")
		sub(self.onShowNbTab, "show_nb_tab")
		sub(self.onSaveArgs, 'save_args')
		sub(self.onSaveSessionAs, 'save_session_as')
		sub(self.onSetKeepDumpFile, "set_keep_data_file")
		
		sub(self.onSaveSessionAsTemplate, "save_as_template")
		sub(self.onSetBarStatus, "set_bar_status")
		sub(self.onRunSession, "run_session")
		
		#self.SetSizeHints(250,300,500,400)

		
		#self.Refresh()
		self.Center()
		#(x,y) = self.GetScreenPositionTuple()
		#self.SetPosition((x,y-80))
		#x,y=self.GetSize()
		#self.SetSize((x+100,y))
		#self.Refresh()
		#self.SetSize(size)
		#self.EnsureVisible(self.btn_run)
		self.Layout()
		#self.Fit()
		self.Show(True)
		self.generic_size=None
		self.ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
		#print self.GetSize()
		self._hmMenu=None
		self._saMenu=None
		self._mainMenu=None

		
	def get_default_hm_file(self):
		return self.aconf['defaults']['host_map']
	def OnMainMenu(self, event):
		#print self.recent
		#e(0)
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()

		# Create the popup menu
		#print self._mainMenu
		self.CreateMainMenu()
		#print self._mainMenu
		# Position the menu:
		# The menu should be positioned at the bottom left corner of the button.
		btnSize = btn.GetSize()
		btnPt = btn.GetPosition()

		# Since the btnPt (button position) is in client coordinates, 
		# and the menu coordinates is relative to screen we convert
		# the coords
		btnPt = btn.GetParent().ClientToScreen(btnPt)

		# A nice feature with the Popup menu, is the ability to provide an 
		# object that we wish to handle the menu events, in this case we
		# pass 'self'
		# if we wish the menu to appear under the button, we provide its height
		self._mainMenu.SetOwnerHeight(btnSize.y)
		self._mainMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)	
	def CreateMainMenu(self):

		if not self._mainMenu:
		
			self._mainMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------
			self.i=0
			if 1: #len(self.recent):				
				menuItem = FM.FlatMenuItem(self._mainMenu, wx.NewId(), 'About', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.onAboutDlg,[])
				#menuItem.Bind(FM.EVT_FLAT_MENU_SELECTED, self.onAboutDlg, id=wx.NewId())
				#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
				self._mainMenu.AppendItem(menuItem)
				self._mainMenu.AppendSeparator()
				
				menuItem = FM.FlatMenuItem(self._mainMenu, wx.NewId(), 'Dimensions', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditDimensions,[])
				#menuItem.Bind(FM.EVT_FLAT_MENU_SELECTED, self.onAboutDlg, id=wx.NewId())
				#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
				self._mainMenu.AppendItem(menuItem)
				self._mainMenu.AppendSeparator()
				
				menuItem = FM.FlatMenuItem(self._mainMenu, wx.NewId(), 'Default DB', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.onAboutDlg,[])
				#menuItem.Bind(FM.EVT_FLAT_MENU_SELECTED, self.onAboutDlg, id=wx.NewId())
				#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
				self._mainMenu.AppendItem(menuItem)
				menuItem.Enable(False)
				self._mainMenu.AppendSeparator()
				
				menuItem = FM.FlatMenuItem(self._mainMenu, wx.NewId(), 'Default Editor', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.onAboutDlg,[])
				#menuItem.Bind(FM.EVT_FLAT_MENU_SELECTED, self.onAboutDlg, id=wx.NewId())
				#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
				self._mainMenu.AppendItem(menuItem)
				menuItem.Enable(False)
				#self._mainMenu.AppendSeparator()				
	def OnEditDimensions(self, evt,params):
		#print 'OnEditSQL'
		(obj) = params
				
		fpath = os.path.join(home,'config','dimensions.py')
		if not os.path.isfile(fpath):
			self.Warn('File \n%s\ndoes not exests.' % fpath)
		else:
			webbrowser.open(fpath)
			
	def ResetAll(self):
		#print 'reset all'
		self.sids={}
		self.changed=[]
		self.copy_vector=['','']
		self.tmpl='n/a.n/a'
		self.the_id=[None,None,None]
		self.btn={}
		self.timers={}
		self.counters={}
		self.th={}
		self.btn={}
		self.p={}
		self.hwnd={}
		self.elapsed={}
		self.q={}
		self.s={}
		from include.default_args import default_args
		(self.cargs,self.fargs,self.targs)=default_args
		
		self.nb_tab=0
		self.cmd=''
		self.session_name=None
		
	def onSetBarStatus(self, data, extra1, extra2=None):		
		(id,msg)= data	
		#print 'data',data
		self.set_bar_status(id,msg)
	def set_bar_status(self, id, msg):
		if id in [2]:
			msg= 'Run at: %s' % msg
		self.statusbar.SetStatusText(msg, id)
	def setLibHome(self,lname):
		#print 'setLibHome', lname
		if self.S:
			self.save_to_dir=os.path.join(session_home,lname)
			if not os.path.isdir(self.save_to_dir):
				os.makedirs(self.save_to_dir)
		elif self.bT:
			self.save_to_dir=os.path.join(tmpl_home,lname)
			if not os.path.isdir(self.save_to_dir):
				os.makedirs(self.save_to_dir)
		else:
			assert 1==2, 'lib type is not set'
	
	def onSaveSessionAsTemplate(self, data, extra1, extra2=None):
		
		self.saveTemplate(data)
	def saveTemplate(self,data):
		(tname, tlib) = data
		#sname=self.getSessionName() 
		#save_as=self.session_name!=sname 
		#print self.session_name, sname
		save_as=True
		#sm=self.tm
		if self.if_duplicate_tmpl_name(tname, tlib):
			self.Warn('Duplicate template name.')
			self.tc_session_name.SetFocus()
		else:
			#self.save_to_dir=os.path.join(tmpl_home,default_tmpl_lib)
			(sname,cv,tmpl,dname,fname)=self.saveSession(sess_home=tmpl_home,slib_name=tlib, sname=tname)
			if save_as:
				session=[sname,cv[0],cv[1],'Copy',tmpl,dname,fname]
				#print dname
				#e(0)
				list=self.tm.lists[tlib]
				#print tlib
				#print self.tm.slps.keys()
				slp=self.tm.slps[tlib]
				idx=slp.addSession(session)	
				slp.list.set_data()
				slp.RecreateList(None,(slp.list,slp.filter))
				idx = slp.getIdFromText(sname)
				if idx>-1:				
					list.SetItemState(idx, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED) 
					list.EnsureVisible(idx)
			#self.output_panel.Save()
			#self.editor_panel.Save()
			#self.parent.btn_save.Enable(False)
			#print 'test'
			self.args_panel._sMenu=None
			self.args_panel._tMenu=None
			#self.save_to_dir=os.path.join(session_home,default_sess_lib)
	def if_duplicate_tmpl_name(self,tname,tlib='My_Templates'):
		#print 'if_duplicate_tmpl_name'
		tmpl_loc=os.path.join(tmpl_home,tlib,tname)
		#print tmpl_loc, os.path.isdir(tmpl_loc)
		return os.path.isdir(tmpl_loc)		
	def OnSaveAsMenu(self, event):
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()
		#print 
		if 1:
			# Create the popup menu
			self.CreatePopupMenuSA()
			btnSize = btn.GetSize()
			
			btnPt = btn.GetPosition()
			#print '1 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			#print '2 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			#print 'btnSize.y', btnSize.y
			self._saMenu.SetOwnerHeight(btnSize.y)
			#print 'btnPt.x, btnPt.y', btnPt.x, btnPt.y
			self._saMenu.Popup(wx.Point(btnPt.x, btnPt.y+50), self)
			mpsn=self._saMenu.GetScreenPosition()
			#print 'mpsn', mpsn
			#adjust
			if btnPt.y<mpsn[1]:
				self._saMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
			#print self._hmMenu.ClientToScreen(mpsn)
			#print	dir(self._hmMenu)

		
	def CreatePopupMenuSA(self):
		#global conf
		if not self._saMenu:
		
			self._saMenu = FM.FlatMenu()
			mitems={0:'Save', 1: 'Save As', 2:'Save As Template'}
			#hm=self.args_panel.hm
			#(hmap, active_map) =hm.get_host_map()
			#print active_map
			self.i=0
			
			#for k,v in mitems.items():
			if 1:
				self.i +=1
				self.recentMenu = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._saMenu, wx.NewId(), 'Save', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSaveSessionMenu,(self.getSessionName()))
				self._saMenu.AppendItem(menuItem)
				#if not self.changed:
				#	menuItem.Enable(False)
				self._saMenu.AppendSeparator()

				self.i +=1
				self.recentMenu = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._saMenu, wx.NewId(), 'Save As', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSaveAsSessionMenu,(self.getSessionName()))
				self._saMenu.AppendItem(menuItem)
				#self._saMenu.AppendSeparator()

				self.i +=1
				self.recentMenu = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._saMenu, wx.NewId(), 'Save As Template', '', wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSaveAsTemplateMenu,(self.getSessionName()))
				self._saMenu.AppendItem(menuItem)
				#self._saMenu.AppendSeparator()
	def OnSaveSessionMenu(self, event,params):				
		(sname)=params
		msg='Save session\n"%s"\nas\n"%s"' % (self.session_name, sname)
		if (not  self.session_name==sname) and self.if_yes( msg, 'Save As'):
			#print 'saveas'
			send('save_args',())
		else:
			send('save_args',())				
	def OnSaveAsSessionMenu(self, event,params):				
		(sname)=params
		if 1:
			dlg = SaveAsDialog(self, -1, 'Save As'  , saveas_name=sname,size=(-1, -1),				
				 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
				 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
				 useMetal=False
				 )
			dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			if val == wx.ID_OK:
				(new_sname, sess_lib)= dlg.getNewSessionInfo()
				old_sname=self.session_name
				#self.setSessionName(new_sname)
				#self.c
				self.tc_session_name.SetValue(new_sname)
				send('save_session_as',(new_sname, sess_lib))

		
	def OnSaveAsTemplateMenu(self, event,params):				
		(sname)=params
		if 1:
			dlg = SaveAsTemplateDialog(self, -1, 'Save As Template'  , saveas_name=sname,size=(-1, -1),				
				 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
				 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
				 useMetal=False
				 )
			dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			if val == wx.ID_OK:
				(tmpl_name,tmpl_lib)= dlg.getTemplateInfo()
				#old_sname=self.session_name
				#self.setSessionName(new_sname)
				#self.c
				#self.tc_session_name.SetValue(tmpl_name)
				send('save_as_template',(tmpl_name,tmpl_lib))
				
						
	def OnOpenHostMapMenu(self, event):
		# Demonstrate using the wxFlatMenu without a menu bar
		btn = event.GetEventObject()
		#print 
		if 1:
			# Create the popup menu
			self.CreatePopupMenu()
			btnSize = btn.GetSize()
			
			btnPt = btn.GetPosition()
			#print '1 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			btnPt = btn.GetParent().ClientToScreen(btnPt)
			#print '2 btnPt.x, btnPt.y', btnPt.x, btnPt.y
			#print 'btnSize.y', btnSize.y
			self._hmMenu.SetOwnerHeight(btnSize.y)
			#print 'btnPt.x, btnPt.y', btnPt.x, btnPt.y
			self._hmMenu.Popup(wx.Point(btnPt.x, btnPt.y+50), self)
			mpsn=self._hmMenu.GetScreenPosition()
			#print 'mpsn', mpsn
			#adjust
			if btnPt.y<mpsn[1]:
				self._hmMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
			#print self._hmMenu.ClientToScreen(mpsn)
			#print	dir(self._hmMenu)

		
	def CreatePopupMenu(self):
		global hmap
		#global conf
		hm_type= 'session'
		#print self.args_panel.hm
		if not self._hmMenu:
		
			self._hmMenu = FM.FlatMenu()
			#mitems={0:'Open SQL*Plus', 1: 'count(*)', 2:'DESCRIBE'}
			hm=self.args_panel.hm
			#default_hm=None
			
			#print default_hostmap_loc
			#if not hm:
			#	hm_type='default'
			#default_hostmap_loc = os.path.join(transport_home, 'config','host_map_v2.py')
				#new_hostmap_loc=self.parent.args_panel.CreateNewSessionHostMap(hostmap_loc)
				#if new_hostmap_loc not in [hostmap_loc]:
				#	self.obj[k][1].SetValue(new_hostmap_loc)
				#e(0)
				#print conf._to.join(self.copy_vector)
				
			#	default_hm = hmap(('ora11g','ora11g'), default_hostmap_loc)
				#self.args_panel.hm=default_hm
			#	hm=default_hm

			(hostmap, active_map) =hm.get_host_map()
			#print active_map
			self.i=0
			
			for v in hostmap.keys():
				self.i +=1
				self.recentMenu = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._hmMenu, wx.NewId(), v, '', wx.ITEM_RADIO)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnHostMapMenu,(v,hm))
				self._hmMenu.AppendItem(menuItem)
				if v==active_map:
					menuItem.Check(True)
			#default_hostmap_loc = os.path.join(transport_home, 'config','host_map','host_map.py')
			
			default_hostmap_dir = os.path.join(transport_home, 'config','host_map')
			default_hostmap_loc = os.path.join(default_hostmap_dir, self.default_hm_file)
			#print default_hostmap_loc
			#self.set_hm(self.parent.get_default_cv(),default_hostmap_loc )
			
			
			is_default = hm.host_map_loc in [default_hostmap_loc] or not self.btn_run.Enabled
			if 1:
				self._hmMenu.AppendSeparator()
				imageFile = os.path.join(home,'images','Right_Arrow_16.png')
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				defaultMenu = FM.FlatMenu()
				menuItem1 = FM.FlatMenuItem(self._hmMenu, wx.NewId(), 'Set default global "host_map"', '', wx.ITEM_NORMAL,defaultMenu,context_bmp)
				if is_default:
					menuItem1.Enable(True)
				else:
					menuItem1.Enable(False)			
				#default_hostmap_dir = os.path.join(transport_home, 'config','host_map')
				files = [x for x in os.listdir(default_hostmap_dir) if x.upper().endswith('.PY') and not x.startswith('__init__')]
				for f in files:
					#imageFile = os.path.join(home,'images','gear_24_g.png')
					#context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
					#hmMenu = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(defaultMenu, wx.NewId(), f, '', wx.ITEM_CHECK)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnSetDefaultHostMap,(default_hostmap_dir,f))
					#print f,self.default_hm_file,f==self.default_hm_file
					#menuItem.Check(True)
					if f==self.default_hm_file:
						#print '---'
						menuItem.Check(True)
					else:
						menuItem.Check(False)
					#menuItem.Check(True)
					defaultMenu.AppendItem(menuItem)
				#e(0)
				self._hmMenu.AppendItem(menuItem1)
			
			if 1:
				self.i +=1
				self._hmMenu.AppendSeparator()
				imageFile = os.path.join(home,'images','gear_24_g.png')
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				menuItem = FM.FlatMenuItem(self._hmMenu, wx.NewId(), 'Edit session "%s"' % self.default_hm_file, '', wx.ITEM_NORMAL, None, context_bmp)
				#print self.args_panel.hm.host_map_loc				
				if not is_default:					
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
					menuItem.Enable(True)
				else:
					menuItem.Enable(False)
				
				self._hmMenu.AppendItem(menuItem)
			if 1:
				self.i +=1
				self._hmMenu.AppendSeparator()
				#imageFile = os.path.join(home,"images/database_red_16.png")
				imageFile = os.path.join(home,'images','gear_24_b.png')
				context_bmp = wx.Bitmap(imageFile, wx.BITMAP_TYPE_PNG)
				
				menuItem = FM.FlatMenuItem(self._hmMenu, wx.NewId(), 'Edit global "%s"' % self.default_hm_file , '', wx.ITEM_NORMAL, None, context_bmp)
				#print default_hm.host_map_loc
				if is_default:
					menuItem.Enable(True)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(hm.host_map_loc))
				else:
					#default_hm = hmap(('ora11g','ora11g'), default_hostmap_loc)
					menuItem.Enable(True)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnEditHostMap,(default_hostmap_loc))
				self._hmMenu.AppendItem(menuItem)				
	def get_default_cv(self):
		return self.aconf['defaults']['copy_vector']
	def OnSetDefaultHostMap(self, event,params):
		
		(hm_dir, hm_file) = params
		#print 'OnSetDefaultHostMap',hm_file
		#send('set_hostmap', (hm_file))
		#pprint(self.aconf)
		self.aconf['defaults']['host_map']=hm_file
		self.save_app_config()
		self.default_hm_file= hm_file
		self.args_panel.hm.Destroy()
		cv=self.get_default_cv()
		if self.copy_vector[0]:
			cv=self.copy_vector
		#print cv
		hm_loc=os.path.join(hm_dir, hm_file)
		#print hm_loc
		self.args_panel.set_hm(cv, hm_loc)
		#print self.args_panel.hm
		del self._hmMenu
		self._hmMenu=None
	def save_app_config(self):
		#change active mapping
		app_config_loc=os.path.join(home,'config','app_config.py')
		f = open(app_config_loc, 'w')
		#f.write('mapping=%s' % cp.pprint(hm.mapping))
		print >>f,'app_conf=%s' % pp.pformat(self.aconf)
		f.close()
		
	def OnEditHostMap(self, event,params):				
		(host_map_loc)=params	
		if not os.path.isfile(host_map_loc):
			self.parent.Warn('Host map\n%s\ndoes not exests.' % host_map_loc)
		else:
			webbrowser.open(host_map_loc)
					
	def OnHostMapMenu(self, event,params):				
		(v,hm)=params	
		#print v
		#print self.args_panel.hm
		self.args_panel.hm.set_active_mapping(v)
		send('set_bar_status', (2,v))
		
	def onSetKeepDumpFile(self, data, extra1, extra2=None):
		#print 'onSetKeepDumpFile'
		(val)=data	
		#print val
		if  val in ['1'] or val ==1 :
			self.keep_dump.SetValue(True)
			self.EnableShowDumpButton()
		else:
			self.keep_dump.SetValue(False)	
			self.EnableShowDumpButton()
		

	def getActiveLibName(self):
		type= self.snb.GetSelection()
		lib_types=('Session','Template')
		lib_mans=(self.sm,self.tm)
		assert lib_types[type], 'Lib type is not defined.'
		return '|'.join([lib_types[type],lib_mans[type].getActiveLibName()]) 
	def OnEditSQL(self, evt,params):
		#print 'OnEditSQL'
		(obj) = params
				
		#(ftype) = params
		#sqldr_dir=os.path.join(self.getLogDir(),'sqlloader')
		#print sqldr_dir
		#fname=self.getSqlLoaderFileName()
		#ctl_fname=os.path.join(sqldr_dir,'%s.%s' % (fname,ftype) )
		#print self.tfile
		#cb = evt.GetEventObject()	
		fpath = obj.GetValue()
		if not os.path.isfile(fpath):
			self.parent.Warn('File \n%s\ndoes not exests.' % fpath)
		else:
			webbrowser.open(fpath)
	def getEditButton(self, parent):
		imageFile = os.path.join(home,"images/editor_icon_16_2.png")
		image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		btn = bButton(parent, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
		return btn
		#getEditButton self.gen_bind(wx.EVT_BUTTON,bitbtn, self.OnEditSQL,(self.obj[k][1]))		

		
	def onKeyPressNB(self, event):
		#print 'pnl onKeyPress'
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc
		controlDown = event.CmdDown()
		if controlDown:
			if kc == 19:
				print 'Ctrl-S 5'
				send('save_args',())				
				#self.Save()
			if	kc == 4:
				print 'Ctrl-D 5'
				self.parent.frame.tryToDelete()
		else:				
			event.Skip()
	def enableLoaderTab_(self):
		k='loader_profile'
		if self.args_panel.obj.has_key(k):			
			self.nb.EnableTab(1,True)
		else:
			self.nb.EnableTab(1,False)
	def enableEditorTab_(self):
		#print 'enableEditorTab'
		k='job_pre_etl'
		if self.args_panel.obj.has_key(k):			
			self.nb.EnableTab(2,True)
		else:
			self.nb.EnableTab(2,False)
			
			
			
	def onShowNbTab(self, data, extra1, extra2=None):
		(tab_id,fname)=data
		#print tab_id
		#print fname
		self.nb.SetSelection(tab_id)
		if 0:
			if tab_id==1:
				self.sizer.SetItemSpan(self.nb,(5,4))
				self.panel.Fit()
				self.Layout()
			else:
				#self.nb.Freeze()
				self.sizer.SetItemSpan(self.nb,(4,4))
				#self.panel.Fit()
				#self.Layout()
				#self.sizer.Refresh() #Fit(self.panel)
				#self.args_panel.Freeze()
				self.args_panel.Freeze()
				self.nb.Refresh()
				
				self.args_panel.Fit()
				self.args_panel.Thaw()
				#self.args_panel.Layout()
				#self.args_panel.Thaw()
				#x,y=self.args_panel.GetSize()
				#self.args_panel.SetSize((x-1,y))
			#self.nb_tab=		
		
	def refreshType_1(self):
		self.panel1.Layout()
		self.panel1.Fit()
	def enableConfirmTruncate(self):
		if self.args_panel.cargs.has_key('ask_to_truncate') and self.args_panel.cargs['ask_to_truncate'][2] in [1,'1']:
			#print self.args_panel.cargs['ask_to_truncate'][2], self.args_panel.cargs['truncate_target'][2]
			#e(0)
			if self.args_panel.cargs.has_key('truncate_target') and self.args_panel.cargs['truncate_target'][2] in [1,'1']:
				self.confirm_truncate.SetValue(True)	
				self.confirm_truncate.Enable(True)
		else:
			#self.args_panel.cargs.has_key('truncate_target') and self.args_panel.cargs['truncate_target'][2] in [0,'0']:
			
			self.confirm_truncate.SetValue(False)
			self.confirm_truncate.Enable(False)
	def ifTruncateTarget(self):
		#print self.args_panel.cargs.has_key('truncate_target') , self.args_panel.cargs['truncate_target'][2] in ['1',1]
		return self.args_panel.cargs.has_key('truncate_target') and self.args_panel.cargs['truncate_target'][2] in ['1',1]
	def enableKeepDump(self):
		if hasattr(self, 'keep_dump') and self.keep_dump:
			self.keep_dump.Enable(True)
	def enableShowDump(self):
		self.btn_show_dump.Enable(False)
	def OnKeepDump(self, evt):
		#print 'OnKeepDump'
		cb = evt.GetEventObject()	
		name=cb.Name
		#print name
		if not name in self.args_panel.obj.keys():
			self.args_panel.obj[name]=[DummyStaticText(name), DummyTextControl('1',True)]
			self.args_panel.cargs[name]=['-K', '--%s' % name, '0', 'Keep dump file after load.']
		if cb.GetValue():
			self.args_panel.obj[name][1].SetValue('1')
			self.EnableShowDumpButton()
		else:
			self.args_panel.obj[name][1].SetValue('0')
			self.btn_show_dump.Enable(False)
		#self.updateCommand()
	def EnableShowDumpButton(self):
		#print 'EnableShowDumpButton'
		
		if self.args_panel.obj.has_key('default_spool_dir') and self.keep_dump.GetValue():
			#check if dump file exists
			self.dump_dir=self.getDumpDir()
			self.dump_file=os.path.join(self.dump_dir,'shard_0.data')
			#print 'dump file: %s' % self.dump_file
			if os.path.isfile(self.dump_file):
				self.btn_show_dump.Enable(True)
			else:
				self.btn_show_dump.Enable(False)
		else:
			self.btn_show_dump.Enable(False)
			
	def onShowDump(self, evt):
		if self.keep_dump.GetValue():
			#check if dump file exists
			dump_dir=self.getDumpDir()
			dump_file=os.path.join(dump_dir,'shard_0.data')
			#print 'dump file: %s' % dump_file
			self.ShowLocation(dump_file)
	def getDumpDir(self):
		dump_dir=self.args_panel.obj['default_spool_dir'][1].GetValue()
		#print 'dump_dir',dump_dir
		#dump_dir=r'C:\tmp'
		job_name=self.args_panel.obj['job_name'][1].GetValue()
		#print job_name
		time_stamp=self.ts 
		if self.args_panel.obj.has_key('time_stamp'):
			time_stamp=self.args_panel.obj['time_stamp'][1].GetValue()
		#print time_stamp
		return os.path.join(dump_dir, job_name,time_stamp)			
	def OnChangeEmailYesNo(self,evt):
		#print 'OnChangeEmailYesNo'
		cb = evt.GetEventObject()		
		#self.updateCommand()
	def if_send_email(self):
		return self.send_email.GetValue()
	def restore_changed_args(self):
		#print 'restore_changed_args'
		#pprint(self.changed)
		sess=self.get_session_args(os.path.join(self.sdir,self.fname))
		(self.cargs,self.fargs,self.targs)=sess
		#print len(self.cargs),len(self.fargs),len(self.targs)
		for k,v in self.cargs.items():
			#print k, v
			if k in self.changed:
				#restoring value
				
				#print 'restoring',k,'from',self.args_panel.obj[k][1].GetValue(),'to', v[2]
				self.args_panel.obj[k][1]=v[2].strip('"')
				del self.changed[self.changed.index(k)]
		for k,v in self.fargs.items():
			#print k, v
			if k in self.changed:
				#restoring value
				#print self.args_panel.obj[k][1]
				#print 'restoring',k,'from',self.args_panel.obj[k][1].GetValue(),'to', v[2]
				self.args_panel.obj[k][1]=v[2].strip('"')
				del self.changed[self.changed.index(k)]
		for k,v in self.targs.items():
			#print k, v
			if k in self.changed:
				#restoring value
				#print 'restoring',k,'from',self.args_panel.obj[k][1].GetValue(),'to', v[2]
				self.args_panel.obj[k][1]=v[2].strip('"')
				del self.changed[self.changed.index(k)]
		self.changed=[]
		#self.loader_panel.changed=False
	def openDefault(self, sname):
		print 'openDefault'
	def onLibTypeChanged(self, evt):
		#print str(self.__class__) +' - onLibTypeChanged'
		ltype=self.snb.GetPageText(self.snb.GetSelection())	
		if ltype in ['Sessions']:
			self.S=True
			self.bT=False
			self.setLibHome(default_sess_lib)
		elif 'Templates' in ltype:
			self.S=False
			self.bT=True
			self.setLibHome(default_tmpl_lib)
		else:
			assert 1==2, 'Unknown lib type "%s"' % ltype

		type= self.snb.GetSelection()
		#lib_types=('Session','Template')
		lib_mans=(self.sm,self.tm)
		assert lib_mans[type], 'Lib type is not defined.'
		lib_mans[type].setTab()		
	def onTabChanged(self, evt):
		#print str(self.__class__) +' - onTabChanged'
		self.nb_tab= self.nb.GetSelection()
		libname=self.nb.GetPageText(self.nb.GetSelection())	
		#self.setLibHome(libname)
		#print self.nb_tab
		if self.nb_tab:
			self.btn_clearall.Enable(False)
		else:
			self.btn_clearall.Enable(True)
		#self.updateCommand(self.nb_tab)

		
				
	def onDeleteSessions_(self,  data, extra1, extra2=None):
		(items)=data
		for k,v in items.items():
			#print k, v
			if os.access(v, os.W_OK) and os.path.isfile(v):
				os.remove(v)
				#print 'removed', v
			
		
	def onDisableAllForDelete(self, data, extra1, extra2=None):	
		#print 'onDisableAllForDelete'	
		
		self.DisableAll()
		self.btn_delete.Enable(True)
		
	def DisableAll(self):
		self.Freeze()
		#self.args_panel.DisableAll()
		self.btn_delete.Enable(False)
		self.btn_new.Enable(False)
		self.btn_clearall.Enable(False)
		self.btn_save.Enable(False)
		self.save_as.Enable(False)
		self.btn_run.Enable(False)
		self.btn_show.Enable(False)
		
		self.st_session_name.Enable(False)
		self.confirm_run.Enable(False)
		self.tc_session_name.Enable(False)
		self.auto_save.Enable(False)
		self.args_panel.st_type.Enable(False)
		self.args_panel.st_copy_vector.Enable(False)
		self.args_panel.st_sourcet.Enable(False)
		self.args_panel.st_targett.Enable(False)
		self.nb.EnableTab(0,False)
		self.nb.EnableTab(1,False)	
		#self.nb.EnableTab(2,False)
		del self._hmMenu
		self._hmMenu=None		
		self.Thaw()
		
	def onDisableAll(self, data, extra1, extra2=None):	
		#print 'onDisableAll'	
		
		self.DisableAll()
		self.btn_new.Enable(True)
		
	def onEnableAll(self, data, extra1, extra2=None):	
		#print '-----------onEnableAll-----------'	
		#self.args_panel.DisableAll()
		#self.btn_delete.Enable(True)
		self.Freeze()
		self.btn_new.Enable(True)
		self.btn_clearall.Enable(True)
		self.btn_save.Enable(True)
		self.save_as.Enable(True)
		self.btn_run.Enable(True)
		self.btn_show.Enable(True)
		self.btn_delete.Enable(True)
		self.st_session_name.Enable(True)
		self.tc_session_name.Enable(True)
		self.confirm_run.Enable(True)
		self.auto_save.Enable(True)
		self.args_panel.st_type.Enable(True)
		self.args_panel.st_copy_vector.Enable(True)
		self.args_panel.st_sourcet.Enable(True)
		self.args_panel.st_targett.Enable(True)
		self.nb.EnableTab(0,True)
		#self.enableLoaderTab() 
		#self.enableEditorTab()
		#self.nb.EnableTab(1,True)
		#self.nb.EnableTab(2,True)
		self.Thaw()		
	def onKeyPress(self, event):
		#print 'frame onKeyPress'
		tc = event.GetEventObject()
		#print 'name=',tc.Name
		kc = event.GetKeyCode()
		#print 'kc=', kc

			#self.parent.changed=True
		controlDown = event.CmdDown()
		if controlDown:
			#print 'controlDown', kc
			if kc == 1: #in ['a','A']:
				#print 'Ctrl-A'
				tc.SelectAll()
			if	kc == 4:
				print 'Ctrl-D 4'
				self.parent.tryToDelete()
		else:
			if not (kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
				self.btn_save.Enable(True)
				self.save_as.Enable(True)
				if not tc.Name in self.changed:
					self.changed.append(tc.Name)		
		event.Skip()

	def IncCounter(self, the_id):
		self.counters[the_id] = self.counters[the_id] + 1
	def StopTimer(self, the_id):
		self.timers[the_id].Stop()
	def SetBtn(self,the_id, val):
		self.btn[the_id]=val
	def EnableBtn(self,the_id, boo):
		self.btn[the_id].Enable(boo)
	def TimerHandler(self, event, the_id):
		#self.closing_in=15
		wx.CallAfter(self.IncCounter, the_id)
		#print self.counters[the_id], the_id
		#if self.counters[the_id]>10:
		#	self.timers[the_id].Stop()
		btn=self.btn[the_id]
		#print 'TimerHandler', the_id, btn.Name
		sn=self.getSessionName()
		if btn.Name in ['source', 'target'] :
			#SQL*Plus/Test connect
			#print self.counters[the_id], the_id
			
			#print btn
			#print the_id, self.session_name, self.args_panel.the_id
			
			p=self.p[the_id]
			#print self.timers
			msg= 'Closing in %d' % (self.closing_in-self.counters[the_id])
			hwnd= self.get_hwnds_for_pid (p.pid)
			
			if not hwnd or self.counters[the_id] >= self.closing_in:
				#poll=p.poll()
				#print 'poll', p
				wx.CallAfter(self.close_exec,p)
				if 1:
					self.counters[the_id] = 0
					#self.timers[the_id].Stop()
					wx.CallAfter(self.StopTimer,the_id)
					
					if btn:										
						btn.Enable(True)
						btn.SetLabel('Test connect')
						wx.CallAfter(self.SetBtn,the_id,None)
						
			else:			
				if btn and self.counters[the_id]>0:
					#print the_id, self.counters[the_id],msg,  'poll', p.poll()
					wx.CallAfter(self.EnableBtn, the_id, False)
					win32gui.SetWindowText (hwnd[0], '%s: %s' %(self.session_name,msg))
					btn.SetLabel(msg)
					if 0:
						def all_ok(hwnd, param):
							#print hwnd
							return True
						#print win32gui.EnumChildWindows(hwnd[0], all_ok, None)
					if 0:
						buf_size = 1 + win32gui.SendMessage(hwnd[0], win32con.WM_GETTEXTLENGTH, 0, 0)
						if buf_size:
							buffer = win32gui.PyMakeBuffer(buf_size)
							win32gui.SendMessage(hwnd[0], win32con.WM_GETTEXT, buf_size, buffer)
							txt = buffer[:buf_size]

						if buf_size:
							selinfo  = win32gui.SendMessage(hwnd[0], win32con.EM_GETSEL, 0, 0)
							endpos   = win32api.HIWORD(selinfo)
							startpos = win32api.LOWORD(selinfo)
							#print 'txt', txt[startpos: endpos]
			
					if 0:
						control = win32gui.FindWindowEx(hwnd[0], 0, 'static', None)
						buffer = win32gui.PyMakeBuffer(255)
						length = win32gui.SendMessage(control, win32con.WM_GETTEXT, 255, buffer)

						result = buffer[:length]
						#print 'buffer', result
						#time.sleep(1)
		else:
			
			#print btn.Name, the_id, self.the_id,the_id==self.the_id[2],self.counters[the_id]
			if the_id==self.the_id[2]:
				#print 1
				#print btn.Name,self.counters[the_id] 
				p=self.p[the_id]
				poll=p.poll()
				#print 'poll', poll
				if poll in [None]:
					#Still alive
					self.Freeze()
					msg= self.getRunning(the_id,p)
					
					btn.SetLabel(msg)
					self.DisableOnRun()
					ld=os.path.isdir(self.args_panel.getLogDir())
					if (self.last_log_dir.has_key(self.session_name) and self.last_log_dir[self.session_name]) or ld:
						self.btn_log.Enable(True)
					else:
						self.btn_log.Enable(False)
					self.args_panel.enableSqlLoaderButtons()
					self.EnableShowDumpButton()
					self.Thaw()
					line=' '
					if 0:
					#for i in range(100):
						(t,q)=self.q[the_id]
						try:  line = q.get_nowait() # or q.get(timeout=.1)

						except Empty:
							pass
							#print('no output yet')
						except: 
							raise							
						else: # got line
							#print line
							self.pipefh.close() 
							#break
													
				else:
					#pprint(self.s)
					btn.SetLabel('Run')
					self.btn_run.SetBackgroundColour(self.c_default)
					self.timers[the_id].Stop()
					del self.p[the_id]
					self.p.pop(the_id, None)
					self.counters[the_id]=0
					self.EnableAfterRun()
					send('lowlight_session',self.session_name)
					self.EnableShowDumpButton()
					if self.elapsed.has_key(self.getSessionName()):
						del self.elapsed[self.getSessionName()]
					#del self.sids[sn][2]
					if self.q.has_key(the_id):
						del self.q[the_id]
				#else:
				#	print 'Unknown poll status %s, id %d' % (poll, the_id)
			#print 2	
			for x,v in self.q.items():
				(t,q)=v
				#print x
				try:  line = q.get_nowait() # or q.get(timeout=.1)

				except Empty:
					pass
					#print('no output yet')
				except: 
					raise							
				else: # got line
					self.s[the_id]=eval(line)
					#self.pipefh.close() 
					del self.q[x]
					#break
							
							
							
	def getRunning(self,the_id, pid):
		elapsed='%dm%ds' % (self.counters[the_id]/60,self.counters[the_id]%60)
		#print the_id, pid
		#print self.s
			
		if self.counters[the_id]<60:
			elapsed='%ds' % (self.counters[the_id])
		#print the_id, self.hwnd[the_id]
		#title=win32gui.GetWindowText (self.hwnd[the_id][0])
		#print title
		sn=self.getSessionName()
		if self.s.has_key(the_id):
			if self.elapsed and self.elapsed.has_key(sn):
				pass
			else:
				self.elapsed[sn]='%dm%ds' % (self.counters[the_id]/60,self.counters[the_id]%60)
			
			#status=title.split(':')[1]
			#print status
			status='FAILED'
			if self.s[the_id]['status']:
				status='SUCCESS'
			if status in ['FAILED']:
				#print status
				self.btn_run.SetBackgroundColour(self.c_failed)
				send('highlight_session',(self.session_name,self.c_failed))
			elif status in ['SUCCESS']:
				#print status
				self.btn_run.SetBackgroundColour(self.c_ok)
				send('highlight_session',(self.session_name,self.c_ok))

			
			return '%s (%s)' % (status, self.elapsed[sn])
		else:
			return 'Running...(%s)' % (elapsed)
	def onOpenSession(self, data, extra1, extra2=None):
		#print 'onOpenSession'
		#pprint(data)
		#size=self.GetSize()
		#pprint(data)
		#print len(data)
		(sname,tmpl2,cv_from,cv_to,type,tmpl1,sdir, fname) = data
		#print sname
		x,y=self.GetSize()
		self.Freeze()
		self.enableForm()
		self.tmpl='.'.join([tmpl1,tmpl2])
		self.open_session([sname,[cv_from.upper(),cv_to.upper()],type,self.tmpl,sdir,fname])
		
		self.btn_delete.Enable(True)
		self.btn_new.Enable(True)
		self.btn_save.Enable(False)
		#self.save_as.Enable(False)
		#pprint(self.args_panel.obj.keys())
		ld=os.path.isdir(self.args_panel.getLogDir())
		if (self.last_log_dir.has_key(self.session_name) and self.last_log_dir[self.session_name]) or ld:
			self.btn_log.Enable(True)
		else:
			self.btn_log.Enable(False)
		self.args_panel.enableSqlLoaderButtons()
		self.changed=[]
		
		#self.Fit()
		#self.Layout()
		#print size
		#self.Refresh()
		#self.sm.nb.SetSize((300,-1))
		
		if self.if_generic_tremplate():	
			#e(0)
			#self.Freeze()
			self.updateTimeStamp()
			self.Layout()
			if not self.generic_size:
				self.Fit()
				#x2,y2=self.GetSize()
				#print x2,y2
				self.generic_size=self.GetSize()
				#self.SetSize((1200,985))
				#x1, y1=(1200, 985)
				#print x1,y1
				x1, y1=self.GetSize()
				self.Center()
			else:
				size=self.GetSize()
				#self.SetSize(self.generic_size)
				x1, y1=self.GetSize()
				self.generic_size=size
				
			if x>x1:
				self.SetSize((x,-1))
			#self.Thaw()
		else:
			self.SetSize((x,y))
		self.Thaw()
		for k in self.args_panel.disabled:
			if  self.args_panel.obj.has_key(k):
				self.args_panel.obj[k][1].Enable(False)
		#
		#self.Refresh()
		#send('set_focus_on_run',())
		
	def if_generic_tremplate(self):
		return 'generic' in self.tmpl
	def close_exec(self,p):

		if 1:
			#import subprocess
			#import time
			#notepad = subprocess.Popen ([r"notepad.exe"])
			#
			# sleep to give the window time to appear
			#
			#time.sleep (5)

			for hwnd in self.get_hwnds_for_pid (p.pid):
				#print hwnd, "=>", win32gui.GetWindowText (hwnd)
				#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
				win32gui.SendMessage (hwnd, win32con.WM_CLOSE, 0, 0)		
	def get_hwnds_for_pid (self, pid):
		def callback (hwnd, hwnds):
			if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
				_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
				if found_pid == pid:
					hwnds.append (hwnd)
			return True

		hwnds = []
		win32gui.EnumWindows (callback, hwnds)
		#print hwnds
		return hwnds		
	def enableForm(self):
		self.btn_new.Enable(True)
		self.btn_clearall.Enable(True)
		self.btn_save.Enable(True)
		self.btn_run.Enable(True)
		self.btn_show.Enable(True)
		self.save_as.Enable(True)
		self.st_session_name.Enable(True)
		self.tc_session_name.Enable(True)
		self.confirm_run.Enable(True)
		self.auto_save.Enable(True)
		self.args_panel.st_type.Enable(True)
		self.args_panel.st_copy_vector.Enable(True)
		self.args_panel.st_sourcet.Enable(True)
		self.args_panel.st_targett.Enable(True)
		#self.nb.EnableTab(0,True)
		#self.nb.EnableTab(1,True)	
	def OnDeleteButton(self,evt):
		#print '#####', self.sm.list.GetSelectedItemCount()
		self.tryToDelete()
	def tryToDelete(self):
		#print  'tryToDelete'
		items={}
		#self.lists[default_slib_name]
		#print self.sm.lists.keys()
		#print self.sm.slib_name
		#e(0)
		list=self.sm.lists[self.sm.slib_name]
		data =list.data[list.current_list]
		#pprint(data)
		selected=list.GetSelectedItems()
		#print selected
		names=[]
		for i in selected:
			#print '$$$$$',i
			ii=list.getItemInfo(i)
			#print i, self.sm.list.getItemInfo(i)
			#print data[i]
			key = ii[1] #pprint  (data[i])
			names.append(list.GetItemText(i))
			items[key]=os.path.join(data[i][-2],data[i][-1])
			#del data[i]
		#pprint (names)	
		#pprint (items)		
		msg='Delete these sessions?\n%s' % '\n'.join(names)
		if len(names)==1:
			msg='Delete this session?\n%s' % '\n'.join(names)
		if self.if_yes(msg):
			#print items
			#e(0)
			send('delete_sessions', (items))
			if len(selected)==1:
				send('disable_all_for_delete',())
			self.btn_delete.Enable(False)
			self.btn_new.Enable(True)
			#print(len(list.GetSelectedItems()))			
			self.ResetAll()
			self.session_name=None
			
	def if_yes(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.YES_NO | wx.ICON_QUESTION)
		dlg.SetSize((500,-1))
		answer=dlg.ShowModal()
		#pprint(dir(dlg))
		dlg.Destroy()
		return answer==wx.ID_YES
	def if_yes_2(self, msg, caption = 'Warning!'):
		#print 'if_yes_2'
		dlg = NewDialog(self, msg=msg, title=caption, style=wx.YES_NO | wx.ICON_QUESTION|wx.THICK_FRAME|wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		#dlg.SetSize((500,-1))
		dlg.CenterOnParent()
		answer=dlg.ShowModal()
		#pprint(dir(dlg))
		#dlg.CenterOnScreen()
		dlg.Destroy()
		#print answer
		return answer==wx.ID_OK		
	def onNewSession(self, data, extra1, extra2=None):	
		#print 'onNewSession'
		if 1:
			(sname,cv,tmpl,args,reuse) = data
			#print sname
			#e(0)
			#self.setSessionName(sname)
			#print sname,copy_vector,tmpl,
			#pprint (api_args)
			#self.set_new_session(data)
			#pprint (data)
			#e(0)
			(sname,cv,tmpl,dname,fname)=self.saveSession(data)
			#refresh session list
			#self.save_to_dir,f
			send('add_session',(sname,cv,tmpl,dname,fname))
			#self.parent.RecreateList(None,(self.parent.list,self.parent.filter))
			#self.Layout()
			#self.Fit()
			#self.Refresh()
	def onValueChanged(self, data, extra1, extra2=None):		
		self.btn_save.Enable(True)
		self.save_as.Enable(True)
		
	def setSessionName(self, sn):
		self.tc_session_name.SetValue(sn)
		#ORA11G_TimezoneQueryFile_to_ORA11G_Subpartitio
		self.tc_session_name.Enable(True)
		self.session_name=self.getSessionName()
		self._saMenu = None #save as popup menu
	def getSessionName(self):
		return self.tc_session_name.GetValue().strip().strip(' ')
	def getCopyVector(self):
		return self.copy_vector		
	def setCopyVector(self, cv):
		self.copy_vector=cv	
		#print self.copy_vector
		#e(0)
		self.args_panel.st_copy_vector.SetLabel('{:s} -> {:s}'.format(cv[0], cv[1]))
	def setTemplates(self,tmpl):
		self.tmpl=tmpl
		a,b=tmpl.split('.')
		self.args_panel.st_sourcet.SetLabel(a[:30])
		self.args_panel.st_targett.SetLabel(b[:30])
	def setType(self,tmpl):
		a,b=tmpl.split('.')
		type='Copy'
		if a.startswith('CSV'):
			type='Load'
		elif b.startswith('CSV'):
			type='Extract'
		self.args_panel.st_type.SetLabel('{:s}'.format(type))
		
	def getTemplates(self):
		return (self.args_panel.st_sourcet.GetLabel().strip(),self.args_panel.st_targett.GetLabel().strip())
	def OnClearAllButton(self, event):
		self.args_panel.ClearAll()
	def OnSaveButton(self, event):
		self.saveArgs()
	def onSaveArgs(self, data, extra1, extra2=None):
		#print 'onSaveArgs'
		self.saveArgs()
	def onSaveSessionAs(self, data, extra1, extra2=None):
		(sname, lname) = data
		#print 'onSaveSessionAs', sname, lname
		self.saveArgs(slib=lname)		
		
	def saveArgs(self, slib='My_Sessions'):
		#print 'saveArgs', slib
		sname=self.getSessionName() 
		save_as=self.session_name!=sname 
		#print '#'*60
		#print '#'*60
		#print 'saveArgs:', self.session_name, 'sname:', sname, 'save_as:', save_as, self.saved
		if sname and self.session_name:		
			#a=1/0
			if ( save_as and ( self.if_duplicate_name(sname,slib))): #self.if_duplicate_name(self.session_name,slib) or
				self.Warn('Duplicate session name.', 'saveArgs')
				self.tc_session_name.SetFocus()
			else:
				(sname,cv,tmpl,dname,fname)=self.saveSession(slib_name=slib)
				if save_as:
					session=[sname,cv[0],cv[1],'Copy',tmpl,dname,fname]
					#print dname
					#e(0)
					list=self.sm.lists[slib]
					#print slib
					#print self.sm.slps.keys()
					slp=self.sm.slps[slib]
					idx=slp.addSession(session)	
					slp.list.set_data()
					slp.RecreateList(None,(slp.list,slp.filter))
					idx = slp.getIdFromText(sname)
					if idx>-1:				
						list.SetItemState(idx, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED) 
						list.EnsureVisible(idx)
				#self.output_panel.Save()
				#self.editor_panel.Save()
				#self.parent.btn_save.Enable(False)
				#print 'test'
				self.args_panel._sMenu=None
				self.args_panel._tMenu=None
		
	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,sname,slib='My_Sessions'):
		#print 'if_duplicate_name', slib
		sfile_loc=os.path.join(session_home,slib,sname)
		#print session_home,slib,sname
		#print sfile_loc, os.path.isdir(sfile_loc)
		#raise;
		#e(0)
		#print sfile_loc
		#return os.path.isdir(sfile_loc)
		
	def if_sname_changed(self):
		print 'if_sname_changed'
		#print self.tc_session_name.GetItemData()
		
	def saveSession(self, sess_home=session_home, slib_name='My_Sessions', sname=None, data=None):
		#print '---------------------------saveSession'
		#print len(args[0]), len(args[1]),len(args[2])
		if data:
			#print '---new session'
			#it's a new session
			(sname,copy_vector,tmpl,args,reuse)=data
			sname=sname.strip().strip(' ')
			if reuse:
				(cargs,fargs,targs)=args
				#print 'reuse',reuse
				#e(0)
				#print len(args)
				#print len(cargs),len(fargs),len(targs)
				(reuse_cargs,reuse_fargs,reuse_targs)= self.args_panel.getArgs() 
				if reuse[0]:
					ckeys= [x for x in cargs.keys() if x not in self.args_panel.disabled]
				
					for k in reuse_cargs:
						
						if k in ckeys:
							#print 'adding cargs %s' % k
							#print k, cargs[k][2],self.args_panel.obj[k][1].GetValue()
							cargs[k]=list(cargs[k])
							#val=self.args_panel.obj[k][1].GetValue()
							cargs[k][2]=self.args_panel.obj[k][1].GetValue().strip()
				if reuse[1]:
					for k in reuse_fargs:
						
						if k in fargs.keys():
							#print 'adding fargs %s' % k
							#print k, fargs[k][2], self.args_panel.obj[k][1].GetValue()
							fargs[k]=list(fargs[k])
							#val=self.args_panel.obj[k][1].GetValue()
							fargs[k][2]=self.args_panel.obj[k][1].GetValue().strip()	
				#if reuse[2]:
					for k in reuse_targs:	
						
						if k in targs.keys():
							#print 'adding targs %s' % k
							#print k, targs[k][2], self.args_panel.obj[k][1].GetValue()
							targs[k]=list(targs[k])
							#val=self.args_panel.obj[k][1].GetValue()
							targs[k][2]=self.args_panel.obj[k][1].GetValue().strip()
				args=(cargs,fargs,targs)
				#pprint(fargs)
				#print reuse_targs
				#pprint(targs)
		else:
			#print 'exising session----'
			
			if not sname:
				sname=self.getSessionName()
			if sname: 
				(copy_vector,tmpl,args)=[ self.getCopyVector(), '.'.join(self.getTemplates()), self.args_panel.getArgs()]
			#print len(args[0]), len(args[1]),len(args[2])
			#assert self.session_name==sname, 'session name changed!'
		#print sess_home
		#print self.save_to_dir
		#e(0)
		#if not os.path.isdir(sess_home):
		#	os.makedirs(sess_home)
		if sname:
			
			#sname=self.getSessionName()
			#print self.tmpl
			#print self.copy_vector
			#print sname
			#pprint((sname,copy_vector,tmpl,args)) 
			fname='%s;%s;%s.p' % ('.'.join(copy_vector), tmpl,sname)
			#print fname
			#print copy_vector
			#print tmpl
			#print sname
			
			#print '#'*60
			#print sess_home
			#print slib_name
			#a=1/0
			save_to_dir=os.path.join(sess_home,slib_name)
			assert os.path.isdir(save_to_dir), 'Cannot save new session to\n%s' % save_to_dir
			save_to_file=os.path.join(save_to_dir, fname)
			
			#print save_to_file
			#print sname
			#print copy_vector
			#print tmpl
			#print args
			#print
			#print len(args[0]), len(args[1]),len(args[2])
			#e(0)
			#args=self.obfuscate(args)
			#print len(args[0]), len(args[1]),len(args[2])
			import pickle
			pickle.dump( [sname,copy_vector, tmpl, args], open( save_to_file, "wb" ) )
			#print save_to_dir
			#print self.save_to_dir
			
			#e(0)
			if self.session_name:
				if (self.save_to_dir not in [save_to_dir]) or (sname not in [self.session_name] and self.session_name):
					#copy session details
					to_dir=os.path.join(save_to_dir,sname)
					#print self.save_to_dir,self.session_name
					from_dir=os.path.join(self.save_to_dir,self.session_name)
					#os.mkdir(to_dir)
					#print from_dir
					#print to_dir
					if not os.path.isdir(to_dir):
						shutil.copytree(from_dir, to_dir)
			self.btn_save.Enable(False)	
			self.session_name=sname
			self.changed=[]
			self.saved=True
			return (sname,copy_vector, tmpl,save_to_dir, fname)
		else:
			self.saved=True
			return (None,None, None,None, None)
			
	def obfuscate(self, data):
		
		for k in data[1]:
		
			if 'passwd' in k:	
				#print k
				#print data[1][k]
				#e(0)
				data[1][k]=list(data[1][k])
				data[1][k][2]=base64.b64encode(data[1][k][2])
		for k in data[2]:
			#print k
			if 'passwd' in k:				
				#print k
				#print data[2][k]
				#a=1/0
				data[2][k]=list(data[2][k])
				data[2][k][2]=base64.b64encode(data[2][k][2])	
		#e(0)
		return data	
	def OnNewButton(self, event):
		if 1:
			#print self.session_name, 'self.session_name
			defaults=None
			if self.copy_vector and self.tmpl:
				defaults=(self.copy_vector, self.tmpl)
			#print self.sm.slib_name
			#e(0)
			gc.collect()
			dlg = NewSessionDialog(self, -1, "Create new session.", size=(750, 500),				
							 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
							 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
							 useMetal=False, data=self.data, slib=self.sm.slib_name, values_source=self.session_name,
							 defaults=defaults
							 )
			#dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			#print wx.ID_OK, ID_EXIT, val
			if val == wx.ID_OK:
				if 1:					
					(sname,slib, cv,tmpl,api_args,reuse)= dlg.getConfig()
					#print tmpl
					#e(0)
					#tmpl=self.get_template()
					#api_args=self.api_args[tmpl]
					#print '-----',self.tc_sname.GetValue(),self.copy_vector, tmpl
					data=(sname,cv,tmpl,api_args,reuse)
					slib_name=slib #self.getActiveLibName()
					(sname,cv,tmpl,dname,fname)=self.saveSession(data=data,slib_name=slib_name)
					#sess_home=session_home, slib_name='My_Sessions', sname
					#send("create_new_session", (sname,cv, tmpl,api_args,reuse) )
					send('add_session',(sname,cv,tmpl,dname,fname,slib_name))

			##print gc.get_count()
			dlg.Destroy()
			#print gc.get_count()
			#[self.sname, self.copy_vector, self.tmpl, self.args]=dlg.getConfig()
			#print conf
			#print val
			#self.saveSession(self.args)
			#self.set_new_session([self.sname, self.copy_vector, self.tmpl]+[self.get_api_args(data[1], data[2])])
			#e(0)


	def get_api_args(self,cv,tmpl):
		api_file= os.path.join(home,aa_dir,cv[0],'%s-%s.py' % tuple(cv))
		
		assert os.path.isfile(api_file), 'api_file %s does not exists.' % (api_file)
		apimod=import_module(api_file)
		self.api_args=apimod.aa
		#tmpl=data[2]
		#print self.api_args[tmpl]
		return self.api_args[tmpl]
		
	def get_session_args(self,fname):
		session_api_file = fname
		
		assert os.path.isfile(session_api_file), 'session_api_file %s does not exists.' % (session_api_file)
		#unpickle
		import pickle
		#print self.sname,self.copy_vector, self.tmpl
		(self.sname,self.copy_vector, self.tmpl, session_args) = pickle.load( open( session_api_file, "rb" ) )
		#print self.sname,self.copy_vector, self.tmpl
		#self.session_args
		#apimod=import_module(session_api_file)
		#self.api_args=apimod.aa
		#tmpl=data[2]
		#print self.api_args[tmpl]
		#session_args=self.unobfuscate(session_args)
		return session_args
	def unobfuscate(self,data) 	:
		#pprint(data)
		for k in data[1]:
			#print '--k--',k
			if 'passwd' in k:
				data[1][k]=list(data[1][k])
				try:
					data[1][k][2]=base64.b64decode(data[1][k][2])
				except:
					e = sys.exc_info()[0]
					#print sys.exc_info()
		for k in data[2]:
			if 'passwd' in k:				
				#print 'data[2][k]', data[2][k]
				data[2][k]=list(data[2][k])
				try: 
					data[2][k][2]=base64.b64decode(data[2][k][2])
				except:
					e = sys.exc_info()[0]
					#print sys.exc_info()
		return data	
		
	def open_session(self,data):
			#print '22222222222222open_session222222222222222222'
			#print len(data)
			(self.sname,self.copy_vector,self.type, self.tmpl,self.sdir,self.fname) = data
			self.setSessionName(self.sname)
			self.setCopyVector(self.copy_vector)
			#print self.tmpl
			#print sname,copy_vector,tmpl
			self.setTemplates(self.tmpl)
			self.setType(self.tmpl)
			#print len(self.cargs),len(self.fargs),len(self.targs)
			sess=self.get_session_args(os.path.join(self.sdir,self.fname))
			#pprint(sess.keys())
			(self.cargs,self.fargs,self.targs)=sess
			#print len(self.cargs),len(self.fargs),len(self.targs)
			
			ids=None

			if 1:
				sn = self.sname
				if not sn in self.sids.keys():
					ids=[wx.NewId(),wx.NewId(),wx.NewId()]
					self.sids[sn]=ids
					self.the_id=ids
					for i in self.the_id:
						if not self.timers.has_key(i):
							self.timers[i]=wx.Timer(self, id=i)
							self.counters[i]=0					
						
							#self.th[i]=self.TimerHandler
							self.Bind(wx.EVT_TIMER, lambda event, i=i: self.TimerHandler (event, the_id=i), id=i)					
				else:
					self.the_id=self.sids[sn]


			self.btn_run.SetLabel('Run')
			self.btn_run.SetBackgroundColour(self.c_default)			
			#print 'open_session---------------', ids,self.sname, self.the_id
			#pprint (self.sids)
			nb_tab=self.nb_tab
			#size=(800,500)
			size=self.GetSize()
			#old_panel=self.args_panel
			
			#
			if 0:
				self.nb.DeleteAllPages()
				self.args_panel= pnl_args(self,self.copy_vector,self.tmpl,self.the_id,(self.cargs,self.fargs,self.targs),size=size,style=wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
				#self.nb.DeletePage(0)
				#self.nb.DeletePage(0)
				#old_panel.Destroy()
				self.Freeze()
				self.args_panel.Freeze()
				self.nb.AddPage(self.args_panel, 'Arguments')
				self.editor = TacoTextEditor(self.args_panel)
				self.editor.AppendText(self.args_panel.get_cmd(self.transport))
				self.editor.SetEditable(False)
				self.nb.AddPage(self.editor, 'pre-etl.py')
				self.nb_tab=nb_tab
				
				self.nb.SetSelection(self.nb_tab)
				#self.updateCommand(self.nb_tab)
			else:
				#print len(self.cargs),len(self.fargs),len(self.targs)
				self.args_panel.load_session(self.copy_vector,self.tmpl,self.the_id,(self.cargs,self.fargs,self.targs))
				#print '```````````````EnableTab```````'
				#print len(self.cargs),len(self.fargs),len(self.targs)
				self.nb.EnableTab(0,True)
				send('disable_unused_args', [])
				self.nb.EnableTab(1,True)
				#self.nb.EnableTab(2,True)
				#self.nb.EnableTab(1,True)
				#self.enableLoaderTab() 
				if 0:
					self.sizer.Layout()
					self.sizer.Fit(self.panel)
					self.panel.Layout()
					#self.panel.Fit()
					self.Layout()
				#self.Fit()
			#self.args_panel.Thaw()
			self.enableConfirmTruncate()
			#self.refreshType()
			#self.Thaw()
			#self.nb.SetSize((100,-1))
			self.btn_show.Enable(True)
			self.btn_run.Enable(True)
			self.btn_save.Enable(True)
			self.save_as.Enable(True)			
			self.btn_clearall.Enable(True)
			self.saved=False
			#print len(self.cargs),len(self.fargs),len(self.targs)
			
	def updateCommand(self, page_id=1):
		#print 'updateCommand', page_id
		page_title=self.nb.GetPageText(page_id)
		#print page_title
		if page_title in ['Output']:
			#pprint(self.args_panel.get_cmd(self.transport))
			self.editor.SetEditable(True)
			self.editor.SetText(self.args_panel.get_cmd(self.transport))
			self.editor.SetEditable(False)
			self.editor.Refresh()
	def getLogDir(self):
		return self.args_panel.getLogDir()
	def OnButtonShowLog(self, event):
		#show log location in  explorer
		log_dir=self.getLogDir()
		#print log_dir
		#dirname=os.path.join(home,'qc32','logs')
		#print log_dir
		if not os.path.isdir(log_dir):
			self.Warn('Log dir\n%s\ndoes not exists.' % log_dir)
		else:
			self.ShowLocation(log_dir)
	def ShowLocation(self, dir_or_file):
		EXPLORER = 'C:\\windows\\explorer.exe' 
		if not os.path.isfile(EXPLORER):
			EXPLORER = 'C:\\WINNT\\explorer.exe' 
		os.spawnl(os.P_NOWAIT, EXPLORER, '.', '/n,/e,/select,"%s"' %  dir_or_file)  
	def OnButtonShowInFolder(self, event):
		# 
		btn = event.GetEventObject()
		#save changes
		if_save=self.auto_save.GetValue() 
		if if_save:
			(sname,cv,tmpl,dname,fname)=self.saveSession()
		#create bat file
		ts=time.strftime('%Y%m%d_%H%M%S')
		dirname=os.path.join(home,'run')
		fname = os.path.join(dirname, '%s_%s.bat' % (self.getSessionName(),ts))
		if not os.path.isdir(dirname):
			os.makedirs(dirname)
		f=open(fname,'w')
		cmd=self.args_panel.get_cmd(self.transport)
				
		if_yes=True #self.send_yes.GetValue()
		yes=''
		if if_yes:
			yes='echo y|'		
		f.write('%s%s' % (yes,cmd))
		f.close()
			
		
	
		EXPLORER = 'C:\\windows\\explorer.exe' 
		if not os.path.isfile(EXPLORER):
			EXPLORER = 'C:\\WINNT\\explorer.exe' 
		os.spawnl(os.P_NOWAIT, EXPLORER, '.', '/n,/e,/select,"%s"'%fname)

	def get_title(self):
		#print self.copy_vector
		return '%s: %s->%s' % (self.session_name,conf.dbs[self.copy_vector[0].upper()],conf.dbs[self.copy_vector[1].upper()])
	def updateTimeStamp(self):
		ts=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
		self.args_panel.obj['time_stamp'][1].SetValue(ts)
	def onRunSession(self, data, extra1, extra2=None):
		self.run_session(self.btn_run)			
	def OnButtonRun(self, event):
		# 
		btn = event.GetEventObject()
		self.run_session(btn)
	def run_session(self, btn):
			the_id=self.the_id[2]
			
			title=self.get_title()
			#print the_id, title
			#pprint(self.p.keys())
			#print 'OnButtonRun'
			#pprint(self.p)
			#print len(self.cargs),len(self.fargs),len(self.targs)
			if self.p.has_key(the_id) and self.p[the_id]:
				#window1 = find_window(title)
				#print window1
				
				if self.hwnd.has_key(the_id):
					hwnd=self.hwnd[the_id]
				else:
					while not hwnd:
						hwnd=self.get_hwnds_for_pid(self.p[the_id].pid)
								
				#print window1.SetFocus()
				(x,y) = self.GetScreenPositionTuple()
				(l,w) =self.GetClientSizeTuple()
				dl,dw= self.GetSize()
				#print window1.SetWindowPos(0, (x/2,y/2,dl,dw),0)
				if 0:
					window1 = find_window(title)
					window1.ShowWindow()
					window1.SetFocus()
				win32gui.SetWindowPos (hwnd[0],  0, x/2,y/2, dl, dw, 0)
				#print(dir(win32gui))
				#win32gui.SetActiveWindow(hwnd[0])
				#win32gui.BringWindowToTop(hwnd[0])
				#win32gui.EnableWindow(hwnd[0],True)
				#win32gui.SetFocus(hwnd[0])
				win32gui.ShowWindow(hwnd[0], win32con.SW_SHOWNORMAL)
				#win32gui.ShowWindow(whnd, win32con.SW_SHOWNORMAL) # SW_RESTORE does not work 
				win32gui.SetForegroundWindow(hwnd[0])
				#print dir(window1)
				#win32con.HWND_TOPMOST
			else:
				#print len(self.cargs),len(self.fargs),len(self.targs)
				if self.validateOnRun():
					msg='Are you sure you want to execute this command?\n%s' % self.args_panel.get_cmd(self.transport)
					yes=True
					if_run=self.confirm_run.GetValue()
					if if_run:
						if not self.send_email.GetValue():
							msg='%s\n\nSend email: NO (Check "Post-etl email" to enable).' %msg
						else:
							msg='%s\n\nSend email: YES (Check "Post-etl email" to disable).' %msg
						yes= self.if_yes_2( msg, 'Confirmation.')
					else:
						if_run=True
						
					if if_run and yes:
						self.updateTimeStamp()
						#time_stamp=datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')
						
						btn.SetLabel('Running...(0)')
						cmd=self.args_panel.get_cmd_line_new(self.transport)
						#pprint (cmd)

						if_save=self.auto_save.GetValue() 
						if if_save:
							#print 'if_save'
							(sname,cv,tmpl,dname,fname)=self.saveSession()
							
						
						#yes=''
						#if if_yes:
						#	yes='echo y|'
			
						cfg=[]
						if 1:
							import shlex 
							#cmd2=''.join(cmd.split('^\n'))
							#print cmd
							lexer=shlex.shlex(cmd)
							#lexer = shlex.shlex(input)
							lexer.quotes = '"'
							#lexer.wordchars += '\''
							lexer.whitespace_split = True
							lexer.commenters = ''
							cfg = list(lexer)
							#cfg=['start',"'%s'" % title] + cfg
							#C:\app\alex_buz\product\11.2.0\dbhome_2\BIN\sqlplus.exe SCOTT/tiger2@orcl @C:\Users\alex_buz\Documents\GitHub\DataBuddy\test\test_connnect\Oracle.sql
							#C:\Users\alex_buz\Documents\GitHub\DataBuddy\qc32\qc32.exe -t "^|" -w "ora11g2ora11g" -r "1" -o "1" -q "C:\Python27\data_migrator_1239\test\v101\query\oracle_query.sql" -b "orcl" -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -z"C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -j "SCOTT" -x "tiger2" -d "orcl" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -p "tiger2" -m "YYYY-MM-DD HH24.MI.SS.FF2" -u "SCOTT" -e "YYYY-MM-DD HH24.MI.SS" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -a "SCOTT.Partitioned_test_to" -G "part_15"
							if 0:
								p = Popen(cfg, stdin=PIPE, stdout=PIPE, shell=True ) #creationflags=CREATE_NEW_CONSOLE
								#print p
								out, err = p.communicate()
								#print out, err
								p.wait()
							else:
								#py
								#

								if 0:
									#pprint(cfg)
									nls_timestamp_format=self.args_panel.obj['nls_timestamp_format'][1].GetValue()
									nls_timestamp_tz_format=self.args_panel.obj['nls_timestamp_tz_format'][1].GetValue()
									if 1:
										if nls_timestamp_format:
											os.environ['NLS_TIMESTAMP_FORMAT'] = nls_timestamp_format
										else:
											os.environ['NLS_TIMESTAMP_FORMAT'] =''
										if nls_timestamp_tz_format:
											os.environ['NLS_TIMESTAMP_TZ_FORMAT'] = nls_timestamp_tz_format
										else:
											os.environ['NLS_TIMESTAMP_TZ_FORMAT'] =''	
								if 1:

									# Create pipe for communication
									self.pipeout, self.pipein = os.pipe()

									# Prepare to pass to child process
									if sys.platform == "win32":
										self.curproc = _subprocess.GetCurrentProcess()
										#pprint (dir(curproc))
										pipeouth = msvcrt.get_osfhandle(self.pipein)
										self.pipeoutih = _subprocess.DuplicateHandle(self.curproc, pipeouth, self.curproc, 0, 1,
												_subprocess.DUPLICATE_SAME_ACCESS)

										self.pipearg = str(int(self.pipeoutih))   
										#print self.pipearg
									else:
										pipearg = str(self.pipein)

							
									


								
								if exe:	#exe										
									cfg=cfg+['-X','1'] +['-spID', self.pipearg]
									#pprint (cfg)
									p = Popen(cfg, creationflags=CREATE_NEW_CONSOLE,close_fds=ON_POSIX) #stderr=PIPE, stdout=PIPE,
								else:	#py
									cfg[0]=r'%s\datamule.py' % transport_home
									cfg=cfg+['-X','1']+['-spID',self.pipearg]
									#pprint (cfg)
			
									p = Popen([sys.executable]+cfg, creationflags=CREATE_NEW_CONSOLE,close_fds=ON_POSIX) #stderr=PIPE, stdout=PIPE,
									#p.wait()
								if 1:
									#ON_POSIX = 'posix' in sys.builtin_module_names

									def enqueue_output(out, queue):
										for line in iter(out.readline, b''):
											queue.put(line)
										#out.close()
										
									q= Queue()
									import io
									# Write to child (could be done with os.write, without os.fdopen)
									self.pipefh = io.open(self.pipeout, 'r') #os.fdopen(pipeout, 'r',0)
									t = Thread(target=enqueue_output, args=(self.pipefh, q))
									t.daemon = True # thread dies with the program
									t.start()
									self.q[the_id]=(t,q)
									os.close(self.pipein)
									#if sys.platform == "win32":
									#	self.pipeoutih.Close()
								if 1:
									hwnd=None
									while not hwnd:
										self.hwnd[the_id]=self.get_hwnds_for_pid(p.pid)
										hwnd=self.hwnd[the_id]
									#print hwnd
									#e(0)
									#pprint(dir(win32gui))
									#(x,y) = self.GetScreenPositionTuple()
									#(l,w) =self.GetClientSizeTuple()
									#dl,dw= 600,400
									
									the_id=self.the_id[2]
									#print self.the_id,the_id
									
									self.btn[the_id]=btn #event.GetEventObject()
									sn=self.session_name
									#print sn
									self.p[the_id]=p
									self.timers[the_id].Start(1000)
									
									win32gui.SetWindowText (hwnd[0], title)
									#print title
									#e(0)
									#sending 'y' to job
									if 1: #if_yes:
										window1 = find_window( title )
										#print window1
										#sleep(0.2)
										#hwnd= self.get_hwnds_for_pid (p.pid)
										#print hwnd
										#s_app_name
										#win32gui.SetWindowPos (hwnd[0],  win32con.HWND_TOPMOST, x,y, 850, 500, 0)
										(x,y) = self.GetScreenPositionTuple()
										(l,w) =self.GetClientSizeTuple()
										dl,dw= self.GetSize()
										#self.SetDimensions(x+(l-dl)/2, y+(w-dw)/2, dl,dw)
										window1.SetWindowPos(0, (x/2,y/2,dl,dw),0)
										 #win32con.HWND_TOPMOST, x,y, 850, 500, 0)
						 
										send_yes( window1)
									
									if_confirm_truncate=self.confirm_truncate.GetValue()
									yes_truncate=self.ifTruncateTarget()
									#print '````', yes_truncate, if_confirm_truncate
									if yes_truncate and if_confirm_truncate:
										yes_truncate= self.if_yes('Truncate target')
									
									if yes_truncate:
										window1 = find_window( title )
										(x,y) = self.GetScreenPositionTuple()
										(l,w) =self.GetClientSizeTuple()
										dl,dw= self.GetSize()
										window1.SetWindowPos(0, (x/2,y/2,dl,dw),0)
						 
										send_yes( window1)
									else:
										window1 = find_window( title )
										(x,y) = self.GetScreenPositionTuple()
										(l,w) =self.GetClientSizeTuple()
										dl,dw= self.GetSize()
										window1.SetWindowPos(0, (x/2,y/2,dl,dw),0)
						 
										send_no( window1)
										
									#p.wait()
									#print 'after p'
									if 1:
										
										#os.close(self.pipein)
										if sys.platform == "win32":
											self.pipeoutih.Close()
										if 0:
											line=' '
											while 1:
											#for i in range(100):
												try:  line = q.get_nowait() # or q.get(timeout=.1)
												except Empty:
													pass
													#print('no output yet')
												else: # got line
													#print 2, line
													self.pipefh.close() 
													break
												#time.sleep(1)
									if 0:
										#subproc = subprocess.Popen(['python', 'child_in.py', pipearg], close_fds=ON_POSIX)

										# Close read end of pipe in parent
										os.close(self.pipein)
										if sys.platform == "win32":
											self.pipeoutih.Close()
										if 0:
											import io
											# Write to child (could be done with os.write, without os.fdopen)
											pipefh = io.open(self.pipeout, 'r') #os.fdopen(pipeout, 'r',0)
											#while 1:
											# Wait for the child to finish
											#pprint(dir(pipefh))
											#for i in range(100):
											#print pipefh.closed, pipefh.tell(), pipefh.isatty()
											test= pipefh.read()
											#print 1, test	
											#time.sleep(1)
											pipefh.close()
											#p.wait()
									
								#disable form
								self.DisableOnRun()
								send('highlight_session',(self.session_name,wx.BLACK))
								self.last_log_dir[self.session_name]=self.getLogDir()
								self.EnableShowDumpButton()
								
	def validateOnRun(self):
		if self.if_generic_tremplate():
			return True
		else:
						
			obj=self.args_panel.obj
			msg=''
			keys= [k for k in sorted(obj.keys()) if self.args_panel.checks[k].GetValue()]  #  if k not in ['email_to']
			for k in keys:
				val=obj[k][1].GetValue()
				if not (val and val.strip('"') and val.strip(' ')):
					
					if k in ['email_to']:
						if self.if_send_email():
							msg='%s\nERROR: "%s" is not set.' % (msg,k)
							msg='%s\nHINT: Uncheck "Post-etl Email" to pass email validation.\n' % msg
					else:
						msg='%s\nERROR: "%s" is not set.' % (msg,k)
			if msg:
				msg='Some arguments are not set:\n%s' % msg
				self.Warn(msg,'Validation log.')
				return False 
			return True
	def DisableOnRun(self):
		self.args_panel.DisableAll()
		self.btn_delete.Enable(False)
		self.btn_clearall.Enable(False)
		self.tc_session_name.Enable(False)
	def EnableAfterRun(self):
		self.args_panel.EnableAll()
		self.btn_delete.Enable(True)
		self.btn_clearall.Enable(True)
		self.tc_session_name.Enable(True)		
	def exec_cmd(self, title, cmd):
		#print r'start "%s" cmd.exe  /k "%s"' % (title, cmd)
		os.system(r'start "%s" cmd.exe  /k "%s"' % (title, cmd))
	def OnVectorButton(self, event,params):
		(loc)=params
		#print (loc)
		#print dir(event)
		#btn=event.GetEventObject()
		#print btn.GetPosition()
		#print btn.GetSize()
		#print btn.GetPosition()[0]
		btn = event.GetEventObject()
		#import flat_menu2
		# Create the popup menu
		#self.CreateLongPopupMenu()
		self.CreateVectMenu(loc)

		# Postion the menu:
		# The menu should be positioned at the bottom left corner of the button.
		btnSize = btn.GetSize()

		# btnPt is returned relative to its parent 
		# so, we need to convert it to screen 
		btnPt  = btn.GetPosition()
		btnPt = btn.GetParent().ClientToScreen(btnPt)
		#self._longPopUpMenu.SetOwnerHeight(btnSize.y)
		#self._longPopUpMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
		self._vectMenu.SetOwnerHeight(btnSize.y)
		self._vectMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)
	def CreateVectMenu(self,loc):

		if 1 or not self._popUpMenu.has_key(loc):
			#print self.list.data[loc]
			pmenu=FM.FlatMenu()
			self._vectMenu = pmenu
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			#subMenu = FM.FlatMenu()
			#subSubMenu = FM.FlatMenu()
			id=wx.ID_ANY
			# Create the menu items
			#relative_path=self.getVarsToPath()
			for id in range(10):
				#path=self.hist_btn.keys()[id]
				#loc_to=self.hist_btn[path]
				
				itype=wx.ITEM_NORMAL
				#print '>>>>>>>>>>>>>>',relative_path,path
				if 3==id:
					itype=wx.ITEM_CHECK
				menuItem = FM.FlatMenuItem(pmenu, wx.ID_ANY, '%s' % ( id), "", itype)
				#print item[0], self.list.nav_list['vars'][loc],  item[0]==self.list.nav_list['vars'][loc]
				pmenu.AppendItem(menuItem)				
				if 3==id:
					menuItem.Check(True)
					#subMenu.UpdateItem(menuItem)
					#print menuItem.IsChecked(), menuItem.IsCheckable()
					#menuItem.Enable(False)
				#pmenu.AppendRadioItem(wx.ID_ANY,menuItem)

				#print menuItem.isChecked()
				#print menuItem.IsChecked(), menuItem.IsChecked()
				#menuItem.Enable(True)
				#self.Bind(FM.EVT_FLAT_MENU_SELECTED, self.OnMenu, id=20001+key)
				#
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnVectMenu,(3,id))		
	def OnVectMenu(self, event, params):
		(a,b) = params
		#print a,b	
	def onRadioButton(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
		#print self.txt_transport.GetLabel()
		self.txt_transport.SetLabel('.\qc32\qc%s.exe' % label[:2])
		if 0:
			message = "You just selected %s" % label
			dlg = wx.MessageDialog(None, message, 'Message', 
								   wx.OK|wx.ICON_EXCLAMATION)
			dlg.ShowModal()
			dlg.Destroy()
		
	def onTransportLoc(self, data, extra1, extra2=None):		
		(tloc) = data
		#print tloc
		self.txt_transport.SetLabel(tloc[0])

	def loadFile(self, event):
		
		openFileDialog = wx.FileDialog(self, "Path to DataMigrator (dm*.exe)", self.home, "", 
			"exe files (*.exe)|*.exe", 
			wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		openFileDialog.ShowModal()
		tloc= openFileDialog.GetPath()
		send( "set_transport_location", (tloc,) )
		openFileDialog.Destroy()
		if 0 and tloc:
			self.rb_transport.Enable(True)
			self.txt_transport.Value=tloc

	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			

	def OnExit(self,e):
		#print self.changed
		if (self.changed  ) and self.if_yes('Do you want to save changes?','Application exit.'):
			send('save_args',())
			#(sname,cv,tmpl,dname,fname)=self.saveSession()
			#self.loader_panel.Save()
		else:
			pass
		self.Close(True)
	def onAboutDlg(self, event,params):
		(data)=params
		
		info = wx.AboutDialogInfo()
		info.Name = __appname__
		info.Version = __version__
		if __copyright__:
			info.Copyright = __copyright__
		info.Description = wordwrap(
			#'This is session manager for  <b><a href="https://github.com/DataMigrator/DataMigrator-for-Oracle">DataMigrator</a></b>.</p>',
			'Manages "QueryCopy" sessions \nfor data spool, load, copy.',
			350, wx.ClientDC(self.panel))
		if __github__:
			info.WebSite = (__github__, "%s Github" % __appname__)
		info.Developers = [__maintainer__]
		info.License = wordwrap("Open source", 500, wx.ClientDC(self.panel))
		# Show the wx.AboutBox
		wx.AboutBox(info)		
	def onAboutHtmlDlg(self, event):
		aboutDlg = AboutDlg(None)
		aboutDlg.Show()		
	def OnClose(self, event):
		#self.ticker.Stop()
		self.Destroy()
class AboutDlg(wx.Frame): 
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title="About %s" % __title__, size=(300,300))
		html = wxHTML(self) #
		page="""
<h2>%s</h2>						
<p>Ad-hoc data migrator for Oracle 11G.</p>
<p>Author: %s (<a href="mailto:alexbuzunov@gmail.com?subject=%s issue&body=Hi, Alex. Here's a screenshot and description of a problem.">Support</a>)</p>
<p><b>Software used in making this tool:</h3></p>
<p><b><a href="http://www.python.org">Python 2.7</a></b></p>
<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>
		""" % (__title__,__author__,__title__)
		
		html.SetPage(
			page
			)
		self.Center()
		#self.SetSize((300,300))
		#self.Fit()
		self.Refresh()
class AboutDlg2(wx.Frame): 
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, title="About %s" % __title__, size=(300,300))
		html = wxHTML(self) #ab95022@imcnam.ssmb.com
		page="""
<h2>%s</h2>						
<p>Ad-hoc data migrator for Oracle 11G.</p>
<p>Author: %s (<a href="mailto:alexbuzunov@gmail.com?subject=%s issue&body=Hi, Alex. Here's a screen-shot and description of a problem.">Support</a>)</p>
<p><b>Software used in making this tool:</h3></p>
<p><b><a href="http://www.python.org">Python 2.7</a></b></p>
<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>
		""" % (__title__,__author__,__title__)
		
		html.SetPage(
			page
			)
		self.Center()
		#self.SetSize((300,300))
		#self.Fit()
		self.Refresh()

class NewDialog ( wx.Dialog ):
	def __init__( self, parent, msg=wx.EmptyString , title=wx.EmptyString, style= wx.DEFAULT_DIALOG_STYLE ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY,  title = title, pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = style )

		#set the minimum Size of the frame to Fit()
		self.SetSizeHintsSz( wx.Size( 300,-1 ), wx.DefaultSize )

		fgSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.NO_FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN )
		gSizer = wx.GridSizer( 1, 1, 0, 0 )

		self.m_staticText = wx.StaticText( self.m_panel, wx.ID_ANY, u"test", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText.Wrap( 300 )
		gSizer.Add( self.m_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel.SetSizer( gSizer )
		self.m_panel.Layout()
		gSizer.Fit( self.m_panel )
		fgSizer.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 5 )
		self.m_panel.SetBackgroundColour("white") 
		m_sdbSizer = wx.StdDialogButtonSizer()
		self.m_sdbSizerOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer.AddButton( self.m_sdbSizerOK )
		self.m_sdbSizerCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer.AddButton( self.m_sdbSizerCancel )
		m_sdbSizer.Realize()

		fgSizer.Add( m_sdbSizer, 1, wx.ALL|wx.EXPAND, 5 )
		self.SetSizer( fgSizer )
		self.Layout()
		#self.Center()
		self.Centre( wx.BOTH )
		#self.setMessageLine(10)
		self.m_staticText.SetLabel(msg)
		self.Fit()
		self.m_sdbSizerOK.SetFocus()

	def setMessageLine(self, messageLine):
		msg = ""
		for i in range(0, messageLine):
			msg += "Line %d \n" % i

		self.m_staticText.SetLabel(msg)
		self.Fit()

class wxHTML(wx.html.HtmlWindow):	
	def OnLinkClicked(self, link):
		webbrowser.open(link.GetHref())
def incrcounter(n):
    global _count
    _count = _count + n

def savecounter():
    open("counter", "w").write("%d" % _count)	