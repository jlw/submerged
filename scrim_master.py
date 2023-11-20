
from robot import Robot_Plus

from M09 import mo9
from M04 import mo4b
from M08 import mo8

robot = Robot_Plus()
button_press = robot.ev3.buttons.pressed()

while True:
  # M09 #
  while button_press != [CENTER]:
    # check for advancing to next
    if button_press == [DOWN]:
      break
  mo9(robot)
  break

while True:
  # M04 #
  while button_press != [CENTER]:
    # check for advancing to next
    if button_press == [DOWN]:
      break
  mo4b(robot)
  break

while True:
  # M08 #
  while button_press != [CENTER]:
    # check for advancing to next
    if button_press == [DOWN]:
      break
  mo8(robot)
  break