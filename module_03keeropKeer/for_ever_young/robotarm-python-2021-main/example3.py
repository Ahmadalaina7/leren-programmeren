from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
for count in range (0,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()