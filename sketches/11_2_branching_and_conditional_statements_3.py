from processing import *
radius = 10


def setup():
  size(300, 300)


def keyPressed():
  global radius
  if key == "+":
    radius = radius + 5
  if key == "-":
    radius = radius - 5


def draw():
  global radius
  ellipse(150, 150, radius, radius)


run()