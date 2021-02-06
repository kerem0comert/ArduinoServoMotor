from tkinter import Scale
from socket import socket
import main

class PositionSlider(Scale):
    def __init__(self, tp, connection: socket, master=None, **kwargs):
        # default constructor of tkinter slider
        Scale.__init__(self, master, **kwargs)
        self.tp = tp
        self.bind("<ButtonRelease-1>", self.updateValue)
        self.connection = connection
    
    def printAngle(self): print("Angle = ", self.get(), " ", self.tp)

    def updateValue(self, event):
        self.printAngle()
        sendData(self.get(), self.tp)

    def moveLeft(self, event):
        self.set(self.get() + 1)
        self.printAngle()
    
    def moveRight(self, event):
        self.set(self.get() - 1)
        self.printAngle()
        
    def moveUp(self, event):
        self.set(self.get() - 1)
        self.printAngle()
        
    def moveDown(self, event):
        self.set(self.get() + 1)
        self.printAngle()
    
    def powerUp(self, event):
        self.set(self.get() + 1)
        self.printAngle()

    def powerDown(self, event):
        self.set(self.get() - 1)
        self.printAngle()
        
    def keyReleased(self, event): 
        sendData(self.get(), self.tp)