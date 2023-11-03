from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.nxtdevices import LightSensor

from pid import PIDController


class Generic_Robot:
  def __init__(self, EV3Brick, DriveBase, LeftMotor, RightMotor, LightSensorLeft, LightSensorRight, GyroSensor):
    self.ev3 = EV3Brick
    self.robot = DriveBase
    self.lm = LeftMotor
    self.rm = RightMotor
    self.sen1 = LightSensorLeft
    self.sen2 = LightSensorRight
    self.gyro = GyroSensor
    self.stopWatch = StopWatch()

  ### DRIVE MILIMETERS ###
  def drive_mm(self, angle, speed, mm, rate=500, brake=True):
    self.robot.reset()
    if angle == 0:
      self.robot.settings(speed, rate)
      self.robot.straight(mm)
    else:
      while self.robot.distance() < mm:
        self.robot.drive(speed, angle)
    self.robot.stop()
    self.lm.brake()
    self.rm.brake()
  
  ### PIVOT ANGLE ###
  def pivot(self, angle, speed, rate=500):
    self.robot.settings(speed, rate, speed, rate)
    self.robot.turn(angle)
    self.robot.stop()
    self.lm.brake()
    self.rm.brake()

  ### DRIVE GYRO MILIMETERS ###
  def gyro_drive(self, angle, speed, distance_mm, gainP=6, gainI=0.15, gainD=1.5, reset_sensor=True):
    if reset_sensor == True:
      self.gyro.reset_angle(0)
    pid_controller = PIDController(gainP, gainI, gainD)
    while self.robot.distance() < distance_mm:
      self.robot.drive(speed, pid_controller.adjust(angle - self.gyro.angle()))
      print(self.gyro.angle(), self.robot.state())
    self.robot.stop()
    self.lm.brake()
    self.rm.brake()

  ### ULTIMATE LINE SQUARING ###
  def black_line_square(self, target, targetBlack, targetWhite, approachSpeed, finetuneSpeed):
    def __waitUntil(sensor, input1):
      while sensor.reflection() <= input1:
        wait(0)
    def __colorIsInRange(value):
      if targetBlack <= value and targetWhite >= value:
        return True
      else:
        return False
    # Initiate Variables
    ev3.light.on(Color.RED)
    stopWatch.pause()
    stopWatch.reset()
    stopWatch.resume()
    reverseFinetuneSpeed = (0 - finetuneSpeed)
    ref1 = sen1.reflection()
    ref2 = sen2.reflection()
    # Roughly lines up with the black line
    robot.drive(approachSpeed)
    while True:
      if sen1.reflection() <= target:
        robot.stop()
        lm.hold()
        rm.run(approachSpeed)
        waitUnitl(sen2, target)
        rm.hold()
        break
      elif sen2.reflection() <= target:
        robot.stop()
        rm.hold()
        lm.run(approachSpeed)
        waitUntil(sen1, target)
        lm.hold()
        break
    # Sets status light to Yellow for fine tuning
    ev3.light.on(Color.YELLOW)
    while (colorIsInRange(ref1) and colorIsInRange(ref2)) or stopWatch.time() == returnTime:
      # Fine tunes the left motor
      if sen1.reflection() < targetBlack:
        lm.run(reverseFinetuneSpeed)
      elif sen1.reflection() > targetWhite:
        lm.run(finetuneSpeed)
      else:
        lm.hold()
      # Fine tunes the right motor
      if sen2.reflection() < targetBlack:
        rm.run(reverseFinetuneSpeed)
      elif sen2.reflection() > targetWhite:
        rm.run(finetuneSpeed)
      else:
        rm.hold()
      ref1 = sen1.reflection()
      ref2 = sen2.reflection()
    ev3.light.on(Color.GREEN)


class Robot_Plus(Generic_Robot):
  def __init__(self, name = "Bilbo"):

    ############################################
    ### THIS MUST BE CONFIGURED TO THE ROBOT ###             
    ############################################

    self.name = name
    self.ev3 = EV3Brick()
    self.left_motor = Motor(Port.B, Direction.CLOCKWISE, gears=None)
    self.right_motor = Motor(Port.C, Direction.CLOCKWISE, gears=None)
    self.act_right = Motor(Port.A, Direction.CLOCKWISE, gears=None)
    self.act_left = Motor(Port.D, Direction.CLOCKWISE, gears=None)
    self.drive_base = DriveBase(self.left_motor, self.right_motor, 57, 120)
    #self.infared = InfraredSensor(Port.S1)
    self.left_color = ColorSensor(Port.S1)
    self.right_color = ColorSensor(Port.S2)
    self.gyro_sensor = GyroSensor(Port.S3)
    Generic_Robot.__init__(self, self.ev3, self.drive_base, self.left_motor, self.right_motor, self.left_color, self.right_color, self.gyro_sensor)
  
  def query(self):
    return self.name

  def high_tork_angle(self, angle, speed):
    self.act_right.run_angle(speed, angle, wait=False)
    self.act_left.run_angle(speed, angle)
  
  def high_tork_time(self, time, speed):
    self.act_right.run_time(speed, time, wait=False)
    self.act_left.run_time(speed, time)