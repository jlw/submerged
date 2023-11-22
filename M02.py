#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor

from robot import Robot_Plus

robot = Robot_Plus()

def mo2(robot):
  robot.gyro_drive(0, 150, 200)
  robot.pivot(45, 50)
  robot.gyro_drive(0, 150, 400)
  robot.pivot(-45, 50)
  robot.gyro_drive(0, 150, 130)
  robot.pivot(-45, 50)
  robot.gyro_drive(0, 150, 50)
  robot.drive_mm(0, 150, -50)


  #this is for pink add this code to add more pushes

  #robot.gyro_drive(0, 150, 50)
  # robot.drive_mm(0, 150, -50)

  robot.pivot(60, 50)
  robot.drive_mm(0, 250, -800)