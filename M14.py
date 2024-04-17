import Commands

def m14():
  return [
    # Move off wall
    Commands.GyroDrive(speed=150, distance=135),
    # Aim for Emily
    Commands.Pivot(angle=-90, speed=100),
    Commands.GyroDrive(angle=-90, speed=200, distance=300, reset_sensor=False),
    # Capture Emily
    Commands.DriveMotor(motor="left", angle=200, speed=250),
    Commands.DriveMotor(motor="right", angle=200, speed=250),
    # Drive and drop arm
    Commands.GyroDrive(angle=-90, speed=175, distance=300, reset_sensor=False),
    Commands.ActMotorTime(motor='left', speed=100, time=1000),
    # Release audience member
    Commands.DriveMM(speed=175, distance=190),
    Commands.ActMotorTime(motor='right', speed=-100, time=1000),
    # Push M08 camera & back up
    Commands.DriveMM(speed=175, distance=200),
    Commands.DriveMM(speed=175, distance=-75),
    # Lift arm
    Commands.ActMotorTime(motor='left', speed=-100, time=1000),
    # Reset Motors
    Commands.ActMotorTime(motor='right', speed=100, time=1500, wait=False),
    Commands.ActMotorTime(motor='left', speed=-100, time=1500, wait=False),
    # Drive to home
    Commands.DriveMM(speed=250, distance=1000)
  ]