import pygame
import threading
#import main

class Joystick(threading.Thread):
    def __init__(self, sliderPan, sliderTilt, sliderPower):
        threading.Thread.__init__(self)
        self.sliderPan = sliderPan
        self.sliderTilt = sliderTilt
        self.sliderPower = sliderPower
        pygame.init()
        self.j = pygame.joystick.Joystick(0)
        self.j.init()
        print (f"init: {self.j.get_init()}")
        print (f"id: {self.j.get_id()}")
        print (self.j.get_name())
        print (f"axes: {self.j.get_numaxes()}")
        print (f"numballs: {self.j.get_numballs()}")
        print (f"numbuttons: {self.j.get_numbuttons()}")
        print (f"numhats: {self.j.get_numhats()}")
        print (self.j.get_axis(0))


    def run(self):
        while 1:
            #
            # EVENT PROCESSING STEP
            #
            # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
            # JOYBUTTONUP, JOYHATMOTION
            for event in pygame.event.get(): # User did something.
                if event.type == pygame.JOYAXISMOTION:
                    print(f"Left-right: {self.j.get_axis(0)}") #left -1 / right 1
                    print(f"Up-down: {self.j.get_axis(1)}")  #power up -1 / power down 1"""
                    if(self.j.get_axis(0) < -0.95): 
                        self.sliderPan.increment()
                        self.sliderPan.keyReleased()
                    elif(self.j.get_axis(0) > 0.95): 
                        self.sliderPan.decrement()
                        self.sliderPan.keyReleased()
                    if(self.j.get_axis(1) < -0.95): 
                        self.sliderTilt.increment()
                        self.sliderTilt.keyReleased()
                    elif(self.j.get_axis(1) > 0.95): 
                        self.sliderTilt.decrement()
                        self.sliderTilt.keyReleased()

                elif event.type == pygame.JOYHATMOTION:
                    print(f"X: {self.j.get_hat(0)[0]}") #left hat -1 /right hat 1 
                    print(f"Y: {self.j.get_hat(0)[1]}") #down hat -1 / right hat 1

              

