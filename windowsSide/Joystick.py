import pygame
from main import App


class Joystick:
    def __init__(self, app):
        self.app = app
        pygame.init()
        j = pygame.joystick.Joystick(0)
        print (f"init: {j.get_init()}")
        print (f"id: {j.get_id()}")
        print (j.get_name())
        print (f"axes: {j.get_numaxes()}")
        print (f"numballs: {j.get_numballs()}")
        print (f"numbuttons: {j.get_numbuttons()}")
        print (f"numhats: {j.get_numhats()}")
        print (j.get_axis(0))

        while 1:
            #
            # EVENT PROCESSING STEP
            #
            # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
            # JOYBUTTONUP, JOYHATMOTION
            for event in pygame.event.get(): # User did something.
                """print (j.get_id())
                print (j.get_name())
                print (j.get_numaxes())
                print (j.get_numballs())
                print (j.get_numbuttons())
                print (j.get_numhats())
                print(j.get_axis(0))"""
                """print(f"Left-right: {j.get_axis(0)}") #left -1 / right 1
                print(f"Up-down: {j.get_axis(1)}")  #power up -1 / power down 1"""
                print(f"Ball count: {j.get_numballs()}")
                print(f"Hat: {j.get_hat(0)}")
                print(f"X: {j.get_hat(0)[0]}") #left hat -1 /right hat 1 
                print(f"Y: {j.get_hat(0)[1]}") #down hat -1 / right hat 1
                #print(f"Ball: {j.get_hat(1)}")
                print(f"B0: {j.get_button(0)}")
                print(f"B1: {j.get_button(1)}")
                print(f"B2: {j.get_button(2)}")
                #print(f"Trackball: ")
                if not event.type == 1536: print(event.type)
                if event.type == pygame.QUIT: # If user clicked close.
                    done = True # Flag that we are done so we exit this loop.
                elif event.type == pygame.JOYBUTTONDOWN:
                    print("Joystick button pressed.")
                elif event.type == pygame.JOYBUTTONUP:
                    print("Joystick button released.")
                """elif event.type == pygame.JOYBUTTONRIGHT:
                    print("Joybutton")"""
