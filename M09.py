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

def mo9(robot):
  robot.gyro_drive(0, 150, 455)
  robot.act_right.run_time(-1000, 600, wait=False)
  wait(350)
  robot.pivot(-10, 100)
  robot.drive_mm(0, 150, -100)
  robot.pivot(-55, 150)
  robot.act_right.run_angle(120, 100)
  robot.pivot(45, 100)
  robot.drive_mm(0, 200, -300)
  robot.act_right.run_time(1000, 500)