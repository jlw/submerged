import Commands

def mo3():
  return [
    Commands.GyroDrive (speed=150, distance=100),
    Commands.GyroDrive (speed=150, distance=-100),
  ]