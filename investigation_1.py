screen_size = 220
min_square_size = 5


def setup():
    global screen_size
    size(screen_size, screen_size)


def draw():
    global screen_size
    global min_square_size
    square_size = 200
    while square_size >= min_square_size:
        rect(0, 0, square_size, square_size)
        square_size = square_size / 2


