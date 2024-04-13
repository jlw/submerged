import Commands

def mo2():
  return [
    # Drive around M01
    Commands.GyroDrive(speed=175, distance=100),
    Commands.Pivot(angle=44, speed=100),
    Commands.GyroDrive(speed=200, distance=280),
    Commands.DriveMotor(motor="right", angle=250, speed=150),
    # Drop arm for Sam
    Commands.ActMotorTime(motor="left", time=600, speed=-300, wait=False),
    # Drive to M02 & push
    Commands.GyroDrive(speed=200, distance=160),
    Commands.DriveMotor(motor="right", angle=200, speed=150),
    Commands.DriveMM(speed=100, distance=40),
    # Capture Sam
    Commands.ActMotorTime(motor="left", time=800, speed=350, wait=False),
    Commands.DriveMM(speed=100, distance=-80),
    # Pivot towards M01
    Commands.Pivot(angle=-90, speed=100),
    # Manuver around M10
    Commands.DriveMM(speed=100, distance=-230),
    Commands.Pivot(angle=-47, speed=100),
    Commands.DriveMM(speed=150, distance=30),
    Commands.LineSquare(returnTime=3000, finetuneSpeed=40),
    Commands.Pivot(angle=-70, speed=100),
    Commands.DriveMM(speed=150, distance=225),
    Commands.Pivot(angle=125, speed=100),
    # Deliver Izzy
    Commands.ActMotorTime(motor="right", speed=600, time=900),
    Commands.ActMotorTime(motor="right", speed=-500, time=800),
    Commands.Pivot(angle=48, speed=120),
    # Complete M03
    Commands.ActMotorTime(motor="right", speed=700, time=1500),
    Commands.ActMotorTime(motor="right", speed=-800, time=1200, wait=False),
    Commands.Wait(time=200),
    Commands.Pivot(angle=9, speed=120),
    # Drive to M11 & Complete
    Commands.DriveMM(speed=175, distance=-120),
    Commands.ActMotorTime(motor="left", speed=888, time=6250),
    # Face & Return to home
    Commands.DriveMM(speed=200, distance=50),
    Commands.Pivot(angle=-100, speed=100),
    Commands.DriveMM(speed=250, distance=1000, angle=18)
  ]
    
  