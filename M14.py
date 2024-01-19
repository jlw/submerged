import Commands

def m14():
  return [
    Commands.DriveMM(angle=12, speed=125, distance=355),
    Commands.Wait(time=75),
    Commands.DriveMM(angle=-14, speed=125, distance=270),
    Commands.Wait(time=75),
    Commands.ActMotorTime(motor='left', speed=-250, time=1000, wait=False),
    Commands.GyroDrive(angle=0, speed=150, distance=260, reset_sensor=False),
    Commands.ActMotorTime(motor='right', speed=-250, time=1000),
    Commands.ActMotorTime(motor='left', speed=250, time=1000),
    Commands.GyroDrive(speed=100, distance=240),
    Commands.GyroDrive(speed=200, distance=800),
  ]