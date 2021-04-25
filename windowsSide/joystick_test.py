import pygame
import threading
#import main

class Joystick(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        pygame.init()
        self.j = pygame.joystick.Joystick(0)
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
                if event.type == pygame.JOYAXISMOTION: print("axis")
                if event.type == pygame.JOYHATMOTION:
                    print(f"X: {self.j.get_hat(0)[0]}") #left hat -1 /right hat 1 
                    print(f"Y: {self.j.get_hat(0)[1]}") #down hat -1 / right hat 1

                if event.type == pygame.JOYBALLMOTION: print("ball")
                if event.type == pygame.JOYBUTTONDOWN: 
                    print("buttondown")
                if event.type == pygame.JOYBUTTONUP: print("buttonup")


                
j = Joystick()
j.start()