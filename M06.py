import Commands

def m06():
  return [

    #Drive to M06
    Commands.ActMotorTime(motor='right', speed=575, time=1500, wait=False),
    Commands.GyroDrive (speed=150, distance=500),
    Commands.Pivot (angle=89, speed=100),
    Commands.GyroDrive (speed=150, distance=145),
    #Grab Treasure chest
    Commands.ActMotorTime (motor='right', speed=-150, time=1600),
    Commands.GyroDrive (speed=150, distance=-8),
    Commands.GyroDrive (speed=100, distance=10),
    Commands.ActMotorTime (motor='right', speed=250, time=1555),
    Commands.GyroDrive (speed=150, distance=-100),
    #Raise the mast
    Commands.ActMotorTime (motor='right', speed=-400, time=1300),
    Commands.GyroDrive (speed=125, distance=130),
    Commands.ActMotorTime (motor='right', speed=600, time=1200, wait=False),
    Commands.GyroDrive (speed=90, distance=-90),
    Commands.Wait (time=400),
    Commands.ActMotorTime (motor='right', speed=-300, time=1300),
    #Return to home
    Commands.Pivot (angle=120, speed=150),
    Commands.GyroDrive (speed=250, distance=475),
    ]