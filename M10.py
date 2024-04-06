import Commands

def m10():
  return [
  # Drive to M10
  Commands.GyroDrive(speed=150, distance=15),
  Commands.Pivot(angle=42, speed=150),
  # Push M10
  Commands.GyroDrive(speed=175, distance=600),
  # Back up & align with M09
  Commands.DriveMM(speed=200,distance=-400),
  Commands.Pivot(angle=48, speed=150),
  # Drive to M09 camera
  Commands.GyroDrive(speed=200, distance=420),
  # Capture Camera & Deliver Sam
  Commands.ActMotorTime(motor="right", speed=400, time=900, wait=False),
  Commands.ActMotorTime(motor="left", speed=500, time=900, wait=True),
  # Back up & move camera to zone
  Commands.DriveMM(speed=200, distance=-150),
  Commands.Pivot(speed=150, angle=-45),
  # Deposit camera
  Commands.ActMotorTime(motor="left", speed=-500, time=800),
  # Leave
  Commands.DriveMM(speed=200, distance=-100),
  Commands.Pivot(angle=45, speed=500),
  Commands.DriveMM(distance=-250, speed=500)
  ]