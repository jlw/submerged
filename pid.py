from pybricks.tools import wait, StopWatch

class PIDController:
  def __init__(self, gainP, gainI, gainD):
    self.gainP = gainP
    self.gainI = gainI
    self.gainD = gainD
    self.integral = 0
    self.last_error = 0

    self.desiredTime = 100
    
  def adjust(self, error):
    wait(self.desiredTime)

    self.integral = error + self.integral * (2/3)
    derivative = error - self.last_error
    return (error * self.gainP) + (self.integral * self.gainI) + (derivative * self.gainD)