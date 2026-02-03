# Right Motors
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)

# Left Motors
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Drivetrain
drivetrain = DriveTrain(motor_group_1,motor_group_2)

# Intake Motors
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

# Controller
controller_1 = Controller()

brain.screen.clear_screen()
brain.screen.print("driver control")

# User control function setting up controller and handling buttons
def user_control():
    # Setting up controller for user control portion
    while True:
        wait(20,MSEC)
        # Right joystick for moving forward and backward
        if controller_1.axis2.position()>10:
            drivetrain.drive(FORWARD,controller_1.axis2.position(),PERCENT)
        elif controller_1.axis2.position()<-10:
            drivetrain.drive(REVERSE,abs(controller_1.axis2.position()),PERCENT)

        # Left joystick for moving left and right
        if controller_1.axis4.position()>10:
            drivetrain.turn(RIGHT,controller_1.axis4.position(),PERCENT)
        elif controller_1.axis4.position()<-10:
            drivetrain.turn(LEFT,abs(controller_1.axis4.position()),PERCENT)

        # Intake pull
        if controller_1.buttonL1.pressing():
            motor_intake_1.spin(FORWARD,100,PERCENT)
        elif controller_1.buttonL2.pressing():
            motor_intake_1.spin(REVERSE,100,PERCENT)

        # Intake discharge
        if controller_1.buttonR1.pressing():
            motor_intake_2.spin(FORWARD,100,PERCENT)
        elif controller_1.buttonR2.pressing():
            motor_intake_2.spin(REVERSE,100,PERCENT)
