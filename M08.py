import Commands

def mo8():
  return [
    Commands.Pivot(angle=-90, speed=100),
    Commands.GyroDrive(speed=200, distance=165),
    Commands.Pivot(angle=46, speed=100),
    Commands.GyroDrive(speed=250, distance=275),
    Commands.ActMotorTime(motor='left', speed=1000, time=400),
    Commands.GyroDrive(speed=250, distance=75),
    Commands.ActMotorTime(motor='right', time=7000, speed=-1000),
    Commands.DriveMM(angle=0, speed=120, distance=-300),
    Commands.Pivot(angle=-50, speed=100),
    Commands.DriveMM(angle=0, speed=200, distance=190),
    Commands.DriveMM(angle=0, speed=250, distance=-500)
]