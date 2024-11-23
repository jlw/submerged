import Commands

def mo6():
  return [
    Commands.Pivot (angle=180, speed=25),
    Commands.Wait (time=3),
    Commands.Pivot(angle=60, speed=100)
  ]