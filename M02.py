import Commands

def mo2():
  return [
    # Drive around M01
    Commands.GyroDrive(speed=200, distance=100),
    Commands.Pivot(angle=45, speed=100),
    Commands.GyroDrive(speed=200, distance=280),
    Commands.DriveMotor(motor="right", angle=250, speed=150),
    # Drop arm for Sam
    Commands.ActMotorTime(motor="left", time=500, speed=-300, wait=False),
    # Drive to M02 & push
    Commands.GyroDrive(speed=200, distance=170),
    Commands.DriveMotor(motor="right", angle=200, speed=150),
    Commands.DriveMM(speed=100, distance=40),
    # Capture Sam
    Commands.ActMotorTime(motor="left", time=800, speed=350, wait=False),
    Commands.DriveMM(speed=100, distance=-80),
    # Deliver Izzy
    Commands.ActMotorAngle(motor="right", speed=400, angle=340),
    Commands.Wait(time=600),
    Commands.ActMotorAngle(motor="right", speed=400, angle=-340),
    # Pivot towards M01
    Commands.Pivot(angle=-90, speed=100),
    # Manuver around M10
    Commands.DriveMM(speed=100, distance=-80),
    Commands.DriveMotor(motor="right", angle=230, speed=-150),
    # Drive to M11
    Commands.DriveMM(speed=150, distance=-350),
    Commands.DriveMotor(speed=-100, angle=50, motor="left"),
    # Complete M03 & M11
    Commands.ActMotorTime(motor="right", speed=600, time=900, wait=False),
    Commands.ActMotorTime(motor="left", speed=600, time=2500),
    Commands.ActMotorTime(motor="right", speed=-600, time=900, wait=False),
    # Pivot & Drive between M10 & M11
    Commands.Pivot(angle=-70, speed=100),
    Commands.GyroDrive(speed=250, distance=400),
    # Face & Return to home
    Commands.Pivot(speed=150, angle=60, wait=0),
    Commands.GyroDrive(speed=250, distance=600)
  ]