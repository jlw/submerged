import Commands

def m14():
  commands = [
    ['gyro_drive',[0, 150, 100, 'True']],
    ['pivot',[-110, 100]],
    ['gyro_drive',[0, 150, 750, 'True']]
  ]
  return [
    Commands.LineSquare(target=10, targetBlack=10, targetWhite=85, approachSpeed=100, finetuneSpeed=25)
  ]