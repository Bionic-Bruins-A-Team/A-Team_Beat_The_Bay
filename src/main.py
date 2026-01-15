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
import motor
import motor_group

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

# Setting up motors and controller

# Left side motors
motor_1a = vex.Motor(vex.Ports.PORT1)
motor_2a = vex.Motor(vex.Ports.PORT2)
motor_3a = vex.Motor(vex.Ports.PORT3)

# Right side motors
motor_1b = vex.Motor(vex.Ports.PORT4)
motor_2b = vex.Motor(vex.Ports.PORT5)
motor_3b = vex.Motor(vex.Ports.PORT6)

# Initalize motor groups
motor_group_1 = motor_group(motor_1a, motor_2a, motor_3a)
motor_group_2 = motor_group(motor_1b, motor_2b, motor_3b)

# Initialize controller
controller_1 = Controller()

# Set up controller buttons
while True:
    # Setting up arrow buttons for controlling the left motor group
    
    # If the up arrow button is pressed, the left motor group spins forward
    if controller_1.buttonUp.pressing():
        motor_group_1.spin(FORWARD,100)
        
    # If the down arrow button is pressed, the left motor group spins backwards
    elif controller_1.buttonDown.pressing():
        motor_group_1.spin(REVERSE,100)
        
    # If neither of these buttons are pressed the left motor group stops
    else:
        motor_group_1.stop()
    
    # Setting up the letter buttons (A, B, X, & Y) for the right motor group
    
    # If the X button is pressed, the right motor group spins forward
    if controller_1.buttonX.pressing():
        motor_group_2.spin(FORWARD,100)
        
    # If the B button is pressed, the right motor group spins backward
    elif controller_1.buttonB.pressing():
        motor_group_2.spin(REVERSE,100)
        
    # If neither of these buttons are pressed, the right motor group stops
    else:
        motor_group_2.stop()
    
    # A small wait is necessary to prevent the brain from getting overwhelmed and crashing
    wait(5, MSEC)

