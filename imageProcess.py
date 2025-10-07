import cv2 as cv
import numpy as np
from processes import Process

class ImageProcess(Process):
    __image = "None" #private image - not changable
    
    def __init__(self,imageUrl):
        self.__image = cv.imread(imageUrl)
        super().__init__()

    def getImage(self) : 
        return self.__image
    
    def vidCvtGray(self):
        return super().vidCvtGray()
    def vidCvtBlackWhite(self):
        return super().vidCvtBlackWhite()
    
