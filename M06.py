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

def mo6(robot):
  robot.drive_mm(0, 200, 100)
  wait(200)
  robot.pivot(35, 100)
  robot.gyro_drive(0, 200, 630)
  wait(200)
  robot.pivot(55, 100)
  robot.gyro_drive(0, 200, 400)
  robot.pivot(-60, 100)
  robot.drive_mm(0, 150, 200)
  robot.pivot(45, 100)
  robot.act_left.run_time(-700, 1000, wait=False)
  robot.act_right.run_time(700, 400)
  robot.drive_mm(0, 75, 30)
  robot.pivot(30, 250)
  robot.act_right.run_time(-700, 250, wait=False)
  robot.gyro_drive(0, 150, 200)
  robot.pivot(-45, 100)
  wait(150)
  robot.gyro_drive(0, 150, 400)
  robot.pivot(-60, 100)
  wait(150)
  robot.act_right.run_time(-200, 1000, wait=False)
  robot.drive_mm(0, 75, 140)
  robot.act_right.run_time(700, 400)
  wait(100)
  robot.pivot(20, 100)
  robot.drive_mm(0, 200, -100)
  robot.pivot(-90, 100)
  robot.drive_mm(0, 300, -750)