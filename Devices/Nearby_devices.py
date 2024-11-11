from Light import Light
from Fridge import Fridge
from Heater import Heater
from Lock import SmartLock
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
    Light(id(), "Smart LED Strip Light", "Govee"),
    Light(id(), "Nanoleaf Shapes", "Nanoleaf"),
    Light(id(), "Cync Smart LED", "GE Lighting"),
    Light(id(), "Kasa Smart Bulb", "TP-Link"),
    Light(id(), "Echo Glow", "Amazon"),
    Light(id(), "Sengled Smart LED", "Sengled"),
    Light(id(), "Yeelight Smart LED", "Yeelight"),
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
    Heater(id(), "Smart Ceramic Tower Heater", "Govee"),
]

locks = [
    SmartLock(id(), "August Smart Lock Pro + Connect", "August"),
    SmartLock(id(), "Kwikset Kevo 2nd Gen", "Kwikset"),
    SmartLock(id(), "Schlage Encode Plus", "Schlage"),
    SmartLock(id(), "Yale Assure Lock SL", "Yale"),
    SmartLock(id(), "Level Lock+", "Level"),
    SmartLock(id(), "Nest x Yale Lock", "Nest"),
    SmartLock(id(), "Ultraloq U-Bolt Pro", "Ultraloq"),
    SmartLock(id(), "Eufy Security Smart Lock", "Eufy"),
    SmartLock(id(), "SimpliSafe Smart Lock", "SimpliSafe"),
    SmartLock(id(), "Lockly Secure Pro", "Lockly"),
]

#print(heaters[0].name, heaters[0].brand)
