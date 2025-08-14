from py5canvas import *

erase_line = 0
erase_col = 0

step_every = 20


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    global erase_line
    global erase_col

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    # text_style("normal")
    text_size(25)

    word = "silencio"
    n_line = 5
    n_col = 3

    sleep_time = 0.2

    # loop 1
    for i in range(n_line):
        line = ""
        # loop 2
        for j in range(n_col):
            if i == erase_line and j == erase_col:
                line += " " * (len(word) + 1)
            else:
                line += word + " "
        text(line, [30 * j, 50 + 50 * i])

    if sketch.frame_count % step_every == 0:
        erase_col = (erase_col + 1) % n_col

        if erase_col == 0:
            erase_line = (erase_line + 1) % n_line


run()
