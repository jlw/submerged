import Commands

def m14():
  return [
    # Move off wall
    Commands.DriveMM(speed=150, distance=185),
    # Align with M08
    Commands.Pivot(angle=-90, speed=100),
    # Drive and drop arm
    Commands.GyroDrive(speed=175, distance=600),
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
    Commands.GyroDrive(speed=250, distance=1000)
  ]