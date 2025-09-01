from py5canvas import *

erase_row = 0
erase_col = 0
step_every = 20


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    global erase_row
    global erase_col

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    # text_style("normal")
    text_size(25)

    word = "silencio"
    n_row = 5
    n_col = 3

    # loop 1
    for i in range(n_row):
        line = ""
        # loop 2
        for j in range(n_col):
            if i == erase_row and j == erase_col:
                line += " " * (len(word) + 1)
            else:
                line += word + " "
        text(line, [60, 50 + 50 * i])

    if sketch.frame_count % step_every == 0:
        erase_col = (erase_col + 1) % n_col
        if erase_col == 0:
            erase_row = (erase_row + 1) % n_row

run()
