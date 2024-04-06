import Commands

def m10():
  return [
    # Commands.GyroDrive(speed=150, distance=390),
    # Commands.ActMotorTime(motor="left", speed=-400, time=500, wait=False),
    # Commands.ActMotorTime(motor="right", speed=300, time=3000),
    # Commands.Wait(time=300),
    # Commands.ActMotorTime(motor="right", speed=-700, time=2000, wait=False),
    # Commands.DriveMM(speed=150, distance=-100),
    # Commands.Pivot(angle=-45, speed=100),
    # Commands.ActMotorTime(motor="left", speed=500, time=250),
    # Commands.Pivot(angle=45, speed=250),
    # Commands.DriveMM(speed=250, distance=-300)--backwards
  Commands.ActMotorTime(motor="left", speed=-1000, time=900, wait=False),
  Commands.GyroDrive(speed=150, distance=15),
  Commands.Pivot(angle=42, speed=150),
  Commands.GyroDrive(speed=175, distance=600),
  Commands.DriveMM(speed=200,distance=-400),
  Commands.Pivot(angle=48, speed=150),
  Commands.GyroDrive(speed=200, distance=420),
  Commands.ActMotorTime(motor="right", speed=400, time=900, wait=False),
  Commands.ActMotorTime(motor="left", speed=500, time=900, wait=True),
  Commands.GyroDrive(speed=-150, distance=150)
  ]