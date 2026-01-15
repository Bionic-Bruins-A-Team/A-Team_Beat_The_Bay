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
from autonomous import *
from user import *

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

#Initialize controller
controller_1 = vex.Controller()

brain.screen.print("Hello Vex World!")
Brain().screen.print("Hello Vex World!")

def autonomous():
    brain.screen.clear_screen()
    brain.screen.print("autonomous code")
    drivetrain = SmartDrive (motor_group_1, motor_group_2)
     


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts

brain.screen.clear_screen()

