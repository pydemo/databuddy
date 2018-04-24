#!/usr/bin/env python
import wx
#This one is copied from MaskedEditControls.py
import  wx.lib.masked as  masked

#The masks is taken from MaskedEditControls.py around line 118-125
maskFloat = ["Float (signed)", "#{6}.#{9}", "", 'F-_R', "", '','', '000000.000000000'] 
maskText = ["Full Name", "C{14}", "", 'F_', '^[A-Z][a-zA-Z]+ [A-Z][a-zA-Z]+', '', '', '1']
class MyFrame(wx.Frame):
	"""
	The Class For creating Base Frame
	inherit the Frame class from wx
	"""
	def __init__(self, *args, **kwds):
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		#Frame is defined, let's defined the panel inside
		self.panel_1 = wx.Panel(self, -1)
		#Panel is defined, lets try to define 2 masked.TextControl,
		#1. masked with MaskText
		#2. masked with MaskFloat
		self.ctrl_maskText = masked.TextCtrl( self.panel_1, -1, "",
												mask         = maskText[1],
												excludeChars = maskText[2],
												formatcodes  = maskText[3],
												includeChars = "",
												validRegex   = maskText[4],
												validRange   = maskText[5],
												choices      = maskText[6],
												choiceRequired = False,
												defaultValue = maskText[7])
		self.ctrl_maskFloat = masked.TextCtrl(	self.panel_1, -1, "",
												mask = maskFloat[1], 
												excludeChars = maskFloat[2], 
												formatcodes = maskFloat[3],
												includeChars = "",
												validRegex = maskFloat[4], 
												validRange = maskFloat[5], 
												choices = maskFloat[6],
												choiceRequired = False,
												defaultValue = maskFloat[7])

		self.__set_properties()
		self.__do_layout()
		#self.Bind(wx.EVT_TEXT, self.OnIpAddrChange, id=ipaddr1.GetId())
		self.Bind(wx.EVT_TEXT_ENTER, self.f_EVT_TEXT_ENTER, id=self.ctrl_maskText.GetId()) 
		self.Bind(wx.EVT_TEXT_ENTER, self.f_EVT_TEXT_ENTER, id=self.ctrl_maskFloat.GetId())

	def __set_properties(self):
		self.SetTitle("frame_1")

	def __do_layout(self):
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		sizer_2 = wx.BoxSizer(wx.VERTICAL)
		sizer_2.Add(self.ctrl_maskText, 0, 0 , 0)
		sizer_2.Add(self.ctrl_maskFloat, 0, 0 , 0)
		self.panel_1.SetSizer(sizer_2)
		sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()

	def f_EVT_TEXT_ENTER(self, event):
		print "MASKED TextCTRL --> EVT_TEXT_ENTER"


if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	frame_1 = MyFrame(None, -1, "")
	app.SetTopWindow(frame_1)
	frame_1.Show()
	app.MainLoop()