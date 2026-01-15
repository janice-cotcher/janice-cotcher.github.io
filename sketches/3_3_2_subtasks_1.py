from processing import *


def setup():
  # define the size of the canvas
  size(200, 200)

def draw():
  # the signature function is called in draw()
  signature()


def signature():
  text("Cookie Monster", 5, 10)
# indention is incorrect so the program won't run
text("123 Sesame Street", 5, 20)


run()