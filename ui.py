
import ctypes
import subprocess
import tkinter as tk
from jsondb import JsonDatabase, JsonReadWrite
import sys
sys.path.append('Devices/')
from Nearby_devices import lights,fridges,heaters

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

db = JsonDatabase("userdb")

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


#buttons: back, log out

#Tilbakeknapp til innloggingsside fra brukeropprettelsesside
def back_btn(prev_page):
    def on_back_btn(evt):
        prev_page()

    main_dialog.back_btn = wx.Button(main_dialog,label="< Back",pos=[30,400])
    main_dialog.back_btn.Bind(wx.EVT_BUTTON, on_back_btn)

#Loggut knapp
def log_out_btn():
    def on_log_out_btn(evt):
        confirm_decision = wx.MessageBox(
            "Are you sure you want to log out?",
            "Log out",
            wx.YES_NO | wx.ICON_QUESTION
        )
        if confirm_decision == wx.YES:
            create_login_page()

    main_dialog.log_out_btn = wx.Button(main_dialog,label="Log out",pos=[395,15])
    main_dialog.log_out_btn.Bind(wx.EVT_BUTTON, on_log_out_btn)


import wx

def create_login_page():
    destroy_everything()

    panel = wx.Panel(main_dialog)

    # Create sizers
    main_sizer = wx.BoxSizer(wx.VERTICAL)
    form_sizer = wx.GridBagSizer(vgap=20, hgap=10)

    # Add a spacer to move the form down
    main_sizer.Add((0, 50))

    # Add a logo or title
    title = wx.StaticText(panel, label="Welcome to MySmartHome")
    title_font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
    title.SetFont(title_font)
    title.SetForegroundColour(wx.Colour(0, 70, 140))

    # Input fields with placeholders
    username_input = wx.TextCtrl(panel, style=wx.TE_LEFT, value="")
    username_input.SetHint("username")
    username_input.SetFocus()
    password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD | wx.TE_LEFT, value="")
    password_input.SetHint("Password")
    # Buttons
    create_user_btn = wx.Button(panel, label="Create new account")
    login_btn = wx.Button(panel, label="Log in")

    # Arrange items using the form sizer
    form_sizer.Add(username_input, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(password_input, pos=(1, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(create_user_btn, pos=(2, 0), flag=wx.ALIGN_LEFT)
    form_sizer.Add(login_btn, pos=(2, 1), flag=wx.EXPAND)

    # Make the input fields column growable
    form_sizer.AddGrowableCol(0)
    form_sizer.AddGrowableCol(1)

    # Add the title and form sizer to the main sizer
    main_sizer.Add(title, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 15)
    main_sizer.Add(form_sizer, 1, wx.ALL | wx.EXPAND, 20)

    # Set the main sizer and layout
    panel.SetSizer(main_sizer)
    main_dialog.Layout()




    def login_btn_click(evt):
        try_logging_in(username_input.GetValue(), password_input.GetValue())

    def create_user_btn_click(evt):
        create_user_creation_page()

    login_btn.Bind(wx.EVT_BUTTON, login_btn_click)
    create_user_btn.Bind(wx.EVT_BUTTON, create_user_btn_click)


    def login_btn_click(evt):
        try_logging_in(username_input.GetValue(), password_input.GetValue())

    def create_user_btn_click(evt):
        create_user_creation_page()

    def is_login_valid(username, password):
        users = db.read_json()

        for user in users:
            if user.get("username").lower() == username.lower():
                if user.get("password") == password:
                    return True

        return False

    def try_logging_in(username, password):
        users = db.read_json()

        if is_login_valid(username, password) == True:
            create_home_page(username)
        
        else:
            errText = ErrorText("Wrong username or password", 340)



    login_btn.Bind(wx.EVT_BUTTON, login_btn_click)
    create_user_btn.Bind(wx.EVT_BUTTON, create_user_btn_click)

def create_user_creation_page():
    destroy_everything()
    error_text = ErrorText("", 340)
    username_text = wx.StaticText(main_dialog, label="Username:", pos = [80, 100], size=(100, -1), style=wx.ALIGN_RIGHT)
    username_input = wx.TextCtrl(main_dialog, pos = [190, 100], size=(200, -1))
    username_input.SetFocus()
    email_text = wx.StaticText(main_dialog, label="Email adress:", pos = [80, 130], size=(100, -1), style=wx.ALIGN_RIGHT)
    email_input = wx.TextCtrl(main_dialog, pos = [190, 130], size=(200, -1))
    password_text = wx.StaticText(main_dialog, label="Password:", pos = [80, 160], size=(100, -1), style=wx.ALIGN_RIGHT)
    password_input = wx.TextCtrl(main_dialog, pos = [190, 160], size=(200, -1), style=wx.TE_PASSWORD)
    password_text2 = wx.StaticText(main_dialog, label="Confirm password:", pos = [80, 190], size=(100, -1), style=wx.ALIGN_RIGHT)
    password_input2 = wx.TextCtrl(main_dialog, pos = [190, 190], size=(200, -1), style=wx.TE_PASSWORD)


    back_btn(create_login_page)

    create_btn = wx.Button(main_dialog, label = "Create user", pos = [310, 220])

    def try_create(evt):
        username = username_input.GetValue()
        email = email_input.GetValue()
        password = password_input.GetValue()


        if db.is_username_taken(username) != False: 
            error_text.NewError("An account with this username already exists", 340)
            return
        else:
            if db.is_username_valid(username) != True:
                error_text.NewError(db.is_username_valid(username), 340)
                return
            else:
                if db.is_email_taken(email) != False:
                    error_text.NewError("An account with this email already exists", 340)
                    return
                else:
                    if db.is_email_valid(email) != True:
                        error_text.NewError(db.is_email_valid(email), 340)
                    else:
                        password_validation_result = db.is_password_valid(password)
                        if password_validation_result != True:
                            error_text.NewError(db.is_password_valid(password), 340)
                            return
                        else:
                            if password != password_input2.GetValue():
                                error_text.NewError("Passwords do not match", 340)
                                return
                            else:
                                #https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
                                ctypes.windll.user32.MessageBoxW(0, "Your account was created!", "Success", 1)
                                db.add_user_to_json( username, password, email)
                                create_home_page(username)


    create_btn.Bind(wx.EVT_BUTTON, try_create)




def create_home_page(username):
    destroy_everything()

    #functionality for adding new devices which will open 'create_add_new_device_page'
    #The function is there to make sure the event isnt executed immideatly, instead its being done on button click
    def on_add_device(evt):
        create_add_new_device_page(username)

    add_device_btn = wx.Button(main_dialog,label="Add new device",pos=[360,150])
    add_device_btn.Bind(wx.EVT_BUTTON, on_add_device)

    log_out_btn()

    #Todo: Button for adjusting a specific devices settings

    #Creates list of already added devices
    def make_listbox_device_list(list):
        db.remove_duplicate_devices_from_user( username)
        new_list = []
        for device in list:
            new_list.append(device.get("name") + " " + device.get("brand"))

        return new_list

    welcome_text = wx.StaticText(main_dialog, label=f"Welcome, {username}!", pos=[169, 50])

    device_list = db.find_device_list_user(username)
    items = make_listbox_device_list(device_list)

    listbox = wx.ListBox(main_dialog, size = [150, 200], choices = items)
    listbox.Center()
    listbox.SetFocus()



def create_add_new_device_page(username):
    destroy_everything()
    
    all_devices = lights + fridges + heaters

    listbox = wx.ListBox(main_dialog, size = [200, 200], choices = [])
    listbox.Center()
    listbox.SetFocus()

    log_out_btn()
    #Using a lambda function to make sure the functions called when button is clicked
    back_btn(lambda: create_home_page(username))

    def get_all_devices():
        #device_list = [f"{device.name} {device.brand}" for device in all_devices]
        device_list = []
        user_devices = db.find_device_list_user(username)

#fix: det var 2 hovedproblemer - 1. vi sammenlignet et objekt med et dict, 2. prod_id varulik for hver gang programmet startet
        for device in all_devices:
            device_already_added = False
            for user_device in user_devices:
                if device.prod_id == user_device['prod_id']:
                    device_already_added = True
                    break
            if not device_already_added:
                device_list.append(f"{device.name} {device.brand}")
            
        return device_list

    def search_for_devices(evt):
        device_list = get_all_devices()
        listbox.SetItems(device_list)

    search_btn = wx.Button(main_dialog, label = "search", pos = [200, 100])
    search_btn.Bind(wx.EVT_BUTTON, search_for_devices)
    #Todo: Lage en dropdown-meny for å få en liste med kun lys, kjøleskap eller varmeovner

    def on_add_device_to_user(evt):
        selected_index = listbox.GetSelection()
        if selected_index != wx.NOT_FOUND:
            selected_device = all_devices[selected_index]
            #Converts object -> dictionary
            device = {
                'prod_id': selected_device.prod_id,
                'name': selected_device.name,
                'brand': selected_device.brand,
                'category': selected_device.category
            }
            db.add_device_to_user(username,device)
            create_home_page(username)

    add_device_btn = wx.Button(main_dialog,label="Add selected device",pos=[360,150])
    add_device_btn.Bind(wx.EVT_BUTTON, on_add_device_to_user)

    main_dialog.Show()

#https://discuss.wxpython.org/t/getchildren/27335
def destroy_everything():
    for child in main_dialog.GetChildren():
        child.Destroy()
create_login_page()
main_dialog.Show()
app.MainLoop()
