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
from master import Master_Main

from M09 import mo9
from M08 import mo8
from M06 import mo6
from M02 import mo2
from M15 import m15

import _thread
import time

robot = Robot_Plus()
master = Master_Main()

master.module()