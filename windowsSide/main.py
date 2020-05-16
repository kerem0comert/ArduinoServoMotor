
from tkinter import *
import numpy as np
import time
import socket
import cv2
from PIL import ImageTk, Image
from VideoStreamThread import *


class OrientationSlider(Scale):
    def __init__(self, tp, master=None, **kwargs):
        # default constructor of tkinter slider
        Scale.__init__(self, master, **kwargs)
        self.tp = tp
        self.bind("<ButtonRelease-1>", self.updateValue)

    def updateValue(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        #sendData(self.get(), self.tp)

    def moveLeft(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        self.set(self.get() + 1)
        #sendData(self.get() - 1, self.tp)
    def moveRight(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        self.set(self.get() - 1)
        #sendData(self.get() - 1, self.tp)
    def moveUp(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        self.set(self.get() - 1)
        #sendData(self.get() - 1, self.tp)
    def moveDown(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        self.set(self.get() + 1)
        #sendData(self.get() - 1, self.tp)
    def keyReleased(self, event): sendData(self.get(), self.tp)
    



def ResetSlider():
    sliderTilt.set(0)
    sliderPan.set(0)
    print("T: ", sliderTilt.get(), ",P: ", sliderPan.get())
    #sendData(sliderTilt.get(), sliderPan.get())


def sendData(data, datatp):
    data = data if data > 90 else data + 90
    if(data < 10):
        data = "00" + str(data)
    elif(data < 100):
        data = "0" + str(data)
    else:
        data = str(data)
    toSend = data + 't'  if datatp == 't' else data + 'p'
    print(toSend)
    #connection.send(repr(toSend).encode('utf-8'))"""

# ------------------------------------

WINDOWS_HOST = "localhost"
STREAM_HOST = 'http://192.168.1.39:8081/'
RASPBERRY_PORT = 5000
BIT_RATE = 9600
canvas = "800x800"
labelFont = ('times', 20, 'bold')
buttonFont = ('times', 10, 'bold')


root = Tk()
root.geometry(canvas)

# Create a frame
app = Frame(root, bg="white")
app.grid()
app.focus_set()


# Create a label in the frame
lmain = Label(app)
lmain.grid(row=0, column=0)


"""mySocket = socket.socket()
mySocket.bind((WINDOWS_HOST, RASPBERRY_PORT))
mySocket.listen(1)
print("Listening...")
connection, address = mySocket.accept()
print ("Connection from: " + str(address))"""


while 1:
    #data = connection.recv(BIT_RATE).decode()
    # if not data:
    #    break
    #print ("From raspberry pi: " + str(data))
    sliderTilt = OrientationSlider('t', root, from_=90, to=-90, tickinterval=20,
                                   orient=HORIZONTAL, troughcolor='grey', length=200)  # creates widget
    sliderTilt.grid(row=1, column=1)
    sliderTilt.set(0)

    x = IntVar()
    sliderPan = OrientationSlider('p', root, from_=-90, to=90, tickinterval=20,
                                  orient=VERTICAL, troughcolor='grey', length=200, showvalue=0,
                                  variable=x)  # creates widget
    sliderPan.grid(row=1, column=1)
    sliderPan.set(0)
    buttonReset = Button(root, text='Reset To Origin',
                         command=ResetSlider, bg='red', fg='#fff')
    buttonReset.config(font=buttonFont)
    buttonReset.grid(row=3, column=1)

    #videoStream = VideoStreamThread(lmain)
    # videoStream.start()
    root.bind("<Left>", sliderTilt.moveLeft)
    root.bind("<Right>", sliderTilt.moveRight)
    root.bind("<Up>", sliderPan.moveUp)
    root.bind("<Down>", sliderPan.moveDown)
    root.bind('<KeyRelease-Left>',sliderTilt.keyReleased)
    root.bind('<KeyRelease-Right>',sliderTilt.keyReleased)
    root.bind('<KeyRelease-Up>',sliderPan.keyReleased)
    root.bind('<KeyRelease-Down>',sliderPan.keyReleased)
    root.mainloop()

# connection.close()

# ----------------------------------
