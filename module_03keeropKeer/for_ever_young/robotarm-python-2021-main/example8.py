from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')
robotArm.speed = 3
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for count in range (8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()
   

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()