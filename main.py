from imageProcess import ImageProcess 
from videoProcess import VideoProcess
import cv2 as cv
from fileHandler import FileHandler

image = None #for save pixels of the image
fileHandler = FileHandler()
imgProcess = None
vidProcess = None

while True : 

    imageMode = input("Using images of : 1-Saved 2-Camera")
    match(imageMode) : 
        case "1":
            urlMode = input("Reading image with absolute or relative url : Absolute(a) or Relative(r)?")
            if urlMode == 'a' : 
                absoluteUrl = input("Please enter name absolute url")
                image = fileHandler.readSavedImage(isUrlAbsolute=True,absUrl=absoluteUrl)
            else :
                relativeMode = input("Do you want specific image or default ? Specific(s) or Default(d)?")
                if relativeMode == 's' : 
                    relativeImgName = input("Please enter name of image(with format)")
                    image = fileHandler.readSavedImage(isUrlAbsolute=False,realativeImgName=relativeImgName)
                else :
                    image = fileHandler.readSavedImage()
            break
        case "2":
            image = fileHandler.readCamImage(isDefault=True) #default is your camera of laptop
            isSave = input("Do you want to saving image of camera? Yes(y) or No(n)?")
            if isSave == 'y' : 
                nameSaveImg = input("Please enter name of image(with format)")
                fileHandler.saveImage(image=image,imgName=nameSaveImg)
            break
        
cv.imshow('image',image)
cv.waitKeyEx()
imgProcess = ImageProcess(image)

processId = input('Do you like show a process in your image ?\n1-Convert to blackwhite\n2-Convert to gray')
match (processId) :
    case "1" :
        processImg = imgProcess.imgCvtBlackWhite()
    case _ :
        processImg = image

cv.imshow('Process image',processImg)
cv.waitKeyEx()
cv.destroyAllWindows()
