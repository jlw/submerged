def mo2():
  commands = [
    ['gyro_drive',[0, 150, 100, 'True']],
    ['pivot',[30, 100]],
    ['gyro_drive',[0, 150, 100, 'True']],
    ['pivot',[-90, 100]],
    ['gyro_drive',[0, 150, 100, 'True']],
    ['drive_mm',[0, 150, -50]],
    ['pivot',[60, 100]],
    ['drive_mm',[0, 500, -800]]
  ]
  return commands