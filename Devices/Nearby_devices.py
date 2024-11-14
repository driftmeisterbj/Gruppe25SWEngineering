from Light import Light
from Fridge import Fridge
from Heater import Heater
from Lock import Lock
from Camera import Camera
import random

counter = 0
def id():
    global counter
    counter += 1 
    return counter
    

lights = [
    Light(id(), "Hue White and Color Ambiance", "Philips"),
    Light(id(), "LIFX Color A19", "LIFX"),
    Light(id(), "Wyze Bulb Color", "Wyze"),
    Light(id(), " LED Strip Light", "Govee"),
    Light(id(), "Nanoleaf Shapes", "Nanoleaf"),
    Light(id(), "Cync  LED", "GE Lighting"),
    Light(id(), "Kasa  Bulb", "TP-Link"),
    Light(id(), "Echo Glow", "Amazon"),
    Light(id(), "Sengled  LED", "Sengled"),
    Light(id(), "Yeelight  LED", "Yeelight"),
]

fridges = [
    Fridge(id(), "Family Hub RF28R7551SR", "Samsung"),
    Fridge(id(), "InstaView Door-in-Door", "LG"),
    Fridge(id(), "Profile PFE28KYNFS", "GE"),
    Fridge(id(), "B36CT80SNS", "Bosch"),
    Fridge(id(), "Brilliant Series 36", "Miele"),
    Fridge(id(), "WRF560SEHZ", "Whirlpool"),
    Fridge(id(), "CFE28TP4MW2", "Café"),
    Fridge(id(), "QuadroCool X", "Haier"),
    Fridge(id(), "Counter-Depth Max", "Frigidaire"),
    Fridge(id(), "KMHC319ESS", "KitchenAid"),
]

heaters = [
    Heater(id(), "AM09 Fan Heater", "Dyson"),
    Heater(id(), "HCE840B HeatGenius", "Honeywell"),
    Heater(id(), "Dragon4 TRD40615T", "DeLonghi"),
    Heater(id(), "AVH10 Vortex Heater", "Vornado"),
    Heater(id(), "AW300 Air Logic", "Lasko"),
    Heater(id(), "Comfort Temp", "Rowenta"),
    Heater(id(), "Oscillating Ceramic Heater", "Pelonis"),
    Heater(id(), "Silent System 28", "Mill"),
    Heater(id(), "Compact Propane Heater", "Mr. Heater"),
    Heater(id(), " Ceramic Tower Heater", "Govee"),
]

locks = [
    Lock(id(), "August  Lock Pro + Connect", "August"),
    Lock(id(), "Kwikset Kevo 2nd Gen", "Kwikset"),
    Lock(id(), "Schlage Encode Plus", "Schlage"),
    Lock(id(), "Yale Assure Lock SL", "Yale"),
    Lock(id(), "Level Lock+", "Level"),
    Lock(id(), "Nest x Yale Lock", "Nest"),
    Lock(id(), "Ultraloq U-Bolt Pro", "Ultraloq"),
    Lock(id(), "Eufy Security  Lock", "Eufy"),
    Lock(id(), "SimpliSafe  Lock", "SimpliSafe"),
    Lock(id(), "Lockly Secure Pro", "Lockly"),
]

cameras = [
    Camera(id(), "Nest Cam IQ Outdoor", "Nest", resolution="1080p", motion_detection=True),
    Camera(id(), "Ring Stick Up Cam Elite", "Ring", resolution="1080p", motion_detection=True),
    Camera(id(), "Arlo Pro 4", "Arlo", resolution="4K", motion_detection=True),
    Camera(id(), "Wyze Cam v3", "Wyze", resolution="1080p", motion_detection=False),
    Camera(id(), "Eufy Security SoloCam E40", "Eufy", resolution="1080p", motion_detection=True),
    Camera(id(), "SimpliSafe HD Camera", "SimpliSafe", resolution="1080p", motion_detection=False),
    Camera(id(), "Blink Outdoor Camera", "Blink", resolution="1080p", motion_detection=True),
    Camera(id(), "Ring Spotlight Cam", "Ring", resolution="1080p", motion_detection=True),
    Camera(id(), "Google Nest Cam (battery)", "Nest", resolution="1080p", motion_detection=True),
    Camera(id(), "Lorex 4K Ultra HD IP Camera", "Lorex", resolution="4K", motion_detection=True),
]


#print(heaters[0].name, heaters[0].brand)
