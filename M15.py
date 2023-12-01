#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from robot import Robot_Plus

robot = Robot_Plus()

def m15(robot):
  robot.pivot(-75, 100)
  robot.gyro_drive(0, 200, 250)
  robot.pivot(-30, 100)
  robot.gyro_drive(0, 200, 500)
  robot.pivot(-25, 100)