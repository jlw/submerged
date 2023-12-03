def mo9():
  commands = [
    ['gyro_drive',[0, 150, 440, 'True']],
    ['act_run_time',[-1000, 750, 'right', 'False']],
    ['wait',[350]],
    ['pivot',[-10, 100]],
    ['drive_mm',[0, 150, -100]],
    ['pivot',[-55, 150]],
    ['act_run_time',[300, 1000, 'right', 'True']],
    ['pivot',[20, 100]],
    ['act_run_time',[-700, 500, 'right', 'True']],
    ['pivot',[25, 100]],
    ['drive_mm',[0, 200, -300]],
    ['act_run_time',[1000, 1000, 'right', 'True']],
  ]
  return commands