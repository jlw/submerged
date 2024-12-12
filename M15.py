import Commands

def m15():
  return [
    Commands.GyroDrive (speed=250, distance=150),
    Commands.GyroDrive (speed=250, distance=-150),
  ]