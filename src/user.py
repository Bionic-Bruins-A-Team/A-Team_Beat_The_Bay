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

# Controller
controller_1 = Controller()


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