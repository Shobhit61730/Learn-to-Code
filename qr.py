!pip install qrcode

import qrcode as qr
img=qr.make("https://www.instagram.com/__abhisek__roy__/?hl=en")
img.save("abhisek_roy_instragram.png")
