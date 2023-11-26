from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, Image, ImageFile

from M09 import mo9

class Master_Main():
  def __init__(self):
    self.ev3 = EV3Brick()
    self.missions = []

  def start(self):
    step = 0
    while step < 5:
      print("Initializing ")
      wait(200)
      print("Initializing .")
      wait(200)
      print("Initializing . .")
      wait(200)
      print("Initializing . . .")
      step = step + 1
    print("Ready")
    module()

  def module(self):
    run_num = 0
    while True:
      if self.ev3.buttons.pressed == [CENTER]:
        # Play current module
        play_mission(run_num)
      elif self.ev3.buttons.pressed == [RIGHT]:
        # Move to next module
        if run_num >= self.mission.len():
          run_num = 0
        else:
          run_num += 1
      elif self.ev3.buttons.pressed == [LEFT]:
        # Move to last module
        if run_num <= 0:
          run_num = self.missions.len()
        else:
          run_num -= 1
      
      display()

  def play_mission(self, run_number):
    self.missions[mission_number].run()

  def display(self):
    