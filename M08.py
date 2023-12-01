def mo8():
  commands = [
    ['pivot',[-90, 100]],
    ['gyro_drive',[-90, 150, 145, 'False']],
    ['pivot',[45, 100]],
    ['gyro_drive',[0, 200, 350, 'True']],
    ['high_tork_time',[400, 4500]],
    ['drive_mm',[0, 150, -310]],
    ['drive_tank',[75, -215, 0]],
    ['drive_mm',[0, 200, 210]],
    ['drive_mm',[0, 250, -380]]
  ]
  return commands