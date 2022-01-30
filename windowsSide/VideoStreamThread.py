import threading
from cv2 import cv2
from PIL import ImageTk, Image
import qimage2ndarray # for a memory leak,see gist


class VideoStreamThread(threading.Thread):
    def __init__(self, graphicsView, STREAM_HOST):
        threading.Thread.__init__(self)
        self.stream = cv2.VideoCapture(STREAM_HOST)
        self.graphicsView = graphicsView
        if cv2.waitKey(1) == 27: exit(0)

    def run(self):
        print("i am running")
        returnValue, frame = self.stream.read()
        if returnValue: 
            image = qimage2ndarray.array2qimage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA))
            self.graphicsView.setPix
            self.lmain.after(3, self.run) 
