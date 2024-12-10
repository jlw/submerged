import Commands

def mo5():
  return [
    # Lower the arm
    Commands.ActMotorTime(motor='right', speed=500, time=1850, wait=False),
    Commands.GyroDrive(speed=200, distance=320),
    Commands.Pivot(speed=80, angle=-63),
    # Ram the Quatropus
    Commands.GyroDrive(speed=175, distance=110),
    Commands.GyroDrive(speed=175, distance=-13),
    Commands.ActMotorTime(motor='right', speed=-300, time=3500, wait=False),
    # Turn to coral and collect
    Commands.Pivot(speed=80, angle=73),
    Commands.GyroDrive(speed=175, distance=120),
    # Drive to sub station
    Commands.Pivot(angle=-27),
    Commands.GyroDrive(speed=175, distance=140),
    Commands.Pivot(angle=-64),
    Commands.GyroDrive(speed=175, distance=290),
    # Turn to square
    Commands.Pivot(speed=80, angle=30),
    Commands.GyroDrive(speed=150, distance=90),
    # LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    Commands.GyroDrive(speed=100, distance=-12),
    # Turn to angler fish
    Commands.Pivot(angle=-73),
    Commands.GyroDrive(speed=175, distance=240),
    Commands.GyroDrive(speed=125, distance=-6),
    # Scare it away
    Commands.Pivot(speed=100, angle=20),
    Commands.GyroDrive(speed=150, distance=10),
    Commands.Pivot(speed=100, angle=43),
    # Run to the coral
    Commands.ActMotorTime(motor='right', speed=600, time=1500, wait=False),
    Commands.GyroDrive(speed=200, distance=280),
    # agressavly hit coral untill it revives it somehow
    Commands.ActMotorTime(motor='right', speed=500, time=1000),
    # Run away
    Commands.ActMotorTime(motor='right', speed=-500, time=1850, wait=False),
    Commands.GyroDrive(speed=200, distance=-90),
    Commands.DriveMotor(motor="right", angle=185, speed=175),
    # Scoop up all nearby wildlife
    Commands.GyroDrive(speed=200, distance=300),
    Commands.Pivot(angle=-40),
    # Return to saftey
    Commands.DriveMM(speed=222, distance=800),
#   Commands.Fix_it (amount='everything')
  ]