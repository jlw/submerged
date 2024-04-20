import Commands

def mo3():
  return [
    Commands.ActMotorTime(motor="right", speed=-800, time=2000, wait=False),
    Commands.GyroDrive(speed=200, distance=500),
    Commands.DriveMotor(motor="left", angle=200, speed=150),
    Commands.GyroDrive(speed=200, distance=350),
    Commands.DriveMotor(speed=200, angle=200, motor="left"),
    Commands.DriveMM(distance=75, speed=150),
    Commands.ActMotorTime(motor="right", speed=900, time=1500),
    Commands.ActMotorTime(motor="right", speed=-800, time=1500, wait=False),
    Commands.DriveMM(speed=150, distance=-100),
    Commands.Pivot(speed=150, angle=60),
    Commands.GyroDrive(distance=350, speed=250),
    Commands.Pivot(angle=35, speed=150),
    Commands.GyroDrive(distance=350, speed=200),
    Commands.Pivot(angle=-95, speed=150),
    Commands.GyroDrive(angle=-95, distance=80, speed=150, reset_sensor=False),
    Commands.ActMotorTime(time=1500, speed=-700),
    Commands.GyroDrive(angle=-95, distance=500, speed=150, reset_sensor=False),
    Commands.ActMotorTime(time=750, speed=500, wait=False),
    Commands.DriveMM(distance=-2500, speed=250),
  ]