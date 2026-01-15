from processing import *


def setup ():
  size (200, 200)


def draw ():
  size = 100
  count = 0
  while count < 10:
    ellipse(100, 100, size , size)
    size = size - 10
    count = count + 1


run()