from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3

for s in range(1, 5):
  for box in range(s):
    robotArm.grab()
    for move in range(5):
      robotArm.moveRight()
    robotArm.drop()
    for move in range(5 - int(box == s - 1)):
      robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
