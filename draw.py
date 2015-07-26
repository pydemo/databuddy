# -*- coding: iso-8859-1 -*-#
#!/usr/bin/env python2.4

import wx
import random
import sys

# This has been set up to optionally use the wx.BufferedDC if
# USE_BUFFERED_DC is True, it will be used. Otherwise, it uses the raw
# wx.Memory DC , etc.

USE_BUFFERED_DC = 0
width = 8000
height = 8000

# The original of this program is http://wiki.wxpython.org/index.cgi/DoubleBufferedDrawing
# by Chris Barker and has been hacked about by me (David Hughes) to use a scrolled window
# and to demonstrate what happens as the bitmap size is increased to destruction.
# On (my) Windows XP, when width = height = > ~16000 (Buffersize around 732 MBytes):
#       When USE_BUFFERED_DC = 0
#                   wx._core.PyAssertionError: C++ assertion
#                   "bmp.Ok()" failed at ..\..\src\msw\dc.cpp(1181)
#                   in wxDC::DoDrawBitmap(): invalid bitmap in wxDC::DrawBitmap"
#       When USE_BUFFERED_DC = 1
#                   wx._core.PyAssertionError: C++ assertion
#                   "m_buffer && m_buffer->IsOk()" failed at ..\..\include\wx/dcbuffer.h(104)
#                   in wxBufferedDC::UnMask(): invalid backing store
# Under OSX :
#   Width input = 16000
#   Height input = 16000
#   about to initialize the app. USE_BUFFERED_DC = 0
#   Bitmap: width 16000 height 16000 depth 32 bits
#   Buffersize 976 MBytes
#   wx.free -1 MBytes 
#   Wed Jul 29 12:16:06 MacLeo.config Python[1293] <Error>: CGBitmapContextCreateImage:
#           failed to allocate 1024000000 bytes.
#   Wed Jul 29 12:16:06 MacLeo.config Python[1293] <Error>: CGImageCreate:
#           invalid image provider: NULL.

class BufferedWindow(wx.ScrolledWindow):

    """

    A Buffered window class.

    To use it, subclass it and define a Draw(DC) method that takes a DC
    to draw to. In that method, put the code needed to draw the picture
    you want. The window will automatically be double buffered, and the
    screen will be automatically updated when a Paint event is received.

    When the drawing needs to change, you app needs to call the
    UpdateDrawing() method. Since the drawing is stored in a bitmap, you
    can also save the drawing to file by calling the
    SaveToFile(self,file_name,file_type) method.

    """

    def __init__(self, parent, id,
                 pos = wx.DefaultPosition,
                 size = wx.DefaultSize,
                 style = wx.NO_FULL_REPAINT_ON_RESIZE):
        wx.ScrolledWindow.__init__(self, parent, id, pos, size, style)

        wx.EVT_PAINT(self, self.OnPaint)
        wx.EVT_SIZE(self, self.OnSize)

        self.SetVirtualSize((width, height))
        self.SetScrollRate(20,20)

        # Make new offscreen bitmap: this bitmap will always have the
        # current drawing in it, so it can be used to save the image to
        # a file, or whatever.
        self._Buffer = wx.EmptyBitmap(width, height)
        # self.UpdateDrawing()

        # OnSize called to make sure the buffer is initialized.
        # This might result in OnSize getting called twice on some
        # platforms at initialization, but little harm done.
        self.OnSize(None)

    def Draw(self,dc):
        ## just here as a place holder.
        ## This method should be over-ridden when subclassed
        pass

    def OnPaint(self, event):
        # All that is needed here is to draw the buffer to screen
        ## ALWAYS use BufferedPaintDC otherwise need to work out which part
        ## of the bitmap is visible
        dc = wx.BufferedPaintDC(self, self._Buffer, wx.BUFFER_VIRTUAL_AREA)
        #if USE_BUFFERED_DC:
        #    dc = wx.BufferedPaintDC(self, self._Buffer, wx.BUFFER_VIRTUAL_AREA)
        #else:
        #    dc = wx.PaintDC(self)
        #    dc.DrawBitmap(self._Buffer,0,0)

    def OnSize(self,event):
        # The Buffer init is done here, to make sure the buffer is always
        # the same size as the Window
        Size  = self.GetClientSizeTuple()

        # Make new offscreen bitmap: this bitmap will always have the
        # current drawing in it, so it can be used to save the image to
        # a file, or whatever.
        ## self._Buffer = wx.EmptyBitmap(*Size)
        ## self.UpdateDrawing()

    def SaveToFile(self,FileName,FileType):
        ## This will save the contents of the buffer
        ## to the specified file. See the wxWindows docs for 
        ## wx.Bitmap::SaveFile for the details
        self._Buffer.SaveFile(FileName,FileType)

    def UpdateDrawing(self):
        """
        This would get called if the drawing needed to change, for whatever reason.

        The idea here is that the drawing is based on some data generated
        elsewhere in the system. If that data changes, the drawing needs to
        be updated.

        """

        if USE_BUFFERED_DC:
            dc = wx.BufferedDC(wx.ClientDC(self), self._Buffer, wx.BUFFER_VIRTUAL_AREA)
            self.Draw(dc)
        else:
            # update the buffer
            dc = wx.MemoryDC()
            dc.SelectObject(self._Buffer)
            self.Draw(dc)
            # update the screen
            wx.ClientDC(self).DrawBitmap(self._Buffer,0,0)
        self.Refresh()
        b = self._Buffer
        print 'Bitmap: width %d height %d depth %d bits' % (
                                        b.GetWidth(), b.GetHeight(), b.GetDepth())   
        print 'Buffersize %d MBytes' % (b.GetWidth()*b.GetHeight()*b.GetDepth()/8/1024/1024)
        print 'wx.free %d MBytes ' % (wx.GetFreeMemory()/1024/1024)
                        # Amount of free memory seems to be irrelevant. You can successfully
                        # run several instances of this program, each sized just below the 
                        # crash threshold and when free memory gets low you see the 
                        # paging file at work in Windows Task Manager.

class DrawWindow(BufferedWindow):
    def __init__(self, parent, id = -1):
        ## Any data the Draw() function needs must be initialized before
        ## calling BufferedWindow.__init__, as it will call the Draw
        ## function.

        self.DrawData = {}
        BufferedWindow.__init__(self, parent, id)

    def Draw(self, dc):
        dc.SetBackground( wx.Brush("White") )
        dc.Clear() # make sure you clear the bitmap!
        # Here's the actual drawing code.
        for key,data in self.DrawData.items():
            if key == "Rectangles":
                dc.SetBrush(wx.BLUE_BRUSH)
                dc.SetPen(wx.Pen('VIOLET', 4))
                for r in data:
                    dc.DrawRectangle(*r)
            elif key == "Ellipses":
                dc.SetBrush(wx.Brush("GREEN YELLOW"))
                dc.SetPen(wx.Pen('CADET BLUE', 2))
                for r in data:
                    dc.DrawEllipse(*r)
            elif key == "Polygons":
                dc.SetBrush(wx.Brush("SALMON"))
                dc.SetPen(wx.Pen('VIOLET RED', 4))
                for r in data:
                    dc.DrawPolygon(r)
        dc.DrawText('Something completely different.', 50,50)

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Double Buffered Test",
                         wx.DefaultPosition,
                         size=(500,500),
                         style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)

        ## Set up the MenuBar
        MenuBar = wx.MenuBar()

        file_menu = wx.Menu()
        ID_EXIT_MENU = wx.NewId()
        file_menu.Append(ID_EXIT_MENU, "E&xit","Terminate the program")
        wx.EVT_MENU(self, ID_EXIT_MENU, self.OnQuit)
        MenuBar.Append(file_menu, "&File")

        draw_menu = wx.Menu()
        ID_DRAW_MENU = wx.NewId()
        draw_menu.Append(ID_DRAW_MENU, "&New Drawing","Update the Drawing Data")
        wx.EVT_MENU(self, ID_DRAW_MENU,self.NewDrawing)
        BMP_ID = wx.NewId()
        draw_menu.Append(BMP_ID,'&Save Drawing\tAlt-I','')
        wx.EVT_MENU(self,BMP_ID, self.SaveToFile)
        MenuBar.Append(draw_menu, "&Draw")

        self.SetMenuBar(MenuBar)

        self.Window = DrawWindow(self)

    def OnQuit(self,event):
        self.Close(True)

    def NewDrawing(self,event):
        self.Window.DrawData = self.MakeNewData()
        self.Window.UpdateDrawing()

    def SaveToFile(self,event):
        dlg = wx.FileDialog(self, "Choose a file name to save the image as a PNG to",
                           defaultDir = "",
                           defaultFile = "",
                           wildcard = "*.png",
                           style = wx.SAVE)
        if dlg.ShowModal() == wx.ID_OK:
            self.Window.SaveToFile(dlg.GetPath(),wx.BITMAP_TYPE_PNG)
        dlg.Destroy()

    def MakeNewData(self):
        ## This method makes some random data to draw things with.
        MaxX, MaxY = width, height
        DrawData = {}

        # make some random rectangles
        l = []
        for i in range(5):
            w = random.randint(1,MaxX/2)
            h = random.randint(1,MaxY/2)
            x = random.randint(1,MaxX-w)
            y = random.randint(1,MaxY-h)
            l.append( (x,y,w,h) )
        DrawData["Rectangles"] = l

        # make some random ellipses
        l = []
        for i in range(5):
            w = random.randint(1,MaxX/2)
            h = random.randint(1,MaxY/2)
            x = random.randint(1,MaxX-w)
            y = random.randint(1,MaxY-h)
            l.append( (x,y,w,h) )
        DrawData["Ellipses"] = l

        # Polygons
        l = []
        for i in range(3):
            points = []
            for j in range(random.randint(3,8)):
                point = (random.randint(1,MaxX),random.randint(1,MaxY))
                points.append(point)
            l.append(points)
        DrawData["Polygons"] = l

        return DrawData

class DemoApp(wx.App):
    def OnInit(self):
        #wx.InitAllImageHandlers() # called so a PNG can be saved      
        frame = TestFrame()
        frame.Show(True)

        ## initialize a drawing
        ## It doesn't seem like this should be here, but the Frame does
        ## not get sized until Show() is called, so it doesn't work if
        ## it is put in the __init__ method.
        frame.NewDrawing(None)

        self.SetTopWindow(frame)

        return True

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            width = int(sys.argv[1])
            print 'Width input = %d' % width
        except IntegerError:
            pass
    if len(sys.argv) >= 3:
        try:
            height = int(sys.argv[2])
            print 'Height input = %d' % height
        except IntegerError:
            pass
    if len(sys.argv) >= 4:
        try:
            USE_BUFFERED_DC = int(sys.argv[3])
        except IntegerError:
            pass
    print "about to initialize the app. USE_BUFFERED_DC = %d"  % USE_BUFFERED_DC
    app = DemoApp(0)
    app.MainLoop()