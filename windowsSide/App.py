from tkinter import Tk, Frame, Label, Button, HORIZONTAL, VERTICAL
from windowsSide.VideoStreamThread import VideoStreamThread
from windowsSide.PositionSlider import PositionSlider

class App:
    def __init__(self):
        self.canvas = "800x800"
        self.labelFont = ('times', 20, 'bold')
        self.buttonFont = ('times', 10, 'bold')
        self.root = Tk()
        self.root.geometry(self.canvas)
        
        # Create a frame
        self.app = Frame(self.root, bg="white")
        self.app.grid()
        self.app.focus_set()


    def initVideoStream(self, STREAM_HOST):
        # Create a label in the frame
        self.lmain = Label(self.app)
        self.lmain.grid(row=0, column=0)
        self.videoStream = VideoStreamThread(self.lmain, STREAM_HOST)
        self.videoStream.start()

    def initGuiElements(self, connection):
        self.sliderTilt = PositionSlider(self.connection, 't', self.root, 
                                    from_=90, to=-90, tickinterval=20,
                                   orient=HORIZONTAL, troughcolor='grey', length=200)
        self.sliderTilt.grid(row=1, column=0)
        self.sliderTilt.set(0)

        self.sliderPan = PositionSlider(self.connection, 'p', self.root, 
                                    from_=-90, to=90, tickinterval=20,
                                    orient=VERTICAL, troughcolor='grey', length=200, showvalue=0)  
        self.sliderPan.grid(row=1, column=1)
        self.sliderPan.set(0)

        self.sliderPower = PositionSlider(self.connection, 'w', self.root, 
                                    from_=255, to=0, tickinterval=20,
                                    orient=VERTICAL, troughcolor='green', length=200, showvalue=0)  
        self.sliderPower.grid(row=1, column=2)
        self.sliderPower.set(0)

        """buttonReset = Button(root, text='Reset To Origin',
                            command=self.resetSlider, bg='red', fg='#fff')
        buttonReset.config(font=buttonFont)
        buttonReset.grid(row=3, column=0)"""

        self.root.bind("<Left>", self.sliderTilt.moveLeft)
        self.root.bind("<Right>", self.sliderTilt.moveRight)
        self.root.bind("<Up>", self.sliderPan.moveUp)
        self.root.bind("<Down>", self.sliderPan.moveDown)
        self.root.bind("<W>", self.sliderPower.powerUp)
        self.root.bind("<S>", self.sliderPower.powerDown)
        self.root.bind('<KeyRelease-Left>',self.sliderTilt.keyReleased)
        self.root.bind('<KeyRelease-Right>',self.sliderTilt.keyReleased)
        self.root.bind('<KeyRelease-Up>',self.sliderPan.keyReleased)
        self.root.bind('<KeyRelease-Down>',self.sliderPan.keyReleased)
        self.root.bind("<KeyRelease-W>", self.sliderPower.keyReleased)
        self.root.bind("<KeyRelease-S>", self.sliderPower.keyReleased)
