import cv2
import pytesseract

img = cv2.imread('Wikinews_Breaking_News.png')
text = pytesseract.image_to_string(img)
print(text)
