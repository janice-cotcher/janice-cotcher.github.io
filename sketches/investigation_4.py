from processing import *


def setup():
    size(400, 100)
    # white background
    background(255)
    for i in xrange(10, 350, 50):
        house(i, 20)

def house(x, y):
    """
    Draws a house with a door
    x: x-coordinates
    y: y-coordinates
    """
    # roof
    triangle(x + 15, y, x, y + 15, x + 30, y + 15)
    # bottom of the house
    rect(x, y + 15, 30, 30)
    # door
    rect(x + 12, y + 30, 10, 15)


run()