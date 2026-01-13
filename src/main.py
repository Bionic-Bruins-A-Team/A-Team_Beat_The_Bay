# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       levyz                                                        #
# 	Created:      1/12/2026, 5:12:55 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

brain = Brain()
controller_1 = Controller()

brain.screen.print("Hello Vex World!")
Brain().screen.print("Hello Vex World!")

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    # place automonous code
    

def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # place driver control in this while loop
    while True:
        wait(20, MSEC)
        if controller_1.buttonA.pressing():
            brain.screen.set_cursor(3, 12)
            brain.screen.print("Button A is being pressed")
            while controller_1.buttonA.pressing() == True:
                pass
            brain.screen.clear_screen()
            brain.screen.set_cursor(3, 12)
            brain.screen.print("Button A was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonB.pressing():
            brain.screen.set_cursor(4, 12)
            brain.screen.print("Button B is being pressed")
            while controller_1.buttonB.pressing() == True:
                pass
            brain.screen.clear_screen()
            brain.screen.set_cursor(4, 12)
            brain.screen.print("Button B was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonX.pressing():
            brain.screen.set_cursor(5, 12)
            brain.screen.print("Button X is being pressed")
            while controller_1.buttonX.pressing() == True:
                pass
            brain.screen.clear_screen()
            brain.screen.set_cursor(5, 12)
            brain.screen.print("Button X was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonY.pressing():
            brain.screen.set_cursor(6, 12)
            brain.screen.print("Button Y is being pressed")
            while controller_1.buttonY.pressing() == True:
                pass
            brain.screen.clear_screen()
            brain.screen.set_cursor(6, 12)
            brain.screen.print("Button Y was released")
            wait(500, MSEC)
            brain.screen.clear_screen()
        

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()