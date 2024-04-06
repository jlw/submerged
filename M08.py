import Commands

def mo8():
  return [
  # Reset Arm for Izzy
  # Drive Forward and Pivot to face M08
  Commands.DriveMM(speed=150, distance=25),
  Commands.Pivot(angle=-95, speed=80),
  # Drive to & Push M08
  Commands.GyroDrive(speed=200, distance=340),
  # Back up & aim for pablo
  Commands.DriveMM(speed=200, distance=-190),
  Commands.Pivot(angle=50, speed=150),
  # *BRZZZT*  Mayday! Mayday! Chicken ahead! AAAAHHHHHH! *BRRZzzt*
  Commands.GyroDrive(speed=200, distance=345),
  # Yoink Izzy, Spin pablo
  Commands.ActMotorTime(motor='right', speed=-250, time=1750, wait=False),
  Commands.ActMotorTime(motor='left', speed=-99999, time=1250),
  # Escape the crime scene
  Commands.DriveMM(speed=250, distance=-200),
  Commands.Pivot(speed=250, angle=-25),
  Commands.DriveMM(speed=250, distance=-400),
]