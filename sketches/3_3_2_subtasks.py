from processing import *


def setup():
  # sets the size of the canvas
  size(200, 200)

def draw():
  # calls the signature function
  signature()


def signature():
  text("Cookie Monster", 5, 10)
  text("123 Sesame Street", 5, 20)


run()