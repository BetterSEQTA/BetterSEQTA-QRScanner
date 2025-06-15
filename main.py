import cv2 as cv
from pyzbar.pyzbar import decode

img = cv.imread('./images/thumbnail_qrcode.png', cv.IMREAD_GRAYSCALE)

decoded = decode(img)

print(decoded)

cv.imshow('QR Code', img)
cv.waitKey(0)