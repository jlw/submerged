import Commands

def mo6():
  commands = [
    ['act_run_time',[700, 400, 'right', 'True']],
    ['wait',[100]],
    ['pivot',[20, 100]],
    ['drive_mm',[0, 200, -100]],
    ['pivot',[-90, 100]],
    ['drive_mm',[0, 300, -750]]
  ]
  return [
    Commands.ActMotorTime(motor="right", speed=500, time=500, wait=False),
    Commands.DriveMM(speed=150, distance=300),
    Commands.ActMotorTime(motor="right", speed=-400, time=700, wait=False),
    Commands.Wait(time=300),
    Commands.Pivot(angle=10, speed=20),
    Commands.Wait(time=300),
    Commands.DriveMM(speed=150, distance=-200),
    Commands.Pivot(angle=60, speed=100),
    Commands.GyroDrive(speed=150, distance=250),
    Commands.Pivot(angle=-60, speed=100),
    Commands.Wait(time=300),
    Commands.GyroDrive(speed=150, distance=400),
    Commands.Pivot(angle=85, speed=100),
    Commands.GyroDrive(speed=200, distance=500),
    Commands.Pivot(angle=-60, speed=100),
    Commands.DriveMM(speed=150, distance=200),
    Commands.Pivot(angle=45, speed=100),
    Commands.ActMotorTime(motor="left", speed=-700, time=1000, wait=False),
    Commands.ActMotorTime(motor="right", speed=700, time=600),
    Commands.DriveMM(speed=75, distance=30),
    Commands.Pivot(angle=30, speed=250),
    Commands.ActMotorTime(motor="right", speed=-700, time=250, wait=False),
    Commands.GyroDrive(speed=150, distance=200),
    Commands.Pivot(angle=-45, speed=100),
    Commands.Wait(time=150),
    Commands.GyroDrive(speed=150, distance=400),
    Commands.Pivot(angle=-45, speed=100),
  ]