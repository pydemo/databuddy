if 0:
	import wxversion
	import wxversion as wv
	wv.select("3.0")
import wx
import os, glob, sys
#from wx.lib.pubsub import Publisher
from pprint import pprint
 
import xml.dom.minidom
from xml.dom.minidom import Node

from tc_lib import send

from  tree_lib import *
if 0:
	import images as i
	global images
	images = i
_tacoPngs=[]
winuser='zkqfas6'
userLoc = os.path.expanduser('~%s' % winuser)
appLoc = os.getcwdu()

projRootName ='_devel_'
projRootLoc = os.path.join(userLoc,projRootName)

confDirName ='_CONFIG_'
configDirLoc = os.path.join(appLoc,confDirName)

activeProjName = 'sql'
activeProjLoc= os.path.join(projRootLoc,activeProjName)
cml =3
default_config='pipeline_spec.xml'	  	  
def log(msg):
	wx.LogMessage(msg)
ehosts = {'dev':('zkqfas6','200Grove','lrche25546',22)}
def getRunHosts(h):
	return [x for x in h]
	
def getPipelineConfig(configDirLoc, ml):
	print configDirLoc
	for root, dirnames, filenames in os.walk(configDirLoc):
		#print filenames
		#print root
		if not dirnames:
			#print filenames
			sf= root.split('\\')
			#print len(sf)
			if len(sf)==ml+1:
				dn= os.path.split(root)
				#print dn[1]		
				#if not matches.has_key(dn):
				#	matches[dn]=[]
				if 1:
					files=[]
					for filename in glob.glob('%s\\%s' % (root,'*.xml')):
						#print filename
						sf= filename.split('\\')
						#print sf[ml],sf[ml+1]
						files.append(sf[ml+1])
						#matches.append(os.path.join(root, filename))
				#_treeList.append((dn[1],files))
	return (dn[1],files)

import fnmatch
import os
import glob
matches = []
_treeList=[]


		
		
if 0:
	_treeList.append(('Recent Additions/Updates', [
			'RichTextCtrl',
			'Treebook',
			'Toolbook',
			'BitmapFromBuffer',
			]))


def setConfigTree(ppln,_tree):
	x = ppln
	doc = xml.dom.minidom.parse(x)	
	for node in doc.getElementsByTagName("test_spec"):
	  #isbn = node.getAttribute("isbn")
	  #L = node.getElementsByTagName("title")
	  for node2 in node.childNodes:
		#title = ""
		
		if node2.nodeType != Node.TEXT_NODE:
			#print node2.nodeType, node2.nodeName	
			if node2.nodeName=='process_spec':
				#print dir(node2.attributes.tems)
				values=[]
				for aName, aValue  in node2.attributes.items():
					values.append("%s=%s" % (aName, aValue))				
				_tree.append((node2.nodeName,values))
			if node2.nodeName=='connector':
				#print dir(node2.attributes.tems)
				values=[]
				for node3  in node2.childNodes:
					if node3.nodeType != Node.TEXT_NODE and node3.nodeType != Node.COMMENT_NODE:
						#print node3.nodeName
						#print node3.attributes.keys()
						values.append("%s=%s@%s" % (node3.nodeName,node3.attributes.getNamedItem('schema').value, node3.attributes.getNamedItem('sid').value))
						#sys.exit(1)
				_tree.append((node2.nodeName,values))
	
#print(dir(Node))
#setConfigTree('pipeline_spec.xml',_treeList)
 
def setDirTree(dirLoc,_tree):
	#x = dirLoc
	print '%s\\%s' % (dirLoc,'*.sql')
	for filename in glob.glob('%s\\%s' % (dirLoc,'*.sql')):
						print filename
						print 'before', len(_tree)
						doc = xml.dom.minidom.parse(filename)	
						wid=1
						for node in doc.getElementsByTagName("etldataflow"):
						  #isbn = node.getAttribute("isbn")
						  #L = node.getElementsByTagName("title")
						  pplName=node.attributes.getNamedItem('name').value
						  print pplName
						  _tree.append((pplName,['test']))

	

#activeProjLoc
def setFileTree(pplnLoc,_tree):
	x = pplnLoc
	doc = xml.dom.minidom.parse(x)	
	wid=1
	for node in doc.getElementsByTagName("etldataflow"):
	  #isbn = node.getAttribute("isbn")
	  #L = node.getElementsByTagName("title")
	  pplName=node.attributes.getNamedItem('name').value
	  for node2 in node.childNodes:
		#title = ""
		
		if node2.nodeType != Node.TEXT_NODE:
			#print node2.nodeType, node2.nodeName	
			if node2.nodeName=='globals':
				#print dir(node2.attributes.tems)
				values=[]
				for node3  in node2.childNodes: 
					if node3.nodeType != Node.TEXT_NODE and node3.nodeType != Node.COMMENT_NODE:
						#print node3.nodeName
						#print node3.attributes.keys()
						values.append("%s=%s" % (node3.attributes.getNamedItem('name').value, node3.attributes.getNamedItem('value').value))
						#sys.exit(1)
				_tree.append(('%s // %s' % (node2.nodeName,pplName),values))
			if node2.nodeName=='worker':
				#print dir(node2.attributes.tems)
				values=[]
				wName="w[%s][%s]" % (wid,node2.attributes.getNamedItem('name').value)
				wid +=1
				if 1:
					#print dir(node2)
					#sys.exit(1)
					for node3  in node2.childNodes:					
						if node3.nodeType != Node.TEXT_NODE and node3.nodeType != Node.COMMENT_NODE:
							#print node3.nodeName
							nodeName= node3.nodeName
							for node4  in node3.childNodes:					
								if node4.nodeType != Node.TEXT_NODE and node4.nodeType != Node.COMMENT_NODE:
									#print '	',node4.nodeName
									nodeName= '%s/%s' % (nodeName,node4.nodeName)
									for param  in node4.childNodes:					
										if param.nodeType != Node.TEXT_NODE and param.nodeType != Node.COMMENT_NODE:
											#print '		',param.nodeName
											if param.nodeName=='param':
												pName= '%s[%s=%s]' % (nodeName,param.attributes.getNamedItem('name').value, param.attributes.getNamedItem('value').value)
												#print pName
												values.append("%s" % (pName))
									#print node3.attributes.keys()
									#values.append("%s" % (nodeName))
									#sys.exit(1)
				#sys.exit(1)
				_tree.append((wName,values))
#setFileTree('prod\\tc_UAT_fail_reports_history.xml',_treeList)
#sys.exit(1)

		  





	
#---------------------------------------------------------------------------

USE_CUSTOMTREECTRL = False
ALLOW_AUI_FLOATING = False
DEFAULT_PERSPECTIVE = "Default Perspective"
#---------------------------------------------------------------------------

from wx.lib.mixins.treemixin import ExpansionState
if USE_CUSTOMTREECTRL:
	import wx.lib.customtreectrl as CT
	TreeBaseClass = CT.CustomTreeCtrl
else:
	TreeBaseClass = wx.TreeCtrl
	

class TacoTree(ExpansionState, TreeBaseClass):
	def __init__(self, parent,images, _tacoPngs):
		TreeBaseClass.__init__(self, parent, style=wx.TR_DEFAULT_STYLE|
							   wx.TR_HAS_VARIABLE_ROW_HEIGHT)
		self.BuildTreeImageList(images,_tacoPngs)
		if USE_CUSTOMTREECTRL:
			self.SetSpacing(10)
			self.SetWindowStyle(self.GetWindowStyle() & ~wx.TR_LINES_AT_ROOT)

	def AppendItem(self, parent, text, image=-1, wnd=None):
		if USE_CUSTOMTREECTRL:
			item = TreeBaseClass.AppendItem(self, parent, text, image=image, wnd=wnd)
		else:
			item = TreeBaseClass.AppendItem(self, parent, text, image=image)
		return item
			
	def BuildTreeImageList(self,images,_tacoPngs):
		imgList = wx.ImageList(16, 16)
		#print _tacoPngs
		#sys.exit(1)
		for png in _tacoPngs:
			img_name='generic'
			if png=='config' or png=='recent':
				img_name=png
			imgList.Add(images.catalog[img_name].GetBitmap())
			
		# add the image for modified demos.
		imgList.Add(images.catalog["custom"].GetBitmap())

		self.AssignImageList(imgList)


	def GetItemIdentity(self, item):
		return self.GetPyData(item)


		

	
class TsqlCodePanel(wx.Panel):
	"""Panel for the 'Worklet Code' tab"""
	def __init__(self, parent, mainFrame, images,fileLoc,fileName):
		wx.Panel.__init__(self, parent, size=(1,1))
		if 'wxMSW' in wx.PlatformInfo:
			self.Hide()
		self.mainFrame = mainFrame
		self.editor = TsqlCodeEditor(self)
		self.editor.RegisterModifiedEvent(self.OnCodeModified)

		self.btnSave = wx.Button(self, -1, "Save Changes")
		self.btnRestore = wx.Button(self, -1, "Delete File")
		self.btnSave.Enable(False)
		self.btnSave.Bind(wx.EVT_BUTTON, self.SaveContents)
		self.btnRestore.Bind(wx.EVT_BUTTON, self.OnRestore)
		
		self.btnRun = wx.Button(self, -1, "Run")
		self.btnRun.Bind(wx.EVT_BUTTON, self.OnRun)
		#self.SetBackgroundColour((179, 179, 179))

		self.treeMap = {}

		#self.radioButtons = { modOriginal: wx.RadioButton(self, -1, "Original", style = wx.RB_GROUP),
		#					  modModified: wx.RadioButton(self, -1, "Modified") }

		#self.controlBox = wx.BoxSizer(wx.HORIZONTAL)
		#self.controlBox.Add(wx.StaticText(self, -1, "Active Version:"), 0,
		#					wx.RIGHT | wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
		#for modID, radioButton in self.radioButtons.items():
			#self.controlBox.Add(radioButton, 0, wx.EXPAND | wx.RIGHT, 5)
			#radioButton.modID = modID # makes it easier for the event handler
			#radioButton.Bind(wx.EVT_RADIOBUTTON, self.OnRadioButton)
			
		#self.controlBox.Add(self.btnSave, 0, wx.RIGHT, 2)
		#self.controlBox.Add(self.btnRestore, 0, wx.RIGHT, 25)

		(dn, cfiles) = getPipelineConfig(configDirLoc,cml)
		self.config=wx.ComboBox(self, 0, value=default_config,  choices=cfiles, style=wx.CB_READONLY)
		#self.controlBox.Add(self.config, 0, wx.RIGHT, 2)
		eh=[x for x in ehosts]
		self.exec_host=wx.ComboBox(self, 0, value='dev',  choices=eh, style=wx.CB_READONLY)
		#self.controlBox.Add(self.exec_host, 0, wx.RIGHT, 5)		
		
		#self.controlBox.Add(self.btnRun, 0)		
		#self.box = wx.BoxSizer(wx.VERTICAL)
		#self.box.Add(self.controlBox, 0, wx.EXPAND)
		#self.box.Add(wx.StaticLine(self), 0, wx.EXPAND)
		#self.controlBox = wx.BoxSizer(wx.HORIZONTAL)
		#self.controlBox.Add(self.editor, 1, wx.EXPAND)
		#self.btnTest = wx.Button(self, -1, "Test")
		#def EmptyHandler(evt): pass
		#self.mgr = wx.aui.AuiManager()
		#self.mgr.SetManagedWindow(self)
		#self.topPanel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
		#self.SetAutoLayout(True)
		#self.topPanel.SetAutoLayout(True)
		self.SetBackgroundColour((176, 176, 176))
		self.controlBox = wx.BoxSizer(wx.HORIZONTAL)
		self.controlBox.Add(self.btnSave, 0, wx.RIGHT, 2)
		self.controlBox.Add(self.btnRestore, 0, wx.RIGHT, 125)
		self.controlBox.Add(self.config, 0, wx.RIGHT, 2)
		self.controlBox.Add(self.exec_host, 0, wx.RIGHT, 5)
		self.controlBox.Add(self.btnRun, 0, wx.ALL)
		#self.editor
		self.editorBox = wx.BoxSizer(wx.VERTICAL)
		self.editorBox.Add(self.controlBox, 0)
		self.editorBox.Add(self.editor, 1,wx.EXPAND)
		self.SetSizer(self.editorBox)
		#self.editorBox.Fit(self)
		#def RecreatePanel(evt,top=self.topPanel): 
		#	#top.SetSizerAndFit(self.controlBox)		
		#	top.Layout()
		#self.topPanel.Bind(wx.EVT_ERASE_BACKGROUND, EmptyHandler)
		#print dir(self.topPanel)
		#self.Bind(wx.EVT_ERASE_BACKGROUND, EmptyHandler)
		if 0:
			def OnTopSize(evt, top=self.topPanel):
				#self.mgr.GetPane("controlBox").Show().Top().Layer(0).Row(0).Position(0)

				#self.auiConfigurations[DEFAULT_PERSPECTIVE] = self.mgr.SavePerspective()
				
				if 1:
					parent.Refresh()
					print top.GetSize(), str(self.GetSize())
					#self.Unbind(wx.EVT_SIZE)
					#self.current_size = (wW, wH)
					(myW, myH)=top.GetSize()
					(wW, wH)=self.GetSize()
					#print self.current_size
					top.SetSize((wW,myH))
					#print time.time()
					
					top.Update() #force update so it does not trigger after rebind
					top.Refresh()
					#top.Paint()
					#rebind Size Event
					#self.Bind(wx.EVT_SIZE, OnTopSize)
					#self.Layout()
					#top.Layout()
					#self.controlBox.Fit(top)
					self.mgr.Update()
			#print(dir(self.topPanel))
			self.Bind(wx.EVT_SIZE, OnTopSize)
		if 0:
			rightPanel = wx.Panel(self, style=wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN)
			# add the windows to the splitter and split it.
			leftBox = wx.BoxSizer(wx.VERTICAL)
			#self.topPanel.Update() #force update so it does not trigger after rebind
			#self.topPanel.Refresh()
			#self.Freeze()
			self.tree = TacoTree(rightPanel,images, _tacoPngs)
			leftBox.Add(self.tree, 1, wx.EXPAND)
			#leftBox.Add(wx.StaticText(rightPanel, label = "Filter Workers:"), 0, wx.TOP|wx.LEFT, 5)
			self.filter = wx.SearchCtrl(rightPanel, style=wx.TE_PROCESS_ENTER)
			self.filter.ShowCancelButton(True)
			#self.filter.Bind(wx.EVT_TEXT, self.RecreateTree)
			#self.filter.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnSearchCancelBtn)
			#self.filter.Bind(wx.EVT_TEXT_ENTER, self.OnSearch)
			searchMenu = wx.Menu()
			item = searchMenu.AppendRadioItem(-1, "Name")
			self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
			item = searchMenu.AppendRadioItem(-1, "Content")
			self.Bind(wx.EVT_MENU, self.OnSearchMenu, item)
			self.filter.SetMenu(searchMenu)
			self.RecreateTree(fileLoc=fileLoc,fileName=fileName)
			leftBox.Add(self.filter, 0, wx.EXPAND|wx.ALL, 5)
			if 'wxMac' in wx.PlatformInfo:
				leftBox.Add((5,5))  # Make sure there is room for the focus ring
		#rightPanel.SetSizer(leftBox)
		#self.controlBox.Add(rightPanel, 1, wx.EXPAND)
		#self.box.Add(self.controlBox, 1, wx.EXPAND)
		#rightPanel.Bind(wx.EVT_ERASE_BACKGROUND, EmptyHandler)
		#mainFrame.Bind(wx.EVT_ERASE_BACKGROUND, EmptyHandler)
		#self.box.Fit(self)
		#self.SetSizer(self.box)

		info = wx.aui.AuiPaneInfo()
		#info.CaptionVisible(True)
		info.BottomDockable(False)
		info.LeftDockable(False)
		info.RightDockable(False)
		info.PaneBorder(False)
		info.CaptionVisible(False) 
		info.BestSize((240, 23))
		info.MinSize((240, 23))
		info.Top()
		info.Resizable(False)
		info.Row(0)
		#info.Fixed()
		
		print dir(info)
		info2 = wx.aui.AuiPaneInfo()
		info2.BottomDockable(False)
		info2.LeftDockable(False)
		info2.RightDockable(False)
		info2.CaptionVisible(False) 
		info2.PaneBorder(False)
		info2.BestSize((240, 23))
		info2.MinSize((240, 23))
		info2.CenterPane()
		info2.Row(1)

		
		#self.mgr.AddPane(self.btnSave, info)
		#self.mgr.AddPane(self.btnRestore, info)
		
		#self.mgr.AddPane(self.exec_host, info)
		#self.mgr.AddPane(self.config, info2)
		#self.mgr.AddPane(self.btnRun, info2)
		
		if 0:			 
			self.mgr.AddPane(self.editor, wx.aui.AuiPaneInfo().CenterPane().Name("Editor"))
			if 0:
				self.mgr.AddPane(rightPanel,
								 wx.aui.AuiPaneInfo().
								 Right().BestSize((280, -1)).
								 MinSize((200, -1)).PaneBorder(False).
								 Floatable(ALLOW_AUI_FLOATING).FloatingSize((240, 700)).
								 Caption("WorkerBrowser").
								 CloseButton(False).
								 Name("WorkerTree"))
			self.mgr.AddPane(self.topPanel, info.Name("controlBox"))	
			#self.mgr.GetPane("controlBox").Show().Top().Layer(0).Row(0).Position(0)

			#self.auiConfigurations[DEFAULT_PERSPECTIVE] = self.mgr.SavePerspective()
			self.mgr.Update()

			self.mgr.SetFlags(self.mgr.GetFlags() ^ wx.aui.AUI_MGR_TRANSPARENT_DRAG)
		#self.Thaw()
		#Publisher().subscribe(self.SaveContents, "save_xml_contents")
		sub(self.SaveContents, "save_xml_contents")
	def OnSearchMenu(self, event):

		# Catch the search type (name or content)
		searchMenu = self.filter.GetMenu().GetMenuItems()
		fullSearch = searchMenu[1].IsChecked()
		
		if fullSearch:
			self.OnSearch()
		else:
			self.RecreateTree()
	#---------------------------------------------    
	def RecreateTree(self, evt=None,fileLoc=None, fileName=None):
		# Catch the search type (name or content)
		searchMenu = self.filter.GetMenu().GetMenuItems()
		fullSearch = searchMenu[1].IsChecked()
			
		if evt:
			if fullSearch:
				# Do not`scan all the demo files for every char
				# the user input, use wx.EVT_TEXT_ENTER instead
				return

		expansionState = self.tree.GetExpansionState()

		current = None
		item = self.tree.GetSelection()
		if item:
			prnt = self.tree.GetItemParent(item)
			if prnt:
				current = (self.tree.GetItemText(item),
						   self.tree.GetItemText(prnt))
					
		self.tree.Freeze()
		self.tree.DeleteAllItems()
		print '----------------', fileName
		#sys.exit(1)
		self.root = self.tree.AddRoot(str(fileName))
		self.tree.SetItemImage(self.root, 0)
		self.tree.SetItemPyData(self.root, 0)

		treeFont = self.tree.GetFont()
		catFont = self.tree.GetFont()

		# The old native treectrl on MSW has a bug where it doesn't
		# draw all of the text for an item if the font is larger than
		# the default.  It seems to be clipping the item's label as if
		# it was the size of the same label in the default font.
		if 'wxMSW' not in wx.PlatformInfo or wx.GetApp().GetComCtl32Version() >= 600:
			treeFont.SetPointSize(treeFont.GetPointSize()+2)
			treeFont.SetWeight(wx.BOLD)
			catFont.SetWeight(wx.BOLD)
			
		self.tree.SetItemFont(self.root, treeFont)
		
		firstChild = None
		selectItem = None
		filter = self.filter.GetValue()
		count = 0
		global _tacoPngs
		_treeList=[]
		_tacoPngs=["overview",  "config"]
		if fileLoc and fileLoc.endswith(confDirName):
			if fileName:
				print "It's a config file"
				setConfigTree(os.path.join(fileLoc,fileName),_treeList)
				
			else:
				print "It's a config dir"
				#setConfigTree(os.path.join(fileLoc,fileName),_treeList)
				print 'Cannot locate config file %s\\%s.' % (fileLoc,fileName)
			_tacoPngs=["overview"]
		else:
			print '---check---',fileName, fileLoc
			if fileLoc and  fileName is None and os.path.isdir(fileLoc):
				print "it's adir"
				_treeList=[]
				setDirTree(fileLoc,_treeList)
				#print _treeList
			else:
				if fileName and os.path.isfile(os.path.join(fileLoc,fileName)):
					print "it's a file"
					setConfigTree(os.path.join(confDirName,default_config),_treeList)
					if fileName:
						setFileTree('%s\\%s' % (fileLoc,fileName),_treeList)
										
				else:
					print fileLoc ,  fileName is None,
					if fileLoc:
						print os.path.isdir(fileLoc)
					print 'Cannot locate pipeline file %s\\%s.' % (fileLoc,fileName)
		print len(_treeList)
		for x in _treeList:
			_tacoPngs.append(x[0])
		print _tacoPngs
		for category, items in _treeList:
			print category, items
			count += 1
			if filter:
				if fullSearch:
					items = self.searchItems[category]
				else:
					items = [item for item in items if filter.lower() in item.lower()]
			if items:
				child = self.tree.AppendItem(self.root, category, image=count)
				self.tree.SetItemFont(child, catFont)
				self.tree.SetItemPyData(child, count)
				if not firstChild: firstChild = child
				for childItem in items:
					print childItem
					image = count
					if DoesModifiedExist(childItem):
						image = len(_tacoPngs)
					theDemo = self.tree.AppendItem(child, childItem, image=image)
					self.tree.SetItemPyData(theDemo, count)
					self.treeMap[childItem] = theDemo
					if current and (childItem, category) == current:
						selectItem = theDemo
						
					
		self.tree.Expand(self.root)
		print self.root
		if firstChild:
			self.tree.Expand(firstChild)
		if filter:
			self.tree.ExpandAll()
		elif expansionState:
			self.tree.SetExpansionState(expansionState)
		if selectItem:
			self.skipLoad = True
			self.tree.SelectItem(selectItem)
			self.skipLoad = False
		
		self.tree.Thaw()
		self.searchItems = {}		


		
	def OnRun(self, event): # Handles the "Delete Modified" button
		log('Running...')	
		ploc ='C:\\Users\\zkqfas6\\Installs\\putty'
		(uname, pwd, hostname, port) = ehosts['dev']
		pname= 'vector_test'
		fname='tc_%s.xml' % pname
		f_loc= 'C:\\Python27\\_taco_\\Projects\\table_copy\\spool_data\\' +fname
		remote_f_loc='/home/zkqfas6/tab_copy/clients/table_copy/spool_data/' +fname
		copycmd=ploc+"\\pscp.exe  -pw "+pwd+"  " +f_loc +" "  +uname+"@" + hostname+":" +remote_f_loc
		if 1:
			p2 = Popen(copycmd, stdout=PIPE,stderr=PIPE)

			if 0:
				(out,err) = p2.communicate()
				print out
				print err
				p2.wait()
			else:
				output=' '
				status=0
				while output:
					output = p2.stdout.readline()
					print output,
					log( output.strip())
				err = ' '
				while err:
					err = p2.stderr.readline().strip()
					if err:
						log('ERROR: %s' % err)
				pstatus=p2.wait()
				print 'scp status', pstatus				


		if 1:
			command = ploc+"\\plink.exe -ssh " +uname+"@" + hostname + " -pw "+pwd+" -batch \" cd tab_copy;./runs.sh "+pname+" spool_data;\" "
			#wx.LogMessage(command)
			#p1 = Popen(['echo', """%s""" % pwd], shell=True,stdout=PIPE,stderr=PIPE)
			p2 = Popen(command, stdout=PIPE,stderr=PIPE)

			if 0:
				(err, out) = p2.communicate()
				print err, out
				p2.wait()
			else:
				output=' '
				status=0
				while output:
					output = p2.stdout.readline()
					print output,
					log( output.strip())
				err = ' '
				while err:
					err = p2.stderr.readline().strip()
					if err:
						log('ERROR: %s' % err)
				pstatus=p2.wait()
				print 'status', pstatus
			#pid = Popen(command).pid
		log('done')
	# Loads a demo from a DemoModules object
	def LoadDemo(self, demoModules):
		self.demoModules = demoModules
		print 'LoadDemo------'
		if 0:
			if (modDefault == modModified) and demoModules.Exists(modModified):
				demoModules.SetActive(modModified)
			else:
				demoModules.SetActive(modOriginal)
			self.radioButtons[demoModules.GetActiveID()].Enable(True)
		self.ActiveModuleChanged()


	def ActiveModuleChanged(self):
		print 'ActiveModuleChanged', self.demoModules.name
		self.LoadDemoSource(self.demoModules.GetXMLSource())
		self.UpdateControlState()
		self.mainFrame.pnl.Freeze()        
		self.ReloadDemo()
		self.mainFrame.pnl.Thaw()
		print 'after self.mainFrame.pnl.Thaw()'
	def ReloadDemo(self):
		if 0 and self.demoModules.name != __name__:
			self.mainFrame.RunModule()	
		
	def LoadDemoSource(self, source):
		self.editor.Clear()
		print 'LoadDemoSource',len(source)
		#i=1/0
		self.editor.SetValue(source)
		print 'after self.editor.SetValue(source)'
		self.JumpToLine(0)
		self.btnSave.Enable(False)


	def JumpToLine(self, line, highlight=False):
		self.editor.GotoLine(line)
		self.editor.SetFocus()
		if highlight:
			self.editor.SelectLine(line)
		
	   
	def UpdateControlState(self):
		active = self.demoModules.GetActiveID()
		print active,  self.demoModules.isConfig()
		if self.demoModules.isConfig():
			self.btnRun.Enable(False)
			self.exec_host.Enable(False)
			self.config.Enable(False)
		else:
			self.btnRun.Enable(True)
			self.exec_host.Enable(True)
			self.config.Enable(True)
		# Update the radio/restore buttons
		if 0:
			for moduleID in self.radioButtons:
				btn = self.radioButtons[moduleID]
				if moduleID == active:
					btn.SetValue(True)
				else:
					btn.SetValue(False)

				if self.demoModules.Exists(moduleID):
					btn.Enable(True)
					if moduleID == modModified:
						self.btnRestore.Enable(True)
				else:
					btn.Enable(False)
					if moduleID == modModified:
						self.btnRestore.Enable(False)

					
	def OnRadioButton(self, event):
		radioSelected = event.GetEventObject()
		modSelected = radioSelected.modID
		if modSelected != self.demoModules.GetActiveID():
			busy = wx.BusyInfo("Reloading demo module...")
			self.demoModules.SetActive(modSelected)
			self.ActiveModuleChanged()


				
	def OnCodeModified(self, event):
		self.btnSave.Enable(self.editor.IsModified())

		
	def OnSave(self, event):
		pass
		if 0:
			if self.demoModules.Exists(modModified):
				if self.demoModules.GetActiveID() == modOriginal:
					overwriteMsg = "You are about to overwrite an already existing modified copy\n" + \
								   "Do you want to continue?"
					dlg = wx.MessageDialog(self, overwriteMsg, "TaCo Demo",
										   wx.YES_NO | wx.NO_DEFAULT| wx.ICON_EXCLAMATION)
					result = dlg.ShowModal()
					if result == wx.ID_NO:
						return
					dlg.Destroy()
				
			self.demoModules.SetActive(modModified)
			modifiedFilename = GetModifiedFilename(self.demoModules.name)

			# Create the demo directory if one doesn't already exist
			if not os.path.exists(GetModifiedDirectory()):
				try:
					os.makedirs(GetModifiedDirectory())
					if not os.path.exists(GetModifiedDirectory()):
						wx.LogMessage("BUG: Created demo directory but it still doesn't exist")
						raise AssertionError
				except:
					wx.LogMessage("Error creating demo directory: %s" % GetModifiedDirectory())
					return
				else:
					wx.LogMessage("Created directory for modified demos: %s" % GetModifiedDirectory())
				
			# Save
			f = open(modifiedFilename, "wt")
			source = self.editor.GetText()
			try:
				f.write(source)
			finally:
				f.close()
				
			busy = wx.BusyInfo("Reloading demo module...")
			self.demoModules.LoadFromFile(modModified, modifiedFilename)
			self.ActiveModuleChanged()

			self.mainFrame.SetTreeModified(True)


	def OnRestore(self, event): # Handles the "Delete Modified" button
		modifiedFilename = GetModifiedFilename(self.demoModules.name)
		self.demoModules.Delete(modModified)
		os.unlink(modifiedFilename) # Delete the modified copy
		busy = wx.BusyInfo("Reloading demo module...")
		
		self.ActiveModuleChanged()

		self.mainFrame.SetTreeModified(False)
		
	def SaveContents(self, evt):
		#(td,desc)=evt.data
		print 'Saving in editor...'
		if 0:
			if self.demoModules.Exists(modModified):
				if self.demoModules.GetActiveID() == modOriginal:
					overwriteMsg = "You are about to overwrite an already existing modified copy\n" + \
								   "Do you want to continue?"
					dlg = wx.MessageDialog(self, overwriteMsg, "TaCo Developer",
										   wx.YES_NO | wx.NO_DEFAULT| wx.ICON_EXCLAMATION)
					result = dlg.ShowModal()
					if result == wx.ID_NO:
						return
					dlg.Destroy()
			
		#self.demoModules.SetActive(modModified)
		#modifiedFilename = GetModifiedFilename(self.demoModules.name)
		fn = self.demoModules.name
		if 0:
			# Create the demo directory if one doesn't already exist
			if not os.path.exists(GetModifiedDirectory()):
				try:
					os.makedirs(GetModifiedDirectory())
					if not os.path.exists(GetModifiedDirectory()):
						wx.LogMessage("BUG: Created demo directory but it still doesn't exist")
						raise AssertionError
				except:
					wx.LogMessage("Error creating demo directory: %s" % GetModifiedDirectory())
					return
				else:
					wx.LogMessage("Created directory for modified demos: %s" % GetModifiedDirectory())
				
			# Save
		f = open(fn, "wt")
		source = self.editor.GetText()
		try:
			f.write(source)
		finally:
			f.close()
			
		busy = wx.BusyInfo("Reloading demo module...")
		#self.demoModules.LoadFromFile(modModified, fn)
		#self.ActiveModuleChanged()

		self.mainFrame.SetTreeModified(True)
		self.btnSave.Enable(False)
		
		