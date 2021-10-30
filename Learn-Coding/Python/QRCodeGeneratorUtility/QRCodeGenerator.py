# To generate QR Code
import qrcode
#Read QRCode
import cv2

qr_img = qrcode.make("HacktoberFest is an amazing way to learning about open-source.")
qr_img.save("hacktober2021.jpg")
qr_detector = cv2.QRCodeDetector()
text, image_array, data_points = qr_detector.detectAndDecode(cv2.imread("hacktober2021.jpg"))
print("Decoded text:", text)
