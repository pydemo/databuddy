import wx
import os
def GetDataDir():
	"""
	Return the standard location on this platform for application data
	"""
	sp = wx.StandardPaths.Get()
	return sp.GetUserDataDir()

def DoesModifiedExist(name):
	"""Returns whether the specified demo has a modified copy"""
	if os.path.exists(GetModifiedFilename(name)):
		return True
	else:
		return False



		
def GetModifiedFilename(name):
	"""
	Returns the filename of the modified version of the specified demo
	"""
	if not name.endswith(".py"):
		name = name + ".py"
	return os.path.join(GetModifiedDirectory(), name)

def GetModifiedDirectory():
	"""
	Returns the directory where modified versions of the demo files
	are stored
	"""
	return os.path.join(GetDataDir(), "modified")	