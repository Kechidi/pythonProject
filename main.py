import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()



cv2.imwrite("image3.png", frame_read.frame)

tello.land()

