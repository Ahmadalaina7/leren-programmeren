from shutil import move
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for count in range(0,2):
    robotArm.moveRight()
robotArm.drop()
for count in range(0,2):
    robotArm.moveLeft()
robotArm.grab()
for count in range(0,2):
    robotArm.moveRight()
robotArm.drop()
for count in range(0,2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()