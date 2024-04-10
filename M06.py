import Commands

def mo6():
  return [
    # Drive to & Complete M01
    Commands.ActMotorTime(motor="right", speed=500, time=500, wait=False),
    Commands.GyroDrive(speed=150, distance=300),
    Commands.ActMotorTime(motor="right", speed=-400, time=700, wait=False),
    Commands.Wait(time=300),
    # Commands.Pivot(angle=10, speed=20),
    Commands.Wait(time=300),
    # Back up from M01, pivot & drive towards M02
    Commands.DriveMM(speed=150, distance=-200),
    Commands.Pivot(angle=60, speed=100),
    Commands.GyroDrive(speed=150, distance=250),
    Commands.Pivot(angle=-50, speed=100),
    Commands.GyroDrive(speed=150, distance=380),
    # Pivot right and drive to M04
    Commands.Pivot(angle=85, speed=100),
    Commands.GyroDrive(speed=200, distance=570),
    Commands.Wait(100),
    # Sneak onto Museum
    Commands.Pivot(angle=-65, speed=100),
    Commands.DriveMM(speed=100, distance=140),
    Commands.Pivot(angle=60, speed=100),
    # Release M04 module
    Commands.ActMotorTime(motor="left", speed=-700, time=1000, wait=False),
    Commands.ActMotorTime(motor="right", speed=700, time=600),
    # Complete M05
    Commands.DriveMM(speed=75, distance=50),
    Commands.Pivot(angle=45, speed=250),
    Commands.DriveMM(speed=75, distance=-30),
    Commands.ActMotorTime(motor="right", speed=-700, time=450, wait=False),
    Commands.DriveMM(speed=75, distance=30),
    # Drive to M06 & M07
    Commands.GyroDrive(speed=150, distance=150),
    Commands.Pivot(angle=-45, speed=100),
    Commands.GyroDrive(speed=150, distance=420),
    Commands.Pivot(angle=-45, speed=100),
    # Complete M06 & M07
    Commands.ActMotorTime(motor="right", time=400, speed=-400, wait=False),
    Commands.LineSquare(),
    Commands.DriveMM(speed=100, distance=100),
    Commands.ActMotorTime(motor="right", speed=1500, time=700),
    Commands.DriveMM(speed=100, distance=-10),
    Commands.Pivot(angle=10, speed=75),
    Commands.DriveMM(speed=100, distance=-100),
    # Return to Blue Home
    Commands.Pivot(angle=-85, speed=150),
    Commands.DriveMM(speed=250, distance=-750)
  ]