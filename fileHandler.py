import cv2 as cv
from pathlib import Path
import os
class FileHandler : 
    
    def readSavedImage(self,isUrlAbsolute=False,absUrl=None,realativeImgName='cats.jpg') :
        """
        isUrlAbsolute -> True : for get image with absolute path
        absUrl -> absolute path
        relativeImgName -> not None : for get image with relative path
            relativeImgName[0] -> name of image
            relativeImgName[1] -> format of image
        """
        if not isUrlAbsolute :
            try : 
                dirPath = Path(__file__).parent
                imgPath = os.path.join(dirPath,'img',realativeImgName)
                return cv.imread(imgPath)
            except :
                print("Error in reading the relative saved image!!")

        else :
            try : 
                return cv.imread(absUrl)
            except :
                print("Error in reading the absolute saved image!!")

    # read image from camera 
    def readCamImage(self,isDefault=True) :
        """
        isDefault -> True : for show camera of your laptop
        """

        if isDefault :
            capture = cv.VideoCapture(0)
            if not capture.isOpened() : 
                print("Error : camera not opened!")
        else : 
            for i in range(1,3) : 
                capture = cv.VideoCapture(i)
                print(f"camera index : {i}")

        
        while True : 
            isTrue ,frame = capture.read()

            cv.imshow('Laptop Camera', frame)
            
            # Press 'q' to exit
            if cv.waitKey(1) == ord('q'):
                return frame
            
    #for saving an image
    def saveImage(self,image,imgName) :
        dirPath = Path(__file__).parent
        imgPath = os.path.join(dirPath,'img','cam',imgName)
        try :
            cv.imwrite(imgPath,image)
        except : 
            print("Error in saving image")
        return


            
