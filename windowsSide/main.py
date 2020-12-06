
from tkinter import *
import numpy as np
import time
import socket
import cv2
from PIL import ImageTk, Image
from VideoStreamThread import *


class PositionSlider(Scale):
    def __init__(self, tp, master=None, **kwargs):
        # default constructor of tkinter slider
        Scale.__init__(self, master, **kwargs)
        self.tp = tp
        self.bind("<ButtonRelease-1>", self.updateValue)

    def updateValue(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        sendData(self.get(), self.tp)

    def moveLeft(self, event):
        self.set(self.get() + 1)
        print("Angle = ", self.get(), " ", self.tp)
    
    def moveRight(self, event):
        self.set(self.get() - 1)
        print("Angle = ", self.get(), " ", self.tp)
        
    def moveUp(self, event):
        self.set(self.get() - 1)
        print("Angle = ", self.get(), " ", self.tp)
        
    def moveDown(self, event):
        self.set(self.get() + 1)
        print("Angle = ", self.get(), " ", self.tp)
    
    def powerUp(self, event):
        self.set(self.get() + 1)
        print("Power = ", self.get(), " ", self.tp)

    def powerDown(self, event):
        self.set(self.get() - 1)
        print("Power = ", self.get(), " ", self.tp)
        
    def keyReleased(self, event): sendData(self.get(), self.tp)
    



def ResetSlider():
    sliderTilt.set(0)
    sliderPan.set(0)
    print(f"T:{sliderTilt.get()} P:{sliderPan.get()} W:{sliderPower.get()}")
    sendData(sliderTilt.get(), sliderPan.get())


def sendData(data, datatp):
    if datatp != 'w': data = data if data > 90 else data + 90
    if(data < 10): data = "00" + str(data)
    elif(data < 100): data = "0" + str(data)
    else:  data = str(data)
    #print("data=", type(data), "datatp=", type(datatp))
    toSend = str(data) + str(datatp)
    print(toSend)
    toSend = str(toSend)
    connection.send(repr(toSend).encode('utf-8'))

# ------------------------------------

WINDOWS_HOST = "192.168.1.107"
STREAM_HOST = 'http://192.168.1.34:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600
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


mySocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
mySocket.bind((WINDOWS_HOST, RASPBERRY_PORT))

mySocket.listen(1)
print("Listening...")
connection, address = mySocket.accept()
print ("Connection from: " + str(address))

videoStream = VideoStreamThread(lmain)
videoStream.start()
while 1:
    data = connection.recv(BAUD_RATE).decode()
    if not data: break
    
    print ("From raspberry pi: " + str(data))
    sliderTilt = PositionSlider('t', root, from_=90, to=-90, tickinterval=20,
                                   orient=HORIZONTAL, troughcolor='grey', length=200)
    sliderTilt.grid(row=1, column=0)
    sliderTilt.set(0)

    sliderPan = PositionSlider('p', root, from_=-90, to=90, tickinterval=20,
                                  orient=VERTICAL, troughcolor='grey', length=200, showvalue=0)  
    sliderPan.grid(row=1, column=0)
    sliderPan.set(0)

    sliderPower = PositionSlider('w', root, from_=255, to=0, tickinterval=20,
                                  orient=VERTICAL, troughcolor='green', length=200, showvalue=0)  
    sliderPower.grid(row=1, column=1)
    sliderPower.set(0)

    buttonReset = Button(root, text='Reset To Origin',
                         command=ResetSlider, bg='red', fg='#fff')
    buttonReset.config(font=buttonFont)
    buttonReset.grid(row=3, column=0)

    
    root.bind("<Left>", sliderTilt.moveLeft)
    root.bind("<Right>", sliderTilt.moveRight)
    root.bind("<Up>", sliderPan.moveUp)
    root.bind("<Down>", sliderPan.moveDown)
    root.bind("<W>", sliderPower.powerUp)
    root.bind("<S>", sliderPower.powerDown)
    root.bind('<KeyRelease-Left>',sliderTilt.keyReleased)
    root.bind('<KeyRelease-Right>',sliderTilt.keyReleased)
    root.bind('<KeyRelease-Up>',sliderPan.keyReleased)
    root.bind('<KeyRelease-Down>',sliderPan.keyReleased)
    root.bind("<KeyRelease-W>", sliderPower.keyReleased)
    root.bind("<KeyRelease-S>", sliderPower.keyReleased)
    root.mainloop()

connection.close()

# ----------------------------------
