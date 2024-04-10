import Commands

def mo8():
  return [
  # Inch forward
  Commands.DriveMM(speed=150, distance=25),
  #Pivot to face camera
  Commands.Pivot(angle=-92, speed=80),
  # Drive & stab the rollar coaster
  Commands.GyroDrive(speed=200, distance=300),
  # Retreat
  Commands.DriveMM(speed=200, distance=-190),
  # Aim for pablo
  Commands.Pivot(angle=50, speed=150),
  # Target accquired, push forward
  Commands.GyroDrive(speed=200, distance=350),
  # Impale Izzy
  Commands.ActMotorTime(motor='right', speed=-250, time=600),
  # Align for overspun poultry
  Commands.DriveMM(speed=150, distance=20),
  Commands.ActMotorTime(motor='left', speed=200, time=250),
  # Progressively make pablo more dizzy
  Commands.ActMotorTime(motor='left', speed=-999, time=3500),
  # Escape the crime scene
  Commands.DriveMM(speed=250, distance=-200),
  # Change course for safe house
  Commands.Pivot(speed=250, angle=-30),
  # Bunker down
  Commands.DriveMM(speed=250, distance=-500),
]