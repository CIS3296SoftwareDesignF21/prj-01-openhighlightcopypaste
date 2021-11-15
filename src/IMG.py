import cv2

class IMG:
    textList: []
    boundaryDict = {}
    def __init__(self, imageName):
        self.imageName = imageName
        self.openCVptr = cv2.imread(imageName)

    def appendTextList(self, word):
        self.textList.append(word)

    def getTextList(self):
        return self.textList

    def appendBoundaryDict(self, word, boundary):
        self.boundaryDict[word] = boundary

    def getBoundaryDict(self):
        return self.boundaryDict

    def getOpenCVptr(self):
        return self.openCVptr




