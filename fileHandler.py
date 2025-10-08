import cv2 as cv
from pathlib import Path
import os
class FileHandler :

    mode = None
    __file = None

    def __init__(self,mode):
        self.mode = mode
        self.__file = self.__userQuestions() 
    
    def getFile(self) :
        return self.__file
    
    def readSavedImage(self,isUrlAbsolute=False,absUrl=None,realativeImgName='cats.jpg') :
        """
        isUrlAbsolute -> True : for get image with absolute path
        absUrl -> absolute path
        relativeImgName -> not None : for get image with relative path
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

    def readSavedVideo(self,isUrlAbsolute=False,absUrl=None,realativeVidName='dog.mp4') :
        """
        isUrlAbsolute -> True : for get video with absolute path
        absUrl -> absolute path
        realativeVidName -> not None : for get image with relative path
        """
        if not isUrlAbsolute :
            try : 
                dirPath = Path(__file__).parent
                vidPath = os.path.join(dirPath,'vid',realativeVidName)
                capture = cv.VideoCapture(vidPath)
                if not capture.isOpened():
                    print(f"Error: Could not open video file {vidPath}")
                    return None
                return capture

            except :
                print("Error in reading the relative saved video!!")

        else :
            try : 
                capture = cv.VideoCapture(absUrl)
                return capture

            except :
                print("Error in reading the absolute saved video!!")


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
                cv.destroyAllWindows()
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
    
    def __userQuestions(self) :
        while True : 
            strMode = "video" if self.mode=="Video" else "image"
            imageMode = "1" if self.mode=="Video" else input(f"Using {strMode}s of : 1-Saved 2-Camera")
            match(imageMode) : 
                case "1":
                    urlMode = input(f"Reading {strMode} with absolute or relative url : Absolute(a) or Relative(r)?")
                    if urlMode == 'a' : 
                        absoluteUrl = input("Please enter absolute url")
                        if self.mode =="Video" :
                            return self.readSavedVideo(isUrlAbsolute=True,absUrl=absoluteUrl)
                        else :
                            return self.readSavedImage(isUrlAbsolute=True,absUrl=absoluteUrl)
                    else :
                        relativeMode = input(f"Do you want specific {strMode} or default ? Specific(s) or Default(d)?")
                        if relativeMode == 's' : 
                            relativeName = input(f"Please enter name of {strMode}(with format)")
                            if self.mode =="Video" :
                                return self.readSavedVideo(isUrlAbsolute=False,realativeVidName=relativeName)
                            else :
                                return self.readSavedImage(isUrlAbsolute=False,realativeImgName=relativeName)

                        else :
                            if self.mode =="Video" :
                                return self.readSavedVideo()
                            else :
                                return self.readSavedImage()

                case "2":
                    image = self.readCamImage(isDefault=True) #default is your camera of laptop
                    isSave = input("Do you want to saving image of camera? Yes(y) or No(n)?")
                    if isSave == 'y' : 
                        nameSaveImg = input("Please enter name of image(with format)")
                        self.saveImage(image=image,imgName=nameSaveImg)
                    return image
                   