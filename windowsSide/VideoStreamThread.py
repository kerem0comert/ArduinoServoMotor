import threading
from cv2 import cv2
from PIL import ImageTk, Image


class VideoStreamThread(threading.Thread):
    def __init__(self, lmain, STREAM_HOST):
        threading.Thread.__init__(self)
        self.stream = cv2.VideoCapture(STREAM_HOST)
        self.lmain = lmain
        if cv2.waitKey(1) == 27: exit(0)

    def run(self):
        print("i am running")
        returnValue, frame = self.stream.read()
        if returnValue: 
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1000, self.run) 
