# Drivetrain
drivetrain = DriveTrain(motor_group_1,motor_group_2)

brain.screen.clear_screen()
brain.screen.print("driver control")

# User control function setting up controller and handling buttons
def user_control():
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
