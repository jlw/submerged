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
    Commands.GyroDrive(speed=150, distance=70),
    Commands.Pivot(angle=-62),
    Commands.GyroDrive(speed=150, distance=220),
    Commands.Pivot(angle=-30),
    
    
    #Commands.LineSquare(targetBlack=80, targetWhite=13, target=20, approachSpeed=100, finetuneSpeed=50, returnTime=2000)
    
    #Commands.GyroDrive(speed=150, distance=350),
  ]