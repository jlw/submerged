import Commands

def m09():
  return [
    # Ram the Quatropus
    Commands.GyroDrive(speed=250, distance=350),
    # Return
    Commands.ActMotorTime(motor='right', speed=-550, time=1850, wait=False),
    Commands.DriveMM(speed=300, distance=-400),
    
  ]