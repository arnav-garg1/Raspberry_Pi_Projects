from gpiozero import LED
from time import sleep

red = LED(9)
yellow = LED(10)
green = LED(11)
myled = LED(17)
myled2 = LED(13)

while True:
    myled.on()
    red.on()
    sleep(0.5)
    red.off()
    yellow.on()
    sleep(0.5)
    yellow.off()
    green.on()
    sleep(0.5)
    green.off()
    myled2.off()
    myled.off()
    myled2.on()
