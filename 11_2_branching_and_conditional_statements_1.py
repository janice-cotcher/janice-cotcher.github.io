radius = 10


def setup():
  size(300, 300)


def keyPressed():
  global radius
  if key == "+":
    radius = radius + 5
  print("Hit + to increase size")


def draw():
  global radius
  ellipse(150, 150, radius, radius)


