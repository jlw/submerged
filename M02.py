def mo2():
  commands = [
    ['gyro_drive',[0, 150, 100]],
    ['pivot',[30, 100]],
    ['gyro_drive',[0, 150, 100]],
    ['pivot',[-90, 100]],
    ['gyro_drive',[0, 150, 100]],
    ['drive_mm'],[0, 150, -50],

    #this is for pink add this code to add more pushes

    #robot.gyro_drive(0, 150, 50)
    # robot.drive_mm(0, 150, -50)

    ['pivot',[60, 100]],
    ['drive_mm',[0, 500, -800]]
  ]
  return commands