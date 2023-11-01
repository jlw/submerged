#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.nxtdevices import LightSensor

from robot import Generic_Robot
from robot import Robot_Plus


robot = Robot_Plus()


robot.gyro_drive(0, 150, 2500, 5, 0, 3)
#test 1 gyro drive: P=0, I=0, D=0. deviated: 25mm
#test 2 gyro drive: P=1, I=0, D=0. deviated: 100mm
#test 3 gyro drive: P=3, I=0, D=0. deviated: 15mm
#test 4 gyro drive: P=5, I=0, D=0. deviated: 15mm
#test 5 gyro drive: P=6, I=0, D=0. deviated: 7mm
#test 6 gyro drive: P=6, I=0, D=1. deviated: 13mm
#test 7 gyro drive: P=6, I=0, D=2. deviated: 1mm
#test 8 gyro drive: P=6, I=0, D=1.5. deviated: 10mm
#test 9 gyro drive: P=6, I=0, D=2. deviated: 45mm
#test 10 gyro drive: P=6, I=0, D=3. deviated: 10mm
#test 11 gyro drive: P=6, I=0, D=4. deviated: 1mm
#test 12 gyro drive: P=5, I=0, D=4. deviated: 30mm
#test 13 gyro drive: P=5, I=0, D=3. deviated: 1mm
#test 14 gyro drive: P=2.5, I=0, D=1.5. deviated: 38mm
#test 15 gyro drive: P=2.5, I=0, D=1.5. deviated: 27mm
#test 16 gyro drive: P=1.5, I=0, D=1.2. deviated: 23mm (last years values)
#test 17 gyro drive: P=3, I=0, D=1. deviated: CIRCLESmm (gyro reading 0-300 3s)
#test 18 gyro drive: P=3, I=0, D=1. deviated: 45mm (fixed circle bug)
#test 19 gyro drive: P=5, I=0, D=3. deviated: 70mm