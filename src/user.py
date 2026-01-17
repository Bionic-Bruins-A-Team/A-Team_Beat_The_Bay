from vex import *

brain = Brain()
# Motor Definition

# Right
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)

# Left
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Intake Motors
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

# Controller
controller_1 = Controller()


def user_control():
    brain.screen.clear_screen()
    brain.screen.print("driver control")
    # Setting up controller for user control portion
    while True:
        wait(20, MSEC)
        # Makes both motor groups spin forward
        if controller_1.buttonUp.pressing() and controller_1.buttonX.pressing():
            while controller_1.buttonUp.pressing() and controller_1.buttonX.pressing():
                motor_group_1.spin(FORWARD, 100)
                motor_group_2.spin(FORWARD, 100)

        # Makes both motor groups spin backward
        if controller_1.buttonDown.pressing() and controller_1.buttonB.pressing():
            while controller_1.buttonDown.pressing() and controller_1.buttonB.pressing():
                motor_group_1.spin(REVERSE, 100)
                motor_group_2.spin(REVERSE, 100)

        # Makes ONLY right motor group spin forward (turning left and forward)
        if controller_1.buttonX.pressing():
            while controller_1.buttonX.pressing():
                motor_group_2.spin(FORWARD, 100)

        # Makes ONLY right motor group spin backward (turning left and backward)
        if controller_1.buttonB.pressing():
            while controller_1.buttonB.pressing():
                motor_group_2.spin(REVERSE, 100)

        # Makes the left motor group spin forward (turning right and forward)
        if controller_1.buttonUp.pressing():
            while controller_1.buttonUp.pressing():
                motor_group_1.spin(FORWARD, 100)

        # Makes the left motor group spin backward (turning right and backward)
        if controller_1.buttonDown.pressing():
            while controller_1.buttonDown.pressing():
                motor_group_1.spin(REVERSE, 100)

        # Intake pull
        if controller_1.buttonR1.pressing():
            while controller_1.buttonR1.pressing():
                motor_intake_1.spin(FORWARD, 100)
        
        # Intake Discharge 
        if controller_1.buttonR2.pressing():
            while controller_1.buttonR1.pressing():
                motor_intake_2.spin(FORWARD, 100)
        
        