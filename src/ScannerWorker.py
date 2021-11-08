try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract

class ScannerWorker:
    def __init__(self, path) -> None:
        self.path_to_image = path

    def basicOCR(self):
        return pytesseract.image_to_string(Image.open(self.path_to_image))

    #TODO - get this to open a new image with boundary drawn onto the image
    def genBoundaryBoxes(self):
        return pytesseract.image_to_boxes(Image.open(self.path_to_image))

