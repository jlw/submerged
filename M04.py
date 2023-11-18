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

def mo4a(robot):
  robot.gyro_drive(0, 200, 465)
  robot.pivot(45, 100)
  robot.gyro_drive(0, 150, 150)
  robot.high_tork_time(400, 3000)
  ### Do M02
  robot.gyro_drive(0, 150, 100)
  robot.pivot(45, 100)
  robot.high_tork_time(500, 1000)

def mo4b(robot):
  robot.gyro_drive(0, 200, 200)
  wait(200)
  robot.pivot(45, 100)
  robot.gyro_drive(0, 200, 600)
  wait(200)
  robot.pivot(45, 100)
  robot.act_right.run_time(500, 500, wait=False)
  robot.gyro_drive(0, 100, 60)
  robot.act_right.run_time(-200, 1000)
  