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
  Commands.Pivot(angle=47, speed=150),
  # Drive to M09 camera
  Commands.GyroDrive(speed=200, distance=450),
  # Capture Camera & Deliver Sam
  Commands.ActMotorTime(motor="right", speed=400, time=900, wait=True),
  Commands.ActMotorTime(motor="left", speed=500, time=900),
  # Back up & move camera to zone
  Commands.DriveMM(speed=200, distance=-150),
  Commands.Pivot(speed=150, angle=-55),
  # Deposit camera
  Commands.ActMotorTime(motor="left", speed=-500, time=800),
  # Leave
  Commands.Pivot(angle=-135, speed=200),
  Commands.DriveMM(speed=250, distance=400)
  ]