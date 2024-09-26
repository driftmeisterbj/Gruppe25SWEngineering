
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
#Fake list of devices
smart_devices = [
    "Philips Hue",
    "Google Nest Home",
    "LG CX",
    "Ring Video Doorbell",
    "Ecobee SmartThermostat",
    "iRobot Roomba s9+",
    "August Smart Lock Pro"
]
searchList = []
def onDestroy(evt):
	exit()
mainDialog = wx.Dialog(None, title = "main", size = [500, 500])
mainDialog.Center()
mainDialog.Bind(wx.EVT_CLOSE, onDestroy)
listBox = wx.ListBox(mainDialog, size = [150, 200], choices = [])
listBox.Center()
# Function for listing up all available devices
def searchForDevices(evt):
	listBox.SetItems(smart_devices)
searchButton = wx.Button(mainDialog, label = "search", pos = [200, 100])
searchButton.Bind(wx.EVT_BUTTON, searchForDevices)
mainDialog.Show()
app.MainLoop()