
import ctypes
import subprocess
import tkinter as tk
import jsondb as db


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

class ErrorText():
    def __init__(self, text, y):
        self.text = text
        #https://docs.wxpython.org/4.0.7/wx.StaticText.html
        self.errorText = wx.StaticText(mainDialog, label=text, size=(300, -1))
        self.errorText.Wrap(300)
        self.RepositionSelf(y)

    def ShowSelf(self):
        self.errorText.Show()

    def HideSelf(self):
        self.errorText.Hide()

    def RepositionSelf(self, y):
        #https://stackoverflow.com/questions/14269880/the-right-way-to-find-the-size-of-text-in-wxpython
        width, height = self.errorText.GetTextExtent(self.text)
        #x = ( (bredde på vinduet) - (bredde på teksten) ) // 2
        if(width > 300):
            width = 300
        x = (500 - width) // 2

        self.errorText.SetPosition((x, y))
        #https://stackoverflow.com/questions/1785227/change-the-colour-of-a-statictext-wxpython
        self.errorText.SetForegroundColour(colourFinder("red"))

    def SetText(self, text, y):
        self.text = text
        self.errorText.SetLabel(text)
        self.errorText.Wrap(300)
        self.RepositionSelf(y)

    def NewError(self, text, y):
        self.HideSelf()
        self.ShowSelf()
        self.SetText(text, y)
        
def colourFinder(colourString):
    #https://html-color.codes/
    colourDict = {
        "red": "rgb(255,0,0)",
        "brown": "rgb(111,78,55)",
        "orange": "rgb(204,85,0)",
        "yellow": "rgb(255,255,0)",
        "green": "rgb(0,128,0)",
        "cyan": "rgb(0,255,255)",
        "blue": "rgb(0,0,255)",
        "purple": "rgb(128,0,128)",
        "pink": "rgb(255,192,203)",
        "grey": "rgb(128,128,128)",
        "black": "rgb(0,0,0)",
        "white": "rgb(255,255,255)"
    }

    return colourDict.get(colourString)



def createLoginPage():
    destroyEverything()
    usernameText = wx.StaticText(mainDialog, label="Username:", pos = [100, 125])
    usernameInput = wx.TextCtrl(mainDialog, pos = [175, 125], size=(200, -1))
    passwordText = wx.StaticText(mainDialog, label="Password:", pos = [100, 175])
    passwordInput = wx.TextCtrl(mainDialog, pos = [175, 175], size=(200, -1), style=wx.TE_PASSWORD)

    loginBtn = wx.Button(mainDialog, label = "Log in", pos = [125, 250])
    createUserBtn = wx.Button(mainDialog, label = "Create new account", pos = [250, 250])

    def loginBtnClick(evt):
        tryLoggingIn(usernameInput.GetValue(), passwordInput.GetValue())

    def createUserBtnClick(evt):
        createUserCreationPage()

    def loginValid(username, password):
        users = db.readJSON("userdb")

        for user in users:
            if user.get("username").lower() == username.lower():
                if user.get("password") == password:
                    return True

        return False

    def tryLoggingIn(username, password):
        users = db.readJSON("userdb")

        if loginValid(username, password) == True:
            createDeviceListPage(username)
        
        else:
            errText = ErrorText("Wrong username or password", 340)



    loginBtn.Bind(wx.EVT_BUTTON, loginBtnClick)
    createUserBtn.Bind(wx.EVT_BUTTON, createUserBtnClick)

def createUserCreationPage():
    destroyEverything()
    errorText = ErrorText("", 340)
    usernameText = wx.StaticText(mainDialog, label="Username:", pos = [80, 100], size=(100, -1), style=wx.ALIGN_RIGHT)
    usernameInput = wx.TextCtrl(mainDialog, pos = [190, 100], size=(200, -1))
    emailText = wx.StaticText(mainDialog, label="Email adress:", pos = [80, 130], size=(100, -1), style=wx.ALIGN_RIGHT)
    emailInput = wx.TextCtrl(mainDialog, pos = [190, 130], size=(200, -1))
    passwordText = wx.StaticText(mainDialog, label="Password:", pos = [80, 160], size=(100, -1), style=wx.ALIGN_RIGHT)
    passwordInput = wx.TextCtrl(mainDialog, pos = [190, 160], size=(200, -1), style=wx.TE_PASSWORD)
    passwordText2 = wx.StaticText(mainDialog, label="Confirm password:", pos = [80, 190], size=(100, -1), style=wx.ALIGN_RIGHT)
    passwordInput2 = wx.TextCtrl(mainDialog, pos = [190, 190], size=(200, -1), style=wx.TE_PASSWORD)

    createBtn = wx.Button(mainDialog, label = "Create user", pos = [310, 220])

    def tryCreate(evt):
        if db.isUsernameTaken("userdb", usernameInput.GetValue()) != False: 
            errorText.NewError("An account with this username already exists", 340)
        else:
            if db.isUsernameValid(usernameInput.GetValue()) != True:
                errorText.NewError(db.isUsernameValid(usernameInput.GetValue()), 340)
            else:
                if db.isEmailTaken("userdb", emailInput.GetValue()) != False:
                    errorText.NewError("An account with this email already exists", 340)
                else:
                    if db.isEmailValid(emailInput.GetValue()) != True:
                        errorText.NewError(db.isEmailValid(emailInput.GetValue()), 340)
                    else:
                        if db.isPasswordValid(passwordInput.GetValue()) == False:
                            errorText.NewError(db.isPasswordValid(passwordInput.GetValue()), 340)
                        else:
                            if passwordInput.GetValue() != passwordInput2.GetValue():
                                errorText.NewError("Passwords do not match", 340)
                            else:
                                #https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
                                ctypes.windll.user32.MessageBoxW(0, "Your account was created!", "Success", 1)
                                db.addUserToJSON("userdb", usernameInput.GetValue(), passwordInput.GetValue(), emailInput.GetValue())
                                createDeviceListPage(usernameInput.GetValue())


    createBtn.Bind(wx.EVT_BUTTON, tryCreate)

def createDeviceListPage(username):
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

    def makeListBoxDeviceList(list):
        newList = []
        for device in list:
            newList.append(device.get("name") + " " + device.get("brand"))

        return newList

    listBox = wx.ListBox(mainDialog, size = [150, 200], choices = [])
    listBox.Center()

    def searchForDevices(evt):
        listBox.SetItems(makeListBoxDeviceList(db.FindDeviceListUser("userdb", username)))

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

