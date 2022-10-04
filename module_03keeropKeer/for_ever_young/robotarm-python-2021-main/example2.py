from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for count in range(0,9):
    robotArm.moveRight()
robotArm.drop()
for count in range(0,5):
    robotArm.moveLeft()
robotArm.grab()
for count in range (0,5):
    robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()