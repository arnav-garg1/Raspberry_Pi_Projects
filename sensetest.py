from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

red = (255,0,0)
sense.clear(red)
sleep(1)
sense.clear()
sense.show_message('hello')