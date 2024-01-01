import Commands

def mo8():
  commands = [
    ['gyro_drive',[0, 150, 60, 'True']],
    ['pivot',[-100, 100]],
    ['gyro_drive',[0, 150, 300, 'True']],
    ['pivot',[45, 100]],
    ['gyro_drive',[0, 200, 350, 'True']],
    ['high_tork_time',[400, 4750]],
    ['drive_mm',[0, 150, -300]],
    ['pivot',[-55, 100]],
    ['drive_mm',[0, 200, 190]],
    ['drive_mm',[0, 250, -380]]
  ]

  return [
    Commands.GyroDrive(speed=150, distance=60),
    Commands.Pivot(angle=-100, speed=100),
    Commands.GyroDrive(speed=150, distance=300),
    Commands.Pivot(angle=45, speed=100),
    Commands.GyroDrive(speed=200, distance=350),
    Commands.ActMotorTime(motor='left', time=4750, speed=400),
    Commands.DriveMM(angle=0, speed=150, distance=-300),
    Commands.Pivot(angle=-55, speed=100),
    Commands.DriveMM(angle=0, speed=200, distance=190),
    Commands.DriveMM(angle=0, speed=250, distance=-380)
  ]