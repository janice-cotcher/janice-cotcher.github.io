def setup():
    size(500, 500)
    background(255)
    smooth()


def draw():
    noStroke()
    i = 500
    while i > 0:
        fill(255, 0, 0)
        ellipse(250, 250, i, i)
        fill(255)
        ellipse(250, 250, i - 100, i - 100)
        i = i - 200


