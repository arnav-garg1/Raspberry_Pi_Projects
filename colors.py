import explorerhat
from time import sleep

explorerhat.motor.one.forward(25)
sleep(5)
explorerhat.light.blink()
explorer.motor.one.stop()
if (explorerhat.touch.pressed() and channel == 1):
    explorerhat.motor.one.forward(25)
else:
    explorerhat.motor.one.stop()
