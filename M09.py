import Commands

def m09():
  return [
    # Lower the arm
    Commands.ActMotorTime(motor='right', speed=550, time=1850, wait=False),
    # Head to M09
    Commands.GyroDrive(speed=200, distance=320),
    Commands.Pivot(speed=80, angle=-65),
    # Ram the Quatropus
    Commands.GyroDrive(speed=175, distance=110),
    # Return
    Commands.GyroDrive(speed=175, distance=-500),
    
  ]