import Commands

def mo2():
  return [
    #drive to mission 2
    Commands.GyroDrive (speed=150, distance=720),
    Commands.Pivot (angle=-45, speed=150),
    #launch the shark
    Commands.GyroDrive (speed=50, distance=360),
    #back up and align with mission 1
    Commands.DriveMM (speed=150, distance=620),
    Commands.Pivot (angle=27, speed=150),
    #drive to mission 1
    Commands.GyroDrive (speed=150, distance=320)
  ]