from picamera import PiCamera
from gpiozero import Button

camera = PiCamera()
button = Button(17)

camera.start_preview(alpha=255)
camera.framerate = 24
camera.start_recording('/home/pi/myvideo.h264')
camera.wait_recording(5)
camera.stop_recording()
camera.stop_preview()
