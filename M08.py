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
    ['drive_mm',[0, 200, 210]],
    ['drive_mm',[0, 250, -380]]
  ]
  return commands