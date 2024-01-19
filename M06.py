import Commands

def mo6():
  return [
    # Drive to & Complete M01
    Commands.ActMotorTime(motor="right", speed=500, time=480, wait=False),
    Commands.GyroDrive(speed=150, distance=260),
    Commands.Pivot(angle=5, speed=100),
    Commands.ActMotorTime(motor="right", speed=125, time=2000, wait=False),
    Commands.Pivot(angle=40, speed=100),
    Commands.ActMotorTime(motor="right", speed=-100, time=500, wait=False),
    Commands.DriveMM(speed=100, distance=-20),

    # Back up from M01, pivot & drive towards M02
    Commands.DriveMM(speed=100, distance=-150),
    Commands.Pivot(angle=45, speed=100),
    Commands.GyroDrive(speed=100, distance=250),
    Commands.Pivot(angle=-70, speed=100),
    Commands.GyroDrive(speed=150, distance=510),
    # Pivot right and drive to M04
    Commands.Pivot(angle=71, speed=100),
    Commands.GyroDrive(speed=200, distance=600),
    # Sneak onto Museum
    Commands.Pivot(angle=-60, speed=100),
    Commands.DriveMM(speed=100, distance=110),
    Commands.Pivot(angle=60, speed=100),
    # Release M04 module
    Commands.ActMotorTime(motor="left", speed=-700, time=1000, wait=False),
    # Complete M05
    Commands.DriveMM(speed=75, distance=50),
    Commands.Pivot(angle=45, speed=250),
    Commands.ActMotorTime(motor="right", speed=-700, time=350, wait=False),
    # Drive to M06 & M07
    Commands.GyroDrive(speed=150, distance=200),
    Commands.Pivot(angle=-45, speed=100),
    Commands.GyroDrive(speed=150, distance=400),
    Commands.Pivot(angle=-45, speed=100)
  ]