from tkinter import Scale

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
    if datatp != 'w': #this is pan tilt data, must do the mapping for 90 degrees
        data = data if data > 90 else data + 90
    #appending zeros until there are 3 digits
    if(data < 10): data = "00" + str(data) 
    elif(data < 100): data = "0" + str(data)

    else:  data = str(data) #w type power data
    toSend = str(data) + str(datatp) #3 digits 
    print(toSend)
    toSend = str(toSend)
    connection.send(repr(toSend).encode('utf-8'))