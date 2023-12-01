def mo8():
  commands = [
    ['pivot',[-90 100]],
    ['gyro_drive',[-90, 150, 145, 'reset_sensor=False']],
    ['pivot',[45, 100]],
    ['gyro_drive',[0, 200, 350]],
    ['high_tork_time',[400, 4500]],
    ['drive_mm',[0, 150, -310]],
    ['left_motor.run_angle',[75, -215]],
    ['drive_mm',[0, 200, 210]],
    ['drive_mm',[0, 250, -380]]
  ]
  return commands