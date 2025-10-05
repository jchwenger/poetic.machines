from py5canvas import *
import math

word = "silencio"

n_col = 3
n_row = 5
row_height = 50
current_indz = None
display_system = True


def setup():
    global word_w
    global word_h

    create_canvas(512, 300)
    background(255)
    frame_rate(60)

    text_font("Courier New")
    text_size(25)
    no_stroke()
    fill(0)

    word_w = text_width(word)
    word_h = text_height(word)


def draw():
    global n_row
    global n_col
    global current_indz

    background(255)

    centers = []

    for i in range(n_row):
        for j in range(n_col):
            x = 50 + j * (word_w + 20)
            y = row_height + row_height * i
            if (
                current_indz is not None
                and current_indz[0] == i
                and current_indz[1] == j
            ):
                pass
            else:
                text(word, [x, y])

            center_x = x + word_w / 2
            center_y = y - row_height / 6
            centers.append([i, j, center_x, center_y])

    current_indz = compute_distances(mouse_x, mouse_y, centers)


def compute_distances(x, y, centers):
    indz = None
    current_dist = math.inf
    for i, j, pos_x, pos_y in centers:
        dist = ((x - pos_x) ** 2 + (y - pos_y) ** 2) / 2
        if dist < current_dist:
            indz = (i, j)
            current_dist = dist
    return indz


run()

# IDEAS, to make it your own:
# - (This is only the 'cleaned-up' version of the previous sketch, just to
#   demonstrate how brief the logic can be, when all explanations are removed.)
