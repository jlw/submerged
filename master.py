from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (ColorSensor, GyroSensor)
from pybricks.media.ev3dev import SoundFile, Image, Font
from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot_Plus

from M10 import m10
from M08 import mo8
from M06 import mo6
from M02 import mo2
from M14 import m14

import threading
import _thread
import math

class Master_Main():
  def __init__(self):
    self.robot = Robot_Plus()
    self.ev3 = EV3Brick()
    self.missions = [["M06", mo6()], ["M08", mo8()], ["M14", m14()], ["M02", mo2()], ["M10", m10()]]
    self.wait_for_mission_end = True
    self.has_aborted = False
    self.count = 0
    self.mission_font = Font('lucidia console', size=32, monospace=True)
    self.init_font = Font('lucidia console', size=24, monospace=True)
    self.ev3.screen.set_font(self.init_font)

    self.init_images = ["IMAGES/init-1", "IMAGES/init-2", "IMAGES/init-3", "IMAGES/init-4", "IMAGES/init-5", "IMAGES/init-6"]

  def display(self, run_num):
    current_mission = self.missions[run_num]
    self.ev3.screen.clear()
    self.ev3.screen.draw_text(50, 50, current_mission[0])
    wait(500)

  def play(self, run_number):
    run = self.missions[run_number]
    commands = run[1]
    for command in commands:
      if self.has_aborted:
        self.ev3.speaker.beep()
        self.has_aborted = False
        break
      command.run(self.robot)
    commands = []

    print(run[0])
    self.wait_for_mission_end = False

  def play_mission(self, run_number):
    self.wait_for_mission_end = True
    _thread.start_new_thread(self.play, (run_number))

    while self.wait_for_mission_end:
      while self.ev3.buttons.pressed() == []:
        wait(50)
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.DOWN]:
        self.has_aborted = True
        self.ev3.speaker.play_file(SoundFile.GENERAL_ALERT)
    print("Mission has been aborted.")
    #self.robot.reset_motors(1)

  def module(self):
    run_num = 0

    while True:
      while self.ev3.buttons.pressed() == []:
        wait(50)
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.CENTER]:
          # Play current module
          self.robot.gyro_sensor.reset_angle(0)
          self.play_mission(tuple([run_num]))
          run_num += 1
          if run_num >= len(self.missions):
            run_num = 0
          print("playing", run_num)
      elif buttons == [Button.RIGHT]:
        # Move to next module
        if run_num >= len(self.missions) - 1:
          run_num = 0
        else:
          run_num += 1
        print("moved right", run_num)
      elif buttons == [Button.LEFT]:
        # Move to last module
        run_num -= 1
        if run_num <= -1:
          run_num = len(self.missions) - 1
        print("moved left", run_num)

      self.display(run_num)
    
  def calibrate_gyro(self):
    error = 0
    self.count = 0
    drift = False
    while self.ev3.buttons.pressed() != [Button.CENTER]:
      if error != 0:
        print("Gyro is drifing!")
        drift = True
        break

      if self.count >= 10:
        print("No drift here!")
        drift = False
        break
  
      error = (self.robot.gyro_sensor.angle())
      self.count += 1
      print("Error is", error,". . ", "Looped", self.count, "times.")
      wait(1000)

  def start(self):
    cal_g = threading.Thread(target=self.calibrate_gyro)
    cal_g.start()

    while self.count < 10:
      # Calibrate gyro & color sensors

      num = math.floor((6 * self.count) / 10)
      self.ev3.screen.clear()
      self.ev3.screen.draw_image(10, 10, self.init_images[num])
      wait(900)
    #self.ev3.speaker.beep(duration=200)
    for x in range(0, 3):
      self.ev3.screen.clear()
      self.ev3.screen.draw_image(10, 10, "IMAGES/ready-1")
      self.ev3.speaker.beep(frequency=440, duration=200)
      self.ev3.screen.clear()
      self.ev3.screen.draw_image(10, 10, "IMAGES/ready-2")
      wait(200)
    self.ev3.screen.clear()
    self.ev3.screen.draw_image(10, 10, "IMAGES/ready-1")
    wait(200)

    self.robot.calibrate_color()
    
    self.ev3.screen.set_font(self.mission_font)
    self.display(0)
    self.module()