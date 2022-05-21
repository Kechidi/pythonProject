# Importing libraries
import qrcode
import numpy as np

# Data for which you want to make QR code
# Here we are using the URL of the MakeUseOf website
img = qrcode.make('https://www.google.com/search?q=le+roi+de+la+frite+le+havre+donner+son+avis&client=ubuntu&hs=Kw1&channel=fs&ei=m8V4YoTqHouVxc8PjIG0sAk&oq=le+roi+de+la+frite+le+havre+donner+&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCCEQoAEyBQghEKABMgUIIRCgATIFCCEQoAEyBQghEKABOgcIABBHELADOgUIABCABDoGCAAQFhAeOgIIJkoECEEYAEoECEYYAFCGAVjwGGDaJmgBcAF4AIABmQGIAbAGkgEDNi4ymAEAoAEByAEIwAEB&sclient=gws-wiz&hl=fr#lrd=0x47e02f0415f87365:0x229624ba5ead6c3f,3,,,')
# File name of the QR code Image
# Change it with your desired file name
img.save('qrcode7.png')
