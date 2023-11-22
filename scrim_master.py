#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from robot import Robot_Plus

from M09 import mo9
from M06 import mo6
from M08 import mo8
from M02 import mo2

robot = Robot_Plus()
img = ImageFile()

def start(robot):
  button_press = robot.ev3.buttons.pressed()
  while True:
    # M09 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    wait(100)
    mo9(robot)
    break

  while True:
    # M04 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    wait(100)
    mo4b(robot)
    break

  while True:
    # M08 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    wait(100)
    mo8(robot)
    break