# Drivetrain
drivetrain = DriveTrain(motor_group_1,motor_group_2)

brain.screen.clear_screen()
brain.screen.print("driver control")

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
