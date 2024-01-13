import Commands

def mo8():
  return [
    Commands.Pivot(angle=-90, speed=100),
    Commands.Wait(time=250),
    Commands.GyroDrive(speed=200, distance=165),
    Commands.Wait(time=250),
    Commands.Pivot(angle=45, speed=100),
    Commands.Wait(time=250),
    Commands.GyroDrive(speed=250, distance=350),
    Commands.ActMotorTime(motor='left', speed=-1000, time=800),
    Commands.GyroDrive(speed=250, distance=90),
    Commands.ActMotorTime(motor='right', time=7500, speed=-1000),
    Commands.DriveMM(angle=0, speed=120, distance=-300),
    Commands.Pivot(angle=-52, speed=100),
    Commands.DriveMM(angle=0, speed=200, distance=190),
    Commands.DriveMM(angle=0, speed=250, distance=-380)
]