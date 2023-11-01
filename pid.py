class PIDController:
  def __init__(self, gainP, gainI, gainD):
    self.gainP = gainP
    self.gainI = gainI
    self.gainD = gainD
    self.integral = 0
    self.last_error = 0

  def adjust(self, error):
    self.integral = error + self.integral
    derivative = error - self.last_error
    return (error * self.gainP) + (self.integral * self.gainI) + (derivative * self.gainD)