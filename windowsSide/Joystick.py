import pygame
import threading
from numpy import interp
import time
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
        while True:
            current = time.time()
            elapsed = 0
            
            # Joystick reading
            pygame.event.pump()
            self.sliderTilt.set(int(interp(self.j.get_axis(0), [-1,1], [-90,90])))     
            self.sliderPan.set(int(interp(self.j.get_axis(1), [-1,1], [-30,90])))
            self.sliderTilt.keyReleased()  
            self.sliderPan.keyReleased()

            # Make this loop work at update_rate
            while elapsed < 0.1:
                elapsed = time.time() - current

            

              