import Commands

def mo8():
  return [
#     Commands.Pivot(angle=-90, speed=100),
#     Commands.GyroDrive(speed=150, distance=165),
#     Commands.Pivot(angle=46, speed=100),
#     Commands.GyroDrive(speed=150, distance=275),
#     Commands.ActMotorTime(motor='left', speed=1000, time=400),
#     Commands.GyroDrive(speed=150, distance=75),
#     Commands.ActMotorTime(motor='right', time=3500, speed=-1000),
#     Commands.DriveMM(angle=0, speed=120, distance=-300),
#     Commands.Pivot(angle=-50, speed=100),
#     Commands.DriveMM(angle=0, speed=200, distance=190),
#     Commands.DriveMM(angle=0, speed=250, distance=-500)


  Commands.GyroDrive(speed=150, distance=3),
  Commands.Pivot(angle=-90, speed=100),
  Commands.GyroDrive(speed=200, distance=311.5),
  Commands.GyroDrive(speed=200, distance=-200),
  Commands.Pivot(angle=45, speed=150)
  #Commands.GyroDrive()
]