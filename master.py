from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (ColorSensor, GyroSensor)
from pybricks.parameters import Button
from pybricks.tools import wait

from robot import Robot_Plus

from M09 import mo9
from M08 import mo8
from M06 import mo6
from M02 import mo2
from M15 import m15

import threading
import _thread

robot = Robot_Plus()

class Master_Main():
  def __init__(self):
    self.ev3 = EV3Brick()
    self.missions = [["M09", mo9], ["M02", mo2], ["M06", mo6], ["M08", mo8], ["M15", m15]]
    self.wait_for_mission_end = True
    self.has_aborted = False

  def display(self, run_num):
    current_mission = self.missions[run_num]
    self.ev3.screen.clear()
    self.ev3.screen.draw_text(10, 10, current_mission[0])
    wait(500)

  def play(self, run_number):
    run = self.missions[run_number]
    mission = run[1]
    commands = mission(robot)
    for command in commands:
      if self.has_aborted:
        print("Mission has been aborted.")
        self.has_aborted = False
        break
      getattr(robot, command[0])(*command[1])

    print(run[0])
    self.wait_for_mission_end = False

  def play_mission(self, run_number):
    _thread.start_new_thread(self.play, (run_number))

    while True:
      while self.ev3.buttons.pressed() == []:
          wait(0)
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.DOWN]:
        self.has_aborted = True
        self.wait_for_mission_end = False
        break
      if self.wait_for_mission_end == False:
        break
    self.wait_for_mission_end = True

  def module(self):
    run_num = 0

    while True:
      while self.ev3.buttons.pressed() == []:
        wait(0)
      buttons = self.ev3.buttons.pressed()
      if buttons == [Button.CENTER]:
          # Play current module
          robot.gyro_sensor.reset_angle(0)
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
    gyro_drift = False
    error = []
    no_drift = 0
    while self.ev3.buttons.pressed() != [Button.CENTER]:
      angle = robot.gyro_sensor.angle()
      error.append(angle)
      for x in error:
        if x == 0:
          no_drift += 1
      if no_drift >= 50:
        gyro_drift = False
        break

      if len(error) > 10:
        gyro_drift = True
        break
      
      wait(500)
    
    self.ev3.screen.draw_text(50, 80, gyro_drift)
    print("Gyro Drift is", gyro_drift)
    return gyro_drift

  def start(self):
    cal_g = threading.Thread(target=self.calibrate_gyro)
    cal_g.start()

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
    wait(1000)

    self.display(0)
    self.module()