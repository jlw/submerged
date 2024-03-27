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


  Commands.GyroDrive(speed=150, distance=25),
  Commands.Pivot(angle=-94, speed=80),
  Commands.GyroDrive(speed=200, distance=360),
  Commands.DriveMM(speed=200, distance=-170),
  Commands.Pivot(angle=50, speed=150),
  Commands.ActMotorTime(motor='right', speed=-999, time=500, wait=False),
  Commands.GyroDrive(speed=200, distance=333),
  Commands.Wait(Time=1000),
  Commands.ActMotorTime(motor='right', speed=999, time=100, wait=False),
  Commands.ActMotorTime(motor='left', speed=-999, time=4000),
]