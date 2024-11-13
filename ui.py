
import ctypes
import subprocess

from jsondb import JsonDatabase, JsonReadWrite
import os
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
userDb = os.path.join(os.path.dirname(__file__), "userdb")
db = JsonDatabase(userDb)

class ErrorText():
    def __init__(self, parent, y):
        self.error_text = wx.StaticText(parent, label="")
        self.error_text.SetForegroundColour(wx.RED)
        self.y = y
        self.error_text.Wrap(y)
        self.error_text.Hide()

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
        self.HideSelf()
        self.ShowSelf()
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



main_dialog.SetBackgroundColour(wx.Colour(0, 70, 140))

#buttons: back, log out, display name

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

    main_dialog.log_out_btn = wx.Button(main_dialog,label="Log out",pos=[395,30])
    main_dialog.log_out_btn.Bind(wx.EVT_BUTTON, on_log_out_btn)

#display name
def display_name(username):
    title = wx.StaticText(main_dialog, label=f"Hi, {username}!",pos=[395,10], style=wx.ALIGN_CENTER)
    title.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_NORMAL))
    title.SetForegroundColour(wx.Colour(255, 255, 255))

#display app name
def display_app_name():
    title = wx.StaticText(main_dialog, label=f"MySmartHome",pos=[10,8], style=wx.ALIGN_CENTER)
    title.SetFont(wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    title.SetForegroundColour(wx.Colour(255, 255, 255))
    return title



def create_login_page():
    destroy_everything()

    panel = wx.Panel(main_dialog)

    # Create sizers
    main_sizer = wx.BoxSizer(wx.VERTICAL)
    form_sizer = wx.GridBagSizer(vgap=10, hgap=10)

    # Add a spacer to move the form down
    main_sizer.AddSpacer(50)

    # Header
    header = wx.StaticText(panel, label="Login")
    header_font = header.GetFont()
    header_font.PointSize += 15
    header_font = header_font.Bold()  
    header.SetFont(header_font)
    header.SetForegroundColour(wx.Colour(255, 255, 255))  
    main_sizer.Add(header, 0, wx.ALIGN_CENTER | wx.BOTTOM, 0)

    # Input fields with placeholders
    username_input = wx.TextCtrl(panel, style=wx.TE_LEFT, value="")
    username_input.SetHint("Username")

    password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD | wx.TE_LEFT, value="")
    password_input.SetHint("Password")

    # Buttons
    create_user_btn = wx.Button(panel, label="Create New Account")
    login_btn = wx.Button(panel, label="Log In")

    error_text = ErrorText(panel, 300)

    # Arrange items using the form sizer
    form_sizer.Add(username_input, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(password_input, pos=(1, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(create_user_btn, pos=(2, 0), flag=wx.ALIGN_LEFT)
    form_sizer.Add(login_btn, pos=(2, 1), flag=wx.EXPAND)

    # Make the input fields columns growable
    form_sizer.AddGrowableCol(0)
    form_sizer.AddGrowableCol(1)

    # Error text
    form_sizer.Add(error_text.error_text, pos=(3, 0), span=(1, 2), flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL)

    # Add the form sizer to the main sizer
    main_sizer.Add(form_sizer, 1, wx.ALL | wx.EXPAND, 20)

    # Set the main sizer and layout
    panel.SetSizer(main_sizer)
    panel.Layout()
    main_dialog.Layout()

    # Display the app name
    display_app_name()



    def login_btn_click(evt):
        try_logging_in(username_input.GetValue(), password_input.GetValue())

    def create_user_btn_click(evt):
        create_user_creation_page()

    login_btn.Bind(wx.EVT_BUTTON, login_btn_click)
    create_user_btn.Bind(wx.EVT_BUTTON, create_user_btn_click)

    def is_login_valid(username, password):
        users = db.read_json()

        for user in users:
            if user.get("username").lower() == username.lower():
                if user.get("password") == password:
                    return True

        return False

    def try_logging_in(username, password):
        users = db.read_json()

        if is_login_valid(username, password):
            create_home_page(username)
        
        else:
            error_text.NewError("Wrong username or password", 300)



def create_user_creation_page():
    destroy_everything()
    panel = wx.Panel(main_dialog)

    # Create sizers
    main_sizer = wx.BoxSizer(wx.VERTICAL)
    form_sizer = wx.GridBagSizer(vgap=10, hgap=10)

    # Create account header

    # Add a spacer to move the form down
    main_sizer.AddSpacer(50)  


    # Customize header font
    header = wx.StaticText(panel, label="Create Account")
    header_font = header.GetFont()
    header_font.PointSize += 15
    header_font = header_font.Bold()  
    header.SetFont(header_font)
    header.SetForegroundColour(wx.Colour(255, 255, 255))  
    main_sizer.Add(header, 0, wx.ALIGN_CENTER | wx.BOTTOM, 0)

    # Input fields with placeholders
    username_input = wx.TextCtrl(panel)
    username_input.SetHint("Your Username")

    email_input = wx.TextCtrl(panel)
    email_input.SetHint("Your Email")

    password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
    password_input.SetHint("Your Password")

    confirm_password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
    confirm_password_input.SetHint("Confirm Your Password")

    # Error text
    error_text = ErrorText(panel, 400)

    # Arrange items using the form sizer
    form_sizer.Add(username_input, pos=(0, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(email_input, pos=(1, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(password_input, pos=(2, 0), span=(1, 2), flag=wx.EXPAND)
    form_sizer.Add(confirm_password_input, pos=(3, 0), span=(1, 2), flag=wx.EXPAND)

    # Add the error text to the form_sizer at the desired position
    form_sizer.Add(error_text.error_text, pos=(4, 0), span=(1, 2), flag=wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL)

    # Buttons
    back_btn_widget = wx.Button(panel, label="< Back")
    create_btn = wx.Button(panel, label="Create Account")
    form_sizer.Add(back_btn_widget, pos=(5, 0), flag=wx.ALIGN_LEFT)
    form_sizer.Add(create_btn, pos=(5, 1), flag=wx.ALIGN_RIGHT)

    # Make the input fields column growable
    form_sizer.AddGrowableCol(0)
    form_sizer.AddGrowableCol(1)

    # Add the form sizer to the main sizer
    main_sizer.Add(form_sizer, 0, wx.ALL | wx.EXPAND, 20)

    # Set the main sizer and layout
    panel.SetSizer(main_sizer)
    panel.Layout()
    main_dialog.Layout()

    # Display the app name
    display_app_name()

    # Event handlers
    def back_btn_click(evt):
        create_login_page()

    def try_create(evt):
        username = username_input.GetValue().strip()
        email = email_input.GetValue().strip()
        password = password_input.GetValue()
        confirm_password = confirm_password_input.GetValue()

        error_text.HideSelf()  # Hide previous errors

        # Validation Checks
        if not username:
            error_text.SetText("Username cannot be empty.", 400)
            panel.Layout()
            return
        if not email:
            error_text.SetText("Email cannot be empty.", 400)
            panel.Layout()
            return
        if not password:
            error_text.SetText("Password cannot be empty.", 400)
            panel.Layout()
            return
        if password != confirm_password:
            error_text.SetText("Passwords do not match.", 400)
            panel.Layout()
            return
        if db.is_username_taken(username):
            error_text.SetText("An account with this username already exists.", 400)
            panel.Layout()
            return
        elif db.is_username_valid(username) != True:
            error_text.SetText(db.is_username_valid(username), 400)
            panel.Layout()
            return
        elif db.is_email_taken(email):
            error_text.SetText("An account with this email already exists.", 400)
            panel.Layout()
            return
        elif db.is_email_valid(email) != True:
            error_text.SetText(db.is_email_valid(email), 400)
            panel.Layout()
            return
        elif db.is_password_valid(password) != True:
            error_text.SetText(db.is_password_valid(password), 400)
            panel.Layout()
            return
        else:
            ctypes.windll.user32.MessageBoxW(0, "Your account was created!", "Success", 1)
            db.add_user_to_json(username, password, email)
            create_home_page(username)

    # Bind events to buttons
    back_btn_widget.Bind(wx.EVT_BUTTON, back_btn_click)
    create_btn.Bind(wx.EVT_BUTTON, try_create)

    # Ensure the layout is updated
    panel.Layout()
    main_dialog.Layout()




def create_home_page(username):
    destroy_everything()

    title = wx.StaticText(main_dialog, label="Your Devices",pos=[188,100], style=wx.ALIGN_CENTER)
    title.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
    title.SetForegroundColour(wx.Colour(255, 255, 255))


    #functionality for adding new devices which will open 'create_add_new_device_page'
    #The function is there to make sure the event isnt executed immideatly, instead its being done on button click
    def on_add_device(evt):
        create_add_new_device_page(username)

    def on_configure_device(evt):
        device_name = ""
        device = db.get_device(username, device_name)

    add_device_btn = wx.Button(main_dialog,label="Add new device",pos=[360,150])
    add_device_btn.Bind(wx.EVT_BUTTON, on_add_device)

    log_out_btn()
    display_app_name()
    display_name(username)

    #Todo: Button for adjusting a specific devices settings
    configure_device_btn = wx.Button(main_dialog,label="Configure Device",pos=[360,170])
    configure_device_btn.Bind(wx.EVT_BUTTON, on_configure_device)

    #Creates list of already added devices
    def make_listbox_device_list(list):
        db.remove_duplicate_devices_from_user( username)
        new_list = []
        for device in list:
            new_list.append(device.get("name") + " " + device.get("brand"))

        return new_list


    device_list = db.find_device_list_user(username)
    items = make_listbox_device_list(device_list)

    listbox = wx.ListBox(main_dialog, size = [150, 200], choices = items)
    listbox.Center()



def create_add_new_device_page(username):
    destroy_everything()
    
    all_devices = lights + fridges + heaters

    listbox = wx.ListBox(main_dialog, size = [200, 200], choices = [])
    listbox.Center()

    log_out_btn()
    #Using a lambda function to make sure the functions called when button is clicked
    back_btn(lambda: create_home_page(username))

    def get_all_devices():
        #device_list = [f"{device.name} {device.brand}" for device in all_devices]
        device_list = []
        user_devices = db.find_device_list_user(username)

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

    search_btn = wx.Button(main_dialog, label = "search", pos = [205, 100])
    search_btn.Bind(wx.EVT_BUTTON, search_for_devices)
    #Todo: Lage en dropdown-meny for å få en liste med kun lys, kjøleskap eller varmeovner

    def on_add_device_to_user(evt):
        selected_index = listbox.GetSelection()
        if selected_index != wx.NOT_FOUND:
            selected_device = all_devices[selected_index]
            """
            #Converts object -> dictionary
            device = {
                'prod_id': selected_device.prod_id,
                'name': selected_device.name,
                'brand': selected_device.brand,
                'category': selected_device.category
            }
            """
            device = db.create_new_device(selected_device.prod_id, selected_device.name,
                                          selected_device.brand, selected_device.category)
            db.add_device_to_user(username,device)
            create_home_page(username)

    add_device_btn = wx.Button(main_dialog,label="Add selected device",pos=[360,150])
    add_device_btn.Bind(wx.EVT_BUTTON, on_add_device_to_user)
    
    display_app_name()

    main_dialog.Show()

def create_device_page():
    destroy_everything()



#https://discuss.wxpython.org/t/getchildren/27335
def setFocusOnFirstChild():
	focusableObj = False
	children = main_dialog.GetChildren()
	for i in children:
		if isinstance(i, (wx.Button, wx.CheckBox, wx.TextCtrl,)):
			focusableObj = True
			break
	if focusableObj:
		i.SetFocus()
        
def destroy_everything():
    for child in main_dialog.GetChildren():
        child.Destroy()
    wx.CallLater(500, setFocusOnFirstChild)

create_login_page()
main_dialog.Show()
app.MainLoop()
