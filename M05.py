import Commands

def m05():
  return [
    Commands.GyroDrive(speed=200, distance=403),
    Commands.Pivot(angle=-48.5),
    Commands.GyroDrive(speed=175, distance=555),
    # LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    Commands.GyroDrive(speed=80, distance=-15),
    # Turn to angler fish
    Commands.Pivot(speed=80, angle=-72),
    Commands.GyroDrive(speed=175, distance=264),
    Commands.GyroDrive(speed=125, distance=-10),
    # Scare it away
    Commands.Pivot(speed=100, angle=20),
    Commands.Wait(time=300),
    #Commands.GyroDrive(speed=150, distance=10),
    Commands.Pivot(speed=100, angle=36),
    # Run to the coral
    Commands.ActMotorTime(motor='right', speed=600, time=1100, wait=False),
    Commands.GyroDrive(speed=200, distance=290),
    # agressavly hit coral untill it revives it somehow
    Commands.ActMotorTime(motor='right', speed=500, time=1000),
    # Run away
    Commands.ActMotorTime(motor='right', speed=-500, time=1850, wait=False),
    Commands.GyroDrive(speed=200, distance=-90),
    Commands.DriveMotor(motor="right", angle=185, speed=175),
    # Scoop up all nearby wildlife
    Commands.GyroDrive(speed=200, distance=300),
    Commands.Pivot(angle=-41),
    # Return to saftey
    Commands.DriveMM(speed=222, distance=800),
  ]