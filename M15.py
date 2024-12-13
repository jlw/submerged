import Commands

def m15():
  return [
    # Out to dump
    Commands.GyroDrive (speed=250, distance=150),
    # Return to home
    Commands.GyroDrive (speed=250, distance=-150),
  ]