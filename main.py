import tkinter as tk

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


#Function for what is displayed when search is complete
def search_for_devices():
    devices = ''
    for device in smart_devices:
        devices += device + '\n'

    completed_search.config(text=devices)



#Initializing window
root = tk.Tk()
#Setting window size
root.geometry('600x400')

#Label above the "search for devices" button
search_label = tk.Label(root, text='Search for devices on your network')
#Adds padding
search_label.pack(pady=20)

#Adds button that executes function above
button = tk.Button(root, text="Search", command=search_for_devices)
button.pack()

#Creating empty label for devices
completed_search = tk.Label(root, text='')
completed_search.pack(pady=20)


root.mainloop()