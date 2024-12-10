import Commands

def mo2():
  return [
    #drive to mission 2
    Commands.GyroDrive (speed=175, distance=720),
    Commands.Pivot (angle=-57, speed=150),
    #launch the shark
    Commands.GyroDrive (speed=80, distance=65),
    #back up and align with mission 1
    Commands.DriveMM (speed=175, distance=-200),
    Commands.Pivot (angle=-38, speed=150),
    #drive to mission 1
    Commands.GyroDrive (speed=175, distance=93),
    #return to home
    Commands.GyroDrive (speed=175, distance=-90),
    Commands.Pivot (angle=-50, speed=155),
    Commands.GyroDrive (speed=222, distance=750)
  ]