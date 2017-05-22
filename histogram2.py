import cv2
import numpy as np
from matplotlib import pyplot as plt

gray_img = cv2.imread('sepatu.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Sepatu', gray_img)
hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])

plt.hist(gray_img.ravel(),256,[0,256])
plt.title('Histogram dari Gambar')
plt.show()

while True:
     k = cv2.waitKey(0) & 0xFF
     if k == 27 : break           # tombol ESC untuk keluar
cv2.destroyAllWindows()