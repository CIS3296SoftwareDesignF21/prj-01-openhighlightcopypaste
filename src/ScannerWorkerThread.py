try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract # only accepts rgb values so convert vals

class ScannerWorkerThread:
       def test(self):
              print(pytesseract.image_to_boxes(Image.open('../data/txt1.png')))

