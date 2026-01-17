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
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)
    
# Right side motors
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)
    
# Initalize motor groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

#Initialize controller
controller_1 = Controller()

# Initialize inertial sensor
inertial_1 = Inertial(Ports.PORT7)

brain.screen.print("Hello Vex World!")


# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts
brain.screen.clear_screen()