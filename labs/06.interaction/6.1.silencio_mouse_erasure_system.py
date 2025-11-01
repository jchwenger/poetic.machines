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
    # print(word_w, word_h)


def draw():
    global n_row
    global n_col
    global current_indz

    background(255)

    # we will save the indices and coordinates of the 'word centre': (i,j,x,y)
    centers = []

    # loop 1: loop through each row
    for i in range(n_row):
        # loop 2: loop through each column
        for j in range(n_col):
            # compute the x & y (bottom left corner of text)
            x = 50 + j * (word_w + 20)
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
            center_x = x + word_w / 2
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
        fill(200, 200, 200)
        for c_x, c_y, _, _ in centers:
            line(
                mouse_x,
                mouse_y,
                50 + c_y * (word_w + 20) + word_w / 2,
                row_height + row_height * c_x - row_height / 6,
            )
        fill(0, 255, 0)
        stroke_weight(2)
        line(
            mouse_x,
            mouse_y,
            50 + current_indz[1] * (word_w + 20) + word_w / 2,
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
        # compute the distance of this point to the mouse (squared: you could
        # take the square root, but it'd be more compute & same result)
        dist = (x - pos_x) ** 2 + (y - pos_y) ** 2
        # if this distance is smaller than the current one, save the indices &
        # update the distance
        if dist < current_dist:
            indz = (i, j)
            current_dist = dist
    return indz


def mouse_pressed():
    global display_system
    # when we click, we change the value to its boolean opposite
    display_system = not display_system
    # print(f"mouse pressed: {display_system=}")


run()

# IDEAS, to make it your own:
# - TADAA: this is it! The *final* silencio sketch! Here the key thing I would
#   like you to focus on is how the system is built up: using a notion of
#   distance and looping through all elements (words) to compute the shortest
#   one, which then gives us the index at which we want to erase the word.
# - Apart from the usual change of words and design, something that could be
#   attempted could be to have 1) multiple words in an array, instead of just
#   'silencio'; 2) an array containing as many *indices*  as there are slots
#   (selecting which word from your list is selected at each slot – it might be
#   easier to work with an array of arrays, one array per row, since we work
#   with two indices i and j); 3) when the mouse is over a word, a random
#   number is generated to replace the index for the current word (that could
#   lead to a rapid flickering effect, like slot machines in a casino?), then
#   when the mouse gets close to the next slot, the last index remains, leaving
#   one particular word selected?
# - Beyond such technical considerations, the real topic at hand is what
#   interaction can be, especially at an artistic level. Of course, mouse
#   interaction is perhaps the most direct, and most banal, way to interact
#   with a computer, but the real applications and possibilities of this are
#   infinite. Your mouse lives in 2D space, giving you live coordinates
#   constantly updated by the movements of the user: these are just numbers,
#   and so long as any other aspect, dimension, or even concept, of your piece,
#   can be represented in some numeric form, it is then possible to create a
#   bridge between the two! (Example: if instead of one poem, you have a lot of
#   them, and somehow you assign a 'coordinate' to each of them, according to a
#   specific method, then suddenly the 2D space of the mouse can be a way to
#   navigate the space of poems – to select one. And of course this needn't be
#   just selecting one poem: this 2D interaction could somehow be turned into a
#   new approach, a new interface, for writing, as seen in Allison Parrish's
#   experiments.
# - Advanced TODO: Python loops are very slow. If you don't feel intimidated by
#   NumPy, I would recommend looking into ways of using a numpy array and
#   broadcasting (`np.array` * 2, for instance, mutliplies all elements of such
#   an array by 2, similar with addition and other arithmetic operations).
