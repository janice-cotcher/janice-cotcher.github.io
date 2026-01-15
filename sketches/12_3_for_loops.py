from processing import *

def draw():
  word = "COOKIE"
  x = 10
  y = 10
  for letter in word:
    text(letter , x, y)
    x = x + 10
    y = y + 10


run()