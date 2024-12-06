import Commands

def mo8():
  return [
    Commands.ActMotorTime(motor='right', speed=500, time=1800, wait=False),
    Commands.GyroDrive(speed=200, distance=610),
    Commands.GyroDrive(speed=150, distance=-5),
    Commands.ActMotorTime(motor='right', speed=-600, time=1000),
    Commands.Pivot(angle=5),
    Commands.GyroDrive(speed=150, distance=90),
    #Commands.wait(time=2000),
    Commands.ActMotorTime(motor='right', speed=700, time=3000, wait=False),
    Commands.DriveMM(speed=80, distance=-200),
    #Commands.DriveMM(speed=200, distance=-700),
  ]