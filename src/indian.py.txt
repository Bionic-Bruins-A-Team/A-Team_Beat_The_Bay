 #OLD CODE
    #example turn right 90 degrees
  #  while Inertial_sensor.heading () < 90:
   #     left_drive.spin(FORWARD, 80, RPM)
#        right_drive.spin(REVERSE, 80, RPM)
    #left_drive.stop()
   # right_drive.stop()

    #THE DEBUG OUTPUT
    #brain.screen.print(Inertial_sensor.heading())

from vex import *

#initialize the brain
brain = Brain()

# Initialize les motors
left_drive = MotorGroup(Ports.PORT1, Ports.PORT2, Ports.PORT3)
right_drive = MotorGroup(Ports.PORT4, Ports.PORT5, Ports.PORT6) 

intake_motor = Motor(Ports.PORT7)
output_motor = Motor(Ports.PORT8)
Inertial_sensor = Inertial(Ports.PORT9)

#initialize the drivetrain
drivetrain = SmartDrive(left_drive, right_drive, Inertial_sensor, wheel_travel, track_width, wheel_base, MM, gear_ratio)

def autonomous (): #calibrate the inertial sensor
    Inertial_sensor.calibrate()
    while Inertial_sensor.is_calibrating():
        wait(20, MSEC)

    #new CODE              
    #                      !FIRST SECTOR!
#-------------SECTOR 1: GO TO MIDGOAL AND INTAKE 3 BALLS----------------
#Note: 
#intake_motor.spin(FORWARD, 100, RPM) #start the intake
drivetrain.drive_for(FORWARD, 1219, MM, 190,RPM) #drive forward 4 feet
#intake_motor.stop() #stop the intake after reaching the 3 balls near the midgoal

#-------------SECTOR 2:  APPRACHING THE DISPENSER AND INTAKING 3 BALLS ----------------

drivetrain.drive_for(REVERSE, 609.6, MM, 190, RPM) #drive backward 2 feet
drivetrain.turn_for(90, DEGREES) #turn to face 90 degrees 
drivetrain.drive_for(FORWARD, 609.6, MM, 190,RPM) #drive towards, between the long goal and the dispenser
drivetrain.turn_for(180, DEGREES) #turn to face 90 degrees  
#WE DONT KNOW THE RATE OF SPEED OF THE INTAKE AND OUTPUT SYSTEM YET! So for now it is commented out 
#  intake_motor.spin(FORWARD, 100, RPM) #start the intake
drivetrain.drive_for(FORWARD, 609.6, MM, 190, RPM) #drive towards the dispenser
wait(3000, MSEC) #wait 3000 miliseconds (3 sec) to intake the balls
#intake_motor.stop() #stop the intake after reaching the dispenser

#                                 !FINAL SECTOR!
#---------------SECTOR 3: GO TO LONG GOAL AND OUTPUT 6 BALLS ----------------

#drive backward from the dispenser straight to the long goal
drivetrain.drive_for(REVERSE, 1219, MM,190, RPM)
#start the output to shoot the balls into the long goal
output_motor.spin(FORWARD, 100, RPM)
# start the intake to help push the balls into the long goal
intake_motor.spin(FORWARD, 100, RPM)
# wait 1.5 seconds to output the balls into the long goal
wait(1500, MSEC)
#stop the output
output_motor.stop()
#stop the intake
intake_motor.stop()
