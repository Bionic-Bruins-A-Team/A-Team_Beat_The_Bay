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
 # Setting up motors and controller

# Left side motors
motor_1a = Motor(vex.Ports.PORT1)
motor_2a = Motor(vex.Ports.PORT2)
motor_3a = Motor(vex.Ports.PORT3)
    
# Right side motors
motor_1b = Motor(vex.Ports.PORT4)
motor_2b = Motor(vex.Ports.PORT5)
motor_3b = Motor(vex.Ports.PORT6)
    
# Initalize motor groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)
controller_1 = vex.Controller()

brain.screen.print("Hello Vex World!")
Brain().screen.print("Hello Vex World!")

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    drivetrain = SmartDrive (motor_group_1, motor_group_2)
     
def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # Setting up controller for user control portion
    while True:
        wait(20, MSEC)
        if controller_1.buttonUp.pressing():
            brain.screen.set_cursor(3, 12)
            brain.screen.print("Up Arrow Button is being pressed")
            while controller_1.buttonUp.pressing() == True:
                motor_group_1.spin(FORWARD, 100)
            brain.screen.clear_screen()
            brain.screen.set_cursor(3, 12)
            brain.screen.print("Up Arrow Button was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonDown.pressing():
            brain.screen.set_cursor(4, 12)
            brain.screen.print("Down Arrow Button is being pressed")
            while controller_1.buttonDown.pressing() == True:
                motor_group_1.spin(REVERSE, 100)
            brain.screen.clear_screen()
            brain.screen.set_cursor(4, 12)
            brain.screen.print("Down Arrow Button was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonX.pressing():
            brain.screen.set_cursor(5, 12)
            brain.screen.print("Button X is being pressed")
            while controller_1.buttonX.pressing() == True:
                motor_group_2.spin(FORWARD, 100)
            brain.screen.clear_screen()
            brain.screen.set_cursor(5, 12)
            brain.screen.print("Button X was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

        if controller_1.buttonB.pressing():
            brain.screen.set_cursor(6, 12)
            brain.screen.print("Button B is being pressed")
            while controller_1.buttonB.pressing() == True:
                motor_group_2.spin(REVERSE, 100)
            brain.screen.clear_screen()
            brain.screen.set_cursor(6, 12)
            brain.screen.print("Button B was released")
            wait(500, MSEC)
            brain.screen.clear_screen()

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts

brain.screen.clear_screen()
