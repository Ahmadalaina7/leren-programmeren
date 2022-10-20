from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
i = 9
while i >= 0:
    robotArm.grab()
    for count in range(0, i):
        robotArm.moveRight()
    i -= 1
    robotArm.drop()
    for x in range(0, i):
        robotArm.moveLeft()
    i -= 1

    
       

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()