from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, Image, ImageFile

from robot import Robot_Plus

from M09 import mo9
from M08 import mo8
from M06 import mo6
from M02 import mo2
from M15 import m15

robot = Robot_Plus()

class Master_Main():
  def __init__(self):
    self.ev3 = EV3Brick()
    self.missions = [["M09", mo9], ["M02", mo2], ["M06", mo6], ["M08", mo8], ["M15", m15]]

  def display(self, run_num):
    current_mission = self.missions[run_num]
    self.ev3.screen.clear()
    self.ev3.screen.draw_text(10, 10, current_mission[0])
    wait(500)

  def play_mission(self, run_number):
    run = self.missions[run_number]
    mission = run[1]
    mission(robot)
    print(self.missions[run_number])

  def module(self):
    run_num = 0

    while True:
      while self.ev3.buttons.pressed() == []:
        #do nothing
        r = 0
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.CENTER]:
          print("play")
          # Play current module
          self.play_mission(run_num)
          run_num += 1
          if run_num >= len(self.missions) - 1:
            run_num = 0
      elif buttons == [Button.RIGHT]:
        # Move to next module
        if run_num >= len(self.missions) - 1:
          run_num = 0
        else:
          run_num += 1
      elif buttons == [Button.LEFT]:
        # Move to last module
        run_num -= 1
        if run_num <= -1:
          run_num = len(self.missions) - 1

      self.display(run_num)
        


    #old code
    while False:
      if self.ev3.buttons.pressed() == [Button.CENTER]:
        print("play")
        # Play current module
        self.play_mission(run_num)
      elif self.ev3.buttons.pressed() == [Button.RIGHT]:
        # Move to next module
        if run_num >= len(self.missions) - 1:
          run_num = 0
        else:
          run_num += 1
      elif self.ev3.buttons.pressed() == [Button.LEFT]:
        # Move to last module
        run_num -= 1
        if run_num <= -1:
          run_num = len(self.missions) - 1
      
      self.display(run_num)

  def start(self):
    step = 0
    while step < 5:
      #calibrate gyro & color sensors at same time
      
      self.ev3.screen.clear()
      self.ev3.screen.draw_text(10, 10, "Initializing ")
      wait(200)

      self.ev3.screen.clear()
      self.ev3.screen.draw_text(10, 10, "Initializing .")
      wait(200)

      self.ev3.screen.clear()
      self.ev3.screen.draw_text(10, 10, "Initializing . .")
      wait(200)

      self.ev3.screen.clear()
      self.ev3.screen.draw_text(10, 10, "Initializing . . .")
      wait(200)

      step = step + 1

    self.ev3.screen.clear()
    self.ev3.screen.draw_text(60, 60, "Ready!")
    self.ev3.speaker.beep(duration=200)
    wait(500)

    self.display(0)
    self.module()