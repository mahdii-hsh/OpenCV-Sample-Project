from processes import Process
import cv2 as cv
class VideoProcess(Process) :
    __capture = None #private capture - not changable

    def __init__(self,capture):
        super().__init__()
        self.__capture = capture

    def getCapture(self) :
        return self.__capture
    
    # this function for show main video (without a process)
    def vidShowMain(self) :
        while True : 
            isTrue ,frame = self.capture.read()
            cv.imshow('Gray Video', self.imgRGBCvtGray(frame))
            
            # Press 'q' to exit
            if cv.waitKey(1) == ord('q'):
                self.capture.release()
                cv.destroyAllWindows()
                return
            
    # this function for convert main video to gray video
    def vidRGBCvtGray(self,capture):
        while True : 
            isTrue ,frame = capture.read()
            cv.imshow('Gray Video', self.imgRGBCvtGray(frame))
            
            # Press 'q' to exit
            if cv.waitKey(1) == ord('q'):
                capture.release()
                cv.destroyAllWindows()
                return
            
    # this function for convert main video to blackwhite video
    def vidRGBCvtBlackWhite(self,capture):
        # super().vidCvtGray()
        capture = self.getCapture()
        while True : 
            isTrue ,frame = capture.read()
            cv.imshow('Gray Video', self.imgRGBCvtBlackWhite(frame))
            
            # Press 'q' to exit
            if cv.waitKey(20) == ord('q'):
                capture.release()
                cv.destroyAllWindows()
                return