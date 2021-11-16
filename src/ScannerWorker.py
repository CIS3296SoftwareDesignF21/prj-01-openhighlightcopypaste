try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import numpy as np
import cv2
import IMG

class ScannerWorker:
    def __init__(self, image: IMG) -> None:
        self.image = image

    def basicOCR(self):
        return pytesseract.image_to_string(Image.open(self.image.getFilePath()))

    def genBoundaryBoxes(self):
        return pytesseract.image_to_boxes(Image.open(self.image.getFilePath()))

    def genWordBox(self):
        img = self.image.getOpenCVptr()
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # Extract the V channel
        out_img = img_hsv[:, :, 2]

        d = pytesseract.image_to_data(out_img, output_type=Output.DICT)
        n_boxes = len(d['text'])

        for i in range(n_boxes):
            if int(float(d['conf'][i])) > 60:
                boundary = (d['left'][i],d['top'][i], d['width'][i],d['height'][i])
                word = d['text'][i]
                self.image.appendBoundaryList(word, boundary)
        print(self.image.getBoundaryList())

    def checkHighlightAmount(self, item: tuple):
        img = self.image.getOpenCVptr()
        boundary = item[1]
        cropped = img[boundary[1]:(boundary[3]+boundary[1]), boundary[0]:(boundary[2]+boundary[0])]

        lowerValues = np.array([0,100,100])
        upperValues = np.array([170,255,255])
        hsvImage = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
        hsvMask = cv2.inRange(hsvImage, lowerValues, upperValues)

        ratio = cv2.countNonZero(hsvMask) / (cropped.size / 3)
        return(np.round(ratio * 100, 2))

        
    def getOutput(self):
        for i in self.image.getBoundaryList():
            if (self.checkHighlightAmount(i) >= 50.0):
                print(i[0])
                self.image.appendTextList(i[0])
        print(self.image.getTextList())

    