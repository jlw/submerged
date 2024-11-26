import Commands

def mo9():
  return{
    Commands.GyroDrive(speed=300 distance=200)
    Commands.Pivot(angle=-45 speed=200)
    Commands.GyroDrive(speed=300 distance=250)
    Commands.GyroDrive(speed=500 distance=400)
  }