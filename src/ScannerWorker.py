try:
   from PIL import Image #PIL is the pillow 
except ImportError:
    import Image

import pytesseract # only accepts rgb values so convert vals

class ScannerWorker:
       def test(self, path):
              print(pytesseract.image_to_boxes(Image.open(path)))

