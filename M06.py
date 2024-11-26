import Commands

def mo6():
  return [

    #Drive to M06
    Commands.ActMotorTime(motor='right', speed=575, time=1500, wait=False),
    Commands.GyroDrive (speed=150, distance=500),
    Commands.Pivot (angle=90, speed=150),
    Commands.GyroDrive (speed=150, distance=145),
    Commands.ActMotorTime (motor='right', speed=-150, time=1600),
    Commands.GyroDrive (speed=150, distance=-8),
    #Grab treasure chest
    Commands.GyroDrive (speed=100, distance=20),
    Commands.GyroDrive (speed=100, distance=-10),
    Commands.ActMotorTime (motor='right', speed=400, time=1500),
    Commands.GyroDrive (speed=150, distance=-100),
    Commands.Pivot (angle=130, speed=150),
    Commands.GyroDrive (speed=250, distance=475),
    ]