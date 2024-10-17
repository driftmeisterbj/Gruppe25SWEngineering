
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

search_list = []

def on_destroy(evt):
    exit()

main_dialog = wx.Dialog(None, title = "main", size = [500, 500])
main_dialog.Center()
main_dialog.Bind(wx.EVT_CLOSE, on_destroy)

class ErrorText():
    def __init__(self, text, y):
        self.text = text
        #https://docs.wxpython.org/4.0.7/wx.StaticText.html
        self.error_text = wx.StaticText(main_dialog, label=text, size=(300, -1))
        self.error_text.Wrap(300)
        self.RepositionSelf(y)

    def ShowSelf(self):
        self.error_text.Show()

    def HideSelf(self):
        self.error_text.Hide()

    def RepositionSelf(self, y):
        #https://stackoverflow.com/questions/14269880/the-right-way-to-find-the-size-of-text-in-wxpython
        width, height = self.error_text.GetTextExtent(self.text)
        #x = ( (bredde på vinduet) - (bredde på teksten) ) // 2
        if(width > 300):
            width = 300
        x = (500 - width) // 2

        self.error_text.SetPosition((x, y))
        #https://stackoverflow.com/questions/1785227/change-the-colour-of-a-statictext-wxpython
        self.error_text.SetForegroundColour(colour_finder("red"))

    def SetText(self, text, y):
        self.text = text
        self.error_text.SetLabel(text)
        self.error_text.Wrap(300)
        self.RepositionSelf(y)

    def NewError(self, text, y):
        self.HideSelf()
        self.ShowSelf()
        self.SetText(text, y)
        
def colour_finder(colour_string):
    #https://html-color.codes/
    colour_dict = {
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

    return colour_dict.get(colour_string)



def create_login_page():
    destroy_everything()
    username_text = wx.StaticText(main_dialog, label="Username:", pos = [100, 125])
    username_input = wx.TextCtrl(main_dialog, pos = [175, 125], size=(200, -1))
    password_text = wx.StaticText(main_dialog, label="Password:", pos = [100, 175])
    password_input = wx.TextCtrl(main_dialog, pos = [175, 175], size=(200, -1), style=wx.TE_PASSWORD)

    login_btn = wx.Button(main_dialog, label = "Log in", pos = [125, 250])
    create_user_btn = wx.Button(main_dialog, label = "Create new account", pos = [250, 250])

    def login_btn_click(evt):
        try_logging_in(username_input.GetValue(), password_input.GetValue())

    def create_user_btn_click(evt):
        create_user_creation_page()

    def is_login_valid(username, password):
        users = db.read_json("userdb")

        for user in users:
            if user.get("username").lower() == username.lower():
                if user.get("password") == password:
                    return True

        return False

    def try_logging_in(username, password):
        users = db.read_json("userdb")

        if is_login_valid(username, password) == True:
            create_device_list_page(username)
        
        else:
            errText = ErrorText("Wrong username or password", 340)



    login_btn.Bind(wx.EVT_BUTTON, login_btn_click)
    create_user_btn.Bind(wx.EVT_BUTTON, create_user_btn_click)

def create_user_creation_page():
    destroy_everything()
    error_text = ErrorText("", 340)
    username_text = wx.StaticText(main_dialog, label="Username:", pos = [80, 100], size=(100, -1), style=wx.ALIGN_RIGHT)
    username_input = wx.TextCtrl(main_dialog, pos = [190, 100], size=(200, -1))
    email_text = wx.StaticText(main_dialog, label="Email adress:", pos = [80, 130], size=(100, -1), style=wx.ALIGN_RIGHT)
    email_input = wx.TextCtrl(main_dialog, pos = [190, 130], size=(200, -1))
    password_text = wx.StaticText(main_dialog, label="Password:", pos = [80, 160], size=(100, -1), style=wx.ALIGN_RIGHT)
    password_input = wx.TextCtrl(main_dialog, pos = [190, 160], size=(200, -1), style=wx.TE_PASSWORD)
    password_text2 = wx.StaticText(main_dialog, label="Confirm password:", pos = [80, 190], size=(100, -1), style=wx.ALIGN_RIGHT)
    password_input2 = wx.TextCtrl(main_dialog, pos = [190, 190], size=(200, -1), style=wx.TE_PASSWORD)

    create_btn = wx.Button(main_dialog, label = "Create user", pos = [310, 220])

    def try_create(evt):
        if db.is_username_taken("userdb", username_input.GetValue()) != False: 
            error_text.NewError("An account with this username already exists", 340)
        else:
            if db.is_username_valid(username_input.GetValue()) != True:
                error_text.NewError(db.is_username_valid(username_input.GetValue()), 340)
            else:
                if db.is_email_taken("userdb", email_input.GetValue()) != False:
                    error_text.NewError("An account with this email already exists", 340)
                else:
                    if db.is_email_valid(email_input.GetValue()) != True:
                        error_text.NewError(db.is_email_valid(email_input.GetValue()), 340)
                    else:
                        if db.is_password_valid(password_input.GetValue()) == False:
                            error_text.NewError(db.is_password_valid(password_input.GetValue()), 340)
                        else:
                            if password_input.GetValue() != password_input2.GetValue():
                                error_text.NewError("Passwords do not match", 340)
                            else:
                                #https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
                                ctypes.windll.user32.MessageBoxW(0, "Your account was created!", "Success", 1)
                                db.add_user_to_json("userdb", username_input.GetValue(), password_input.GetValue(), email_input.GetValue())
                                create_device_list_page(username_input.GetValue())


    create_btn.Bind(wx.EVT_BUTTON, try_create)

def create_device_list_page(username):
    destroy_everything()
    smart_devices = [
        "Philips Hue",
        "Google Nest Home",
        "LG CX",
        "Ring Video Doorbell",
        "Ecobee SmartThermostat",
        "iRobot Roomba s9+",
        "August Smart Lock Pro"
    ]

    def make_listbox_device_list(list):
        db.remove_duplicate_devices_from_user("userdb", username)
        new_list = []
        for device in list:
            new_list.append(device.get("name") + " " + device.get("brand"))

        return new_list

    listbox = wx.ListBox(main_dialog, size = [150, 200], choices = [])
    listbox.Center()

    def search_for_devices(evt):
        listbox.SetItems(make_listbox_device_list(db.find_device_list_user("userdb", username)))

    search_btn = wx.Button(main_dialog, label = "search", pos = [200, 100])
    search_btn.Bind(wx.EVT_BUTTON, search_for_devices)
    main_dialog.Show()

#https://discuss.wxpython.org/t/getchildren/27335
def destroy_everything():
    for child in main_dialog.GetChildren():
        child.Destroy()
create_login_page()
main_dialog.Show()
app.MainLoop()
