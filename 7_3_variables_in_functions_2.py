def donut(size):
  """
  Draws a white donut with a black hole.
  The parameter size gives the diameter of the donut.
  """
  fill(255)
  ellipse(50, 50, size, size)
  fill(0)
  size = size/2
  ellipse(50, 50, size, size)


def draw():
  donut(50)


