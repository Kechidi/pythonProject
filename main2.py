
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()

frame_read = tello.get_frame_read()

cv2.imwrite("qrcode3.png", frame_read.frame)

# Name of the QR Code Image file
filename = 'qrcode3.png'
# read the QRCODE image
image = cv2.imread(filename)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()
# detect and decode
data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# if there is a QR code
# print the data
print('QRCode data:')
print(data)

tello.land()