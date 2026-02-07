# Drivetrain
drivetrain = DriveTrain(motor_group_1,motor_group_2)
from vex import *

# Brain
brain = Brain()

# Devices

# Left Motors
motor_1a = Motor(Ports.PORT1)
motor_2a = Motor(Ports.PORT2)
motor_3a = Motor(Ports.PORT3)

# Right Motors
motor_1b = Motor(Ports.PORT4)
motor_2b = Motor(Ports.PORT5)
motor_3b = Motor(Ports.PORT6)

# Motor Groups
motor_group_1 = MotorGroup(motor_1a, motor_2a, motor_3a)
motor_group_2 = MotorGroup(motor_1b, motor_2b, motor_3b)

# Drivetrain
drivetrain = SmartDrive(motor_group_1,motor_group_2)

# Intake Motors
motor_intake_1 = Motor(Ports.PORT8)
motor_intake_2 = Motor(Ports.PORT9)

# Pneumatics
pneumatic_1 = Pneumatics(brain.three_wire_port.a)
pneumatic_2 = Pneumatics(brain.three_wire_port.b)

# Controller
controller_1 = Controller()

brain.screen.clear_screen()
brain.screen.print("Driver Control")

# User control function setting up controller and handling joystick/button inputs
def user_control():
  while True:
      wait(20,MSEC)
      back_forth = controller_1.axis3.position()
      left_right = controller_1.axis1.position()

      # Right joystick for moving forward and backward
      if back_forth > 10:
          drivetrain.drive(FORWARD,back_forth,PERCENT)
      elif back_forth < -10:
          drivetrain.drive(REVERSE,abs(back_forth),PERCENT)

      # Left joystick for moving left and right
      if left_right > 10:
          drivetrain.turn(RIGHT,left_right,PERCENT)
      elif left_right < -10:
          drivetrain.turn(LEFT,abs(left_right),PERCENT)

      elif (back_forth > -10 and back_forth < 10) and (left_right > -10 and left_right < 10):
           drivetrain.stop()

      # Intake pull
      if controller_1.buttonL1.pressing():
          motor_intake_1.spin(FORWARD,100,PERCENT)
      elif controller_1.buttonL2.pressing():
          motor_intake_1.spin(REVERSE,100,PERCENT)
      else:
           motor_intake_1.stop()

      # Intake discharge
      if controller_1.buttonR1.pressing():
          motor_intake_2.spin(FORWARD,100,PERCENT)
      elif controller_1.buttonR2.pressing():
          motor_intake_2.spin(REVERSE,100,PERCENT)
      else:
           motor_intake_2.stop()
    # Setting up controller for user control portion
    while True:
        wait(20,MSEC)
        # Right joystick for moving forward and backward
        if controller_1.axis2.position()>10:
            drivetrain.spin(FORWARD,controller_1.axis2.position(),PERCENT)
        elif controller_1.axis2.position()<-10:
            drivetrain.spin(REVERSE,abs(controller_1.axis2.position()),PERCENT)

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

        # Pneumatics
        if controller_1.buttonUp.pressing():
            pneumatic_1.open()
        else:
            pneumatic_1.close()

        if controller_1.buttonX.pressing():
            pneumatic_2.open()
        else:
            pneumatic_2.close()
