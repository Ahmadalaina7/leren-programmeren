from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3
distance = 5
for stack in range(1, 5):
  for box in range(stack):
    robotArm.grab()
    for move in range(distance):
      robotArm.moveRight()
    robotArm.drop()
    for move in range(distance - int(box == stack - 1)):
      robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
