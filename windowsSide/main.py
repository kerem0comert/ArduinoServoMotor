
from socket import socket
from Socket import Socket
from tkinter import Tk, Frame, Label, Button, HORIZONTAL, VERTICAL, Scale
from VideoStreamThread import VideoStreamThread
from numpy import interp
import threading
from time import sleep
from Joystick import Joystick

class PositionSlider(Scale):
    def __init__(self, dataType, connection: socket, master=None, **kwargs):
        # default constructor of tkinter slider
        Scale.__init__(self, master, **kwargs)
        self.dataType = dataType
        self.bind("<ButtonRelease-1>", self.updateValue)
        self.connection = connection
        self.set(0)
    
    def printAngle(self): print("Angle = ", self.get(), " ", self.dataType)

    def updateValue(self, event):
        self.printAngle()
        sendData(self.get(), self.dataType)

    def decrement(self):
        self.set(self.get() - 1)
        self.printAngle()
    
    def increment(self):
        self.set(self.get() + 1)
        self.printAngle()
        
    def powerDown(self):
        self.set(self.get() - 1)
        self.printAngle()
        
    def keyReleased(self): 
        sendData(self.get(), self.dataType)

class App:
    def __init__(self, connection: socket = None):
        self.canvas = "800x800"
        self.labelFont = ('times', 20, 'bold')
        self.buttonFont = ('times', 10, 'bold')
        self.root = Tk()
        self.root.geometry(self.canvas)
        self.root.grid()
        self.root.rowconfigure(2, minsize=30)
        self.root.columnconfigure(2, minsize=30)
        self.root.focus_set()
        self.connection = connection


    def initVideoStream(self, STREAM_HOST):
        # Create a label in the frame
        self.lmain = Label(self.app)
        self.lmain.grid(row=0, column=1)
        self.videoStream = VideoStreamThread(self.lmain, STREAM_HOST)
        self.videoStream.start()
        
    def initGuiElements(self):
        self.bMainMenu = Button(self.root, text="Main Menu")
        self.bMainMenu.grid(row=0, column=0)
        
        self.bSecondPage = Button(self.root, text="Second Page")
        self.bSecondPage.grid(row=0, column=1)
        
        self.bThirdPage = Button(self.root, text="Third Page")
        self.bThirdPage.grid(row=0, column=2)
        
        self.bFourthPage = Button(self.root, text="Fourth Page")
        self.bFourthPage.grid(row=0, column=3)
        
        self.sliderTilt = PositionSlider('t', self.root, 
                                    from_=-90, to=90, tickinterval=20,
                                   orient=HORIZONTAL, troughcolor='grey', length=200)
        self.sliderTilt.grid(row=1, column=0)

        self.sliderPan = PositionSlider('p', self.root, 
                                    from_=90, to=-30, tickinterval=5,
                                    orient=VERTICAL, troughcolor='grey', length=200, showvalue=0)  
        self.sliderPan.grid(row=1, column=1)

        self.sliderPower = PositionSlider('w', self.root, 
                                    from_=100, to=-100, tickinterval=20,
                                    orient=VERTICAL, troughcolor='green', length=200, showvalue=0)  
        self.sliderPower.grid(row=1, column=2)

        self.lblPotent = Label(self.root, text="PotentValue: ") 
        self.lblPotent.grid(row=2,column=0)

        """buttonReset = Button(root, text='Reset To Origin',
                            command=self.resetSlider, bg='red', fg='#fff')
        buttonReset.config(font=buttonFont)
        buttonReset.grid(row=3, column=0)"""

        self.root.bind("<Left>", self.sliderTilt.decrement)
        self.root.bind("<Right>", self.sliderTilt.increment)
        self.root.bind("<Up>", self.sliderPan.increment)
        self.root.bind("<Down>", self.sliderPan.decrement)
        self.root.bind("<W>", self.sliderPower.increment)
        self.root.bind("<S>", self.sliderPower.decrement)
        self.root.bind('<KeyRelease-Left>',self.sliderTilt.keyReleased)
        self.root.bind('<KeyRelease-Right>',self.sliderTilt.keyReleased)
        self.root.bind('<KeyRelease-Up>',self.sliderPan.keyReleased)
        self.root.bind('<KeyRelease-Down>',self.sliderPan.keyReleased)
        self.root.bind("<KeyRelease-W>", self.sliderPower.keyReleased)
        self.root.bind("<KeyRelease-S>", self.sliderPower.keyReleased)
    
    def initJoystick(self):
        self.j = Joystick(app.sliderPan, app.sliderTilt, app.sliderPower)
        self.j.start()


WINDOWS_HOST = "192.168.1.41"
STREAM_HOST = 'http://192.168.1.46:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600


def sendData(data, dataType, ):
    if dataType == 't': data = int(interp(data, [-90,90], [180,0]))
    elif dataType == 'p': data = int(interp(data, [-30,90], [120,0]))
    else: 
        if data < 0: dataType = 's' #in the case of 'w' datatype, a negative value will indicate 's' for backwards
        data =  int(interp(abs(data), [0,100], [40,255]))

    #make sure data has 3 digits
    if(data < 10): data = "00" + str(data)
    elif(data < 100): data = "0" + str(data)
    else:  data = str(data)
    
    toSend = str(data) + str(dataType)
    print(toSend)
    connection.send((toSend).encode('utf-8'))








#socketInstance = Socket(WINDOWS_HOST, RASPBERRY_PORT)

print("Listening...")
#connection, address = socketInstance.startListening()
#print (f"Connection from: {str(address)}")
app = App()
#app.initVideoStream(STREAM_HOST)

while 1:
    app.initGuiElements()
    """app.initJoystick()
    data = connection.recv(BAUD_RATE).decode()
    if not data: break 
    print(f"From raspberry pi: {str(data)}")"""
    app.root.mainloop()
#connection.close()


