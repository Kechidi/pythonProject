# Import Library
import cv2
# Name of the QR Code Image file
filename = 'pictureà.png'
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
