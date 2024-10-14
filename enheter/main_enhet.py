from Light import Light

light1 = Light(1234,"Hue", "Phillips")

light1.turn_off_device()
print(light1.category)
light1.set_brightness('fd')

