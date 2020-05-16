import threading
import cv2
from PIL import ImageTk, Image


class VideoStreamThread(threading.Thread):
    def __init__(self, lmain):
        threading.Thread.__init__(self)
        self.STREAM_HOST = 'http://192.168.1.39:8081/'
        self.stream = cv2.VideoCapture(self.STREAM_HOST)
        self.lmain = lmain
        if cv2.waitKey(1) == 27: exit(0)



    def run(self):
        returnValue, frame = self.stream.read()
        if returnValue: 
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.lmain.imgtk = imgtk
            self.lmain.configure(image=imgtk)
            self.lmain.after(1, self.run) 
