import Commands

def mo2():
  return [
    # Drive around M01
    Commands.GyroDrive(speed=200, distance=100),
    Commands.Pivot(angle=45, speed=100),
    Commands.GyroDrive(speed=150, distance=260),
    Commands.DriveMotor(motor="right", angle=250, speed=150),
    # Drop arm for Sam
    Commands.ActMotorTime(motor="left", time=500, speed=650),
    # Drive to M02 & push
    Commands.GyroDrive(speed=200, distance=180),
    Commands.DriveMotor(motor="right", angle=200, speed=150),
    Commands.DriveMM(speed=100, distance=80),
    # Capture Sam
    Commands.ActMotorTime(motor="left", time=500, speed=-600),
    Commands.DriveMM(speed=100, distance=-80),
    # Deliver Izzy
    Commands.ActMotorAngle(motor="right", speed=400, angle=340),
    Commands.Wait(time=600),
    Commands.ActMotorAngle(motor="right", speed=400, angle=-340),
    # Pivot towards M01
    Commands.Pivot(angle=-90, speed=100)

    ## NOTE ##
    # Need to add code to drive back to M03 and complete M03 & M11.
    # Also need to fine-tune code for picking up Sam,
    # as well as rebuilding the arm that picks up Sam.
  ]