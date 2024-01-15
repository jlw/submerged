import Commands

def m14():
  commands = [
    ['gyro_drive',[0, 150, 100, 'True']],
    ['pivot',[-110, 100]],
    ['gyro_drive',[0, 150, 750, 'True']]
  ]
  return [
    Commands.LineSquare(target=20, targetBlack=13, targetWhite=80, approachSpeed=150, finetuneSpeed=50)
  ]