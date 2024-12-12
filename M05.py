import Commands

def m05():
  return [
    # Lower the arm
    #Commands.ActMotorTime(motor='right', speed=550, time=1850, wait=False),
    #Commands.GyroDrive(speed=200, distance=320),
    #Commands.Pivot(speed=80, angle=-65),
    ## Ram the Quatropus
    #Commands.GyroDrive(speed=175, distance=110),
    #Commands.GyroDrive(speed=175, distance=-15),
    #Commands.ActMotorTime(motor='right', speed=-300, time=3500, wait=False),
    
    ### NEED TO AJUST FOR NO M09 ###

    # Turn to coral and collect
    #Commands.Pivot(speed=80, angle=73),
    #Commands.GyroDrive(speed=175, distance=125),
    # Drive to sub station
    #Commands.Pivot(angle=-27),


    Commands.GyroDrive(speed=175, distance=590),
    Commands.Pivot(angle=-78),
    Commands.GyroDrive(speed=175, distance=240),
    # Turn to square
    Commands.Pivot(speed=80, angle=37),
    Commands.GyroDrive(speed=140, distance=125),
    # LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    Commands.GyroDrive(speed=80, distance=-15),
    # Turn to angler fish
    Commands.Pivot(speed=80, angle=-73),
    Commands.GyroDrive(speed=175, distance=244),
    Commands.GyroDrive(speed=125, distance=-13),
    # Scare it away
    Commands.Pivot(speed=100, angle=20),
    Commands.GyroDrive(speed=150, distance=10),
    Commands.Pivot(speed=100, angle=41),
    # Run to the coral
    Commands.ActMotorTime(motor='right', speed=600, time=1400, wait=False),
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