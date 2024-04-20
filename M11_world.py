import Commands

def m11():
  return [
    Commands.ActMotorTime(motor="left", time=2000, speed=500),
    Commands.GyroDrive(speed=200, distance=475),
    Commands.Pivot(angle=-45, speed=150),
    Commands.GyroDrive(distance=410, speed=200),
    Commands.ActMotorTime(motor="left", time=2000, speed=-500),
    Commands.DriveMM(distance=-1000, speed=250)
  ]