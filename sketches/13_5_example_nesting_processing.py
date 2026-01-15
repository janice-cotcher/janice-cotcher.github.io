from processing import *
# bullseye that alternates red and white

def setup():
    size(600, 600)
    # black background
    background(0)


def draw():
    # 6 concentric circles that alternate red and white
    for d in range(600, 0, -100):
        # the values for d are 600, 500, 400, 300, 200, 100
        # if I divide each by 100 then they will be 
        # 6, 5, 4, 3, 2, 1
        # I can then choose to fill my even rings with red
        if d/100 % 2 == 0:
            fill(255, 0, 0)
        # and all other rings with white
        else:
            fill(255)
        ellipse(300, 300, d, d)


run()