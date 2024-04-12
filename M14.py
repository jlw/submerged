import Commands

def m14():
  return [
    Commands.DriveMM(speed=150, distance=185),
    Commands.Pivot(angle=-90, speed=100),
    Commands.GyroDrive(speed=175, distance=600),
    Commands.ActMotorTime(motor='left', speed=100, time=1000),
    Commands.DriveMM(speed=175, distance=190),
    Commands.ActMotorTime(motor='right', speed=-100, time=1000),
    Commands.DriveMM(speed=175, distance=185),
    Commands.DriveMM(speed=175, distance=-50),
    Commands.ActMotorTime(motor='left', speed=-100, time=1000),
    Commands.GyroDrive(speed=175, distance=400),
    Commands.ActMotorTime(motor='right', speed=100, time=1500, wait=False),
    Commands.ActMotorTime(motor='left', speed=-100, time=1500, wait=False),
    Commands.DriveMM(speed=250, distance=450),
  ]