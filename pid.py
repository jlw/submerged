class PIDController:
  def __init__(self, gainP, gainI, gainD):
    self.gainP = gainP
    self.gainI = gainI
    self.gainD = gainD
    self.integral = 0
    self.last_error = 0

  def adjust(self, error):
    self.integral = error + self.integral * (2/3)
    derivative = error - self.last_error
    #print(error, self.last_error, derivative, self.integral, self.gainP, self.gainI, self.gainD)
    return (error * self.gainP) + (self.integral * self.gainI) + (derivative * self.gainD)