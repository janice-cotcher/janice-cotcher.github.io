from processing import *
# bullseye that alternates red and white


def setup():
    size(600, 600)
    # black background
    background(0)


def circle(d):
    """circle function that is centred in the middle
    of the screen with diameter d"""
    ellipse(300, 300, d, d)


def draw():
    colour = "red"
    # 6 concentric circles that alternate red and white
    for d in range(600, 0, -100):
        if colour == "red":
            fill(255, 0, 0)
            colour = "white"
        else:
            fill(255)
            colour = "red"
        circle(d)


run()