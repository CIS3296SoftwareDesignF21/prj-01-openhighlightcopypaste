import cv2 # in BGR
import pytesseract # only accepts rgb values so convert vals

pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
img = cv2.imread('txt1.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img)) # pyT library func


# Detecting Characters
hImg,wImg,a  = img.shape # a resolve ValueError
boxes = pytesseract.image_to_boxes(img) # pyTess library func
# pytesseract.image_to_boxes(img) gave Pt. x, y, width, height
for b in boxes.splitlines():
   # print(b)
    b = b.split(' ')
    print(b)
    x,y,w,h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255),2) # var, colors, thickness
   # cv2.putText(img,b[0],(x,hImg-y),cv2.FONT_HERSEY_DUPLEX,1,(50,50,255),2)
   # error for duplex font so check that

cv2.imshow('Result',img)
cv2.waitKey(0)