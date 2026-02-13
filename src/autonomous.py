from vex import *

# Brain
brain = Brain()

# Right Motors
motor_1b = Motor(Ports.PORT4,GearSetting.RATIO_6_1)
motor_2b = Motor(Ports.PORT5,GearSetting.RATIO_6_1)
motor_3b = Motor(Ports.PORT6,GearSetting.RATIO_6_1)

# Left Motors
motor_1a = Motor(Ports.PORT1,GearSetting.RATIO_6_1,True)
motor_2a = Motor(Ports.PORT2,GearSetting.RATIO_6_1,True)
motor_3a = Motor(Ports.PORT3,GearSetting.RATIO_6_1,True)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Drivetrain
drivetrain = DriveTrain(motor_group_1,motor_group_2)

# Intake Motors
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

# Inertial
inertial_1 = Inertial(Ports.PORT7)

# Controller
controller_1 = Controller()

# Pneumatics
descore = Pneumatics(brain.three_wire_port.a)
matchloader = Pneumatics(brain.three_wire_port.b)

brain.screen.clear_screen()
brain.screen.print("autonomous")

def red_alliance():
    # Insert code for red alliance routine here
    pass

def blue_alliance():
    # Insert code for blue alliance routine here
    pass

def autonomous():
    # Selecting which routine to run
    if controller_1.buttonUp.pressed():
        red_alliance()
    elif controller_1.buttonX.pressed():
        blue_alliance()
