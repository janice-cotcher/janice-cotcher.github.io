from processing import *

def setup():
    size(200, 200)


def drawHead():
    ellipse(100, 35, 25, 25)


def drawBody():
    line(100, 50, 100, 80)


def drawArms():
    line(100, 52, 70, 45)
    line(100, 52, 130, 45)


def drawLegs():
    line(100, 80, 85, 125)
    line(100, 80, 115, 125)

def draw():
    drawHead()
    drawBody()
    drawArms()
    drawLegs()


run()