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

    def updateValue(self, event):
        print("Angle = ", self.get(), " ", self.tp)
        main.sendData(self.get(), self.tp)

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
        
    def keyReleased(self, event): 
        main.sendData(self.get(), self.tp)
  


