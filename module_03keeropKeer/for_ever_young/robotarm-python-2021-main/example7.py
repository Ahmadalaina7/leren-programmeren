from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for i in range(6):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
for count in range(3):
    robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
for i in range(3):
        for count in range(2):
            robotArm.moveRight()
        for i in range(6):
            robotArm.grab()
            robotArm.moveLeft()
            robotArm.drop()
            robotArm.moveRight()
      
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
