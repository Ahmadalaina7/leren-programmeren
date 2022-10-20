from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
h = 9
# Jouw python instructies zet je vanaf hier:
while h > 0:
    h = h - 1
    robotArm.grab()
    color = robotArm.scan()

    if color == "red":
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for h in range(h):
            robotArm.moveLeft()
        h = h + 1

    else:
        robotArm.drop()
        for k in range(1):
            robotArm.moveRight()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
