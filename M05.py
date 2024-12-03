import Commands

def mo5():
  return [
    Commands.GyroDrive(speed=150, distance=200),
    Commands.Pivot(angle=-35),
    Commands.GyroDrive(speed=150, distance=225),
    Commands.GyroDrive(speed=150, distance=-50),
    Commands.Pivot(angle=65),
    Commands.GyroDrive(speed=175, distance=130),
    Commands.Pivot(angle=-30),
    Commands.DriveMM(speed=175, distance=240, angle=-44),
    Commands.DriveMM(speed=175, distance=250, angle=13),
    #Commands.GyroDrive(speed=150, distance=50),
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=5000),
    Commands.DriveMM(speed=150, distance=-750, angle=-40),
    #Commands.GyroDrive(speed=175, distance=150), 
    
  ]