from processes import Process
class VideoProcess(Process) :
    __capture = None #private capture - not changable

    def __init__(self,capture):
        super().__init__()
        self.__capture = capture

    def getCapture(self) :
        return self.__capture