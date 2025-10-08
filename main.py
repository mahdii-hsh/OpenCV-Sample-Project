from imageProcess import ImageProcess 
from videoProcess import VideoProcess
import cv2 as cv
from fileHandler import FileHandler

image = None #for save pixels of the image
imgProcess = None #assing after solving questions
vidProcess = None #assing after solving questions

fileMode = input("Work with Video or Image : 1-Video 2-Image")
fileHandler = FileHandler(mode="Video" if fileMode=="1" else "Image")       
if fileMode =="1" :
    vidProcess = VideoProcess(fileHandler.getFile())
else :
    imgProcess = ImageProcess(fileHandler.getFile())

isExistFile = False if (fileHandler.getFile() is None or (hasattr(fileHandler.getFile(), 'size') and fileHandler.getFile().size == 0)) else True

processId = input(f'Do you like show a process in your {"video" if fileMode=="1" else "image"} ?\n1-Convert to blackwhite\n2-Convert to gray\n3-The main {"video" if fileMode=="1" else "image"}(no process!)\n{"4-Count pixels of image\n" if fileMode=="2" else ""}{"5-Change light of image\n" if fileMode=="2" else ""}{"4-exit" if fileMode=="1" else "6-exit"}\n') if isExistFile else "8" if fileMode=="1" else "6"

while True :
    if fileMode == "1" :
        match (processId) :
            case "1" :
                vidProcess.vidRGBCvtBlackWhite(capture=vidProcess.getCapture())
                break
            case "2" :
                vidProcess.vidRGBCvtGray(capture=vidProcess.getCapture())
                break
            case "3" :
                vidProcess.vidShowMain()
                break
            case "4" :
                print("Thank you!!")
                break
            case _ : 
                pass
    else :
        match (processId) :
            case "1" :
                processImg = imgProcess.imgRGBCvtBlackWhite(image=imgProcess.getImage())
                cv.imshow('Process image',processImg)
                cv.waitKeyEx()
                break
            case "2" :
                processImg = imgProcess.imgRGBCvtGray(image=imgProcess.getImage())
                cv.imshow('Process image',processImg)
                cv.waitKeyEx()
                break
            case "3" :
                processImg = imgProcess.getImage()
                cv.imshow('Process image',processImg)
                cv.waitKeyEx()
                break
            case "4" :
                imgProcess.imgPixelDitails()
                break
            case "5" :
                processImg = imgProcess.imgCvtDarker(image=imgProcess.getImage(),isGray=True,rate=1.4)
                cv.imshow('Process image',processImg)
                cv.waitKeyEx()
                break
            case "6" :
                print("Thank you!!")
                break
            case _ :
                pass

cv.destroyAllWindows()