import Commands

def m09():
  return [
    # Ram the Quatropus
    Commands.GyroDrive(speed=250, distance=350),
    # Hook up
    Commands.ActMotorTime(motor='right', speed=-550, time=1850, wait=False),
    # Return
    Commands.DriveMM(speed=300, distance=-400),
    
  ]