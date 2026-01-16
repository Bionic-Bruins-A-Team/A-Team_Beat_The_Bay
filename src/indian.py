
from vex import *

# Initialize les motors
left_drive = Motor(Ports.PORT1)
right_drive = Motor(Ports.PORT2)
intake_motor = Motor(Ports.PORT3)

def autonomous ():
    intake_motor.spin (FORWARD, 160, RPM) # type: ignore
    left_drive.spin (FORWARD, 160, RPM)
    right_drive.spin(FORWARD, 160, RPM)

    wait(1.2, SECONDS)

    left_drive.stop()
    right_drive.stop()
    intake_motor.stop()