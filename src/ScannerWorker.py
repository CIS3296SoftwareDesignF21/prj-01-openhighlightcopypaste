try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract
import cv2

class ScannerWorker:
    def __init__(self, path) -> None:
        self.path_to_image = path

    def basicOCR(self):
        return pytesseract.image_to_string(Image.open(self.path_to_image))

    #TODO - get this to open a new image with boundary drawn onto the image
    def genBoundaryBoxes(self):
        return pytesseract.image_to_boxes(Image.open(self.path_to_image))

    def genRedBox(self):
        pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'  # run which tesseract in cmd prompt
        img = cv2.imread('../data/txt1.png')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # print(pytesseract.image_to_string(img)) # pyT library func

        # Detecting Characters
        hImg, wImg, a = img.shape  # a resolve ValueError
        boxes = pytesseract.image_to_boxes(img)  # pyT library func
        # pytesseract.image_to_boxes(img) gave Pt. x, y, width, height
        for letter in boxes.splitlines():
            # print(b)
            letter = letter.split(' ')
            #print(letter)
            x, y, w, h = int(letter[1]), int(letter[2]), int(letter[3]), int(letter[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 2)  # var, colors, thickness

        cv2.imshow('Result', img)
        cv2.waitKey(0)

