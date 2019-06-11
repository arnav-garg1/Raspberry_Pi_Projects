from gpiozero import LED, Button

button = Button(10)
red = LED(12)

button.when_pressed = red.toggle
#button.when_released = red.off