import Commands

def m03():
  return [
    Commands.GyroDrive (speed=75, distance=100),
    Commands.GyroDrive (speed=75, distance=-100),
  ]