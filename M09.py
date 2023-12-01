def mo9():
  commands = [
    ['gyro_drive',[0, 150, 455]],
    ['act_right.run_time',[-1000, 600, 'wait=False']],
    ['wait',[350]],
    ['pivot',[-10, 100]],
    ['drive_mm',[0, 150, -100]],
    ['pivot',[-55, 150]],
    ['act_right.run_angle',[120, 100]],
    ['pivot',[45, 100]],
    ['drive_mm',[0, 200, -300]],
    ['act_right.run_time',[1000, 500]]
  ]
  return commands