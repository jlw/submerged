from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (ColorSensor, GyroSensor)
from pybricks.media.ev3dev import SoundFile
from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot_Plus

from M09 import mo9
from M08 import mo8
from M06 import mo6
from M02 import mo2
from M14 import m14

import threading
import _thread

class Master_Main():
  def __init__(self):
    self.robot = Robot_Plus()
    self.ev3 = EV3Brick()
    self.missions = [["M06", mo6()], ["M08", mo8()], ["M14", m14()], ["M02", mo2()], ["M09", mo9()]]
    self.wait_for_mission_end = True
    self.has_aborted = False
    self.count = 0

  def display(self, run_num):
    current_mission = self.missions[run_num]
    self.ev3.screen.clear()
    self.ev3.screen.draw_text(10, 10, current_mission[0])
    wait(500)

  def play(self, run_number):
    run = self.missions[run_number]
    commands = run[1]
    for command in commands:
      if self.has_aborted:
        print("Mission has been aborted.")
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
      wait(500)
    
    if drift:
      self.ev3.screen.draw_text(55, 80, "Drifting.")
      self.ev3.screen.clear()
      self.display(0)
      wait(2000)
    elif drift == False:
      self.ev3.screen.draw_text(55, 80, "No Drift.")
      self.ev3.screen.clear()
      self.display(0)
      wait(2000)

  def start(self):
    cal_g = threading.Thread(target=self.calibrate_gyro)
    cal_g.start()

    while self.count < 10:
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

    self.ev3.screen.clear()
    self.ev3.screen.draw_text(60, 60, "Ready!")
    self.ev3.speaker.beep(duration=200)
    wait(1000)

    self.robot.calibrate_color()
    
    self.display(0)
    self.module()