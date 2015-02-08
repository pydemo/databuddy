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
__version__ = "1.0.1"
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

import __builtin__
__builtin__.copy_vector = None
__builtin__.cvarg = None
import common.v101.config as conf

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
		print 'UltListCtrl.appendList'
		pprint(charge)
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
			print 'idx=self.InsertStringItem', idx
			msg =charge[0].strip()
			print 'msg =charge[0].strip()', msg
			if msg:
				s=self.SetStringItem(idx, 1, charge[0].strip())
				print 's=self.SetStringItem(idx, 1, charge[0].strip())',s
				if if_error:
					item = self.GetItem(idx,1)
					item.SetMask(ULC.ULC_MASK_BACKCOLOUR)
					pink=wx.Colour(255, 168, 168, 255)
					item.SetBackgroundColour(pink)
					self.SetItem(item)
					
	def appendList_(self, items,now,charge, if_error=False):
		if len(charge)==1 and type(charge)==types.ListType and '\n' in charge[0]:
			charge=charge[0].split('\n')
		pprint(charge)
		
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
			pprint (msg)
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
	def __init__(self, splitter, parent,  id,pos):
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
		#self.db= OracleDb(self,pos)
		#EVT_SIGNAL(self, self.relaySignal)
		#self.file= FileDir(pos)
		self.il = wx.ImageList(16, 16)
		#self.sm_up = self.il.Add(images.SmallUpArrow.GetBitmap())
		#self.sm_dn = self.il.Add(images.SmallDnArrow.GetBitmap())		
		for i in range(len(self.images)):
			
			img=self.images[i]
			print img
			self.il.Add(wx.Bitmap(img))
			self.image_refs[img]=i
		self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)	
		#self.setNavlist()		
		

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
		print 'Selected!',event.m_itemIndex
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
		print configDirLoc,ConfigList
		config_file= '%s.xml' % os.path.join(configDirLoc,ConfigList )
		print config_file
		#sys.exit(1)
		#e(0)
		#print config_file
		self.InsertColumn(0, 'Name')
		self.InsertColumn(1, 'Type')
		self.InsertColumn(2, 'Vector')
		#self.InsertColumn(4, 'Desription')

		self.SetColumnWidth(0, 120)
		self.SetColumnWidth(1, 60)
		self.SetColumnWidth(2, 100)

		#self.SetColumnWidth(4, 420)
		self.img_col = 1
		
		#self.il = uListCtrl.PyImageList(22,22)	
		#files = os.listdir('.')
		j = 0
		#self.idx_first=self.InsertStringItem(0, '[..]')
		#self.SetItemImage(0, self._imgstart+3)
		
		self.data[self.current_list]={0: (u'TestCopy1', u'Copy', u'ora2ora'),
 1: (u'Extract1', u'Extract', 'ora2csv'),
 2: (u'QA_copy_0', u'Copy', 'ora2db2'),
 3: (u'Daily_qc', u'Load', 'csv2ora',)}
		#print dbs
		#sys.exit(1)
		print self.parent
		self.parent.RecreateList(None,(self.parent.list,self.parent.filter))
		#self.parent.list.Thaw()
		if 0:
			for  key,i in self.data[self.current_list].items():
				#print i
				#sys.exit(1)
				if  1:
					index=self.InsertStringItem(sys.maxint, str(i[0]))
					self.SetStringItem(index, 1, str(i[1]))
					self.SetStringItem(index, 2, str(i[2]))
					self.SetStringItem(index, 3, str(i[3]))
					self.SetItemData(index, key)

					if i[1] == 'DEV':
						self.img[key]=self._imgstart+11
						self.SetItemImage(index, self.img[key])					
					else:
						self.img[key]=self._imgstart+11
						self.SetItemImage(index, self.img[key])	

					if i[1] == 'PROD':
						self.img[key]=self._imgstart+10
						self.SetItemImage(index, self.img[key])	
					if i[1] == 'UAT':
						self.img[key]=self._imgstart+12
						self.SetItemImage(index, self.img[key])	
					if i[1] == 'QA':
						self.img[key]=self._imgstart+13
						self.SetItemImage(index, self.img[key])	
						
					if (j % 2) == 0:
						self._bg='#e6f1f5'
						self.SetItemBackgroundColour(j, self._bg)
					j += 1		
					#sys.exit(1)
					
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
		if 0:
			for i in range(100):
				self.logList.append('test %d' % i)
		self.sizer.Add(self.logList, 1, wx.GROW|wx.ALL, 1)

		self.SetSizer(self.sizer)
		#self.sizer.Fit(self)
		print self.logList._mainWin
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
	def __init__(self, parent, pos, panel_pos # log
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

			self.list = SessionList(self.listsplit, self, -1,self.pos)
			

			self.filter =self.getFilter(self,self.list)
			self.filter_history={}
			self.currentItem = 0
		

		if 1:
			#self.btnHome = wx.Button(self, -1, "[.]", style=wx.BU_EXACTFIT, size=(30,20))
			#self.btnUp = wx.Button(self, -1, "[..]", style=wx.BU_EXACTFIT, size=(30,20))
			

			imageFile = "bmp_source/arrow_back_dgrey_16x2.png"
			image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			if 0:
				self.btn_back=wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				imageFile = "bmp_source/arrow_back_grey_16x2.png"
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.btn_back.SetBitmapDisabled(image1)
				self.btn_back.Disable()
			if 0:
				imageFile = "bmp_source/arrow_forward_dgrey_16x2.png"
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.btn_fwd=wx.BitmapButton(self, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))
				imageFile = "bmp_source/arrow_forward_grey_16x2.png"
				image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
				self.btn_fwd.SetBitmapDisabled(image1)
				self.Bind(wx.EVT_BUTTON, self.OnBackButton, self.btn_back)
				self.Bind(wx.EVT_BUTTON, self.OnForwardButton, self.btn_fwd)
				self.btn_fwd.Bind(wx.EVT_RIGHT_DOWN, self.OnForwardButtonRightUp)
				self.btn_fwd.Disable()
				
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
				#self.statusbar.SetSize((-1, 23))
				#self.statusbar.SetFieldsCount(4)
				#self.SetStatusBar(self.statusbar)        
				#self.statusbar.SetStatusWidths([  250, 120, 140])
				if 0:
					bmp = wx.ArtProvider_GetBitmap(wx.ART_ERROR,
												   wx.ART_TOOLBAR, (16,16))
					
					upbmp = wx.StaticBitmap(self.statusbar, -1, bmp)

					bmp = wx.ArtProvider_GetBitmap(wx.ART_HELP,
												   wx.ART_TOOLBAR, (16,16))
					
					downbmp = wx.StaticBitmap(self.statusbar, -1, bmp)
					btnmio = wx.Button(self.statusbar, -1, "Push Me!")
				
				if 0:
					choice = wx.Choice(self.statusbar, -1, size=(100,-1),
									   choices=['Hello', 'World!', 'What', 'A', 'Beautiful', 'Class!'])
					ticker = Ticker(self.statusbar, -1)
					ticker.SetText("Hello World!")
					ticker.SetBackgroundColour(wx.BLUE)
					ticker.SetForegroundColour(wx.NamedColour("YELLOW"))
					ticker.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD, False))
					statictext = wx.StaticText(self.statusbar, -1, "Welcome To %s!" % prog)
					
					self.ticker = ticker
				#bmp = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
				#titleIco = wx.StaticBitmap(self.panel, wx.ID_ANY, bmp)

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
				if 0:
					self.statusbar = wx.BoxSizer(wx.HORIZONTAL)
					#self.sPanel.status = wx.BoxSizer(wx.HORIZONTAL)
					gauge={}
					self.gauge=gauge
					#self.gauge=gauge
					for pos in self.p_pos:
						self.gauge[pos] = wx.Gauge(self, -1, size=(-1, 12),	style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
						#self.sPanel.statusbar.Add(self.gauge[pos], 0, wx.EXPAND,0)	
						#self.gauge[pos].SetPosition((1,1))
						#self.gauge[pos].Hide()	
						#items.append(self.gauge[pos])
					#self.gauge = gauge

					#self.Bind(wx.EVT_TIMER, self.TimerHandler0)
					#self.gen_bind(wx.EVT_TIMER,self, self.TimerHandler_pos,(self.panel_pos[0]))
					btn_stop={}
				
					self.btn_stop=btn_stop
					#self.btn_stop=btn_stop
					for pos in self.p_pos:
						self.btn_stop[pos] = wx.Button(self, -1, "Stop", size=(30,15)) 
						#self.sPanel.statusbar.Add([self.gauge[pos],self.btn_stop[pos]], 1, wx.EXPAND,1)
						#self.btn_stop[pos].Hide()
						self.btn_stop[pos].SetPosition((self.gauge[pos].GetSize()[0],1))
						self.gen_bind(wx.EVT_BUTTON,self.btn_stop[pos], self.OnStopDbRequest,(pos))
						#self.btn_stop[pos].Hide()
						#items.append(self.btn_stop[pos])
				

					if 0:
						self.cb_c = wx.CheckBox(self, wx.ID_ANY, "cache")
						self.Bind(wx.EVT_CHECKBOX, self.OnUseCache, self.cb_c)
						self.cb_c.SetValue(False)
						self.cb_c.Enable(False)
						self.statusbar.Add((10,5))

					self.statusbar.Add(self.gauge[self.pos], 1,wx.ALL|wx.GROW|wx.EXPAND,1)
					self.statusbar.Add((1,1))
					self.statusbar.Add(self.btn_stop[self.pos], 0,wx.RIGHT,1)

				


			




		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelected, self.list)
		self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.list)

		self.list.Populate()
		if 1:
			if 0:
				from wx.lib.agw import ultimatelistctrl as ULC


				self.url_combo_list = ULC.UltimateListCtrl(self.ulocPanel, wx.ID_ANY, agwStyle=wx.LC_REPORT|wx.LC_VRULES|wx.LC_HRULES|wx.LC_SINGLE_SEL|ULC.ULC_HAS_VARIABLE_ROW_HEIGHT)

				self.url_combo_list.InsertColumn(0, "Column 1")
				self.url_combo_list.InsertColumn(1, "Column 2")

				index = self.url_combo_list.InsertStringItem(sys.maxint, "Item 1")
				self.url_combo_list.SetStringItem(index, 1, "Sub-item 1")

				index = self.url_combo_list.InsertStringItem(sys.maxint, "Item 2")
				self.url_combo_list.SetStringItem(index, 1, "Sub-item 2")

				choice = wx.Choice(self.url_combo_list, -1, choices=["one", "two"])
				index = self.url_combo_list.InsertStringItem(sys.maxint, "A widget")

				self.url_combo_list.SetItemWindow(index, 1, choice, expand=True,)
			if 0:
				self.cc = wx.combo.ComboCtrl(self, style=wx.combo.CC_BUTTON_OUTSIDE_BORDER, size=(30,-1))
				self.cc.SetPopupExtents(-1,100)
				self.cc.SetPopupMaxHeight(50)
				# Create a Popup
				self.popup = ListCtrlComboPopup()

				# Associate them with each other.  This also triggers the
				# creation of the ListCtrl.
				self.cc.SetPopupControl(self.popup)
				for x in range(75):
					self.popup.AddItem("Item-%02d" % x)

			
			#self.popup.Create(wx.PreListCtrl())
			# Add some items to the listctrl.
			
			if 0:
				self.url_combo_list = wx.ListCtrl(self, -1,  size=(-1,100),
				style=wx.LC_REPORT
							 |wx.BORDER_SUNKEN
							 )
							 
				self.url_combo_list.InsertColumn(0, 'Subject')

				self.url_combo_list.InsertColumn(1, 'Due')

				self.url_combo_list.InsertColumn(2, 'Location', width=125)
				self.url_combo_list.InsertStringItem(0, '1')
				self.url_combo_list.SetStringItem(0, 1, "01/19/2010")
				self.url_combo_list.SetStringItem(0, 2, "USA")


			#self.url_combo_list.Hide()
			#print dir(self.ulocPanel)
			#self.createUrlLocator()
			if 0:
				upsizer = wx.BoxSizer(wx.HORIZONTAL)
				upsizer.Add((5,15), 0, wx.EXPAND)
				upsizer.Add(self.ulocPanel, 1, wx.EXPAND|wx.ALL)
			
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
			print (width,height)
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
	def OnUseCache(self, event):
		print 'use cache', self.pos
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
	def setUrlLocator_del(self):
		#print '--setUrlLocator---'
		#self.url_locator={}
		print  self.url_locator
		nav_keys=self.list.nav_list.keys()
		if len(self.url_locator)<len(nav_keys)-1:
			print len(self.url_locator),len(nav_keys)
			self.createUrlLocator()
		
		for loc_id in range(len(nav_keys)): #self.list.loc_url:
			loc=nav_keys[loc_id]
			if 1 and loc!='vars':
				print 'hiding', loc 
				if self.url_locator.has_key(loc):
					self.url_locator[loc].Hide()
					self.find_in_btn[loc].Hide()
				
		#print  self.list.nav_list.keys()
		#print self.list.loc_url
		offset=0
		prev_loc=None
		print  nav_keys
		print self.list.nav_list['vars'].keys()
		var_keys=self.list.nav_list['vars'].keys()[1:]
		print var_keys
		if not var_keys:
			#self.clearUrlLocator()
			pass
		else:
			for loc_id in range(len(var_keys)): #self.list.loc_url:
				loc=var_keys[loc_id]
				print 'location url',  loc
				if 1 or self.list.nav_list['vars'].has_key(loc):
					if 1 or loc!='vars' and loc_id>0:
						#print '???????',loc , self.list.nav_list['vars'].has_key(loc)
						#print self.list.nav_list['vars']
						#self.url_locator[loc].Show()
						if 0:
							if loc_id>1:
								offset +=self.url_locator[loc].GetSize()[0] +12 #+self.find_in_btn[prev_loc].GetSize()[0]
								#print 'offset', offset
								#print self.url_locator[prev_loc].GetSize()[0]
								#print self.find_in_btn[prev_loc].GetSize()[0]
							else:
								if loc_id==1:
									offset +=self.find_in_btn[loc].GetSize()[0] 
									self.find_in_btn[loc].SetPosition((0,0))
									self.find_in_btn[loc].Show()
						self.find_in_btn[loc].SetPosition((offset,0))
							
						
						offset +=self.find_in_btn[loc].GetSize()[0]		
						if 0:
							if self.list.nav_list['vars'].has_key(loc) :					
								#print '000has key00', loc,self.list.current_list

								
								url_label = self.list.nav_list['vars'][loc]
								self.url_locator[loc].SetLabel(url_label)						
								self.url_locator[loc].SetPosition((offset,0))
								self.url_locator[loc].Show()
								

								offset +=self.url_locator[loc].GetSize()[0]
								self.find_in_btn[loc].Show()

								#self.url_locator[loc].Refresh()
								#if self.list.current_list==loc:
								#	break;
							else:
								pass
						if loc_id==(len(var_keys)-1):
							#self.find_in_btn[loc].SetPosition((0,0))
							#self.find_in_btn[loc].Show()						
							#print '000has key00', loc,self.list.current_list
							
							url_label = self.list.nav_list['vars'][loc]
							print 'last url', loc,self.list.current_list, url_label
							self.no_url_loc.SetLabel(url_label)
							self.no_url_loc.SetPosition((offset,0))
							self.no_url_loc.Show()

							self.find_in_btn[loc].Show()
							break
						else:
							url_label = self.list.nav_list['vars'][loc]
							print 'mid url', loc,self.list.current_list,url_label
							self.url_locator[loc].SetLabel(url_label)						
							self.url_locator[loc].SetPosition((offset,0))
							self.url_locator[loc].Show()
							

							offset +=self.url_locator[loc].GetSize()[0]
							self.find_in_btn[loc].Show()

							#self.url_locator[loc].Refresh()
							#if self.list.current_list==loc:
							#	break;

								
					prev_loc=loc

	def OnFindInButton(self, event,params):
		(loc_id,loc)=params
		print (loc_id,loc)
		#print dir(event)
		#btn=event.GetEventObject()
		#print btn.GetPosition()
		#print btn.GetSize()
		#print btn.GetPosition()[0]
		btn = event.GetEventObject()
		#import flat_menu2
		# Create the popup menu
		#self.CreateLongPopupMenu()
		print 'creating PopupMenu((((((((((((', loc
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
			print self.pos
			print loc
			print self.list.data.keys()
			if loc in self.list.data.keys():
				for key, item in self.list.data[loc].items():
					menuItem = FM.FlatMenuItem(pmenu, 20001+key, '%s' % item[0], "", wx.ITEM_RADIO)
					print item[0], self.list.nav_list['vars'][loc],  item[0]==self.list.nav_list['vars'][loc]
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
		print item_id
		#self.list.nav_list['vars'][loc]=
		#print self.list., self.list.data[loc][item_id]
		print  params
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
		self.currentItem = event.m_itemIndex
		#print self.list.GetItemText(self.currentItem)
		msg='%s %s ' % (self.list.current_list[:-4], self.list.GetItemText(self.currentItem).strip('[]'))
		self.Status(msg)		
		#print 'selected'
		#print(self)
		#btns=self.list.nav_list[self.list.current_list]['hot_keys']
		#print btns
		#Publisher().sendMessage( "enable_buttons", (self.pos,btns) )			
		event.Skip()		
		
	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)			
	def __onGaugeStop(self,data, extra1, extra2=None):
		( pos) = data
		if pos==self.pos:		
			print 'onGaugeStop', pos
			self.gaugeStop(pos)	
			#self.gauge[pos].Hide()
			#self.btn_stop[pos].Hide()			
	def __onGaugeStart(self,data, extra1, extra2=None):
		( pos) = data
		print '=============================onGaugeStart',pos,self.pos
		if pos==self.pos:		
			#self.sPanel.SetSizer(self.sPanel.statusbar)
			print 'onGaugeStart',pos
			self.gaugeStart(pos)
			#self.gauge[pos].Show()
			#self.btn_stop[pos].Show()			
		
	def gaugeStart(self,pos):
		print pos
		print self.gauge
		print  'gaugeStart'
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
		print '||||||||||||||||| setting count', self.count[pos]
		self.gauge[pos].SetValue(self.count[pos])
		#self.gauge.Pulse()
		
	def onShowProgress(self, evt):
		if 0:
			self.progress_bar.Show()
			self.progress_bar.SetRange(10)
			print 'in ShowProgress'
			self.progress_bar.SetValue(5)
			#print (dir(self.progress_bar))
		self.gauge.Show()
	def OnClose(self, event):

		#self.ticker.Stop()
		self.Destroy()

	def OnSize1(self, event):
		size = self.GetSize()
		print 'Size event'
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
		print 'onFileDirEvent'
		(st, pos,cache,result) = evt.data
		print '--onFileDirEvent', st
		print self.pos,'==',pos
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
			print '-----------request aborted',self.pos,pos
			if self.pos==pos:
				print 'request aborted',pos
				self.gaugeStop(self.pos)	
				self.list.Thaw()
		#if self.pos==pos:
		#	updateCache(cache,self.list.data)
		
	def onRefreshListEvent(self, evt):
		print 'onRefreshListEvent'
		(st, pos,cache,result) = evt.data
		print 'onRefreshListEvent', st
		print self.pos,'==',pos
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
			print '----------------onForceSearch', position, fltr
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
				print 'OnSearchMenu/fullSearch'
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
		print 'OnSearch',fltr, self.searchItems
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
	def RecreateList(self, evt=None, tf=None):
		# Catch the search type (name or content)
		cl =self.list.current_list
		print '############# in RecreateList', self.pos,'cl:', cl
		(list, filter) = tf
		fltr = filter.GetValue()
		favs={}
		print fltr
		print self.list.current_list, 1
		#btns=self.list.nav_list[self.list.current_list]['hot_keys']
		#Publisher().sendMessage( "set_buttons", (self.list.pos,btns) )
		if 1:
			searchMenu = filter.GetMenu().GetMenuItems()
			fullSearch = searchMenu[1].IsChecked()
			searchItems=self.searchItems
			if evt:
				if fullSearch:
					print 'RecreateList/fullSearch'
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
				print keys
				if keys:
					#print keys
					j=0
					list.DeleteAllItems()

					for key in keys:
						i= list.data[list.current_list][key]

						if  1:
							index=list.InsertStringItem(sys.maxint, item_mask % i[0])
							for idx in range(1,len(i)):
								list.SetStringItem(index, idx, str(i[idx]))
							

							list.SetItemData(index, key)
							
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
							
						

			print 'list.Thaw()'
			#print (dir(list))
			print list.pos

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
		print (loc_to,path)
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
					print id, self.curr_hist_id
					tup=self.nav_hist[id]
					(loc_to, path)=tup
					print id, self.curr_hist_id
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
		print (loc_to,path)
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
		print (loc)
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
			print 'gfavs:', gfavs
			gkeys=gfavs.keys()
			#gkeys=sorted(gkeys,key=lambda path: len(path.split('/'))) #reverse=True
			gkeys.sort()
			pprint(gkeys)
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
					print '--item--',ikey, val
					itype=wx.ITEM_NORMAL
					menuItem = FM.FlatMenuItem(pmenu, wx.ID_ANY, '%s %s' % (ikey, p), "", itype)
					pmenu.AppendItem(menuItem)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnFavMenu,(loc_id,'%s/%s' %(val,ikey)))
				first=False

	def OnHistMenu(self, event, params):
		(loc_to,path) = params

		print (loc_to,path)
		vars=self.list.getVarsFromPath(path,'/')[1:]
		self.list.setNavlist()
		if len(vars)>2:
			conn=self.list.getConnectType(path)
			print conn
			print 'before',self.list.nav_list.keys()
			self.list.extendNavlist(conn)
			print 'after',self.list.nav_list.keys()
				
		self.list.initVarsFromPath(path,'/')
		self.list.setCurrListName(loc_to, 'reset')		
		self.list.execList(loc_to)
		self.add_nav_hist(loc_to)
	def OnFavMenu0(self, event, params):
		(loc_to,path) = params
		if 1:
			print (loc_to,path)
			self.list.initVarsFromPath(path,'/')
			self.list.setCurrListName(loc_to, 'reset')		
			self.list.execList(loc_to)
			self.add_nav_hist(loc_to)
	def OnFavMenu(self, event, params):
		(loc_id,path) = params
		if 1:
			print (loc_id,path)
			vars=self.list.getVarsFromPath(path,'/')[1:]
			print 'new vars:'
			print vars
			self.list.setNavlist()
			if len(vars)>2:
				conn=self.list.getConnectType(path)
				print conn
				print 'before',self.list.nav_list.keys()
				self.list.extendNavlist(conn)
				print 'after',self.list.nav_list.keys()
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
		print "OnItemDeselected: %d" % evt.m_itemIndex
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
		print "OnItemDelete\n"
		#self.log.WriteText("OnItemDelete\n")

	def OnColClick(self, event):
		print "OnColClick: %d\n" % event.GetColumn()
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
		print "OnColRightClick: %d %s\n" % (event.GetColumn(), (item.GetText(), item.GetAlign(), item.GetWidth(), item.GetImage()))
		#self.log.WriteText("OnColRightClick: %d %s\n" %
		#                   (event.GetColumn(), (item.GetText(), item.GetAlign(),
		#                                        item.GetWidth(), item.GetImage())))

	def OnColBeginDrag(self, event):
		print "OnColBeginDrag\n"
		#self.log.WriteText("OnColBeginDrag\n")
		## Show how to not allow a column to be resized
		#if event.GetColumn() == 0:
		#    event.Veto()


	def OnColDragging(self, event):
		print "OnColDragging\n"
		#self.log.WriteText("OnColDragging\n")

	def OnColEndDrag(self, event):
		print "OnColEndDrag\n"
		#self.log.WriteText("OnColEndDrag\n")

	def OnDoubleClick(self, event):
		print "OnDoubleClick item %s\n" % self.list.GetItemText(self.currentItem)
		#self.log.WriteText("OnDoubleClick item %s\n" % self.list.GetItemText(self.currentItem))
		event.Skip()
	def getSide(self,pos):
		side =None
		id ='%d%d' % pos 
		if self.sides.has_key(id):
			side=self.sides[id]
		return side
	def OnRightClick(self, event):
		print "OnRightClick %s\n" % self.list.GetItemText(self.currentItem),self.list.GetSelectedItemCount()
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
					print '---ii--',sid, 20100+int(sid)
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
				print sid, side, self.panel_pos
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
		print self.delete_conn		
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
		print self.delete_conn
		conn_alias=self.delete_conn[0][2].strip('[').strip(']')
		login=(user,db,pwd,host,port) = self.getConnectInfo(conn_alias)
		print login
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
		print self.delete_conn		
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
			print conf_list
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
			print conf_list	
			for crow in conf_list:			
				cfile =crow[2].strip('[').strip(']')		
				config_file= '%s.xml' % os.path.join(configDirLoc, '%s' % cfile)
				print config_file		
				#get env connects
				env_list = self.list.db.getEnvironments(config_file)
				print env_list
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
			print env_list
		
			cfile =self.list._ConfigList
			config_file= '%s.xml' % os.path.join(configDirLoc, '%s' % cfile)
			print config_file		
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
		pprint(cons)
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
		print 'OnAddNewConnection'
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
		print 'OnShowIn'
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
		
	def OnRightClick_00(self, event):
		print "OnRightClick %s\n" % self.list.GetItemText(self.currentItem)
		#self.log.WriteText("OnRightClick %s\n" % self.list.GetItemText(self.currentItem))

		# only do this part the first time so the events are only bound once
		if not hasattr(self, "popupID1"):
			self.popupID1 = wx.NewId()
			self.popupID2 = wx.NewId()
			self.popupID3 = wx.NewId()
			self.popupID4 = wx.NewId()
			self.popupID5 = wx.NewId()
			self.popupID6 = wx.NewId()

			self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
			self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)
			self.Bind(wx.EVT_MENU, self.OnPopupThree, id=self.popupID3)
			self.Bind(wx.EVT_MENU, self.OnPopupFour, id=self.popupID4)
			self.Bind(wx.EVT_MENU, self.OnPopupFive, id=self.popupID5)
			self.Bind(wx.EVT_MENU, self.OnPopupSix, id=self.popupID6)

		# make a menu
		menu = wx.Menu()
		# add some items
		menu.Append(self.popupID1, "FindItem tests")
		menu.Append(self.popupID2, "Iterate Selected")
		menu.Append(self.popupID3, "ClearAll and repopulate")
		menu.Append(self.popupID4, "DeleteAllItems")
		menu.Append(self.popupID5, "GetItem")
		menu.Append(self.popupID6, "Edit")

		# Popup the menu.  If an item is selected then its handler
		# will be called before PopupMenu returns.
		self.PopupMenu(menu)
		menu.Destroy()

	def OnAddToFavorites(self, event):
		print 'OnAddToFavorites'
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

		print 'si',selected_items
		self.addToFavorites(selected_items)

	def OnRemoveFromFavorites(self, event):
		print 'OnRemoveFromFavorites'
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

		print 'si',selected_items
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
				print 'removing:', self.list.data[self.list.current_list][id][0]
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
			print "      %s: %s\n" % (self.list.GetItemText(index), self.getColumnText(index, 1))
			#self.log.WriteText("      %s: %s\n" % (self.list.GetItemText(index), self.getColumnText(index, 1)))
			index = self.list.GetNextSelected(index)

	def OnPopupThree(self, event):
		print "Popup three\n"
		#self.log.WriteText("Popup three\n")
		self.list.ClearAll()
		wx.CallAfter(self.PopulateList)

	def OnPopupFour(self, event):
		self.list.DeleteAllItems()

	def OnPopupFive(self, event):
		item = self.list.GetItem(self.currentItem)
		print item.m_text, item.m_itemId, self.list.GetItemData(self.currentItem)

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
		start=SessionListCtrlPanel(self,pos,self.panel_pos)
		self.start=start
		self.list=start.list
		self.nb.AddPage(start,'')
		self.nb.SetPageText(0, 'My Sessions')
		#tmpl=SessionListCtrlPanel(self,pos,self.panel_pos)
		#self.nb.AddPage(tmpl,'Templates')
		
		self.nb.SetSelection(0)
		
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
					print 'colour----------------------------',dlg.GetColourData().GetColour()
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
			self, parent, ID, title, size,plist, pos=wx.DefaultPosition, 
			style=wx.DEFAULT_DIALOG_STYLE,
			useMetal=False, 
			):

		# Instead of calling wx.Dialog.__init__ we precreate the dialog
		# so we can set an extra style that must be set before
		# creation, and then we create the GUI object using the Create
		# method.
		self.parent=parent
		self.plist=plist
		self._popUpMenu = None
		self.recent=[]
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
			sb = wx.StaticBox(self, label="Type")
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
			
			self.rb_so_query=wx.RadioButton(self, label="Query",style=wx.RB_GROUP)
			boxsizer.Add(self.rb_so_query, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_so_query.Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
			
			self.rb_so_table=wx.RadioButton(self, label="Table")
			boxsizer.Add(self.rb_so_table, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_so_table.Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
			
			self.rb_so_part=wx.RadioButton(self, label="Partition")
			boxsizer.Add(self.rb_so_part, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_so_part.Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
			
			self.rb_so_spart=wx.RadioButton(self, label="Sub-Partition")
			boxsizer.Add(self.rb_so_spart, flag=wx.LEFT|wx.TOP, border=5)
			self.rb_so_spart.Bind(wx.EVT_RADIOBUTTON, self.onSourceObjButton)
			
			if 0:
				rb=wx.RadioButton(self, label="FTP")
				boxsizer.Add(rb, flag=wx.LEFT|wx.TOP, border=5)
				rb.Enable(False)
				rb=wx.RadioButton(self, label="Pipe")
				boxsizer.Add(rb, flag=wx.LEFT|wx.TOP, border=5)
				rb.Enable(False)			
			#sizer.Add(boxsizer, pos=(2, 0), span=(1, 2), flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)
			optsizer.Add(boxsizer, 0 , wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT)	
		if 1:
			sb = wx.StaticBox(self, label="Target Object")
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			#boxsizer.Add(wx.RadioButton(self, label="Query",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=5)
			boxsizer.Add(wx.RadioButton(self, label="Table",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=5)
			boxsizer.Add(wx.RadioButton(self, label="Partition"), flag=wx.LEFT|wx.TOP, border=5)
			boxsizer.Add(wx.RadioButton(self, label="Sub-Partition"), flag=wx.LEFT|wx.TOP, border=5)
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
			
		self.create_btn = wx.Button(self, ID_CREATE, "Create")
		self.create_btn.Enable(False)
		button4 = wx.Button(self, ID_EXIT, "Cancel")
		btnsizer.Add((3,3),1)
		btnsizer.Add(self.create_btn, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		btnsizer.Add((40,5),0)
		
		btnsizer.Add(button4, 0 , wx.RIGHT|wx.BOTTOM|wx.ALIGN_BOTTOM)
		
		self.Bind(wx.EVT_BUTTON, self.OnCreate, id=ID_CREATE)
		self.Bind(wx.EVT_BUTTON, self.OnExit, id=ID_EXIT)
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
			#print api_menu		
		
	def onSourceObjButton(self, event): 
		""" 
		Source object filter
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()

		
	def onUseRbButton(self, event): 
		""" 
		Use type
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		if 'MANUALLY' in label.upper():
			self.create_btn.Enable(True)	
		else:
			print 'targlistCtrl',self.targlistCtrl.GetFirstSelected()
			if self.targlistCtrl.GetFirstSelected()<0:
				self.create_btn.Enable(False)
			else:
				print 'listCtrl', self.listCtrl.GetFirstSelected()
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
		for f in apimod.aa: 
			print f
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
		print str(self.__class__) + " - OnItemSelected"
		currentItem = event.m_itemIndex
		self.targlistCtrl.ClearAll()
		src_val=self.listCtrl.GetItem(itemId=currentItem, col=0).GetText()
		#self.list_ctrl.GetItem(itemId=currentItem, col=0).GetText()
        #    print item
		self.targlistCtrl.InsertColumn(0, 'Target Template')	
		self.targlistCtrl.SetColumnWidth(0, 320)
		print src_val
		#print self.tmpl[src_val]
		for t in self.tmpl[src_val]:
			self.targlistCtrl.InsertStringItem(0, t)
		self.create_btn.Enable(False)
		event.Skip()
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
		self.Close(True)
	def OnCreate(self,e):
		if not self.tc_sname.GetValue():
			self.Warn('Enter session name.')
			self.tc_sname.SetFocus()	
		else:
			send("create_new_session", (self.tc_sname.GetValue(),self.copy_vector) )
			self.Close(True)
	def Warn(self, message, caption = 'Warning!'):
		dlg = wx.MessageDialog(self, message, caption, wx.OK | wx.ICON_WARNING)
		dlg.ShowModal()
		dlg.Destroy()
  

	
	def OnCVClicked(self, event):

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
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, "Recent", "", wx.ITEM_NORMAL, self.recentMenu)
				self._popUpMenu.AppendItem(menuItem)				
				for r in self.recent:
					(a,b)=r
					self.i +=1
					#Menu1 = FM.FlatMenu()
					menuItem = FM.FlatMenuItem(self.recentMenu, 20000+self.i, "%s --> %s" % (conf.dbs[a],conf.dbs[b]), "", wx.ITEM_NORMAL)
					self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
					self.recentMenu.AppendItem(menuItem)
				self._popUpMenu.AppendSeparator()	
			for k in self.api2:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, "From %s" % dbf[k], "", wx.ITEM_NORMAL, Menu1)
				self._popUpMenu.AppendItem(menuItem)
				
				
				for sm in self.api_menu[k]:
					if len(self.api_menu)>1:
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
			for sm in conf.ff:
				self.i +=1
				Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self._popUpMenu, 20000+self.i, "From %s" % sm, "", wx.ITEM_NORMAL, Menu1)
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
			for r in reversed(self.recent):
				(a,b)=r
				self.i +=1
				#Menu1 = FM.FlatMenu()
				menuItem = FM.FlatMenuItem(self.recentMenu, 20000+self.i, "%s --> %s" % (conf.dbs[a],conf.dbs[b]), "", wx.ITEM_NORMAL)
				self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(a,b))
				self.recentMenu.AppendItem(menuItem)

	def create_Menu2(self,Menu1,sm,dbf):
		self.i +=1
		Menu2 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu1, 20000+self.i, "From %s" % conf.dbs[sm] , "", wx.ITEM_NORMAL, Menu2)
		Menu1.AppendItem(menuItem)
		#self.set_sub_submenu(subSubMenu,1, 'CSV')
		
		for k2 in self.api2:
			self.i +=1
			if len(self.api_menu[k2])>1:
				self.create_Menu3(Menu2,k2,dbf,from_db=sm)
			else:
				self.create_Menu4(Menu2,self.api_menu[k2][0],from_db=sm)
			
	def create_Menu3(self,Menu2,k2,dbf,from_db):
		self.i +=1
		Menu3 = FM.FlatMenu()
		menuItem = FM.FlatMenuItem(Menu2, 20000+self.i, "To %s" % dbf[k2], "", wx.ITEM_NORMAL, Menu3)
		Menu2.AppendItem(menuItem)
		
		for sm2 in self.api_menu[k2]:
			self.i +=1
			self.create_Menu4(Menu3,sm2,from_db)	
			

	def create_Menu4(self,Menu3,sm2,from_db):
		#Menu4 = FM.FlatMenu()
		self.i +=1
		
		menuItem = FM.FlatMenuItem(Menu3, 20000+self.i, "To %s" % conf.dbs[sm2] , "", wx.ITEM_NORMAL)
		#print from_db,sm2
		self.gen_bind(FM.EVT_FLAT_MENU_SELECTED,menuItem, self.OnMenu,(from_db,sm2))
		Menu3.AppendItem(menuItem)
		#self.set_sub_submenu(subSubMenu,1, 'CSV')
			

	def set_vector_btn(self,a,b):	
		print a,b
		lbl='%s->%s' % (a,b)
		self.b_vector.SetLabel(lbl.lower())
		self.copy_vector=[a,b]
		self.refresh_src_list()

	def OnMenu(self, event, params):
		(a,b) = params
		if (a,b) not in self.recent:
			self.recent.append((a,b))
		print '###########', self.recent
		self.set_vector_btn(a,b)
		self.create_btn.Enable(False)
		
		
		


	def gen_bind(self, type, instance, handler, *args, **kwargs):
		self.Bind(type, lambda event: handler(event, *args, **kwargs), instance)

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
		args_vbox = wx.BoxSizer(wx.VERTICAL)
		args_hbox = wx.BoxSizer(wx.HORIZONTAL)
		
		if 1: #Common
			
			panel_from = wx.Panel(self)
			hbox = wx.BoxSizer(wx.HORIZONTAL)
			fgs = wx.GridBagSizer(4, 4)
			#sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			#sizer.Add(tc0, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			#fgs = wx.FlexGridSizer(3, 4, 9, 20)
			ttl=['Copy vector','Pool size','Num of shards','Field terminator','Truncate target']
			#pprint(dir(fgs))
			
			txt, txt_ctrl= (wx.StaticText(panel_from, label='Copy vector:'), wx.TextCtrl(panel_from,value='ora11g2ora11g'))
			#txt_ctrl.Value=
			txt_ctrl.Enable(False)
			fgs.Add(txt, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			fgs.Add(txt_ctrl, pos=(0, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(panel_from, label='Field terminator:'), wx.TextCtrl(panel_from, size=(20,-1), value='|'))
			fgs.Add(txt, pos=(1, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			fgs.Add(txt_ctrl, pos=(1, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(panel_from, label='Pool size:'), wx.TextCtrl(panel_from, size=(20,-1), value='1'))
			fgs.Add(txt, pos=(2, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			fgs.Add(txt_ctrl, pos=(2, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			txt, txt_ctrl= (wx.StaticText(panel_from, label='Num of shards:'), wx.TextCtrl(panel_from, size=(20,-1), value='1'))
			fgs.Add(txt, pos=(3, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)
			fgs.Add(txt_ctrl, pos=(3, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=1)

			#sb = wx.StaticBox(panel_from, label="Truncate Target:")
			txt=wx.StaticText(panel_from, label='Truncate target:')
			ynbox =  wx.BoxSizer( wx.HORIZONTAL)
			ynbox.Add(wx.RadioButton(panel_from, label="Yes",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=0)
			ynbox.Add(wx.RadioButton(panel_from, label="No"), flag=wx.LEFT|wx.TOP, border=0)
			fgs.Add(txt, pos=(0, 2), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
			fgs.Add(ynbox, pos=(0, 3), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
			if 0:
				fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				txt, txt_ctrl= (wx.StaticText(panel_from, label='Field terminator:'), wx.TextCtrl(panel_from, size=(20,-1), value='|'))
				fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				txt, txt_ctrl= (wx.StaticText(panel_from, label='Pool size:'), wx.TextCtrl(panel_from, size=(20,-1), value='1'))
				fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
				
				sb = wx.StaticBox(panel_from, label="Truncate Target")
			
				ynbox =  wx.StaticBoxSizer(sb, wx.HORIZONTAL)
				ynbox.Add(wx.RadioButton(panel_from, label="Yes",style=wx.RB_GROUP), flag=wx.LEFT|wx.TOP, border=0)
				ynbox.Add(wx.RadioButton(panel_from, label="No"), flag=wx.LEFT|wx.TOP, border=0)
				
			
				txt_ctrl= ( ynbox)
				fgs.AddMany([(txt_ctrl, 0, wx.EXPAND, 5)])
				txt, txt_ctrl= (wx.StaticText(panel_from, label='Num of shards:'), wx.TextCtrl(panel_from, size=(20,-1), value='1'))
				fgs.AddMany([(txt, 0, wx.EXPAND, 5), (txt_ctrl)])
			
			
			
			
			
			hbox.Add(fgs, 1, flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=5)	
			panel_from.SetSizer(hbox)
			sb_from = wx.StaticBox(self, label="Common")
			boxsizer = wx.StaticBoxSizer(sb_from, wx.VERTICAL)
			boxsizer.Add(panel_from, flag=wx.LEFT|wx.TOP, border=5)
			#sizer.Add(boxsizer, pos=(3, 0), span=(1, 3), flag=wx.TOP|wx.EXPAND, border=5)
			
			args_vbox.Add(boxsizer,1, flag=wx.ALL|wx.EXPAND, border=5)
		if 1: #Source
			
			panel_from = wx.Panel(self)
			hbox = wx.BoxSizer(wx.HORIZONTAL)

			fgs = wx.FlexGridSizer(3, 2, 9, 5)
			ttl=['From table','From database','nls_date_format','nls_timestamp_format','nls_timestamp_tz_format','Client home']
			l=[wx.StaticText(panel_from, label="%s:" % t) for t in ttl]

			p=[wx.TextCtrl(panel_from) for t in ttl]
			pprint(dir(fgs))
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
			
			args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)

		
		if 1: #Target
			panel_from = wx.Panel(self)
			hbox = wx.BoxSizer(wx.HORIZONTAL)

			fgs = wx.FlexGridSizer(3, 2, 9, 5)

			ttl=['To database','To table','To partition','nls_date_format','nls_timestamp_format','nls_timestamp_tz_format','Client home']
			l=[wx.StaticText(panel_from, label="%s:" % t) for t in ttl]

			p=[wx.TextCtrl(panel_from) for t in ttl]
			pprint(dir(fgs))
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
			args_hbox.Add(boxsizer, 1, flag=wx.ALL|wx.EXPAND, border=5)
		args_vbox.Add(args_hbox,0,flag=wx.ALL|wx.EXPAND|wx.GROW)
		self.SetSizer(args_vbox)
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
class DataBuddy(wx.Frame):
	def __init__(self, parent, id, title):
		#wx.Frame.__init__(self, parent, -1, title)
		#super(DataBuddy, self).__init__(parent, title=title , size=(900, 565))
		global app_title, home
		wx.Frame.__init__(self, None, wx.ID_ANY, title=app_title)
		self._vectMenu=None
		self._popUpMenu = None
		#self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
		#self.splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
		#s=self.splitter
		#self.splitter.SetMinimumPaneSize(50)
		#panel layout
		self.panel_pos=[(0,i) for i in range(3)]
		#print self.panel_pos
		self.panel = wx.Panel(self)
		panel=self.panel
		sizer = wx.GridBagSizer(5, 5)
		self.home=home
		self.copy_vector=None
		self.transport=os.path.join(self.home,r'dm32\dm32.exe')
		self.args_panel = default_args(self,style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		
		self.cmd=self.args_panel.get_cmd(self.transport)
		if 1:
			self.st_session_name = wx.StaticText(panel, label="Session name:")
			sizer.Add(self.st_session_name, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=10)
			self.tc_session_name = wx.TextCtrl(panel,value='n/a')
			self.tc_session_name.Enable(False)
			sizer.Add(self.tc_session_name, pos=(0, 1), span=(1, 3), flag=wx.TOP|wx.ALIGN_CENTER|wx.BOTTOM|wx.EXPAND, border=10)
			icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
			sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT,border=6)

		if 1:
			line = wx.StaticLine(panel)
			sizer.Add(line, pos=(1, 0), span=(1, 5), 
				flag=wx.EXPAND|wx.BOTTOM, border=0)

		if 1: #Type
			sb = wx.StaticBox(panel, label="Type")
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			text1 = wx.StaticText(panel, label="Table Copy")
			boxsizer.Add(text1, flag=wx.LEFT|wx.TOP, border=5)
						
			sizer.Add(boxsizer, pos=(2, 0),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Vector')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			text1 = wx.StaticText(panel, label="Oracle 11G -> Oracle 11G")
			boxsizer.Add(text1, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 1),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Source template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			text1 = wx.StaticText(panel, label="ORA_QueryFile_withHeader")
			boxsizer.Add(text1, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 2),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
			#self.gen_bind(wx.EVT_BUTTON,self.b_vector, self.OnVectorButton,('test'))	
		if 1: #Vector
			sb = wx.StaticBox(panel, label='Target template')
			boxsizer = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
			text1 = wx.StaticText(panel, label="ORA_Partition")
			boxsizer.Add(text1, flag=wx.LEFT|wx.TOP, border=5)
			
			sizer.Add(boxsizer, pos=(2, 3),  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=5)	
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
			from editor import TacoTextEditor
			nb = fnb.FlatNotebook(panel, -1, agwStyle=fnb.FNB_COLOURFUL_TABS|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_NO_X_BUTTON|fnb.FNB_NO_NAV_BUTTONS|fnb.FNB_NODRAG) #|fnb.FNB_DCLICK_CLOSES_TABS|fnb.FNB_X_ON_TAB|fnb.FNB_X|fnb.FNB_TAB_X|fnb.FNB_BACKGROUND_GRADIENT|fnb.FNB_BTN_NONE|fnb.FNB_BTN_PRESSED|fnb.FNB_COLOURFUL_TABS|fnb.FNB_BOTTOM|fnb.FNB_SMART_TABS|fnb.FNB_DROPDOWN_TABS_LIST|fnb.FNB_DROP_DOWN_ARROW|fnb.FNB_BTN_HOVER|fnb.FNB_NO_X_BUTTON) #|fnb.FNB_HIDE_ON_SINGLE_TAB)
			
			nb.AddPage(self.args_panel, 'Arguments')
			editor = TacoTextEditor(panel)
			editor.AppendText(self.cmd)
			nb.AddPage(editor, 'Command')
			nb.SetSelection(0)
				
			sizer.Add(nb, pos=(3, 0), span=(4, 4), flag=wx.GROW|wx.EXPAND|wx.ALL, border=0)
		if 1:
			fgs = wx.FlexGridSizer(2, 1, 9, 25)

			#l=[wx.StaticText(panel_from, label="Title"), wx.StaticText(panel_from, label="Author"),wx.StaticText(panel_from, label="Review")]

			#p=[wx.TextCtrl(panel_from), wx.TextCtrl(panel_from), wx.TextCtrl(panel_from)]
			#pprint(dir(fgs))
			new_btn=wx.Button(panel, label="New")
			fgs.AddMany([(new_btn, 1, wx.EXPAND),(wx.Button(panel, label="Delete"), 1, wx.EXPAND),wx.StaticText(panel, label=' '),(wx.Button(panel, label="Clear All"), 1, wx.EXPAND)])
			new_btn.Bind(wx.EVT_BUTTON, self.OnNewButton)	
			#button1 = wx.Button(panel, label="New")
			#sizer.Add(button1, pos=(3, 5), flag=wx.TOP|wx.RIGHT, border=5)

			#button2 = wx.Button(panel, label="Delete")
			#sizer.Add(button2, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
			sizer.Add(fgs, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)
		sb = wx.StaticBox(panel, label="Optional")

		boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
		cb=wx.CheckBox(panel, label="Send 'y'")
		boxsizer.Add(cb, flag=wx.LEFT|wx.TOP, border=5)
		cb.SetValue(True)
		#print(dir(cb))
		sizer.Add(boxsizer, pos=(8, 0), span=(1, 5), 
			flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

		button3 = wx.Button(panel, label='Help')
		sizer.Add(button3, pos=(9, 0), flag=wx.LEFT, border=10)
		button3.Enable(False)

		btn_open = wx.Button(panel, label='Show in Folder')
		btn_open.Bind(wx.EVT_BUTTON, self.OnButtonShowInFolder)
		sizer.Add(btn_open, pos=(9, 2),flag=wx.BOTTOM|wx.ALIGN_RIGHT)


		btn_open = wx.Button(panel, label='Run')
		btn_open.Bind(wx.EVT_BUTTON, self.OnButtonOpen)
		sizer.Add(btn_open, pos=(9, 3),flag=wx.BOTTOM|wx.ALIGN_RIGHT)

		
		button5 = wx.Button(panel, ID_EXIT, label="Cancel")
		#self.Bind(wx.EVT_BUTTON, self.onAboutHtmlDlg, aboutBtn)
		sizer.Add(button5, pos=(9, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=5)

		#sizer.AddGrowableCol(2)
		sizer.AddGrowableRow(7)
				
		if 1:
			self.panel2 = wx.Panel(self, wx.ID_ANY)
			panel2=self.panel2
			vsizer =  wx.BoxSizer(wx.VERTICAL)
			#wx.BoxSizer(wx.VERTICAL)
			#if 1:
				#self.splitter.SetOrientation(wx.VERTICAL)
				
			sm=SessionListCtrlPanelManager(panel2,panel2,(0,0),self.panel_pos)
				
			self.hsizer = wx.BoxSizer(wx.HORIZONTAL)
			vsizer.Add(sm,1,wx.EXPAND|wx.TOP|wx.BOTTOM|wx.LEFT|wx.RIGHT, border=5)
				

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
		#self.SetSizeHints(250,300,500,400)
		self.Fit()
		self.Refresh()
		self.Center()
		self.Show(True)
	def onNewSession(self, data, extra1, extra2=None):		
		(sname,copy_vector) = data
		print sname
		self.copy_vector=copy_vector
		self.tc_session_name.SetValue(sname)
		#self.txt_transport.SetLabel(tloc[0])

	def OnNewButton(self, event):
		dlg = NewSessionDialog(self, -1, "Defaults for new session.", size=(250, 250),
						 #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
						 style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
						 useMetal=False, plist=None
						 )
		#dlg.CenterOnScreen()
		# this does not return until the dialog is closed.
		val = dlg.ShowModal()
		print val

	def OnButtonShowInFolder(self, event):
		# 
		btn = event.GetEventObject()
		#create bat file
		ts=time.strftime('%Y%m%d_%H%M%S')
		dirname=os.path.join(home,'run')
		fname = os.path.join(dirname, '%s_%s.py' % (self.tc_session_name.GetValue(),ts))
		if not os.path.isdir(dirname):
			os.makedirs(dirname)
		f=open(fname,'w')
		f.write(self.cmd)
		f.close()
			
		
	
		EXPLORER = 'C:\\windows\\explorer.exe' 
		os.spawnl(os.P_NOWAIT, EXPLORER, '.', '/n,/e,/select,"%s"'%fname)


	def OnButtonOpen(self, event):
		# 
		btn = event.GetEventObject()
		print btn.GetLabel()
		from subprocess import Popen,PIPE
		if 0:
			
			#Popen("cmd /w dir")
			import shlex 
			cmd=''.join(self.cmd.split('^\n'))
			print cmd
			lexer=shlex.shlex(cmd)
			#lexer = shlex.shlex(input)
			lexer.quotes = '"'
			#lexer.wordchars += '\''
			lexer.whitespace_split = True
			lexer.commenters = ''
			cfg = list(lexer)
			pprint(cfg)		
			#e(0)
			p = Popen(cfg, stdin=PIPE, stdout=PIPE, shell=True)
			out, err = p.communicate('y\n')
			p.wait()
			print err
			print out
			print '-'*40
		if 0:
			p=Popen(['mode con cols=50 lines=50;start "test"', 'cmd', '/k','.\\dm32\\dm32.exe', '-w', 'ora2ora', '-o', '1', '-r', '1',  '-c', 'SCOTT.Date_test_from', '-f', 'SCOTT/tiger2@orcl', '-e', '"YYYY-MM-DD HH24.MI.SS"', '-m', '"YYYY-MM-DD HH24.MI.SS.FF2"', '-O', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"','-z', '"C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"', '-g', 'SCOTT/tiger2@orcl', '-a', 'SCOTT.Partitioned_test_to', '-G', 'part_15', '-e', '"YYYY-MM-DD HH24.MI.SS"', '-m', '"YYYY-MM-DD HH24.MI.SS.FF2"', '-O', '"YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM"', '-Z', '"C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"'], stdin=PIPE, stdout=PIPE, shell=True)
			out, err = p.communicate('y\n')
			print out, err
			p.wait()
			p.close()
		#os.system("mode 45, 20");
		#os.system(r'start "ora2ora" cmd /k echo y^|C:\Users\alex_buz\Documents\GitHub\DataBuddy\dm32\dm32.exe -w ora2ora -o 1 -r 1 -t "|" -c SCOTT.Date_test_from -f SCOTT/tiger2@orcl -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -g SCOTT/tiger2@orcl -a SCOTT.Partitioned_test_to -G part_15 -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN"')
		os.system(r'start "test" cmd.exe  /k "mode 100,45 && echo y|C:\Users\alex_buz\Documents\GitHub\DataBuddy\dm32\dm32.exe -w ora2ora -o 1 -r 1 -t "^|" -c SCOTT.Date_test_from -f SCOTT/tiger2@orcl -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN" -g SCOTT/tiger2@orcl -a SCOTT.Partitioned_test_to -G part_15 -e "YYYY-MM-DD HH24.MI.SS" -m "YYYY-MM-DD HH24.MI.SS.FF2" -O "YYYY-MM-DD HH:MI:SS.FF2 TZH:TZM" -Z "C:\app\alex_buz\product\11.2.0\dbhome_2\BIN""')

		
	def OnVectorButton(self, event,params):
		(loc)=params
		print (loc)
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
		print a,b	
	def onRadioButton(self, event):
		"""
		This method is fired when its corresponding button is pressed
		"""
		btn = event.GetEventObject()
		label = btn.GetLabel()
		#print label
		#print self.txt_transport.GetLabel()
		self.txt_transport.SetLabel('.\dm32\dm%s.exe' % label[:2])
		if 0:
			message = "You just selected %s" % label
			dlg = wx.MessageDialog(None, message, 'Message', 
								   wx.OK|wx.ICON_EXCLAMATION)
			dlg.ShowModal()
			dlg.Destroy()
		
	def onTransportLoc(self, data, extra1, extra2=None):		
		(tloc) = data
		print tloc
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
		info.Name = "data-buddy"
		info.Version = "0.0.1 Beta"
		info.Copyright = "(C) 2015 SequelWorks Inc."
		info.Description = wordwrap(
			'This is session manager for  <b><a href="https://github.com/DataMigrator/DataMigrator-for-Oracle">DataMigrator</a></b>.</p>',
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
		wx.Frame.__init__(self, parent, wx.ID_ANY, title="About", size=(400,400))
		html = wxHTML(self)
		html.SetPage(
			''
			"<h2>About data-buddy</h2>"
			'<p>Session manager for <b><a href="https://github.com/DataMigrator/DataMigrator-for-Oracle">DataMigrator</a></b>.</p>'
			'<p>Created in Jan. 2015 by Alex Buzunov.</p>'
			"<p><b>Software used in making this tool:</h3></p>"
			'<p><b><a href="http://www.python.org">Python 2.7</a></b></p>'
			'<p><b><a href="http://www.wxpython.org">wxPython 2.8</a></b></p>'
			)
		self.Center()
		self.SetSize((300,300))
		#self.Fit()
		self.Refresh()


class wxHTML(wx.html.HtmlWindow):	
	def OnLinkClicked(self, link):
		webbrowser.open(link.GetHref())
		
if __name__ == '__main__':
	freeze_support()	
	app_title='%s %s' % (__title__,__version__)
	class MyApp(wx.App, wx.lib.mixins.inspection.InspectionMixin):
		def OnInit(self):
			import images as i
			global imgs
			imgs = i
			self.Init()
			self.frame = DataBuddy(None, -1,title=app_title)
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