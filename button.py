#from   wxPython.wx     import *
import wx
import os
home=os.path.dirname(os.path.abspath(__file__))
if 0:
		btn = wx.BitmapButton(parent, id=-1, bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6))

class aTextCtrl ( wx.TextCtrl ):
	'''Nested button class for use by ButtonColumn class.'''
	def __init__ ( self, parent, label, whotocall, whotonotify, msg, style ):
		"""Expects reference to 'ButtonColumn', list of labels for buttons and list of functions to be called for OnClick events"""
		id = wx.NewId ( )		
		wx.TextCtrl.__init__ ( self, parent, id, style=style )
		self.whotocall = whotocall
		self.whotonotify = whotonotify
		self.msg = msg
		wx.EVT_BUTTON ( self, id, self.OnClick )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	def OnClick ( self, event ):
		if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.msg )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.msg )
		
class bButton ( wx.BitmapButton ):
	'''Nested button class for use by ButtonColumn class.'''
	def __init__ ( self, parent, label, whotocall, whotonotify, msg, image1 ):
		"""Expects reference to 'ButtonColumn', list of labels for buttons and list of functions to be called for OnClick events"""
		id = wx.NewId ( )		
		wx.BitmapButton.__init__ ( self, parent, id,  bitmap=image1,size = (image1.GetWidth()+6, image1.GetHeight()+6) )
		self.whotocall = whotocall
		self.whotonotify = whotonotify
		self.msg = msg
		wx.EVT_BUTTON ( self, id, self.OnClick )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	def OnClick ( self, event ):
		if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.msg )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.msg )
class aButton ( wx.Button ):
	'''Nested button class for use by ButtonColumn class.'''
	def __init__ ( self, parent, label, whotocall, whotonotify, msg ):
		"""Expects reference to 'ButtonColumn', list of labels for buttons and list of functions to be called for OnClick events"""
		id = wx.NewId ( )
		wx.Button.__init__ ( self, parent, id, label, wxDefaultPosition, wxDefaultSize, 1 )
		self.whotocall = whotocall
		self.whotonotify = whotonotify
		self.msg = msg
		wx.EVT_BUTTON ( self, id, self.OnClick )
		wx.EVT_ENTER_WINDOW ( self, self.OnEnter )
		wx.EVT_LEAVE_WINDOW ( self, self.OnLeave )

	def OnClick ( self, event ):
		if self.whotocall: self.whotocall ( )
		
	def OnEnter ( self, event ) :
		if self.whotonotify : self.whotonotify ( 1, self.msg )
	
	def OnLeave ( self, event ) :
		if self.whotonotify : self.whotonotify ( 0, self.msg )
		
class ButtonColumn ( wx.Panel ):
	'''Create aligned column of equal-sized buttons with distinct labels and OnClick destinations.

	Illustrates use of nested classes for creating a collection of controls.
	Also illustrates use of mouse over and mouse leave events.
	'''


	def __init__ ( self, parent, width, buttons, Bottom = 0 ):
		"""Expects reference to 'parent' of 'ButtonColumn', button column 'width', list of button descriptor tuples, and number of buttons to be displayed at the bottom of the column.

		Each button descriptor consists of a label for the button and a reference to the function to be called when the button is clicked.
		"""
		wx.Panel.__init__ ( self, parent, -1, wx.DefaultPosition, ( 100, 200 ) )
		self.parent = parent

		"""Create the upper collection of buttons"""
		previous = None
		imageFile = os.path.join(home,"images/editor_icon_16_2.png")
		image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		if 0:
			for button in buttons [ 0 : len ( buttons ) -Bottom ]:
				oneButton = bButton ( self, button [ 0 ], button [ 1 ], button [ 2 ], button [ 3 ], image1)
				lc = wx.LayoutConstraints ( )
				lc.left.SameAs ( self, wx.Left, 5 )
				lc.right.SameAs ( self, wx.Right, 5 )
				lc.height.AsIs ( )
				if previous: lc.top.SameAs ( previous, wx.Bottom, 5 )
				else: lc.top.SameAs ( self, wx.Top, 5 )
				oneButton.SetConstraints ( lc )
				previous = oneButton

			"""Create the lower collection of buttons"""
			buttons.reverse ( )
			previous = None
			for button in buttons [ 0 : Bottom ]:
				oneButton = bButton ( self, button [ 0 ], button [ 1 ], button [ 2 ], button [ 3 ], image1 )
				lc = wx.LayoutConstraints ( )
				lc.left.SameAs ( self, wx.Left, 5 )
				lc.right.SameAs ( self, wx.Right, 5 )
				lc.height.AsIs ( )
				if previous: lc.bottom.SameAs ( previous, wx.Top, 5 )
				else: lc.bottom.SameAs ( self, wx.Bottom, 5 )
				oneButton.SetConstraints ( lc )
				previous = oneButton
		button=buttons[0]
		oneTextCtrl = aTextCtrl ( self, button [ 0 ], button [ 1 ], button [ 2 ], button [ 3 ], style=wx.TE_PROCESS_ENTER)
		lc = wx.LayoutConstraints ( )
		lc.left.SameAs ( self, wx.Left, 5 )
		lc.right.SameAs ( self, wx.Right, 5 )
		lc.height.AsIs ( )
		oneTextCtrl.SetConstraints ( lc )

if __name__ == '__main__':
	class TestFrame(wx.Frame):
		def __init__(self):
			wx.Frame.__init__ (
				self, None, -1, "Button Column Test",
				size = ( 450, 300 ),
				style = wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE
				)
			self.SetAutoLayout ( True )
			buttons = [
				( 'OK', self.OKClicked, self.OnMessage, 'OK button text1', ),
				( 'Cancel', self.CancelClicked, self.OnMessage, 'Cancel button text', ),
				( 'Re-invert', self.ReinvertClicked, self.OnMessage, 'Re-invert button text', ),
				( 'Exit', self.ExitClicked, self.OnMessage, 'Exit button text', ),
				]

			self.tp = ButtonColumn ( self, 45, buttons, 2 )

			lc = wx.LayoutConstraints ( )
			lc.right.SameAs ( self, wx.Right)
			lc.width.AsIs ( )
			lc.top.SameAs ( self, wx.Top )
			lc.bottom.SameAs ( self, wx.Bottom )
			self.tp.SetConstraints ( lc )

			self.CreateStatusBar ( )
			
		def OnMessage ( self, on, msg ) :
			if not on : msg = ""
			self.SetStatusText ( msg )

		def OKClicked ( self ):
			print "OKClicked"

		def CancelClicked ( self ):
			print "CancelClicked"

		def ReinvertClicked ( self ):
			print "ReInvertClicked"

		def ExitClicked ( self ):
			print "ExitClicked"
			self.Close ( )

	app = wx.PySimpleApp()
	frame = TestFrame()
	frame.Show(True)
	app.MainLoop()