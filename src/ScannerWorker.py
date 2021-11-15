try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract
from pytesseract import Output
import cv2

class ScannerWorker:
    def __init__(self, path) -> None:
        self.path_to_image = path

    def basicOCR(self):
        return pytesseract.image_to_string(Image.open(self.path_to_image))

    #TODO - get this to open a new image with boundary drawn onto the image
    def genBoundaryBoxes(self):
        return pytesseract.image_to_boxes(Image.open(self.path_to_image))

    def genRedBox1(self):
        img = cv2.imread('../data/txt1.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        d = pytesseract.image_to_data(img,output_type=Output.DICT)
        print(d.keys())
        n_boxes = len(d['text'])

        for i in range(n_boxes):
            if int(float(d['conf'][i])) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i],d['height'][i])
                img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)  # var, colors, thickness

        cv2.imshow('', img)
        cv2.waitKey(0)
