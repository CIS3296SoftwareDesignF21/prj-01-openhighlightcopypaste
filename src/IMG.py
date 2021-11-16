import cv2

class IMG:
    
    textList = []
    boundaryList = []
    def __init__(self, imageName):
        self.imageName = imageName
        self.openCVptr = cv2.imread(imageName)

    def appendTextList(self, word: str):
        self.textList.append(word)

    def getTextList(self):
        return self.textList

    def appendBoundaryList(self, word: str, boundary: tuple):
        self.boundaryList.append((word, boundary))

    def getBoundaryList(self):
        return self.boundaryList

    def getOpenCVptr(self):
        return self.openCVptr

    def getFilePath(self):
        return self.imageName



