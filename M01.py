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

def mo1(robot):
  robot.drive_mm(0, 500, 250)
  robot.pivot(90, 500)
  robot.drive_mm(0, 500, 100)
  robot.act_right.turn_angle(300, 180)