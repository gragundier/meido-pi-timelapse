from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from picamera import PiCamera
from time import sleep
#from PIL import Image
from random import randint

import numpy as np
import RPi.GPIO as GPIO


import time
import argparse

parser = argparse.ArgumentParser()
#parser.add_argument("--zoom", type=int,default=100, help="how much to zoom by percentage")
parser.add_argument("--interval", type=int, default=15, help="Number of seconds between each photo")
parser.add_argument("--total_number_of_photos", type=int, default=3000, help="Total number of photos to take")
parser.add_argument("--resolution_x", type=int, default=1920, help="pixel resolution of width")
parser.add_argument("--resolution_y", type=int, default=1080, help="pixel resolution of height")
parser.add_argument("--rotation", type=int, default=0, help="rotation by degrees")
args = parser.parse_args()

#setup camera
camera = PiCamera()

camera.resolution = (args.resolution_x, args.resolution_y)

camera.led = False
camera.rotation = args.rotation

file_name = "/home/pi/Github/meido-pi-timelapse"

try:
	camera.start_preview(fullscreen = True)
	sleep(2)
	for photo_count in range(args.total_number_of_photos):
		camera.capture("{}/capture_{}.jpg".format(file_name, photo_count))
		sleep(args.interval)
	

except KeyboardInterrupt:
    print("Keyboard Exit...")
finally:
	camera.stop_preview()