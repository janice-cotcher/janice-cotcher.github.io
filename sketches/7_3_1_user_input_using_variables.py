from processing import *
name = ""


def draw():
  global name
  text(name, 20, 20)


def keyPressed():
  global name
  name = name + key


run()