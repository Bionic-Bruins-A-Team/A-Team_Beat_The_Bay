from vex import *
import math

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

# Inertial Sensor
inertial_1 = Inertial(Ports.PORT7)

def autonomous():
    # Manually configuring drivetrain
    drivetrain = SmartDrive(motor_group_1,motor_group_2,inertial_1)
    # Things for the robot to do during the autonomous period
    drivetrain.turn(RIGHT,Insert_Degrees,10,VelocityUnits.DPS)
    wait(Insert_Time,MSEC)
    drivetrain.stop()
    drivetrain.drive_for(FORWARD,Insert_Distance,MM)
    drivetrain.turn(RIGHT,Insert_Degrees,10,VelocityUnits.DPS)
    drivetrain.drive_for(FORWARD,Insert_Distance,MM)
    drivetrain.turn(RIGHT,Insert_Degrees,10,VelocityUnits.DPS)