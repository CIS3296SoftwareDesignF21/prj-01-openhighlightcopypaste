try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import cv2
import IMG
import os

class ScannerWorker:
    def __init__(self, image: IMG):
        self.image = image

        #initialize tesseract binary location whenever we spawn a scanner worker
        #point class towards tesseract binary
        dirname = os.path.dirname(__file__)

        #name of the place where the tessearct binary is found

        filenameBin = os.path.join(dirname, '../lib/tesseract/macBuild/tesseract')
        #name of the directory where the language data is found
        filenameData = os.path.join(dirname, "../lib/tesseract/tessdata/")

        os.environ["TESSDATA_PREFIX"] = filenameData
        pytesseract.pytesseract.tesseract_cmd = filenameBin

    def basicOCR(self):
        return pytesseract.image_to_string(Image.open(self.image.getFilePath()))

    #TODO - get this to open a new image with boundary drawn onto the image
    def genBoundaryBoxes(self):
        return pytesseract.image_to_boxes(Image.open(self.image.getFilePath()))

    def genWordBox(self):
        img = self.image.getOpenCVptr()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        d = pytesseract.image_to_data(img,output_type=Output.DICT)
        print(d.keys())
        n_boxes = len(d['text'])

        for i in range(n_boxes):
            if int(float(d['conf'][i])) > 60:
                boundary = [d['left'][i],d['top'][i], d['width'][i],d['height'][i]]
                word = d['text'][i]
                self.image.appendBoundaryDict(word, boundary)
                #(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i],d['height'][i])
                #img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)  # var, colors, thickness

        cv2.imshow('', img)
        cv2.waitKey(0)
        print(self.image.getBoundaryDict())
