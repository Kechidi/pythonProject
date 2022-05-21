import socket
import time
import cv2
from djitellopy import Tello


tello_ip = '192.168.10.1'
tello_port = 8889
tello_address = (tello_ip, tello_port)


tello = Tello()
tello.connect()
tello.takeoff()
socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)

socket.sendto ('command'.encode (' utf-8 '), tello_address)
socket.sendto ('streamon'.encode (' utf-8 '), tello_address)
print ("Start streaming")


cap = cv2.VideoCapture('udp://0.0.0.0:11111')

# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

if not cap.isOpened():
    cap.open('udp:/0.0.0.0:11111')

while True:
    _, img = cap.read()

    # detect and decode
    data, bbox, _ = detector.detectAndDecode(img)

    # check if there is a QRCode in the image
    if bbox is not None:
        # display the image with lines
        for i in range(len(bbox)):
            # Window name in which image is displayed
            window_name = 'Image'

            # Start coordinate, here (225, 0)
            # represents the top right corner of image
            start_point = (225, 0)

            # End coordinate, here (0, 225)
            # represents the bottom left corner of image
            end_point = (0, 225)

            # Black color in BGR
            color = (0, 0, 0)

            # Line thickness of 5 px
            thickness = 5

            # Using cv2.line() method
            # Draw a diagonal black line with thickness of 5 px
            image = cv2.line(img, start_point, end_point, color, thickness)

        if data:
            print("QR Code detected, data:", data)

    # display the result
    cv2.imshow("QRCODE", img)

    if cv2.waitKey(1) == ord("q"):
        break



cap.release ()

def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)



socket.sendto ('streamoff'.encode (' utf-8 '), tello_address)
