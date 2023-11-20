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

def mo8(robot):
  robot.pivot(-90, 75)
  robot.gyro_drive(-90, 150, 145, reset_sensor=False)
  robot.pivot(45, 75)
  robot.drive_mm(0, 200, 350)
  robot.high_tork_time(400, 4500)
  robot.drive_mm(0, 150, -310)
  robot.left_motor.run_angle(75, -215)
  robot.drive_mm(0, 200, 180)
  robot.drive_mm(0, 250, -380)