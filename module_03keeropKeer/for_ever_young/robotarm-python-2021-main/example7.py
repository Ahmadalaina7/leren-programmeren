from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
for 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
