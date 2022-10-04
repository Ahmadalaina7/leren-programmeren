from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for count in range(7):
    robotArm.moveRight()
for count in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    for count in range(2):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()