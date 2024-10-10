
import subprocess
import tkinter as tk
try:
	import wx
except:
	subprocess.run("powershell", text = True, input = "pip install wxpython")
try:
	import wx
except:
	input("could not find the wx module. Press enter to exit")
app = wx.App()

searchList = []

def onDestroy(evt):
	exit()
	
mainDialog = wx.Dialog(None, title = "main", size = [500, 500])
mainDialog.Center()
mainDialog.Bind(wx.EVT_CLOSE, onDestroy)

usernameText = wx.StaticText(mainDialog, label="Username:", pos = [100, 125])
passwordText = wx.StaticText(mainDialog, label="Password:", pos = [100, 175])

usernameInput = wx.TextCtrl(mainDialog, pos = [175, 125], size=(200, -1))
passwordInput = wx.TextCtrl(mainDialog, pos = [175, 175], size=(200, -1), style=wx.TE_PASSWORD)

loginButton = wx.Button(mainDialog, label = "Log in", pos = [125, 250])
createUserButton = wx.Button(mainDialog, label = "Create new account", pos = [250, 250])

def loginClick(evt):
	print(usernameInput.GetValue())

loginButton.Bind(wx.EVT_BUTTON, loginClick)

mainDialog.Show()
app.MainLoop()