import Commands

def mo2():
  return [
    # Launtch
    Commands.GyroDrive(speed=175, distance=100),
    # Angle to avoid deadly dragon breath
    Commands.Pivot(angle=44, speed=100),
    # Sneak forward like nothing happened
    Commands.GyroDrive(speed=200, distance=280),
    # Trun away
    Commands.DriveMotor(motor="right", angle=250, speed=150),
    # Prepare to yoink sam
    Commands.ActMotorTime(motor="left", time=600, speed=-300, wait=False),
    # Drive to M02
    Commands.GyroDrive(speed=200, distance=160),
    # Align and prepare for shoving
    Commands.DriveMotor(motor="right", angle=200, speed=150),
    # PUSH!
    Commands.DriveMM(speed=100, distance=40),
    # Enslave Sam
    Commands.ActMotorTime(motor="left", time=800, speed=350, wait=False),
    # Retreat form the scene
    Commands.DriveMM(speed=100, distance=-80),
    # Turn the other way
    Commands.Pivot(angle=-90, speed=100),
    # Get out of there!
    Commands.DriveMM(speed=100, distance=-230),
    # Watch out for M10!
    Commands.Pivot(angle=-47, speed=100),
    # We are going the wrong way! Prepare for realignment
    Commands.DriveMM(speed=150, distance=30),
    # Get back on track
    Commands.LineSquare(returnTime=3000, finetuneSpeed=40),
    # Ok on to the next mission
    Commands.Pivot(angle=-70, speed=100),
    # Get in place
    Commands.DriveMM(speed=150, distance=225),
    # Spin around 
    Commands.Pivot(angle=125, speed=100),
    # Give Izzy a concussion
    Commands.ActMotorTime(motor="right", speed=600, time=900),
    # Recoil
    Commands.ActMotorTime(motor="right", speed=-500, time=800),
    # Prepare for next strike
    Commands.Pivot(angle=48, speed=120),
    # Give the M03 guy a concussion
    Commands.ActMotorTime(motor="right", speed=700, time=1500),
    # Recoil again
    Commands.ActMotorTime(motor="right", speed=-800, time=1200, wait=False),
    # Wait...
    Commands.Wait(time=200),
    # Ok! angle for M11!
    Commands.Pivot(angle=9, speed=120),
    # Reverse and slam
    Commands.DriveMM(speed=175, distance=-120),
    # Send the carousel into overdrive!
    Commands.ActMotorTime(motor="left", speed=888, time=6250),
    # Get out of the way!
    Commands.DriveMM(speed=200, distance=50),
    # Trun around!
    Commands.Pivot(angle=-100, speed=100),
    # Run home!
    Commands.DriveMM(speed=250, distance=1000, angle=18)
  ]