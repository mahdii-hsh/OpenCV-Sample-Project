import cv2 as cv
import numpy as np
from abc import ABC,abstractmethod
class Process(ABC) : 
    def __init__(self):
        pass
    
    @abstractmethod
    def vidCvtGray(self) : 
        """must impleated with VideoProcess class"""
        pass
    @abstractmethod
    def vidCvtBlackWhite(self) :
        """must impleated with VideoProcess class"""
        pass
    
    # convert rgb image to gray image
    def imgRGBCvtGray(self) : 
        grayImage = self.__image
        grayImage = grayImage[:,:,0]//3+grayImage[:,:,1]//3+grayImage[:,:,2]//3
        return grayImage
    
    # convert rgb image to black & white image
    def imgCvtBlackWhite(self) : 
        grayImage = self.imgRGBCvtGray()
        for i in range(grayImage.shape[0]) : 
            for j in range(grayImage.shape[1]) : 
                grayImage[i,j] = 0 if grayImage[i,j] <128 else 255

        return grayImage
    # convert rgb or gray image convert to dark mode with specific rate
    def convertDark(self,isGray,rate) : 
        darkRGBImage = self.__image
        if not isGray :
            for i in range(darkRGBImage.shape[0]) : 
                for j in range(darkRGBImage.shape[1]) :
                    for k in range(3) : 
                        darkRGBImage[i,j,k] = darkRGBImage[i,j,k] //rate
                        # if darkRGBImage[i,j,k] >255 :
                        #     darkRGBImage[i,j,k] = 255
                        # if darkRGBImage[i,j,k] < 0 :
                        #     darkRGBImage[i,j,k] = 0
            return self.normalizationRate(darkRGBImage,0,255,isGray=isGray)

        else : 
            grayImage = self.imgRGBCvtGray()
            grayDarkImage = grayImage[:,:] * rate
            print('grayDark',grayDarkImage)
            return self.normalizationRate(grayDarkImage,0,255,isGray=isGray)

    #normalize unormal pixels of an image 
    def normalizationRate(self,unormalImage,newMinLim,newMaxLim,isGray) :
        if not isGray :
            i = 0
            for channel in cv.split(unormalImage) :
                minValue = min(min(row) for row in channel)
                maxValue = max(max(row) for row in channel)

                if minValue != maxValue : 
                    unormalImage[:,:,i] = (unormalImage[:,:,i] - minValue) *((newMaxLim-newMinLim)//(maxValue - minValue)) + newMinLim
                i = i+1
        else :
            minValue = min(min(row) for row in unormalImage)
            maxValue = max(max(row) for row in unormalImage)

            if minValue != maxValue : 
                unormalImage[:,:] = (unormalImage[:,:] - minValue) * ((newMaxLim-newMinLim)//(maxValue - minValue)) + newMinLim


        return unormalImage