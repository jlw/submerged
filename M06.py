import Commands

def mo6():
  return [

    #Drive to M06
    Commands.ActMotorTime(motor='right', speed=575, time=1500, wait=False),
    Commands.GyroDrive (speed=150, distance=500),
    Commands.Pivot (angle=89, speed=100),
    Commands.GyroDrive (speed=150, distance=145),
    Commands.ActMotorTime (motor='right', speed=-150, time=1600),
    Commands.GyroDrive (speed=150, distance=-8),
    Commands.GyroDrive (speed=100, distance=10),
    #Grab Treasure chest
    Commands.ActMotorTime (motor='right', speed=250, time=1555),
    Commands.GyroDrive (speed=150, distance=-100),
    Commands.GyroDrive (speed=150, distance=10),
    #Return to home
    Commands.Pivot (angle=120, speed=150),
    Commands.GyroDrive (speed=250, distance=475),
    ]