from pyzbar.locations import Point, Rect
from pyzbar.pyzbar import decode, Decoded
from PIL import Image

decode(Image.open('qrcode1.png'))
