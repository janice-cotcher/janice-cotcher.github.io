radius = 10


def setup():
  size(300, 300)


def keyPressed():
  global radius
  if key == "+":
    radius = radius + 5
  elif key == "-":
    radius = radius - 5
  else:
    print("Hit + to increase size")
    print("Hit - to decrease size")


def draw():
  global radius
  ellipse(150, 150, radius, radius)


