from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1, 7)

# Jouw python instructies zet je vanaf hier:
for f in range(8):

    robotArm.grab()
    for k in range(1 + f):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(1 + f):
        robotArm.moveLeft()
    if robotArm.grab() == False:
        break


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
