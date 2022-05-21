# Début du programme
from PIL.Image import *

codeQR = open(
    "qrcode3.png")  # Ouverture de mon image de code QR, téléchargez en une sur votre PC, mettez la d'en votre dossier Python, et remplacer le nom "QRcodeim" par le nom de votre image en format jpeg de préférence
largeur, hauteur = codeQR.size
x = 0
y = 0
a = 0
p = codeQR.getpixel((x, y))  # Méthode de lecture de pixel

for y in range(hauteur):
    for x in range(largeur):
        print(x, y)
        if p == (0, 0, 0):  # Dans le cas où un pixel est noir
            a = a + 1
            print(x, y, a)
            if a >= (((largeur) / 21) * 47):  # Nombre de pixels noirs censé se suivre afin de détecter ce que je veux
                print("ok")
                break
        if p == (255, 255, 255):  # Dans le cas où c'est blanc
            a = 0
            print("bad")
        print(a)

# FinDuProgramme