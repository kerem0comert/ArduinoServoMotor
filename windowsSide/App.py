from tkinter import Tk, Frame, Label
from VideoStreamThread import VideoStreamThread
from PositionSlider import PositionSlider

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


    def initVideoStream(self):
        # Create a label in the frame
        self.lmain = Label(self.app)
        self.lmain.grid(row=0, column=0)
        self.videoStream = VideoStreamThread(self.lmain)
        self.videoStream.start()

    def initGuiElements(self):
        sliderTilt = PositionSlider('t', root, from_=90, to=-90, tickinterval=20,
                                   orient=HORIZONTAL, troughcolor='grey', length=200)
        sliderTilt.grid(row=1, column=0)
        sliderTilt.set(0)

        sliderPan = PositionSlider('p', root, from_=-90, to=90, tickinterval=20,
                                    orient=VERTICAL, troughcolor='grey', length=200, showvalue=0)  
        sliderPan.grid(row=1, column=1)
        sliderPan.set(0)

        sliderPower = PositionSlider('w', root, from_=255, to=0, tickinterval=20,
                                    orient=VERTICAL, troughcolor='green', length=200, showvalue=0)  
        sliderPower.grid(row=1, column=2)
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