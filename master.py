from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, Image, ImageFile


class Master_Main():
  def __init__(self):
    self.ev3 = EV3Brick()
    self.missions = []

  def display(self):
    yes = 0

  def play_mission(self, run_number):
    self.missions[mission_number].run()

  def module(self):
    run_num = 0
    while True:
      if self.ev3.buttons.pressed == [Button.CENTER]:
        # Play current module
        self.play_mission(run_num)
      elif self.ev3.buttons.pressed == [Button.RIGHT]:
        # Move to next module
        if run_num >= self.mission.len():
          run_num = 0
        else:
          run_num += 1
      elif self.ev3.buttons.pressed == [Button.LEFT]:
        # Move to last module
        if run_num <= 0:
          run_num = self.missions.len()
        else:
          run_num -= 1
      
      self.display()

  def start(self):
    step = 0
    while step < 5:
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
    self.ev3.screen.draw_text(50, 60, "Ready!")
    self.ev3.speaker.beep(duration=200)
    wait(500)
    
    self.module()