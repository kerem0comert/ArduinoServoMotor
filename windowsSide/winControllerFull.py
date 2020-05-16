
from tkinter import *
import numpy as np
import time, socket, cv2
from PIL import ImageTk, Image



class OrientationSlider(Scale):
    def __init__(self, tp, master = None, **kwargs):
        Scale.__init__(self, master, **kwargs) #default constructor of tkinter slider
        self.tp = tp
        self.bind("<ButtonRelease-1>", self.updateValue)   
    
    def updateValue(self, event):
        print("Angle = ",self.get()," ",self.tp)
        sendData(self.get(), self.tp)



def ResetSlider():
    sliderTilt.set(0)
    sliderPan.set(0)
    print("T: ",sliderTilt.get(),",P: ",sliderPan.get())
    sendData(sliderTilt.get(), sliderPan.get())

def sendData(data, datatp):
    data = data if data > 90 else data + 90
    if(data < 10):
        data = "00" + str(data)
    elif(data < 100):
        data = "0" + str(data)
    else:
        data = str(data)
    toSend = data + 't'  if datatp == 't' else data + 'p'
    connection.send(repr(toSend).encode('utf-8'))

def video_stream():
    _, frame = stream.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream) 

#------------------------------------

host = "192.168.1.42"
streamHost = 'http://192.168.1.34:8081/'
port = 5000
bitRate = 9600
canvas = "800x800"
labelFont = ('times', 20, 'bold')
buttonFont = ('times', 10 , 'bold')


root = Tk()
root.geometry(canvas)

# Create a frame
app = Frame(root, bg="white")
app.grid()

# Create a label in the frame
lmain = Label(app)
lmain.grid()


mySocket = socket.socket()
mySocket.bind((host,port))
mySocket.listen(1)

print("Listening...")
connection, address = mySocket.accept()

print ("Connection from: " + str(address))

stream = cv2.VideoCapture(streamHost)

while True:
    data = connection.recv(bitRate).decode()
    if not data:
        break
    print ("From raspberry pi: " + str(data))

    


    if cv2.waitKey(1) == 27:
        exit(0)


    sliderTilt = OrientationSlider('t', root, from_= 90, to=-90, tickinterval = 10, 
                               orient= HORIZONTAL, troughcolor = 'black') # creates widget
    sliderTilt.place(x=200,y=500, height = 100, width = 400)
    sliderTilt.set(0)

    labelLeft = Label(root, text = "Left")
    labelLeft.config(font=labelFont)
    labelLeft.place(x=120,y=510)

    labelRight = Label(root, text = "Right")
    labelRight.config(font=labelFont)
    labelRight.place(x=610,y=510)

    sliderPan = OrientationSlider('p', root, from_= -90, to=90, tickinterval = 10, 
                               orient= HORIZONTAL, troughcolor = 'black') # creates widget
    sliderPan.place(x=200,y=600, height = 100, width = 400)
    sliderPan.set(0)

    labelTop = Label(root, text = "Top")
    labelTop.config(font=labelFont)
    labelTop.place(x=120,y=610)

    labelBottom = Label(root, text = "Bottom")
    labelBottom.config(font=labelFont)
    labelBottom.place(x=610,y=610)
    

    buttonReset = Button(root, text='Reset To Origin', command=ResetSlider, bg = 'red', fg = '#fff')
    buttonReset.config(font= buttonFont)
    buttonReset.place(x=350,y=700, height = 80, width = 100)



    video_stream()
    root.mainloop()

connection.close()



#----------------------------------

