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

# Drivetrain
drivetrain = Drivetrain(motor_group_1, motor_group_2)


#Initialize controller
controller_1 = Controller()

brain.screen.print("Hello Vex World!")

def user_control():
 while True:
      wait(20,MSEC)
      back_forth = controller_1.axis3.position()
      left_right = controller_1.axis1.position()

      # Right joystick for moving forward and backward
      if back_forth >= 10:
          drivetrain.drive(FORWARD,back_forth,PERCENT)
      elif back_forth <= -10:
          drivetrain.drive(REVERSE,abs(back_forth),PERCENT)

      # Left joystick for moving left and right
      if 10 < left_right <= 20:
          drivetrain.turn(RIGHT,20,PERCENT)
      elif left_right > 20:
          drivetrain.turn(RIGHT,left_right,PERCENT)
      elif -20 <= left_right < -10:
          drivetrain.turn(LEFT,20,PERCENT)
      elif left_right < -20:
          drivetrain.turn(LEFT,abs(left_right),PERCENT)

      elif -10 < back_forth < 10 and -10 < left_right < 10:
           drivetrain.stop()

def autonomous():
 pass

# create competition instance
comp = Competition(user_control, autonomous)

# actions to do when the program starts

brain.screen.clear_screen()
