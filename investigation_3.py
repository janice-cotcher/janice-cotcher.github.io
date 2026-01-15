# set intital number of circles to draw to 3
n_circles = 3

def setup():
    size(300, 300)
    # black background
    background(0)


def draw():
    global n_circles
    # refresh black background
    background(0)
    circle = 0
    # draw circles as a diagonal on the screen
    while circle < n_circles:
        # defines the centre of the circle of radius 20
        ellipse(circle * 20 + 10, circle * 20 + 10, 20, 20)
        # defines the next circle as over 30 and up 30 
        circle = circle + 1

# if the user hits ’+’, increase the number of circles drawn.

# if the user hits ‘-’, decrease the number of circles drawn.

