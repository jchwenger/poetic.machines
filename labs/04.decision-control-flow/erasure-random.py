from py5canvas import *
import numpy as np

step_every = 20

n_line = 5
n_col = 3

random_line = np.random.randint(0, n_line - 1)
random_col = np.random.randint(0, n_col - 1)


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    global n_line
    global n_col
    global random_line
    global random_col

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    # text_style("normal")
    text_size(25)

    word = "silencio"

    sleep_time = 0.2

    # loop 1
    for i in range(n_line):
        line = ""
        # loop 2
        for j in range(n_col):
            if i == random_line and j == random_col:
                line += " " * (len(word) + 1)
            else:
                line += word + " "
        text(line, [30 * j, 50 + 50 * i])

    if sketch.frame_count % step_every == 0:
        random_line = np.random.randint(0, n_line - 1)
        random_col = np.random.randint(0, n_col - 1)


run()
