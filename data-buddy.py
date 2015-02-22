# Title: 	data-buddy
# Description:
#			Session manager for DataMigrator.		
# Environment:
#			Python 2.7 and wxPython 2.8		
#
__author__ = "Alex Buzunov"
__copyright__ = "Copyright 2015, SequelWorks Inc."
__credits__ = []
__license__ = "GPL"
__title__ = "data-buddy"
__version__ = "1.23.9"
__maintainer__ = "Alex Buzunov"
__email__ = "alexbuzunov@gmail.com"
__status__ = "Development" 	


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
import webbrowser
import wx.html 
from tc_lib import sub, send
from collections import OrderedDict
import imp
from editor import TacoTextEditor
import base64
import __builtin__
__builtin__.copy_vector = None
__builtin__.cvarg = None

import common.v101.config as conf
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
	
########################################################################
e=sys.exit
blog=cu.blog
home=os.path.dirname(os.path.abspath(__file__))
aa_dir='args_api'
ID_EXIT = wx.NewId()
ID_CREATE = wx.NewId()
ID_ABOUT = wx.NewId()
LOAD_FILE_ID = wx.NewId()
update_cache=True
dBtn='N/A'
tr='qc'


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
	def __init__(self, splitter, parent, frame, id,pos):
		wx.ListCtrl.__init__(self, splitter, id, style=
										wx.LC_REPORT
										)

		self.parent=parent
		self.images = [ 'bmp_source/arrow_sans_up_16.png', 'bmp_source/arrow_sans_down_16.png','bmp_source/arrow_sans_up_16.png', \
		'bmp_source/Right_Arrow_16.png', 'bmp_source/Left_Arrow_16.png', 'bmp_source/folder_16.png'  \
		 , 'bmp_source/config_16.png','bmp_source/database-sql_16.png', 'bmp_source/database_share_16.png', \
		 'bmp_source/database_connect_16.png','bmp_source/user_16.png','bmp_source/database_table_16.png', \
		'bmp_source/table_select_column_16.png','bmp_source/database_red_16.png',
		'bmp_source/database_green_16.png',
		'bmp_source/database_blue_16.png',
		'bmp_source/database_black_16.png','bmp_source/file_16.png',]
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
		self.save_to_dir=frame.save_to_dir
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
		return self.GetItemText(self.GetFirstSelected())

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
		self.InsertColumn(1, 'From')
		self.InsertColumn(2, 'To')
		self.InsertColumn(3, 'Type')
		self.InsertColumn(4, 'Template')
		#self.InsertColumn(4, 'Desription')

		self.SetColumnWidth(0, 175)
		self.SetColumnWidth(1, 60)
		self.SetColumnWidth(2, 60)
		self.SetColumnWidth(3, 60)
		self.SetColumnWidth(4, 180)

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
		flist={}
		i=0
		for f in os.listdir(self.save_to_dir):
			cv, tmpl,name= f.split(';')
			name=name.split('.')[0]
			type='Copy'
			if tmpl.startswith('CSV'):
				type='Load'
			if '.CSV_' in tmpl:
				type='Spool'
			flist[i] = [name,cv.split('.')[0],cv.split('.')[1],type,tmpl,self.save_to_dir,f]
			i +=1
		self.data[self.current_list]= flist
	def getList(self):
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
	def __init__(self, parent, frame, pos, panel_pos # log
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

			self.list = SessionList(self.listsplit, self, frame, -1,self.pos)
			

			self.filter =self.getFilter(self,self.list)
			self.filter_history={}
			self.currentItem = 0
		

		if 1:
			#self.btnHome = wx.Button(self, -1, "[.]", style=wx.BU_EXACTFIT, size=(30,20))
			#self.btnUp = wx.Button(self, -1, "[..]", style=wx.BU_EXACTFIT, size=(30,20))
			

			imageFile = "bmp_source/arrow_back_dgrey_16x2.png"
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				
			self.btnFav = wx.Button(self, -1, "Fav", style=wx.BU_EXACTFIT, size=(30,20))
			#self.btnHist = wx.Button(self, -1, "Hist", style=wx.BU_EXACTFIT, size=(30,20))	
			imageFile = "bmp_source/refresh_icon_16_grey2.png"
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.btn_refresh=wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
			#self.btn_log = wx.Button(self, -1, "Log", size=(25,20))
			#self.btn_refresh = wx.Button(self, -1, "Refresh", size=(30,20)) 
			#self.sPanel.statusbar.Add([self.gauge[pos],self.btn_stop[pos]], 1, wx.EXPAND,1)
			#self.btn_stop[pos].Hide()
			#self.btn_refresh.SetPosition((1,1))
			#self.gen_bind(wx.EVT_BUTTON,self.btn_refresh, self.OnRefreshList,(self.pos))
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
			navig.Add(self.btnFav, 0, wx.LEFT)
			navig.Add(self.btn_refresh, 0, wx.LEFT)
			

			if 1:
				
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
			self.SetAutoLayout(True)

		self.list.setEnvironmentList(('configDirLoc','ConfigList',))
		sub(self.onRefreshList, "refresh_list")
		sub(self.OnAddSession, "add_session")
		
		sub(self.onDeleteSessions, "delete_sessions")
	def onDeleteSessions(self,  data, extra1, extra2=None):
		(items) = data
		#print 
		for i in items.keys():
			self.list.DeleteItem(i)
		self.list.set_data()
		
	def delete_seleted_items_remove(self):
		print 'OnDeleteButton'
		#print self.list.GetSelectedItemCount()
		#print 
		for i in self.list.GetSelectedItems():
			self.list.DeleteItem(i)
							   
	def onRefreshList(self, data, extra1, extra2=None):
		
		print 'onRefreshList'
		self.list.set_data()
		self.RecreateList(None,(self.list,self.filter))
	def OnAddSession(self, data, extra1, extra2=None):
		(sname,cv,tmpl,dname,fname) = data		
	
		session=[sname,cv[0],cv[1],'Copy',tmpl,dname,fname]
		#add
		idx= self.addSession(session)
		#deselect
		index = self.list.GetFirstSelected()
		while index != -1:
			self.list.SetItemState(index, 0, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED)
			index = self.list.GetNextSelected(index)
		#select
		#print 'selecting %s' % idx
		self.list.SetItemState(idx, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED) 
		self.list.EnsureVisible(idx) 
		
		#self.SetItemState(idx, 0, wxLIST_STATE_SELECTED)

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
		
	def OnItemSelected(self, event):
		##print event.GetItem().GetTextColour()
		cnt=self.list.GetSelectedItemCount()
		if cnt==1:
			self.currentItem = event.m_itemIndex
			#print self.currentItem
			ii=self.list.GetItemData(self.currentItem)
			session= self.list.getList()[ii]
			#print session
			send('open_session',(session))
			
		#else:
		#	send('disable_all_for_delete',(cnt))
		event.Skip()		
	
		
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

		if self.count[pos] >= 180:
			self.count[pos] = 0
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count
		
		self.gauge[pos].SetValue(self.count[pos])
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
		imgs= {'default':'bmp_source/database_green_16.png', 'DEV':'bmp_source/database_green_16.png','PROD':'bmp_source/database_red_16.png', \
		'UAT':'bmp_source/database_blue_16.png','QA':'bmp_source/database_black_16.png'}
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
				if keys:
					#print keys
					j=0
					list.DeleteAllItems()
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
							imgs= {'default':'bmp_source/database_green_16.png', 'DEV':'bmp_source/database_green_16.png','PROD':'bmp_source/database_red_16.png', \
							'UAT':'bmp_source/database_blue_16.png','QA':'bmp_source/database_black_16.png'}
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
		print "OnBeginEdit"
		#self.log.WriteText("OnBeginEdit")
		event.Allow()

	def OnItemDelete(self, event):
		print "OnItemDelete"
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

			print 'si',selected_items
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
class SessionListCtrlPanelManager(wx.Panel):
	"""
	This will be the first notebook tab
	"""
	#----------------------------------------------------------------------
	def __init__(self, parent,frame, pos, panel_pos):
		""""""

		wx.Panel.__init__(self, parent,  id=wx.NewId())

		self.pos=pos
		self.panel_pos=panel_pos

		self.parent=parent
		self.frame=frame
		self.nb = fnb.FlatNotebook(self, -1, agwStyle=fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_SMART_TABS|fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
		slp=SessionListCtrlPanel(self,frame, pos,self.panel_pos)
		self.slp=slp
		self.list=slp.list
		self.nb.AddPage(slp,'')
		self.nb.SetPageText(0, 'My Sessions')
		#tmpl=SessionListCtrlPanel(self,pos,self.panel_pos)
		#self.nb.AddPage(tmpl,'Templates')
		
		self.nb.SetSelection(0)
		#self.nb.EnableTab(0,False)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.nb, 1, wx.GROW|wx.EXPAND|wx.ALL, 0)
		self.SetSizer(self.sizer)
		self.SetAutoLayout(True)

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

class NewSessionDialog(wx.Dialog):
	def __init__(
			self, parent, ID, title, size,data, pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent
		self.data=data
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
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.tc_tables={}
		self.shards_btn={}
		self.tmpl={}
		self.copy_vector=[]
		self.userhome = os.path.expanduser('~')
		self.recent_fname= os.path.join(self.userhome,'recent.p')
		self.recent=[]
		if os.path.isfile(self.recent_fname):
			self.recent=self.readRecent()

		if 1:
			#namesizer = wx.BoxSizer(wx.HORIZONTAL)
			namesizer = wx.GridBagSizer(1, 4)			
			
			text1 = wx.StaticText(self, label="Session name:")
			#sizer.Add(text1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)
			self.tc_sname = wx.TextCtrl(self,size=(400,23))
			#namesizer.Add((3,3),0)
			namesizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			
			namesizer.Add(self.tc_sname, pos=(0, 1),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			namesizer.Add((60,3),pos=(0, 2),  flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND|wx.GROW, border=10)
			icon = wx.StaticBitmap(self, bitmap=wx.Bitmap('exec.png'))
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
				for t, details in self.plist.items():
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
			lbl='Click to set'
			self.b_vector = wx.Button(self, label=lbl,size=(100,25))
			#b_vector.Enable(True)
			vboxsizer.Add(self.b_vector, flag=wx.LEFT|wx.TOP, border=0)
			self.b_vector.Bind(wx.EVT_BUTTON, self.OnCVClicked)
			#sizer.Add(boxsizer, pos=(2, 2),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
		optsizer = wx.BoxSizer(wx.HORIZONTAL)	
		#optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)		
		#optsizer.Add((3,3),0)
		optsizer.Add(vboxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)		
		#optsizer.Add((3,3),0)
		#optsizer.Add((5,5),1, wx.EXPAND)
		#optsizer.Add(button4, 0 , wx.RIGHT)
		sizer.Add(optsizer, 0, wx.EXPAND|wx.ALL|wx.GROW, 5)	
		listsizer = wx.BoxSizer(wx.HORIZONTAL)	
		listsizer.Add(self.listCtrl, 1 , wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)	
		listsizer.Add(self.targlistCtrl, 1 , wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL,5)		
		sizer.Add(listsizer, 1, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
		if 1:
			sb = wx.StaticBox(self, label="Source Object")
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			so=['Query', 'Table', 'Partition', 'Sub-Partition']
			s_rb={}
			style=0
			for i in range(len(so)):
				rbname=so[i]
				if not i:
					style=wx.RB_GROUP
				else:
					style=0
				s_rb[rbname]=wx.RadioButton(self, label=rbname,style=style)
				boxsizer.Add(s_rb[rbname], flag=wx.LEFT|wx.TOP, border=5)
				s_rb[rbname].Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)


			optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)	
		if 1:
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

				
			optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)	
		btnsizer = wx.BoxSizer(wx.HORIZONTAL)
		if 1:
			sb = wx.StaticBox(self, label='Arguments')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.rb_use_templates=wx.RadioButton(self, label="Use templates",style=wx.RB_GROUP)
			boxsizer.Add(self.rb_use_templates, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_set_manually=wx.RadioButton(self, label="Set manually")
			boxsizer.Add(self.rb_set_manually, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_use_templates.Bind(wx.EVT_RADIOBUTTON, self.onUseRbButton)
			self.rb_set_manually.Bind(wx.EVT_RADIOBUTTON, self.onUseRbButton)
			btnsizer.Add(boxsizer, 0 , wx.TOP|wx.BOTTOM|wx.LEFT)
			
		self.create_btn = wx.Button(self, wx.ID_OK, "Create")
		self.create_btn.Enable(False)
		btn_exit = wx.Button(self, wx.ID_CANCEL, "Cancel")
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(btn_exit, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.create_btn.Bind(wx.EVT_BUTTON, self.OnCreate)
		btn_exit.Bind(wx.EVT_BUTTON, self.OnExit)
		#self.Bind(wx.EVT_BUTTON, self.OnTrial, id=ID_TRIAL)
		sizer.Add(btnsizer, 0, wx.EXPAND|wx.ALL, 5)


		self.SetSizer(sizer)
		#sizer.Fit(self)
		#self.SetSize((600,400))
		(x,y) = self.parent.GetScreenPositionTuple()
		(l,w) =self.parent.GetClientSizeTuple()
		dl,dw= 600,400
		self.SetDimensions(x+(l-dl)/2, y+(w-dw)/2, dl,dw)
		self.i=0 #menu counter
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSrcTmplSelected, self.listCtrl)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnTargTmplSelected, self.targlistCtrl)
		self.Bind(wx.EVT_LIST_ITEM_DESELECTED, self.OnTargTmplDeselected, self.targlistCtrl)
		self.api_args=None
		if 1:
			apidir= os.path.join(home,aa_dir)
			self.api_from = [ f for f in os.listdir(apidir) if os.path.isdir(os.path.join(apidir,f)) and 'CSV' not in f ]
			#print api_from
			self.api2= list({ f[:2] for f in self.api_from})
			self.api2.sort()
			self.api_menu={}
			for m in self.api_from:
				#print m
				if not self.api_menu.has_key(m[:2]):
					self.api_menu[m[:2]]=[]
				self.api_menu[m[:2]].append(m)
			#print pprint(self.api_menu)
	def getConfig(self):
		tmpl=self.get_template()
		return [self.getSessionName(), self.copy_vector, tmpl, self.api_args[tmpl]]
	def getSessionName(self):
		return self.tc_sname.GetValue()
	def onSourceObjButton(self, event): 
		""" 
		Source object filter
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
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
		if 'MANUALLY' in label.upper():
			self.create_btn.Enable(True)	
		else:
			#print 'targlistCtrl',self.targlistCtrl.GetFirstSelected()
			if self.targlistCtrl.GetFirstSelected()<0:
				self.create_btn.Enable(False)
			else:
				#print 'listCtrl', self.listCtrl.GetFirstSelected()
				if self.listCtrl.GetFirstSelected()<0:
					self.create_btn.Enable(False)

			
	def refresh_src_list(self):
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
		
		for t in self.tmpl.keys():
			self.listCtrl.InsertStringItem(0, t)
		self.create_btn.Enable(False)

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
		for t in self.tmpl[src_val]:
			self.targlistCtrl.InsertStringItem(0, t)
		self.create_btn.Enable(False)
		event.Skip()
	def get_template(self):
		src_tmpl=self.listCtrl.GetItemText(self.listCtrl.GetFirstSelected())
		trg_tmpl=self.targlistCtrl.GetItemText(self.targlistCtrl.GetFirstSelected())
		return '%s.%s' % (src_tmpl, trg_tmpl)
	def OnTargTmplSelected(self,event):
		print str(self.__class__) + " - OnItemSelected"
		self.create_btn.Enable(True)
		if 0:
			if not self.dirty:
				self.dirty = True
				wx.CallAfter(self.Cleanup)
		event.Skip()
		
	def OnTargTmplDeselected(self,event):
		print str(self.__class__) + " - OnItemDeselected"
		self.create_btn.Enable(False)
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
		
		self.writeRecent()
		e.Skip()
	def writeRecent(self):
		#print 'writeRecent'
		#print self.recent
		if self.recent:
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
		print 'OnCreate'
		sname=self.tc_sname.GetValue()
		if not sname:
			self.Warn('Enter session name.')
			self.tc_sname.SetFocus()
		elif self.if_duplicate_name(sname):
			self.Warn('Duplicate session name.')
			self.tc_sname.SetFocus()

		else:
		
			self.writeRecent()
			e.Skip()
		#self.Close(True)
		#return ID_CREATE
	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,name):
		for k,v in self.data.items():
			if name == v[0]:
				return True
		return False
	def OnCVClicked(self, event):
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
		self._popUpMenu.SetOwnerHeight(btnSize.y)
		self._popUpMenu.Popup(wx.Point(btnPt.x, btnPt.y), self)	
	def CreatePopupMenu(self):

		if not self._popUpMenu:
		
			self._popUpMenu = FM.FlatMenu()
			#-----------------------------------------------
			# Flat Menu test
			#-----------------------------------------------

			# First we create the sub-menu item
			
			#subSubMenu = FM.FlatMenu()




			#e(0)
			
			#dbf={'DB':'DB2', 'EX':'Exadata', 'IN', 'MA', 'MY', 'OR', 'PG', 'SL', 'SS', 'SY', 'TT'}
			dbf={'OR':'Oracle', 'SS':'SQLServer', 'MA':'MariaDB', 'MY': 'MySQL', 'PG':'PostgreSQL', 'DB':'DB2', 'TT':'TimesTen', 'SL':'SQLite', 'IN':'Informix', 'SY':'Sybase'}
			
			#pprint(api_from)
			
			# Add sub-menu to main menu
			self.i=0
			#print '-'*20, self.recent
			if 1: #len(self.recent):
				self.i +=1
				self.recentMenu = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, 'Recent', '', wx.ITEM_NORMAL, self.recentMenu)
				self._popUpMenu.AppendItem(menuItem)
				if self.recent:
					for r in self.recent:
						(a,b)=r
						self.i +=1
						#Menu1 = FM.FlatMenu()
						menuItem = FM.FlatMenuItem(self.recentMenu, 20000+self.i, '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
						self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
						self.recentMenu.AppendItem(menuItem)
					
				self._popUpMenu.AppendSeparator()	
			for k in self.api2:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, 'From %s' % dbf[k], '', wx.ITEM_NORMAL, Menu1)
				self._popUpMenu.AppendItem(menuItem)
				if not k in ['OR']:
					menuItem.Enable(False)
				
				for sm in self.api_menu[k]:
					if len(self.api_menu[k])>1:
						self.i +=1
						self.create_Menu2(Menu1,sm,dbf)
						
					else:
						for k2 in self.api2:
							self.i +=1
							if len(self.api_menu[k2])>1:
								self.create_Menu3(Menu1,k2,dbf,from_db=sm)
							else:
								self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm)
			self._popUpMenu.AppendSeparator()	
			for sm in [conf.ff]:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, 'From %s' % sm, '', wx.ITEM_NORMAL, Menu1)
				self._popUpMenu.AppendItem(menuItem)	
				for k2 in self.api2:
					self.i +=1
					if len(self.api_menu[k2])>1:
						self.create_Menu3(Menu1,k2,dbf,from_db=sm)
					else:
						self.create_Menu4(Menu1,self.api_menu[k2][0],from_db=sm)
						
				
		else:
			#pprint(dir(self.recentMenu))
			self.recentMenu.Clear()
			if self.recent:
				for r in reversed(self.recent):
					(a,b)=r
					self.i +=1
					#Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self.recentMenu, 20000+self.i, '%s --> %s' % (conf.dbs[a],conf.dbs[b]), '', wx.ITEM_NORMAL)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
					self.recentMenu.AppendItem(menuItem)

	def create_Menu2(self,Menu1,sm,dbf, from_to='From'):
		self.i +=1
		Menu2 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu1, 20000+self.i, '%s %s' % (from_to, conf.dbs[sm]) , '', wx.ITEM_NORMAL, Menu2)
		Menu1.AppendItem(menuItem)
		#self.set_sub_submenu(subSubMenu,1, 'CSV')
		
		for k2 in self.api2:
			self.i +=1
			if len(self.api_menu[k2])>1:
				self.create_Menu3(Menu2,k2,dbf,from_db=sm)
			else:
				self.create_Menu4(Menu2,self.api_menu[k2][0],from_db=sm)
		#append to_csv
		Menu2.AppendSeparator()
		for s in [conf.ff]:
			self.i +=1
			#Menu1 = FM.FlatMenu()
			menuItem = FM.FlatMenuItem(Menu2, 20000+self.i, 'To %s' % s, '', wx.ITEM_NORMAL)
			self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(sm,s))
			Menu2.AppendItem(menuItem)	
	
	def create_Menu3(self,Menu2,k2,dbf,from_db, from_to='To'):
		self.i +=1
		Menu3 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu2, 20000+self.i, "%s %s" % (from_to, dbf[k2]), "", wx.ITEM_NORMAL, Menu3)
		Menu2.AppendItem(menuItem)
		if not k2 in ['OR']:
			menuItem.Enable(False)
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4(Menu3,sm2,from_db,from_to)	
			

	def create_Menu4(self,Menu3,sm2,from_db, from_to='To'):
		#Menu4 = FM.FlatMenu()
		self.i +=1
		
		menuItem = FM.FlatMenuItem(Menu3, 20000+self.i, "%s %s" % (from_to, conf.dbs[sm2]) , "", wx.ITEM_NORMAL)
		#print from_db,sm2
		self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(from_db,sm2))
		Menu3.AppendItem(menuItem)
		if not sm2 in self.api_menu['OR']:
			menuItem.Enable(False)
		#self.set_sub_submenu(subSubMenu,1, 'CSV')
			

	def set_vector_btn(self,a,b):	
		#print a,b
		lbl='%s->%s' % (a,b)
		self.b_vector.SetLabel(lbl.lower())
		self.copy_vector=[a,b]
		self.refresh_src_list()

	def OnMenu(self, event, params):
		(a,b) = params
		
		if (a,b) not in self.recent:
			self.recent.append((a,b))
		#print '###########', self.recent
		self.set_vector_btn(a,b)
		self.create_btn.Enable(False)
		
		
		


	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

###################################################################################################


class dummy_args(wx.Panel):
	"""Arguments"""
	def __init__(self, parent, style):
		wx.Panel.__init__(self, parent, -1, style=style)
		#self.frame=frame
		ID_TC_MODE = wx.NewId()
		ID_RUN_AT = wx.NewId()
		#self.SetSizer(sizer)
		#sizer.Fit(self)
		self.args_vbox = wx.BoxSizer(wx.VERTICAL)
		self.args_hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.obj={}
		self.api_args=[{'copy_vector': ('-w',
						  '--copy_vector',
						  'dbtde2maria',
						  'Data copy direction.'),
		  'field_term': ('-t', '--field_term', '"|"', 'Field terminator.'),
		  'num_of_shards': ('-r', '--num_of_shards', 3, 'Number of shards.'),
		  'pool_size': ('-o', '--pool_size', 3, 'Pool size.')},
		 {'from_db_name': ('-b',
						   '--from_db_name',
						   '"SAMPLE"',
						   'DB2 Developer Edition source database.'),
		  'from_db_server': ('-n',
							 '--from_db_server',
							 '"DB2"',
							 'DB2 Developer Edition source instance name.'),
		  'from_passwd': ('-x',
						  '--from_passwd',
						  '"198Morgan"',
						  'DB2 Developer Edition source user password.'),
		  'from_table': ('-c', '--from_table', 'Timestamp_test_from', 'From table.'),
		  'from_user': ('-j',
						'--from_user',
						'"ALEX_BUZ"',
						'DB2 Developer Edition source user.'),
		  'source_client_home': ('-z',
								 '--source_client_home',
								 '"C:\\Program Files (x86)\\IBM\\SQLLIB_01\\BIN"',
								 'Path to DB2 Developer Edition client home.')},
		 {'target_client_home': ('-Z',
								 '--target_client_home',
								 '"C:\\Program Files\\MariaDB 10.0\\bin"',
								 'Path to mysql client home.'),
		  'to_db_name': ('-d', '--to_db_name', '"test"', 'Target database.'),
		  'to_db_server': ('-s',
						   '--to_db_server',
						   '"localhost"',
						   'Target db instance name.'),
		  'to_passwd': ('-p',
						'--to_passwd',
						'"maria_pwd"',
						'Target db user password.'),
		  'to_table': ('-a', '--to_table', 'Timestamp_test_to', 'Target table.'),
		  'to_user': ('-u', '--to_user', '"root"', 'Target MariaDB db user.')}]
		(self.cargs,self.fargs,self.targs)= self.api_args		
		if 1: #Common
			
			self.core_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			self.fgs = wx.GridBagSizer(4, 10)
			#sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			#sizer.Add(tc0, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			#fgs = wx.FlexGridSizer(3, 4, 9, 20)
			ttl=['Copy vector','Pool size','Num of shards','Field terminator','Truncate target']
			#pprint(dir(fgs))
			disable=['copy_vector']
			i=0
			for k,v in self.cargs.items()	:
				#print k,v
				short,long,val,desc=v
				self.obj[k]= (wx.StaticText(self.core_args_panel, label=k), wx.TextCtrl(self.core_args_panel,value="", size=(140,22)))
				self.fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				#if k in disable:
				self.obj[k][1].Enable(False)
				i+=1

		
			hbox.Add(self.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			self.core_args_panel.SetSizer(hbox)
			
			self.sb_common = wx.StaticBox(self, label="Common")
			boxsizer = wx.StaticBoxSizer(self.sb_common, wx.VERTICAL)
			boxsizer.Add(self.core_args_panel,1, flag=wx.LEFT|wx.TOP|wx.GROW|wx.EXPAND, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_vbox.Add(boxsizer,1, flag=wx.ALL|wx.EXPAND|wx.GROW|wx.EXPAND, border=5)
		if 1:
			from_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			fgs = wx.GridBagSizer(4, 10)
			i=0
			for k,v in self.fargs.items()	:
				#print k,v
				#print i
				short,long,val,desc=v
				self.obj[k]= (wx.StaticText(from_args_panel, label=k), wx.TextCtrl(from_args_panel,value="", size=(150,22)))
				fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.obj[k][1].Enable(False)
				i+=1
			hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			from_args_panel.SetSizer(hbox)
			
			sb_from = wx.StaticBox(self, label="Source")
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(from_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
		if 1:
			to_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			fgs = wx.GridBagSizer(4, 10)
			i=0
			for k,v in self.targs.items()	:
				#print k,v
				#print i
				short,long,val,desc=v
				self.obj[k]= (wx.StaticText(to_args_panel, label=k), wx.TextCtrl(to_args_panel,value="", size=(150,22)))
				fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.obj[k][1].Enable(False)
				i+=1
			hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			to_args_panel.SetSizer(hbox)
			
			sb_from = wx.StaticBox(self, label="Target")
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(to_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
			

		self.args_vbox.Add(self.args_hbox,1,flag=wx.ALL|wx.EXPAND|wx.GROW)
		self.SetSizer(self.args_vbox)
		self.Fit()


		
###################################################################################################


class default_args(wx.Panel):
	"""Arguments"""
	def __init__(self, parent, style):
		wx.Panel.__init__(self, parent, -1, style=style)
		#self.frame=frame
		ID_TC_MODE = wx.NewId()
		ID_RUN_AT = wx.NewId()
		#self.SetSizer(sizer)
		#sizer.Fit(self)
		self.args_vbox = wx.BoxSizer(wx.VERTICAL)
		self.args_hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		if 1: #Common
			
			self.core_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			self.fgs = wx.GridBagSizer(4, 4)
			#sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			#sizer.Add(tc0, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			#fgs = wx.FlexGridSizer(3, 4, 9, 20)
			ttl=['Copy vector','Pool size','Num of shards','Field terminator','Truncate target']
			#pprint(dir(fgs))
			
			txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Copy vector:'), wx.TextCtrl(self.core_args_panel,value=''))
			#txt_ctrl.Value=
			txt_ctrl.Enable(False)
			self.fgs.Add(txt, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			self.fgs.Add(txt_ctrl, pos=(0, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Field terminator:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='|'))
			self.fgs.Add(txt, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			self.fgs.Add(txt_ctrl, pos=(1, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Pool size:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='1'))
			self.fgs.Add(txt, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			self.fgs.Add(txt_ctrl, pos=(2, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Num of shards:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='1'))
			self.fgs.Add(txt, pos=(3, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			self.fgs.Add(txt_ctrl, pos=(3, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)

			#sb = wx.StaticBox(panel_from, label="Truncate Target:")
			txt=wx.StaticText(self.core_args_panel, label='Truncate target:')
			ynbox =  wx.BoxSizer( wx.HORIZONTAL)
			ynbox.Add(wx.RadioButton(self.core_args_panel, label="Yes",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=0)
			ynbox.Add(wx.RadioButton(self.core_args_panel, label="No"), flag=wx.LEFT|wx.TOP, border=0)
			self.fgs.Add(txt, pos=(0, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
			self.fgs.Add(ynbox, pos=(0, 3), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
			if 0:
				self.fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Field terminator:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='|'))
				self.fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Pool size:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='1'))
				self.fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				
				sb = wx.StaticBox(self.core_args_panel, label="Truncate Target")
			
				ynbox =  wx.StaticBoxSizer(sb, wx.HORIZONTAL)
				ynbox.Add(wx.RadioButton(self.core_args_panel, label="Yes",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=0)
				ynbox.Add(wx.RadioButton(self.core_args_panel, label="No"), flag=wx.LEFT|wx.TOP, border=0)
				
			
				txt_ctrl= ( ynbox)
				self.fgs.AddMany([(txt_ctrl, 0, wx.EXPAND, 5)])
				txt, txt_ctrl= (wx.StaticText(self.core_args_panel, label='Num of shards:'), wx.TextCtrl(self.core_args_panel, size=(20,-1), value='1'))
				self.fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
			
			
			
			
			
			hbox.Add(self.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			self.core_args_panel.SetSizer(hbox)
			
			self.sb_common = wx.StaticBox(self, label="Common")
			boxsizer = wx.StaticBoxSizer(self.sb_common, wx.VERTICAL)
			boxsizer.Add(self.core_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_vbox.Add(boxsizer,1, flag=wx.ALL|wx.EXPAND, border=5)
		if 1: #Source
			
			panel_from = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
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
			sb_from = wx.StaticBox(self, label="Source[%s]" % self.getCopyVector())
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(panel_from, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)

		
		if 1: #Target
			panel_from = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
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
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
		self.args_vbox.Add(self.args_hbox,0,flag=wx.ALL|wx.EXPAND|wx.GROW)
		self.SetSizer(self.args_vbox)
		self.Fit()
	def get_cmd(self,transport):
	
		return r"""%s ^
-w ora2ora ^
-o 1 ^
-r 1 ^
-t "|" ^
-c SCOTT.Date_test_from ^
-f SCOTT/tiger2@orcl ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" ^
-g SCOTT/tiger2@orcl ^
-a SCOTT.Partitioned_test_to ^
-G part_15 ^
-e "YYYY-MM-DD HH24.MI.SS" ^
-m "YYYY-MM-DD HH24.MI.SS.FF2" ^
-O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" ^
-Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"
""" % transport


###################################################################################################

class pnl_args(wx.Panel):
	"""Arguments"""
	
	def __init__(self, parent, copy_vector,tmpl,args_api,style):
		wx.Panel.__init__(self, parent, -1, style=style)
		#self.frame=frame
		global home
		ID_TC_MODE = wx.NewId()
		ID_RUN_AT = wx.NewId()
		self.parent=parent
		#self.SetSizer(sizer)
		#sizer.Fit(self)
		self.args_vbox = wx.BoxSizer(wx.VERTICAL)
		self.args_hbox = wx.BoxSizer(wx.HORIZONTAL)
		self.args=args_api
		self.cargs,self.fargs,self.targs=self.args
		self.copy_vector=copy_vector
		self.tmpl=tmpl
		self.obj={}
		self.tc_length=190
		if 1:
			i=wx.NewId()			
			self.Bind(wx.EVT_TIMER, lambda event, i=i: self.TimerHandler0(event, the_id=i), id=i)
			
			self.timer=wx.Timer(self, id=i)	
		if 1: #Common
			
			self.core_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			self.fgs = wx.GridBagSizer(6, 2)
			#sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			#sizer.Add(tc0, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			#fgs = wx.FlexGridSizer(3, 4, 9, 20)
			ttl=['Copy vector','Pool size','Num of shards','Field terminator','Truncate target']
			#pprint(dir(fgs))
			disable=['copy_vector']
			i=0
			for k,v in self.cargs.items()	:
				#print k,v
				short,long,val,desc=v
				row=i%4
				col=(i-i%2)
				#print 'row',row, 'col', col
				self.obj[k]= (wx.StaticText(self.core_args_panel, label=k), wx.TextCtrl(self.core_args_panel,value=str(val).strip('"'), size=(100,22)))
				self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
				self.fgs.Add(self.obj[k][0], pos=(i%2, col), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				self.fgs.Add(self.obj[k][1], pos=(i%2, col+1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
				if k in disable:
					self.obj[k][1].Enable(False)
				i+=1
			if 0:

				#sb = wx.StaticBox(panel_from, label="Truncate Target:")
				txt=wx.StaticText(self.core_args_panel, label='Truncate target:')
				ynbox =  wx.BoxSizer( wx.HORIZONTAL)
				ynbox.Add(wx.RadioButton(self.core_args_panel, label="Yes",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=0)
				ynbox.Add(wx.RadioButton(self.core_args_panel, label="No"), flag=wx.LEFT|wx.TOP, border=0)
				self.fgs.Add(txt, pos=(0, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
				self.fgs.Add(ynbox, pos=(0, 3), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
		
			hbox.Add(self.fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			self.core_args_panel.SetSizer(hbox)
			
			self.sb_common = wx.StaticBox(self, label="Common")
			boxsizer = wx.StaticBoxSizer(self.sb_common, wx.VERTICAL)
			boxsizer.Add(self.core_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			self.args_vbox.Add(boxsizer,1, flag=wx.ALL|wx.EXPAND, border=5)
		if 1: #Source
			from_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			fgs = wx.GridBagSizer(3, 10)
			i=0
			for k,v in self.fargs.items()	:
				#print k,v
				#print i
				short,long,val,desc=v
				sval=str(val).strip('"')
				style=0
				if k in ['from_passwd']:
					style=wx.TE_PASSWORD
				length=self.tc_length
				if k in ['input_dirs','input_files', 'source_client_home']:
					length=168
				if k in ['from_passwd']:
					length=168
					self.obj[k]= [wx.StaticText(from_args_panel, label=k)]
				else:
					self.obj[k]= [wx.StaticText(from_args_panel, label=k), wx.TextCtrl(from_args_panel,value=sval, style=style, size=(length,22))]
				fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
				if k in ['input_files']:
					
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k].append(wx.BitmapButton(from_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
					
					#global home
					dir =home
					#print sval
					ffile=sval.split(';')[0]
					if os.path.isfile(ffile):
						dir=os.path.dirname(ffile) 
					print sval
					print dir
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnInputFiles,[self.obj[k][1],dir])
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)				
				elif k in ['input_dirs', 'source_client_home']:
					
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k].append(wx.BitmapButton(from_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
					
					#global home
					dir =home
					#print sval
					if os.path.isdir(sval):
						dir=sval
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnInputDir,[self.obj[k][1],dir])
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				elif k in ['from_passwd']:
					self.obj[k].append(None)
					self.obj[k].append(None)
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k][2]=wx.BitmapButton(from_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
					
					#global home
					dir =home
					#print sval
					if os.path.isdir(sval):
						dir=sval
					
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					pwd_panel = wx.Panel(from_args_panel, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
					self.tc_p1=wx.TextCtrl(pwd_panel,value=sval, style=0, size=(length,22))
					self.tc_p1.SetName(k)
					self.tc_p1.Hide()
					self.tc_p2=wx.TextCtrl(pwd_panel,value=sval, style=style, size=(length,22))
					self.tc_p2.SetName(k)
					self.tc_p2.Show()
					self.src_hide_show=[self.tc_p1, self.tc_p2]
					self.obj[k][1]=self.tc_p2
					 
					bbox.Add(pwd_panel, 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					self.tc_p1.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
					self.tc_p2.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnPassword,[self.src_hide_show])
					#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p1, self.OnPassword,[self.obj[k]])
					#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p2, self.OnPassword,[self.obj[k]])
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				else:
				
					fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				i+=1
				
				self.obj[k][1].Bind(wx.EVT_CHAR, self.onKeyPress)
			
			
			if not self.copy_vector[0].startswith('CSV'):
				lbl="Test connect"					
				btn_test_sconnect = wx.Button(from_args_panel, label=lbl, style=wx.BU_EXACTFIT)
				fgs.Add(btn_test_sconnect, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				btn_test_sconnect.SetName('source')
				btn_test_sconnect.Bind(wx.EVT_BUTTON, self.OnTestConnect)
			hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			from_args_panel.SetSizer(hbox)
			
			sb_from = wx.StaticBox(self, label="Source (%s)" % conf.dbs[self.parent.getCopyVector()[0]])
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(from_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
		if 1: #Target pnl
			to_args_panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			fgs = wx.GridBagSizer(2, 10)
			i=0

				
			for k,v in self.targs.items()	:
				#print k,v
				#print i
				short,long,val,desc=v
				sval=str(val).strip('"')
				style=0
				
				if k in ['to_passwd']:
					style=wx.TE_PASSWORD
				length=self.tc_length
				if k in ['to_dir', 'target_client_home']:
					length=168
				if k in ['to_passwd']:
					length=168
					self.obj[k]= [wx.StaticText(to_args_panel, label=k)]
				else:
					self.obj[k]= [wx.StaticText(to_args_panel, label=k), wx.TextCtrl(to_args_panel,value=sval, style=style, size=(length,22))]
				fgs.Add(self.obj[k][0], pos=(i, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
				
				if k in ['to_file']:
					
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k].append(wx.BitmapButton(to_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
					
					#global home
					dir =home
					#print sval
					if os.path.isdir(sval):
						dir=sval
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnOutputFile,[self.obj[k][1],dir])
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)				
				elif k in ['to_dir', 'target_client_home']:
					
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k].append(wx.BitmapButton(to_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6)))
					
					#global home
					dir =home
					#print sval
					if os.path.isdir(sval):
						dir=sval
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnInputDir,[self.obj[k][1],dir])
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					
					bbox.Add(self.obj[k][1], 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				elif k in ['to_passwd']:
					self.obj[k].append(None)
					self.obj[k].append(None)
					imageFile = os.path.join(home,"bmp_source/refresh_icon_16_grey2.png")
					image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
					#print self.obj[k]
					#print len(self.obj[k])
					
					self.obj[k][2]=wx.BitmapButton(to_args_panel, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
					
					#global home
					dir =home
					#print sval
					if os.path.isdir(sval):
						dir=sval
					
					#self.obj[k][2].Bind(wx.EVT_BUTTON, self.OnDirButton)					
					#self.Bind(wx.EVT_BUTTON, self.OnInputDir, self.btn_dir)
					bbox = wx.BoxSizer(wx.HORIZONTAL)
					pwd_panel = wx.Panel(to_args_panel, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
					self.tc_p1=wx.TextCtrl(pwd_panel,value=sval, style=0, size=(length,22))
					self.tc_p1.SetName(k)
					self.tc_p1.Hide()
					self.tc_p2=wx.TextCtrl(pwd_panel,value=sval, style=style, size=(length,22))
					self.tc_p2.SetName(k)
					self.tc_p2.Show()
					self.trg_hide_show=[self.tc_p1, self.tc_p2]
					self.obj[k][1]=self.tc_p2
					 
					bbox.Add(pwd_panel, 0, flag=wx.ALIGN_CENTER, border=5)	
					bbox.Add(self.obj[k][2], 0, flag=wx.ALIGN_CENTER, border=5)	
					self.tc_p1.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
					self.tc_p2.Bind(wx.EVT_SET_FOCUS, self.OnPwdFocus)
					self.gen_bind(wx.EVT_BUTTON,self.obj[k][2], self.OnPassword,[self.trg_hide_show])
					#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p1, self.OnPassword,[self.obj[k]])
					#self.gen_bind(wx.EVT_SET_FOCUS,self.tc_p2, self.OnPassword,[self.obj[k]])
					#fgs.Add(self.obj[k][2], pos=(i, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)	
					fgs.Add(bbox, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				else:
				
					fgs.Add(self.obj[k][1], pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				i+=1
			
			
			if not self.copy_vector[1].startswith('CSV'):	
				lbl="Test connect"			
				btn_test_tconnect = wx.Button(to_args_panel, label=lbl, style=wx.BU_EXACTFIT)
				btn_test_tconnect.SetName('target')
				btn_test_tconnect.Bind(wx.EVT_BUTTON, self.OnTestConnect)
				
				fgs.Add(btn_test_tconnect, pos=(i, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
				
			hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			to_args_panel.SetSizer(hbox)
			
			sb_from = wx.StaticBox(self, label="Target (%s)" % conf.dbs[self.parent.getCopyVector()[1]])
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(to_args_panel, flag=wx.LEFT|wx.TOP, border=5)
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
			
		if 0: #Source
			
			panel_from = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
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
			
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)

		
		if 0: #Target
			panel_from = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
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
			self.args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
		self.args_vbox.Add(self.args_hbox,0,flag=wx.ALL|wx.EXPAND|wx.GROW)
		self.SetSizer(self.args_vbox)
		self.Fit()
		sub(self.OnCloseExec, "close_exec")
		self.count=0
	def TimerHandler0(self, event,the_id):
		self.count = self.count + 1
		print 'Closing in %d' % (5-self.count)
		if self.count >= 5:
			self.close_exec(self.p)
			self.count = 0
		#print self.count
		#self.gauge.Show()
		#print '||||||||||||||||| setting count', self.count
		
		#self.gauge.SetValue(self.count)
		#self.gauge.Pulse()	
		
	def OnCloseExec(self, data, extra1, extra2=None):		
		p = data	
		self.close_exec(p)
	def OnTestConnect(self, evt):
		print 'OnTestConnect'
		
		
		#print r'start "%s" cmd.exe  /k "%s"' % (title, cmd)
		#os.system(r'start "%s" cmd.exe  /k "%s"' % (title, cmd))
		tc = evt.GetEventObject()
		title='%s connection.' % tc.Name.upper()
		print title
		cmd=None
		if tc.Name=='source':
			cmd=r"%s\%s %s/%s@%s @C:\Users\alex_buz\Documents\GitHub\DataBuddy\test\test_connnect\Oracle.sql" % (
			self.obj['source_client_home'][1].GetValue(), #path to spooler 
			conf.dbtools['SPOOLER'][self.copy_vector[0]], #spooler name
			self.obj['from_user'][1].GetValue(), #db user
			self.obj['from_passwd'][1].GetValue(), #pwd
			self.obj['from_db_name'][1].GetValue(), #pwd
			)
			#print cmd
		if tc.Name=='target':
			cmd=r"%s\%s %s/%s@%s @C:\Users\alex_buz\Documents\GitHub\DataBuddy\test\test_connnect\Oracle.sql" % (
			self.obj['target_client_home'][1].GetValue(), #path to spooler 
			conf.dbtools['SPOOLER'][self.copy_vector[1]], #spooler name
			self.obj['to_user'][1].GetValue(), #db user
			self.obj['to_passwd'][1].GetValue(), #pwd
			self.obj['to_db_name'][1].GetValue(), #pwd
			)
		#print cmd
		assert cmd, 'command is not set'
		if 0:
			self.parent.exec_cmd(title, cmd)
		#evt.Skip()
		#cmd=r'cmd.exe  /k %s' % ( cmd)
		cmd=r'%s' % ( cmd)
		print cmd
		from subprocess import Popen, PIPE,CREATE_NEW_CONSOLE
		cfg=[]
		if 1:
			import shlex 
			cmd2=''.join(cmd.split('^\n'))
			#print cmd
			lexer=shlex.shlex(cmd2)
			#lexer = shlex.shlex(input)
			lexer.quotes = '"'
			#lexer.wordchars += '\''
			lexer.whitespace_split = True
			lexer.commenters = ''
			cfg = list(lexer)
			#cfg=['start',"'%s'" % title] + cfg
			#e(0)
			if 0:
				cfg=['start',
 "'SOURCE connection.'",
 'cmd.exe',
 '/k',
 'C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN\\sqlplus.exe SCOTT/tiger2@orcl @C:\\Users\\alex_buz\\Documents\\GitHub\\DataBuddy\\test\\test_connnect\\Oracle.sql']
			pprint(cfg)	
		print  cmd
		p = Popen(cfg, creationflags=CREATE_NEW_CONSOLE)
		#p = Popen(["C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN\\sqlplus.exe",'SCOTT/tiger2@orcl', '@C:\\Users\\alex_buz\\Documents\\GitHub\\DataBuddy\\test\\test_connnect\\Oracle.sql'],creationflags=CREATE_NEW_CONSOLE)
		print p
		print p.pid
		self.timer.Start(500)
		#self.timer.Stop()
		self.p=p
		#send('close_exec', p)
		#wnd = subprocess.Popen ([cmd], shell=True)

	def close_exec(self,p):
		if 1:
			import win32con
			import win32gui
			import win32process
			

			def get_hwnds_for_pid (pid):
				def callback (hwnd, hwnds):
					if win32gui.IsWindowVisible (hwnd) and win32gui.IsWindowEnabled (hwnd):
						_, found_pid = win32process.GetWindowThreadProcessId (hwnd)
						if found_pid == pid:
							hwnds.append (hwnd)
					return True

				hwnds = []
				win32gui.EnumWindows (callback, hwnds)
				print hwnds
				return hwnds

			if 1:
				#import subprocess
				import time
				#notepad = subprocess.Popen ([r"notepad.exe"])
				#
				# sleep to give the window time to appear
				#
				#time.sleep (5)

				for hwnd in get_hwnds_for_pid (p.pid):
					print hwnd, "=>", win32gui.GetWindowText (hwnd)
					#win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
					win32gui.SendMessage (hwnd, win32con.WM_CLOSE, 0, 0)
		self.timer.Stop()
	def OnDirButton(self, event):
		print 'OnDirButton'
	def onKeyPress(self, event):
		#print 'changed'
		
		kc = event.GetKeyCode()
		if not (kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
			self.parent.btn_save.Enable(True)
		event.Skip()
		return
	def ClearAll(self):
		for k in self.obj:
			if k not in ['copy_vector']:
				self.obj[k][1].SetValue('')
	def DisableAll(self):
		for k in self.obj:
			if k not in ['copy_vector']:
				self.obj[k][0].Enable(False)
				self.obj[k][1].Enable(False)
		
	def getArgs(self):
		for k in self.cargs:
			assert self.obj.has_key(k), 'cargs "%s" is not set' % k
			val=self.obj[k][1].GetValue()
			self.cargs[k]=list(self.cargs[k])
			if str(self.cargs[k][2]).strip('"') not in [val]:
				#print 'cargs "%s" value changed' % k, str(self.cargs[k][2]),'-->' ,val
				self.cargs[k][2]=val
			#,self.fargs,self.targs=self.args
		for k in self.fargs:
			assert self.obj.has_key(k), 'fargs "%s" is not set' % k
			val=self.obj[k][1].GetValue()
			self.fargs[k]=list(self.fargs[k])
			#if k in ['from_passwd']:
			#	#base64.b64decode("cGFzc3dvcmQ=")
			#	self.targs[k][2]=base64.b64encode(val)
			if 1: #else:			
				if str(self.fargs[k][2]).strip('"') not in [val]:
					#print 'fargs "%s" value changed' % k, str(self.fargs[k][2]),'-->' ,val
					self.fargs[k][2]=val		
		for k in self.targs:
			assert self.obj.has_key(k), 'targs "%s" is not set' % k
			val=self.obj[k][1].GetValue()
			self.targs[k]=list(self.targs[k])
			#if k in ['to_passwd']:
			#	#import base64
			#	self.targs[k][2]=base64.b64encode(val)
			if 1: #else:			
				if str(self.targs[k][2]).strip('"') not in [val]:
					#print 'targs "%s" value changed' % k, str(self.targs[k][2]),'-->' ,val
					self.targs[k][2]=val
		#save to file
		return [self.cargs, self.fargs, self.targs]
	def OnPwdFocus (self, evt):
		print 'OnPwdFocus'
		#(objArr)=params
		#print 'OnPwdFocus'
		tc = evt.GetEventObject()
		#print tc.Name
		self.obj[tc.Name][1]=tc
		
	def OnPassword(self, evt,params):
		print 'OnPassword'
		[flip] =params
		for tc in flip:
			print tc
			if tc.IsShown():
				tc.Hide()
			else:
				tc.Show()
			
		#pprint(dir(self.src_hide_show[0]))		
	def OnInputDir(self, evt,params):
		print 'OnInputDir'
		[dir_obj,dir] = params
		if 1: #dirtype in ['input_dirs']:
			import wx.lib.agw.multidirdialog as MDD
			dlg = MDD.MultiDirDialog(None, title="Choose CVS directory:", defaultPath=dir,
							 agwStyle=MDD.DD_MULTIPLE|MDD.DD_DIR_MUST_EXIST)

			if dlg.ShowModal() != wx.ID_OK:
				print("You Cancelled The Dialog!")
				dlg.Destroy()
				return

			paths = dlg.GetPaths()
			for indx, path in enumerate(paths):
				print("Path %d: %s"%(indx+1, path))
			
			dlg.Destroy()
			self.set_dirs(dir_obj, paths)
			#print dir
	def OnInputFiles_del(self, evt,params):
		print 'OnInputDir'
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
			for indx, path in enumerate(paths):
				print("Path %d: %s"%(indx+1, path))
			
			dlg.Destroy()
			self.set_dirs(dir_obj, paths)
			#print dir
			
	def OnInputFiles(self, evt,params):
		print 'OnInputDir'
		[file_obj,dir] = params
		dlg = wx.FileDialog(self, "Choose input CSV file", dir, "",
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
		self.set_files(file_obj, files)
			
	def OnOutputFile(self, evt,params):
		print 'OnInputDir'
		[file_obj,dir] = params
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
		path=[]
		#clean-up
		for dir in dirs:
			if dir.startswith('OS '):
				path.append(dir.strip('OS ').replace('(','').replace(')',''))
			else:
				path.append(dir)
		
		dir_obj.SetValue(';'.join(path))
		
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
		
	def get_cmd(self,transport):
		cmd='%s ^' % transport
		for k, v in self.cargs.items():
			#print k,v
			short,long,val,desc=v
			cmd='%s\n%s "%s" ^' % (cmd, short,self.obj[k][1].GetValue())
		for k, v in self.fargs.items():
			#print k,v
			short,long,val,desc=v
			cmd='%s\n%s "%s" ^' % (cmd, short,self.obj[k][1].GetValue())
		for k, v in self.targs.items():
			#print k,v
			short,long,val,tesc=v
			cmd='%s\n%s "%s" ^' % (cmd, short,self.obj[k][1].GetValue())			
		return cmd
	def get_cmd_line(self,transport):
		cmd='%s' % transport #'python  C:\Python27\data_migrator_1239\datamule.py' #
		for k, v in self.cargs.items():
			#print k,v
			short,long,val,desc=v
			cmd='%s %s "%s"' % (cmd, short,self.obj[k][1].GetValue())
		for k, v in self.fargs.items():
			#print k,v
			short,long,val,desc=v
			val=self.obj[k][1].GetValue()
			if 0 and 'passwd' in long: 
				val= base64.b64decode(val)
			cmd='%s %s "%s"' % (cmd, short,val)
			#print cmd
		for k, v in self.targs.items():
			#print k,v
			short,long,val,tesc=v
			val=self.obj[k][1].GetValue()
			if 0 and 'passwd' in long: 
				#pprint (val)
				val= base64.b64decode(val)
			cmd='%s %s "%s"' % (cmd, short,val)			
		return cmd
		
###################################################################################################
class DataBuddy(wx.Frame):
	def __init__(self, parent, id, title, size):
		global tr
		#wx.Frame.__init__(self, parent, -1, title)
		#super(DataBuddy, self).__init__(parent, title=title , size=(900, 565))
		global app_title, home
		wx.Frame.__init__(self, None, wx.ID_ANY, title=app_title, size=size)
		self._vectMenu=None
		self._popUpMenu = None
		#self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
		#self.splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
		#s=self.splitter
		#self.splitter.SetMinimumPaneSize(50)
		#panel layout
		self.panel_pos=[(0,i) for i in range(3)]
		#print self.panel_pos
		self.panel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		panel=self.panel
		sizer = wx.GridBagSizer(5, 5)
		self.home=home
		self.copy_vector=None
		userhome = os.path.expanduser('~')
		self.save_to_dir=os.path.join(userhome,'sessions')
		if not os.path.isdir(self.save_to_dir):
			os.makedirs(self.save_to_dir)
		self.transport=os.path.join(self.home,r'%s32\%s32.exe' % (tr,tr))
		self.args_panel = dummy_args(self,style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		self.cmd=''
		self.default_session=None
		
		#self.cmd=self.args_panel.get_cmd(self.transport)
		if 1:
			self.st_session_name = wx.StaticText(panel, label="Session name:")
			sizer.Add(self.st_session_name, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			self.session_name=None
			self.tc_session_name = wx.TextCtrl(panel,value='n/a')
			
			self.tc_session_name.Bind(wx.EVT_CHAR, self.onKeyPress)
			self.tc_session_name.Enable(False)
			sizer.Add(self.tc_session_name, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
			sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)

		if 1:
			line = wx.StaticLine(panel)
			sizer.Add(line, pos=(1, 0), span=(1, 5), 
				flag=wx.EXPAND|wx.BOTTOM, border=0)

		if 1: #Type
			sb = wx.StaticBox(panel, label='Type')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_type = wx.StaticText(panel, label="n/a")
			boxsizer.Add(self.st_type, flag=wx.LEFT|wx.TOP, border=5)
						
			sizer.Add(boxsizer, pos=(2, 0),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Vector')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_copy_vector = wx.StaticText(panel, label='{:s}'.format('n/a'))
			boxsizer.Add(self.st_copy_vector, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 1),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Source template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_sourcet = wx.StaticText(panel, label='{:s}'.format('n/a'))
			boxsizer.Add(self.st_sourcet, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 2),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))	
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Target template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			self.st_targett = wx.StaticText(panel, label='{:s}'.format('n/a'))
			boxsizer.Add(self.st_targett, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 3),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=1)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))				
		if 0: #Transport
			sb = wx.StaticBox(panel, label="DataMigrator")
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			#self.rb_transport32=wx.RadioButton(panel, label="DataMigrator",style=wx.RB_GROUP)
			#b_vector = wx.Button(panel, label="ora2ora")
			#self.rb_transport32.Enable(False)
			#boxsizer.Add(self.rb_transport32, flag=wx.LEFT|wx.TOP, border=5)
			#self.rb_transport64=wx.RadioButton(panel, label="64bit")
			#b_vector = wx.Button(panel, label="ora2ora")
			#self.rb_transport.Enable(False)
			#boxsizer.Add(self.rb_transport64, flag=wx.LEFT|wx.TOP, border=5)			
			self.txt_transport= wx.TextCtrl(panel,value='.\\dm32\\dm32.exe')
			boxsizer.Add(self.txt_transport, flag=wx.LEFT|wx.TOP|wx.ALIGN_TOP, border=5)
			#self.txt_transport.Enable(False)
			btn_browse = wx.Button(panel,LOAD_FILE_ID, label="Browse...", style=wx.BU_EXACTFIT)
			boxsizer.Add(btn_browse, flag=wx.LEFT|wx.TOP, border=5)
			self.Bind(wx.EVT_BUTTON, self.loadFile, btn_browse)
			sizer.Add(boxsizer, pos=(2, 3),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
			#self.rb_transport32.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)			
			#self.rb_transport64.Bind(wx.EVT_RADIOBUTTON, self.onRadioButton)			
			
		if 1:
			
			self.nb = fnb.FlatNotebook(panel, -1, agwStyle=fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS|fnb.FNB_NODRAG) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
			#pprint(self.nb)
			self.nb.AddPage(self.args_panel, 'Arguments')
			editor = TacoTextEditor(panel)
			editor.AppendText(self.cmd)
			self.nb.AddPage(editor, 'Command')
			self.nb.SetSelection(0)
			self.nb.EnableTab(0,False)
			self.nb.EnableTab(1,False)
				
			sizer.Add(self.nb, pos=(3, 0), span=(4, 4), flag=wx.GROW|wx.EXPAND|wx.ALL, border=0)
		if 1:
			fgs = wx.FlexGridSizer(10, 1, 9, 25)

			#l=[wx.StaticText(panel_from, label="Title"), wx.StaticText(panel_from, label="Author"),wx.StaticText(panel_from, label="Review")]

			#p=[wx.TextCtrl(panel_from), wx.TextCtrl(panel_from), wx.TextCtrl(panel_from)]
			#pprint(dir(fgs))
			self.btn_new=wx.Button(panel, label='New')
			self.btn_new.Enable(True)
			self.btn_delete=wx.Button(panel, label="Delete")
			self.btn_delete.Enable(False)
			self.btn_clearall=wx.Button(panel, label="Clear All")
			self.btn_clearall.Enable(False)
			self.btn_save=wx.Button(panel, label="Save")
			self.btn_save.Enable(False)			
			fgs.AddMany([(self.btn_new, 1, wx.EXPAND),(self.btn_delete, 1, wx.EXPAND),wx.StaticText(panel, label=' '),(self.btn_clearall, 1, wx.EXPAND),wx.StaticText(panel, label=' \n'),(self.btn_save, 1, wx.EXPAND)])
			self.btn_new.Bind(wx.EVT_BUTTON, self.OnNewButton)	
			self.btn_delete.Bind(wx.EVT_BUTTON, self.OnDeleteButton)	
			self.btn_clearall.Bind(wx.EVT_BUTTON, self.OnClearAllButton)	
			self.btn_save.Bind(wx.EVT_BUTTON, self.OnSaveButton)
			#button1 = wx.Button(panel, label="New")
			#sizer.Add(button1, pos=(3, 5), flag=wx.TOP|wx.RIGHT, border=5)

			#button2 = wx.Button(panel, label="Delete")
			#sizer.Add(button2, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
			sizer.Add(fgs, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
		sb = wx.StaticBox(panel, label='Run')

		boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
		self.send_yes=wx.CheckBox(panel, label="Send 'y'")
		boxsizer.Add(self.send_yes, flag=wx.LEFT|wx.TOP, border=5)
		self.send_yes.SetValue(True)
		self.auto_save=wx.CheckBox(panel, label="Auto-save")
		boxsizer.Add(self.auto_save, flag=wx.LEFT|wx.TOP, border=5)
		self.auto_save.SetValue(True)
		
		#print(dir(cb))
		sizer.Add(boxsizer, pos=(8, 0), span=(1, 5), 
			flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

		button3 = wx.Button(panel, label='Help')
		sizer.Add(button3, pos=(9, 0), flag=wx.LEFT, border=10)
		button3.Enable(False)

		self.btn_show = wx.Button(panel, label='Show in Folder')
		self.btn_show.Bind(wx.EVT_BUTTON, self.OnButtonShowInFolder)
		sizer.Add(self.btn_show, pos=(9, 2),flag=wx.BOTTOM|wx.ALIGN_RIGHT)
		self.btn_show.Enable(False)

		self.btn_run = wx.Button(panel, label='Run')
		self.btn_run.Bind(wx.EVT_BUTTON, self.OnButtonRun)
		sizer.Add(self.btn_run, pos=(9, 3),flag=wx.BOTTOM|wx.ALIGN_RIGHT)
		self.btn_run.Enable(False)
		
		button5 = wx.Button(panel, ID_EXIT, label="Cancel")
		#self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutBtn)
		sizer.Add(button5, pos=(9, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=5)

		#sizer.AddGrowableCol(2)
		sizer.AddGrowableRow(7)
				
		if 1:
			self.panel2 = wx.Panel(self, wx.ID_ANY, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			panel2=self.panel2
			vsizer =  wx.BoxSizer(wx.VERTICAL)
			#wx.BoxSizer(wx.VERTICAL)
			#if 1:
				#self.splitter.SetOrientation(wx.VERTICAL)
				
			self.sm=SessionListCtrlPanelManager(panel2,self,(0,0),self.panel_pos)
				
			self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
			vsizer.Add(self.sm,1,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
			self.data =self.sm.list.data[self.sm.list.current_list]

			#self.vsizer.Add(self.sizer,pos=(0,1),flag=wx.EXPAND)
			aboutBtn = wx.Button(panel2, ID_ABOUT, "About", style=wx.BU_EXACTFIT) #, size=(30,20)
			vsizer.Add(aboutBtn,0,wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
			
			

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
			self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutBtn)
			#self.Bind(wx.EVT_BUTTON, self.onAboutDlg, id=ID_ABOUT)
			panel2.SetSizer(vsizer)
		
		self.Bind(wx.EVT_MENU, self.loadFile, id=LOAD_FILE_ID)
		accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('O'), LOAD_FILE_ID )])
		self.SetAcceleratorTable(accel_tbl)		
		panel.SetSizer(sizer)
		sub(self.onTransportLoc, "set_transport_location")
		sub(self.onNewSession, "create_new_session")
		sub(self.onOpenSession, "open_session")
		sub(self.onValueChanged, "value_changed")
		sub(self.onDisableAllForDelete, "disable_all_for_delete")
		
		#self.SetSizeHints(250,300,500,400)
		if 1:
			self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
			self.statusbar.SetStatusWidths([-3, -3])
			self.statusbar.SetStatusText(os.getcwd(), 0)
			self.statusbar.SetStatusText("Welcome To %s!" % app_title, 1)
		self.Layout()
		self.Fit()
		#self.Refresh()
		self.Center()
		x,y=self.GetSize()
		self.SetSize((x+100,y))
		self.Refresh()
		self.Show(True)
		(self.cargs,self.fargs,self.targs)=(None, None, None)
		#print self.GetSize()
		sub(self.onDeleteSessions, "delete_sessions")
	def openDefault(self, sname):
		print sname
		
	def onDeleteSessions(self,  data, extra1, extra2=None):
		(items)=data
		for k,v in items.items():
			#print k, v
			if os.access(v, os.W_OK) and os.path.isfile(v):
				os.remove(v)
				#print 'removed', v
			
		
	def onDisableAllForDelete(self, data, extra1, extra2=None):	
		print 'onDisableAllForDelete'	
		#self.args_panel.DisableAll()
		#self.btn_delete.Enable(True)
		self.btn_new.Enable(False)
		self.btn_clearall.Enable(False)
		self.btn_save.Enable(False)
		self.btn_run.Enable(False)
		self.btn_show.Enable(False)
		
		self.st_session_name.Enable(False)
		self.tc_session_name.Enable(False)
		self.send_yes.Enable(False)
		self.auto_save.Enable(False)
		self.st_type.Enable(False)
		self.st_copy_vector.Enable(False)
		self.st_sourcet.Enable(False)
		self.st_targett.Enable(False)
		self.nb.EnableTab(0,False)
		self.nb.EnableTab(1,False)
		
	def onKeyPress(self, event):
		#print 'changed'
		
		kc = event.GetKeyCode()
		if not (kc == wx.WXK_TAB or kc == wx.WXK_RETURN):
			self.btn_save.Enable(True)
		event.Skip()
		return
	def onOpenSession(self, data, extra1, extra2=None):
		
		(sname,cv_from,cv_to,type,tmpl,sdir, fname) = data
		#print sname
		self.Freeze()
		self.enableForm()
		self.open_session([sname,[cv_from,cv_to],type,tmpl,sdir,fname])
		self.btn_delete.Enable(True)
		self.btn_new.Enable(True)
		self.btn_save.Enable(False)
		#self.Fit()
		self.Layout()
		#self.Refresh()
		self.Thaw()
		#
		#self.Refresh()		
	def enableForm(self):
		self.btn_new.Enable(True)
		self.btn_clearall.Enable(True)
		self.btn_save.Enable(True)
		self.btn_run.Enable(True)
		self.btn_show.Enable(True)
		
		self.st_session_name.Enable(True)
		self.tc_session_name.Enable(True)
		self.send_yes.Enable(True)
		self.auto_save.Enable(True)
		self.st_type.Enable(True)
		self.st_copy_vector.Enable(True)
		self.st_sourcet.Enable(True)
		self.st_targett.Enable(True)
		#self.nb.EnableTab(0,True)
		#self.nb.EnableTab(1,True)	
	def OnDeleteButton(self,evt):
		#print '#####', self.sm.list.GetSelectedItemCount()
		#print 
		items={}
		data =self.sm.list.data[self.sm.list.current_list]
		selected=self.sm.list.GetSelectedItems()
		names=[]
		for i in selected:
			#print '$$$$$',i
			ii=self.sm.list.getItemInfo(i)
			#print i, self.sm.list.getItemInfo(i)
			#print data[i]
			key = ii[1] #pprint  (data[i])
			names.append(self.sm.list.GetItemText(i))
			items[key]=os.path.join(data[i][-2],data[i][-1])
			del data[i]
		#pprint (names)		 
		if self.if_yes('Delete these sessions?\n%s' % '\\n'.join(names)):
			send('delete_sessions', (items))
			if len(selected)==1:
				send('disable_all_for_delete',())
			self.btn_delete.Enable(False)
			self.btn_new.Enable(True)
	def if_yes(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.YES_NO | wx.ICON_QUESTION)
		answer=dlg.ShowModal()
		dlg.Destroy()
		return answer==wx.ID_YES
		
	def onNewSession(self, data, extra1, extra2=None):	
		#print 'onNewSession'
		if 1:
			(sname,cv,tmpl,args) = data
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
		
	def setSessionName(self, sn):
		self.tc_session_name.SetValue(sn)
		self.tc_session_name.Enable(True)
		self.session_name=sn
	def getSessionName(self):
		return self.tc_session_name.GetValue()
	def getCopyVector(self):
		return self.copy_vector		
	def setCopyVector(self, cv):
		self.copy_vector=cv	
		self.st_copy_vector.SetLabel('{:s} -> {:s}'.format(conf.dbs[cv[0]], conf.dbs[cv[1]]))
	def setTemplates(self,tmpl):
		a,b=tmpl.split('.')
		self.st_sourcet.SetLabel('{:s}'.format(a))
		self.st_targett.SetLabel('{:s}'.format(b))
	def setType(self,tmpl):
		a,b=tmpl.split('.')
		type='Copy'
		if a.startswith('CSV'):
			type='Load'
		elif b.startswith('CSV'):
			type='Extract'
		self.st_type.SetLabel('{:s}'.format(type))
		
	def getTemplates(self):
		return (self.st_sourcet.GetLabel().strip(),self.st_targett.GetLabel().strip())
	def OnClearAllButton(self, event):
		self.args_panel.ClearAll()
	def OnSaveButton(self, event):
		sname=self.tc_session_name.GetValue()
		save_as=self.session_name!=sname 
		if save_as and self.if_duplicate_name(sname):
			self.Warn('Duplicate session name.')
			self.tc_session_name.SetFocus()
		else:
			(sname,cv,tmpl,dname,fname)=self.saveSession()
			#set focus
			#(sname,cv,tmpl,dname,fname) = data		
			if save_as:
				session=[sname,cv[0],cv[1],'Copy',tmpl,dname,fname]
				idx=self.sm.slp.addSession(session)			
				self.sm.list.SetItemState(idx, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED, wx.LIST_STATE_SELECTED|wx.LIST_STATE_FOCUSED) 
				self.sm.list.EnsureVisible(idx)
		
	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()	
	def if_duplicate_name(self,name):
		for k,v in self.data.items():
			if name == v[0]:
				return True
		return False
	def if_sname_changed(self):
		print 'if_sname_changed'
		print self.tc_session_name.GetItemData()
		
	def saveSession(self, data=None):
		
		if data:
			(sname,copy_vector,tmpl,args)=data
		else:
			(sname,copy_vector,tmpl,args)=[self.getSessionName(), self.getCopyVector(), '.'.join(self.getTemplates()), self.args_panel.getArgs()]
		if not os.path.isdir(self.save_to_dir):
			os.makedirs(self.save_to_dir)
		self.session_name=sname
		#sname=self.getSessionName()
		#print self.tmpl
		#print self.copy_vector
		#print sname
		fname='%s;%s;%s.p' % ('.'.join(copy_vector), tmpl,sname)
		save_to_file=os.path.join(self.save_to_dir, fname)
		
		#print save_to_file
		#print sname
		#print copy_vector
		#print tmpl
		#print args
		#print
		#e(0)
		args=self.obfuscate(args)
		import pickle
		pickle.dump( [sname,copy_vector, tmpl, args], open( save_to_file, "wb" ) )
		self.btn_save.Enable(False)	
		return (sname,copy_vector, tmpl,self.save_to_dir, fname)
	def obfuscate(self, data):
		#pprint(data)
		for k in data[1]:
			if 'passwd' in k:	
				data[1][k]=list(data[1][k])
				data[1][k][2]=base64.b64encode(data[1][k][2])
		for k in data[2]:
			#print k
			if 'passwd' in k:				
				data[2][k]=list(data[2][k])
				data[2][k][2]=base64.b64encode(data[2][k][2])	
		#e(0)
		return data	
	def OnNewButton(self, event):
		if 1:
			dlg = NewSessionDialog(self, -1, "Defaults for new session.", size=(250, 250),				
							 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
							 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
							 useMetal=False, data=self.data
							 )
			#dlg.CenterOnScreen()
			# this does not return until the dialog is closed.
			val = dlg.ShowModal()
			#print wx.ID_OK, ID_EXIT, val
			if val == wx.ID_OK:
				if 1:					
					(sname,cv,tmpl,api_args)= dlg.getConfig()
					#print sname
					#e(0)
					#tmpl=self.get_template()
					#api_args=self.api_args[tmpl]
					#print '-----',self.tc_sname.GetValue(),self.copy_vector, tmpl
					send("create_new_session", (sname,cv, tmpl,api_args) )
			dlg.Destroy()
			#[self.sname, self.copy_vector, self.tmpl, self.args]=dlg.getConfig()
			#print conf
			#print val
			#self.saveSession(self.args)
			#self.set_new_session([self.sname, self.copy_vector, self.tmpl]+[self.get_api_args(data[1], data[2])])
			#e(0)


			
		else:
			if 1:
				#data=['dsfdsfdsf', ['SLITE', 'INFOR'], 'SLITE_ParallelQueryDir.INFOR_Table']		
				data=['csv_dirs_to_table', ['CSV', 'ORA11G'], 'CSV_Dirs.ORA11G_Table'] #_Partition_TruncateTarget
				self.session_name,self.copy_vector, self.tmpl=data
				self.Freeze()
				self.set_new_session(data+[self.get_api_args(data[1], data[2])])
				self.Layout()
				self.Thaw()

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
		session_args=self.unobfuscate(session_args)
		return session_args
	def unobfuscate(self,data) 	:
		#pprint(data)
		for k in data[1]:
			#print '--k--',k
			if 'passwd' in k:				
				data[1][k][2]=base64.b64decode(data[1][k][2])
		for k in data[2]:
			if 'passwd' in k:				
				#print 'data[2][k]', data[2][k]
				data[2][k][2]=base64.b64decode(data[2][k][2])				
		return data	
		
	def open_session(self,data):
			#print len(data)
			(self.sname,self.copy_vector,self.type, self.tmpl,self.sdir,self.fname) = data
			self.setSessionName(self.sname)
			self.setCopyVector(self.copy_vector)
			#print self.tmpl
			#print sname,copy_vector,tmpl
			self.setTemplates(self.tmpl)
			self.setType(self.tmpl)
			sess=self.get_session_args(os.path.join(self.sdir,self.fname))
			#pprint(sess.keys())
			(self.cargs,self.fargs,self.targs)=sess
			#if 'to_passwd' in self.targs.keys():
			#	print self.targs['to_passwd']
			#	self.targs['to_passwd']=list(self.targs['to_passwd'])
			#	self.targs['to_passwd'][2]=base64.b64decode(self.targs['to_passwd'][2])
			#print len(self.cargs)
			##print len(self.fargs)
			#print len(self.targs)
			#self.args_panel.Hide()
			#self.args_panel.create_cargs(self.cargs)
			#self.args_panel.Destroy()
			self.args_panel= pnl_args(self,self.copy_vector,self.tmpl,(self.cargs,self.fargs,self.targs),style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.nb.DeletePage(0)
			self.nb.DeletePage(0)
			#self.args_panel.Destroy()
			self.nb.AddPage(self.args_panel, 'Arguments')
			editor = TacoTextEditor(self.args_panel)
			editor.AppendText(self.args_panel.get_cmd(self.transport))
			self.nb.AddPage(editor, 'Command')
			self.nb.SetSelection(0)
			self.btn_show.Enable(True)
			self.btn_run.Enable(True)
			self.btn_save.Enable(True)	
			self.btn_clearall.Enable(True)
  
  
	def set_new_session(self,data):
			#print len(data)
			(sname,copy_vector,tmpl,api_args) = data
			self.setSessionName(sname)
			self.setCopyVector(copy_vector)
			#print sname,copy_vector,tmpl
			self.setTemplates(tmpl)
			self.setType(self.tmpl)
			(self.cargs,self.fargs,self.targs)=api_args
			#print len(self.cargs)
			#print len(self.fargs)
			#print len(self.targs)
			#self.args_panel.Hide()
			#self.args_panel.create_cargs(self.cargs)
			#self.args_panel.Destroy()
			self.args_panel= pnl_args(self,copy_vector,tmpl,api_args,style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			self.nb.DeletePage(0)
			self.nb.DeletePage(0)
			#self.args_panel.Destroy()
			self.nb.AddPage(self.args_panel, 'Arguments')
			editor = TacoTextEditor(self.args_panel)
			editor.AppendText(self.args_panel.get_cmd(self.transport))
			self.nb.AddPage(editor, 'Command')
			self.nb.SetSelection(0)
			self.btn_show.Enable(True)
			self.btn_run.Enable(True)
			self.btn_save.Enable(True)	
			self.btn_clearall.Enable(True)
  
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
		fname = os.path.join(dirname, '%s_%s.bat' % (self.tc_session_name.GetValue(),ts))
		if not os.path.isdir(dirname):
			os.makedirs(dirname)
		f=open(fname,'w')
		cmd=self.args_panel.get_cmd(self.transport)
				
		if_yes=self.send_yes.GetValue()
		yes=''
		if if_yes:
			yes='echo y|'		
		f.write('%s%s' % (yes,cmd))
		f.close()
			
		
	
		EXPLORER = 'C:\\windows\\explorer.exe' 
		if not os.path.isfile(EXPLORER):
			EXPLORER = 'C:\\WINNT\\explorer.exe' 
		os.spawnl(os.P_NOWAIT, EXPLORER, '.', '/n,/e,/select,"%s"'%fname)


	def OnButtonRun(self, event):
		# 
		btn = event.GetEventObject()
		#print btn.GetLabel()
		#from subprocess import Popen,PIPE
		if 0:
			
			#Popen("cmd /w dir")
			import shlex 
			cmd=''.join(self.cmd.split('^\n'))
			#print cmd
			lexer=shlex.shlex(cmd)
			#lexer = shlex.shlex(input)
			lexer.quotes = '"'
			#lexer.wordchars += '\''
			lexer.whitespace_split = True
			lexer.commenters = ''
			cfg = list(lexer)
			#pprint(cfg)		
			#e(0)
			p = Popen(cfg, stdin=PIPE, stdout=PIPE, shell=True)
			out, err = p.communicate('y\n')
			p.wait()
			print err
			print out
			#print '-'*40
		if 0:
			p=Popen(['mode con cols=50 lines=50;start "test"', 'cmd', '/k','.\\dm32\\dm32.exe', '-w', 'ora2ora', '-o', '1', '-r', '1',  '-c', 'SCOTT.Date_test_from', '-f', 'SCOTT/tiger2@orcl', '-e', '"YYYY-MM-DD HH24.MI.SS"', '-m', '"YYYY-MM-DD HH24.MI.SS.FF2"', '-O', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"','-z', '"C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"', '-g', 'SCOTT/tiger2@orcl', '-a', 'SCOTT.Partitioned_test_to', '-G', 'part_15', '-e', '"YYYY-MM-DD HH24.MI.SS"', '-m', '"YYYY-MM-DD HH24.MI.SS.FF2"', '-O', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', '-Z', '"C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"'], stdin=PIPE, stdout=PIPE, shell=True)
			out, err = p.communicate('y\n')
			#print out, err
			p.wait()
			p.close()
		#os.system("mode 45, 20");
		#os.system(r'start "ora2ora" cmd /k echo y^|C:\Users\alex_buz\Documents\GitHub\DataBuddy\dm32\dm32.exe -w ora2ora -o 1 -r 1 -t "|" -c SCOTT.Date_test_from -f SCOTT/tiger2@orcl -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -g SCOTT/tiger2@orcl -a SCOTT.Partitioned_test_to -G part_15 -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"')
		
		cmd=self.args_panel.get_cmd_line(self.transport)
		#self.args_panel
		#e(0)
		cmd=cmd.replace('|','^|')
		#cmd=cmd.replace('csv2ora11g','csv2ora')
		
		#pprint (cmd)
		#save
		if_save=self.auto_save.GetValue() 
		if if_save:
			(sname,cv,tmpl,dname,fname)=self.saveSession()
			
		if_yes=self.send_yes.GetValue()
		yes=''
		if if_yes:
			yes='echo y|'
		if 0:
			os.system(r'start "test" cmd.exe  /k "mode 100,45 && echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\dm32\dm32.exe -w ora2ora -o 1 -r 1 -t "^|" -c SCOTT.Date_test_from -f SCOTT/tiger2@orcl -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -g SCOTT/tiger2@orcl -a SCOTT.Partitioned_test_to -G part_15 -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN""')
		else:
			#os.system(r'start "test" cmd.exe  /k "echo y|python  C:\Python27\data_migrator_1239\datamule.py  -t "^|" -w "csv2ora11g" -r "1" -o "1" -I "c:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_1;c:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_2" -y "1000" -d "orcl" -e "YYYY-MM-DD HH24.MI.SS" -u "SCOTT" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -p "tiger2" -a "SCOTT.Timestamp_test_to" -m "YYYY-MM-DD HH24.MI.SS.FF2"')
			#print r'start "test" cmd.exe  /k "echo y|python  C:\Python27\data_migrator_1239\datamule.py  -t "^|" -w "csv2ora11g" -r "1" -o "1" -I "c:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_1;c:\Python27\data_migrator_1239\test\v101\data\ora_data_dir_2" -y "1000" -d "orcl" -e "YYYY-MM-DD HH24.MI.SS" -u "SCOTT" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -p "tiger2" -a "SCOTT.Timestamp_test_to" -m "YYYY-MM-DD HH24.MI.SS.FF2"'
			#print r'start "test" cmd.exe  /k "%s%s"' % (yes,cmd)
			cmd='%s%s' % (yes,cmd)
			title='%s->%s' % (conf.dbs[self.copy_vector[0]],conf.dbs[self.copy_vector[1]])
			self.exec_cmd(title, cmd)
			#u'C:\\Users\\alex_buz\\Documents\\GitHub\\DataBuddy\\dm32\\dm32.exe -t "|" -w "csv2ora11g" -r "1" -o "1" -I "c:\\Python27\\data_migrator_1239\\test\\v101\\data\\ora_data_dir" -y "1000" -g "SCOTT/tiger2@orcl" -m "YYYY-MM-DD HH24.MI.SS.FF2" -e "YYYY-MM-DD HH24.MI.SS" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -a "SCOTT.Timestamp_test_to" -Z "C:\\app\\alex_buz\\product\\11.2.0\\dbhome_2\\BIN"'		
	def exec_cmd(self, title, cmd):
		print r'start "%s" cmd.exe  /k "%s"' % (title, cmd)
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
		self.Close(True)
	def onAboutDlg(self, event):
		
		from wx.lib.wordwrap import wordwrap
		info = wx.AboutDialogInfo()
		info.Name = "CSV*Loader"
		info.Version = "0.0.1 Beta"
		info.Copyright = "(C) 2015 SequelWorks Inc."
		info.Description = wordwrap(
			#'This is session manager for  <b><a href="https://github.com/DataMigrator/DataMigrator-for-Oracle">DataMigrator</a></b>.</p>',
			'<p>Loads CSV dir file''s data into Oracle table .</p>',
			350, wx.ClientDC(self.panel))
		info.WebSite = ("https://github.com/alexbuz", "My Github")
		info.Developers = ["Alex Buzunov"]
		info.License = wordwrap("Open source", 500,
								wx.ClientDC(self.panel))
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
		wx.Frame.__init__(self, parent, wx.ID_ANY, title="About %s" % __title__, size=(400,400))
		html = wxHTML(self)
		page="""
<h2>%s</h2>						
<p>Loads multiple CSV files' data into Oracle 11G table.</p>
<p>Created in Feb. 2015 by %s.</p>
<p><b>Software used in making this tool:</h3></p>
<p><b><a href="http://www.python.org">Python 2.7</a></b></p>
<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>
		""" % (__title__, __author__)
		
		html.SetPage(
			page
			)
		self.Center()
		#self.SetSize((300,300))
		#self.Fit()
		self.Refresh()


class wxHTML(wx.html.HtmlWindow):	
	def OnLinkClicked(self, link):
		webbrowser.open(link.GetHref())
		
if __name__ == '__main__':
	freeze_support()	
	app_title='%s %s' % (__title__,__version__)
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
			self.frame = DataBuddy(None, -1,title=app_title, size=(700,400))
			if default_session:
				self.frame.openDefault(default_session)
			self.frame.Show(True)
			self.SetTopWindow(self.frame)
			
			return True

	app = MyApp(redirect=False) #=True,filename="applogfile.txt")


	from random import choice
	from sys import maxint

	app.frame.Layout()
	try:
		app.MainLoop()
	except Exception, e:
		traceback.print_exc();