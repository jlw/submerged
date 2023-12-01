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