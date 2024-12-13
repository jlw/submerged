import Commands

def m05():
  return [
    # Start
    Commands.GyroDrive(speed=200, distance=403),
    # Turn to sub station
    Commands.Pivot(angle=-48.5),
    # Drive to sub station
    Commands.GyroDrive(speed=200, distance=575),
    # Slow Down
    Commands.GyroDrive(speed=100, distance=75),
    # LineSquare
    Commands.LineSquare(approachSpeed=100, finetuneSpeed=50, returnTime=4500),
    # Backup
    Commands.GyroDrive(speed=80, distance=-15),
    # Turn to angler fish
    Commands.Pivot(speed=80, angle=-71),
    # drive to angler fish
    Commands.GyroDrive(speed=175, distance=246),
    # Scare it away
    Commands.Pivot(speed=100, angle=20),
    # Wait to prevent springing
    Commands.Wait(time=200),
    # Double check
    Commands.GyroDrive(speed=150, distance=10),
    # Backup
    Commands.GyroDrive(speed=150, distance=-10),
    # Turn to coral
    Commands.Pivot(speed=100, angle=35),
    # Lower hook
    Commands.ActMotorTime(motor='right', speed=600, time=1100, wait=False),
    # Drive to the coral
    Commands.GyroDrive(speed=200, distance=300),
    # Agressavly hit coral untill it revives it somehow
    Commands.ActMotorTime(motor='right', speed=600, time=1250),
    # Up
    Commands.ActMotorTime(motor='right', speed=-500, time=1850, wait=False),
    # Backup
    Commands.GyroDrive(speed=200, distance=-90),
    # One wheel turn
    Commands.DriveMotor(motor="right", angle=168, speed=185),
    # Scoop up all nearby wildlife
    Commands.GyroDrive(speed=200, distance=300),
    # Turn to home
    Commands.Pivot(angle=-42),
    # Return to home
    Commands.DriveMM(speed=222, distance=800),
  ]