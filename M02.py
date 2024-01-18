import Commands

def mo2():
  commands = [
    ['gyro_drive',[0, 150, 100, 'True']],
    ['pivot',[30, 100]],
    ['gyro_drive',[0, 150, 550, 'True']],
    ['pivot',[-90, 100]],
    ['gyro_drive',[0, 150, 100, 'True']],
    ['drive_mm',[0, 150, -50]],
    ['pivot',[60, 100]],
    ['drive_mm',[0, 500, -800]]
  ]
  return [
    # Drive towards M01 & lower left arm
    Commands.ActMotorTime(motor="left", speed=400, time=300, wait=False),
    Commands.GyroDrive(speed=150, distance=150),
    # Drive bewteen M01 and M10
    Commands.Pivot(speed=100, angle=60),
    Commands.GyroDrive(speed=150, distance=280),
    Commands.Pivot(speed=100, angle=-60),
    Commands.ActMotorTime(motor="left", speed=500, time=700, wait=False),
    Commands.GyroDrive(speed=150, distance=280),
    # Pivot into place next to M02 & deliver izzy
    Commands.Pivot(angle=-45, speed=100),
    Commands.ActMotorAngle(motor="right", speed=400, angle=340),
    Commands.Wait(time=600),
    Commands.ActMotorTime(motor="right", speed=-700, time=500, wait=False),
    # Push M02
    Commands.DriveMM(speed=75, distance=70),
    Commands.ActMotorTime(speed=-400, motor="left", time=1700, wait=False),
    # Return to home
    Commands.DriveMM(speed=75, distance=-100),
    Commands.Pivot(speed=100, angle=60),
    Commands.DriveMM(speed=200, distance=-600)
  ]