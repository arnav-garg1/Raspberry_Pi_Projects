from guizero import App, Text, PushButton, Slider, Picture, ButtonGroup
from gpiozero import LED

red = LED(12)
app = App()

label = Text(app, "Red")
onButton = PushButton(app, command=red.on, text = "on")
offButton = PushButton(app, command=red.off, text="off")
blinkButton = PushButton(app, command = red.blink, text="blink")

def slider_changed(slider_value):
    red.blink(int(slider_value), int(slider_value))
    
speedSlider = Slider(app, command=slider_changed, start = 0.5, end = 5)

def speed_changed():
    if speedButton.value_text == 'slow':
        red.blink(1,1)
    if speedButton.value_text == 'medium':
        red.blink(.3,.3)
    if speedButton.value_text == 'fast':
        red.blink(.1, .1)
        
speedButton = ButtonGroup(app, command=speed_changed, options=['slow', 'medium', 'fast'])
my_cat = Picture(app, image= "/home/pi/Pictures/cat.png")
app.display()