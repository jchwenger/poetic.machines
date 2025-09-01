from py5canvas import *
import math

n_col = 3
n_row = 5
row_height = 50
current_indz = None
display_system = True


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    global n_row
    global n_col
    global current_indz

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    word = "silencio"
    word_length = text_width(word)
    h = text_height(word)
    # print(word_length, h)

    # we will save the indices and coordinates of the 'word centre': (i,j,x,y)
    centers = []

    # loop 1: loop through each row
    for i in range(n_row):
        # loop 2: loop through each column
        for j in range(n_col):
            # compute the x & y (bottom left corner of text)
            x = 50 + j * (word_length + 20)
            y = row_height + row_height * i
            # if this is the row/col closest to the mouse, don't draw
            # otherwise use text to draw the word
            if (
                current_indz is not None
                and current_indz[0] == i
                and current_indz[1] == j
            ):
                pass
            else:
                text(word, [x, y])

            # compute the centre:
            # add half the word length to x
            # subtract a sixth of the row height (I improvised that number)
            center_x = x + word_length / 2
            center_y = y - row_height / 6
            centers.append([i, j, center_x, center_y])

            if display_system:
                # display the centre of the word as a small blue dot
                push()
                fill(0, 0, 255)
                circle(center_x, center_y, 2)
                pop()

    if display_system:
        # display the mouse as a small red circle
        push()
        no_fill()
        stroke(255, 0, 0)
        circle(mouse_x, mouse_y, 5)
        pop()

    # compute all the distances
    current_indz = compute_distances(mouse_x, mouse_y, centers)

    if display_system:
        push()
        stroke_weight(1)
        fill(200,200,200)
        for (c_x, c_y, _, _) in centers:
            line(
                mouse_x,
                mouse_y,
                50 + c_y * (word_length + 20) + word_length / 2,
                row_height + row_height * c_x - row_height / 6,
            )
        fill(0, 255, 0)
        stroke_weight(2)
        line(
            mouse_x,
            mouse_y,
            50 + current_indz[1] * (word_length + 20) + word_length / 2,
            row_height + row_height * current_indz[0] - row_height / 6,
        )
        pop()

    # print(mouse_x, mouse_y, centers, current_indz)
    # print(centers)
    # print(current_indz)


def compute_distances(x, y, centers):
    # at first, indz has nothing in it & our 'distance' is infinity (we will
    # gradually reduce this number)
    indz = None
    current_dist = math.inf
    # looping through all the centers
    for i, j, pos_x, pos_y in centers:
        # compute the distance of this point to the mouse
        dist = ((x - pos_x) ** 2 + (y - pos_y) ** 2) / 2
        # if this distance is smaller than the current one, save the indices &
        # update the distance
        if dist <= current_dist:
            indz = (i, j)
            current_dist = dist
    return indz


def mouse_pressed():
    global display_system
    # when we click, we change the value to its boolean opposite
    display_system = not display_system
    # print(f"mouse pressed: {display_system=}")


run()
