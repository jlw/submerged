import Commands

def mo5():
  return [
    Commands.ActMotorTime(motor='right', speed=500, time=1750, wait=False),
    Commands.GyroDrive(speed=200, distance=320),
    Commands.Pivot(angle=-60),
    Commands.GyroDrive(speed=200, distance=125),
    Commands.GyroDrive(speed=200, distance=-10),
    Commands.ActMotorTime(motor='right', speed=-500, time=1750, wait=False),
    Commands.Pivot(angle=73),
    Commands.GyroDrive(speed=175, distance=120),
    Commands.Pivot(angle=-27),
    Commands.GyroDrive(speed=200, distance=140),
    Commands.Pivot(angle=-64),
    Commands.GyroDrive(speed=200, distance=290),
    Commands.Pivot(angle=30),
    Commands.GyroDrive(speed=150, distance=110),
    #LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    Commands.Pivot(angle=-70),
    Commands.GyroDrive(speed=200, distance=240),
    Commands.Pivot(speed=200, angle=60),
    Commands.Pivot(speed=200, angle=-10),
    Commands.Pivot(speed=200, angle=60),
    Commands.GyroDrive(speed=200, distance=240),

  ]