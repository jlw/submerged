import Commands

def mo5():
  return [
    # drive for krill & sample
    Commands.GyroDrive(speed=150, distance=680),
    # turn across back of board
    Commands.Pivot(angle=-90),
    Commands.GyroDrive(speed=150, distance=620),
    # turn slightly to hit angler fish
    # Commands.Pivot(angle=-5),
    # Commands.GyroDrive(speed=150, distance=130),
    Commands.Pivot(angle=15),
    # turn back to avoid ship
    Commands.GyroDrive(speed=150, distance=355),
    Commands.Pivot(angle=-10),
    Commands.GyroDrive(speed=150, distance=150),
    Commands.Pivot(angle=-35),
    Commands.DriveMotor( motor="right", angle=90, speed=150),
    Commands.GyroDrive(speed=150, distance=620)
  ]