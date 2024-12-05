import Commands

def mo5():
  return [
    # Lift the arm
    Commands.ActMotorTime(motor='right', speed=500, time=1750, wait=False),
    Commands.GyroDrive(speed=200, distance=320),
    Commands.Pivot(angle=-60),
    # Ram the Quatropus
    Commands.GyroDrive(speed=200, distance=125),
    Commands.GyroDrive(speed=200, distance=-10),
    Commands.ActMotorTime(motor='right', speed=-500, time=1750, wait=False),
    # Turn to coral and collect
    Commands.Pivot(angle=73),
    Commands.GyroDrive(speed=175, distance=120),
    # Drive to sub station
    Commands.Pivot(angle=-27),
    Commands.GyroDrive(speed=200, distance=140),
    Commands.Pivot(angle=-64),
    Commands.GyroDrive(speed=200, distance=290),
    # Turn to square
    Commands.Pivot(angle=30),
    Commands.GyroDrive(speed=150, distance=110),
    # LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    # Turn to angler fish
    Commands.Pivot(angle=-72),
    Commands.GyroDrive(speed=200, distance=240),
    # Scare it away
    Commands.Pivot(speed=200, angle=60),
    Commands.ActMotorTime(motor='right', speed=500, time=1750, wait=False),
    Commands.GyroDrive(speed=200, distance=275),
    # Run to the coral
    #Commands.Pivot(speed=200, angle=35),
    # agressavly hit coral untill it revives it somehow
    #Commands.GyroDrive(speed=200, distance=320),
    # Run away
    #Commands.ActMotorTime(motor='right', speed=-500, time=1750, wait=False),
    #Commands.GyroDrive(speed=200, distance=-90),
    #Commands.Pivot(speed=200, angle=-60),
    # Scoop up all nearby wildlife
    #Commands.GyroDrive(speed=200, distance=150),
    # Return to saftey
  ]