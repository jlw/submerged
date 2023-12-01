def mo9():
  commands = [
    ['gyro_drive',[0, 150, 455, 'True']],
    ['act_run_time',[-1000, 600, 'right', 'False']],
    ['wait',[350]],
    ['pivot',[-10, 100]],
    ['drive_mm',[0, 150, -100]],
    ['pivot',[-55, 150]],
    ['act_run_angle',[120, 100, 'right', 'True']],
    ['pivot',[45, 100]],
    ['drive_mm',[0, 200, -300]],
    ['act_run_time',[1000, 500, 'right', 'True']]
  ]
  return commands