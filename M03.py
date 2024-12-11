import Commands

def mo3():
  return [
    Commands.GyroDrive (speed=75, distance=100),
    Commands.GyroDrive (speed=75, distance=-100),
  ]