
from tkinter import *
import numpy as np
import time
import socket
import cv2
from PIL import ImageTk, Image
from VideoStreamThread import *
from App import App



# ------------------------------------

WINDOWS_HOST = "192.168.1.107"
STREAM_HOST = 'http://192.168.1.33:8081/'
RASPBERRY_PORT = 5000
BAUD_RATE = 9600

app = App()


mySocket = socket.socket(socket.AF_INET, #for ipv4 communiciation
                                socket.SOCK_STREAM # TCP Protocol
                                )
mySocket.bind((WINDOWS_HOST, RASPBERRY_PORT))

mySocket.listen(1)
print("Listening...")
connection, address = mySocket.accept()
print ("Connection from: " + str(address))


app.initVideoStream()


while 1:
    data = connection.recv(BAUD_RATE).decode()
    if not data: break
    
    print ("From raspberry pi: " + str(data))
    

connection.close()

# ----------------------------------
