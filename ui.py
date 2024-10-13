
import subprocess
import tkinter as tk
import csvdb as db

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


def createLoginPage():
    destroyEverything()
    usernameText = wx.StaticText(mainDialog, label="Username:", pos = [100, 125])
    usernameInput = wx.TextCtrl(mainDialog, pos = [175, 125], size=(200, -1))
    passwordText = wx.StaticText(mainDialog, label="Password:", pos = [100, 175])
    passwordInput = wx.TextCtrl(mainDialog, pos = [175, 175], size=(200, -1), style=wx.TE_PASSWORD)

    loginBtn = wx.Button(mainDialog, label = "Log in", pos = [125, 250])
    createUserBtn = wx.Button(mainDialog, label = "Create new account", pos = [250, 250])

    def loginBtnClick(evt):
        print(usernameInput.GetValue())
        createDeviceListPage()

    def createUserBtnClick(evt):
        createUserCreationPage()

    def tryLoggingIn(username, password):
        db.readCSV("userdb")

    loginBtn.Bind(wx.EVT_BUTTON, loginBtnClick)
    createUserBtn.Bind(wx.EVT_BUTTON, createUserBtnClick)

def createUserCreationPage():
    destroyEverything()
    usernameText = wx.StaticText(mainDialog, label="Username:", pos = [100, 100], style=wx.ALIGN_RIGHT)
    emailText = wx.StaticText(mainDialog, label="Email adress:", pos = [100, 130], style=wx.ALIGN_RIGHT)
    passwordText = wx.StaticText(mainDialog, label="Password:", pos = [100, 160], style=wx.ALIGN_RIGHT)
    passwordText2 = wx.StaticText(mainDialog, label="Confirm password:", pos = [100, 190], style=wx.ALIGN_RIGHT)

    usernameInput = wx.TextCtrl(mainDialog, pos = [175, 125], size=(200, -1))
    passwordInput = wx.TextCtrl(mainDialog, pos = [175, 175], size=(200, -1), style=wx.TE_PASSWORD)

    createBtn = wx.Button(mainDialog, label = "Create user", pos = [125, 250])

    def tryCreate(evt):
        createLoginPage()

    createBtn.Bind(wx.EVT_BUTTON, tryCreate)

def createDeviceListPage():
    destroyEverything()
    smart_devices = [
        "Philips Hue",
        "Google Nest Home",
        "LG CX",
        "Ring Video Doorbell",
        "Ecobee SmartThermostat",
        "iRobot Roomba s9+",
        "August Smart Lock Pro"
    ]
    listBox = wx.ListBox(mainDialog, size = [150, 200], choices = [])
    listBox.Center()

    def searchForDevices(evt):
        listBox.SetItems(smart_devices)

    searchButton = wx.Button(mainDialog, label = "search", pos = [200, 100])
    searchButton.Bind(wx.EVT_BUTTON, searchForDevices)
    mainDialog.Show()

#https://discuss.wxpython.org/t/getchildren/27335
def destroyEverything():
    for child in mainDialog.GetChildren():
        child.Destroy()
createLoginPage()
mainDialog.Show()
app.MainLoop()