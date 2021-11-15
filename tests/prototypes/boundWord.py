import pytesseract
from pytesseract import Output
import cv2
from PIL import Image
img = cv2.imread('../../data/txt1.png')


d = pytesseract.image_to_data(img, output_type=Output.DICT)
print(d)
n_boxes = len(d['level'])
for i in range(n_boxes):
    if(d['conf'][i]!="-1"):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('img', img)
cv2.waitKey(0)
