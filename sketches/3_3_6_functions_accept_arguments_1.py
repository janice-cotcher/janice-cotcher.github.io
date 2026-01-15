from processing import *


def circle(x, y):
  """
  Draws a 15x15 circle
  x: x-coordinate of the circle's centre
  y: y-coordinate of the circle's center
  """
  ellipse(x, y, 15, 15)


def draw():
  circle(10, 10)
  circle(10, 30)


run()