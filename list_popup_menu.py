class BookList(wx.ListCtrl):
  def __init__(self, parent, ID=wx.ID_ANY):
    wx.ListCtrl.__init__(self, parent, ID)

    self.InsertColumn(0, 'Title')
    self.InsertColumn(1, 'Author')

    # set column width ...

    self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
    self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

    # currently selected row
    self.cur = None


  def OnLeftDown(self, event):
    if self.cur != None:
      self.Select( self.cur, 0) # deselect currently selected item

    x,y = event.GetPosition()
    row,flags = self.HitTest( (x,y) )

    self.Select(row)
    self.cur = row


  def OnRightDown(self, event):
    menu = wx.Menu()
    delete = menu.Append(wx.ID_ANY, 'Delete Item')

    self.Bind(wx.EVT_MENU, self.OnDelete, delete)

    # select row
    self.OnLeftDown(event)

    self.PopupMenu(menu, event.GetPosition())