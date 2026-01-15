# x is the x-coordinate of the top of the torso
# y is the y-coordinate of the top of the torso 


def setup():
    size(200, 200)


def drawHead(x, y):
    """
    draws head of a stickman
    """
    ellipse(x, y - 15, 25, 25)


def drawBody(x, y):
    """
    draws the torso of the stickman
    """
    line(x, y, x, y + 30)


def drawArms(x, y):
    """
    draws two arms
    """
    line(x, y + 2, x - 30, y - 5)
    line(x, y + 2, x + 30, y - 5)


def drawLegs(x, y):
    """
    draws two legs
    """
    line(x, y + 30, x - 15, y + 75)
    line(x, y + 30, x + 15, y + 75)


def stickman(x, y):
    """
    draws the stickman with all the body parts
    """
    drawHead(x, y)
    drawBody(x, y)
    drawArms(x, y)
    drawLegs(x, y)


def draw():
    stickman(100, 50)


