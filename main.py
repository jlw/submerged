#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.media.ev3dev import Font
from pybricks.parameters import Button, Stop
from pybricks.tools import wait

from robot import Robot_Plus

# import threading
# import _thread
import math

class Master_Main():
  def __init__(self):
    self.ev3 = EV3Brick()
    self.mission_font = Font('lucidia console', size=32, monospace=True)
    self.init_font = Font('lucidia console', size=14, monospace=True)
    self.ev3.screen.set_font(self.mission_font)

  def display_text(text):
    self.ev3.screen.clear()
    self.ev3.screen.draw_text(50, 50, text)

  def start(self):
    self.ev3.screen.set_font(self.init_font)
    self.ev3.screen.print('center: drive tank')
    self.ev3.screen.print('left: run motor comparison')
    self.ev3.screen.print('right: drive_mm')
    waiting = True
    while waiting:
      while self.ev3.buttons.pressed() == []:
        wait(50)
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.CENTER]:
        robot = Robot_Plus()
        robot.drive_tank(3600, 150, 150)
        waiting = False
      elif buttons == [Button.LEFT]:
        waiting = False
        self.ev3.screen.print('motor check:')
        robot = Robot_Plus()
        start_left = robot.lm.angle()
        robot.lm.run(150)
        wait(10000)
        robot.lm.stop()
        end_left = robot.lm.angle()
        diff_left = end_left - start_left
        self.ev3.screen.print('left ran degrees:')
        self.ev3.screen.print(diff_left)
        start_right = robot.rm.angle()
        robot.rm.run(150)
        wait(10000)
        robot.rm.stop()
        end_right = robot.lm.angle()
        diff_right = end_right - start_right
        self.ev3.screen.print('right ran degrees:')
        self.ev3.screen.print(diff_right)
        wait(20000)
        # left 1491
        # right 1516
      elif buttons == [Button.RIGHT]:
        robot = Robot_Plus()
        robot.drive_mm(0, 150, 3000, 500, True)
        print(robot.drive_base.distance())
        waiting = False

master = Master_Main()
master.start()