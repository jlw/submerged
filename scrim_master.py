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
from M04 import mo4b
from M08 import mo8

robot = Robot_Plus()
img = ImageFile()
button_press = robot.ev3.buttons.pressed()

def start(robot):
  while True:
    # M09 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    mo9(robot)
    break

  while True:
    # M04 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    mo4b(robot)
    break

  while True:
    # M08 #
    while button_press != [Button.CENTER]:
      # check for advancing to next
      if button_press == [Button.DOWN]:
        break
    mo8(robot)
    break