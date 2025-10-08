import cv2 as cv
import numpy as np
from processes import Process
import time

class ImageProcess(Process):
    __image = "None" #private image - not changable
    
    def __init__(self,image):
        self.__image = image
        super().__init__()

    def getImage(self) : 
        return self.__image    
    
    # compare light pixeles and dark pixels of image
    def imgPixelDitails(self) :
        lightPixel = darkPixel = 0
        grayImg = self.imgRGBCvtGray(image=self.__image)
        for x in range(grayImg.shape[0]) :
            for y in range(grayImg.shape[1]) :
                if grayImg[x,y] < 128 :
                    lightPixel+=1
                else :
                    darkPixel+=1

        print("Processing...")
        time.sleep(2)
        print(f"{"Light image" if lightPixel > darkPixel else "Dark image"} - lightPixel : {lightPixel} - darkPixel : {darkPixel}")
        return 
