# Adapted from Dan Shiffman's Nature of Code
# https://natureofcode.com/random/#a-smoother-approach-with-perlin-noise
# https://editor.p5js.org/natureofcode/sketches/_cmWTl2UoV

from py5canvas import *
import numpy as np

# TODO: try `True`
SHOW_SYSTEM = False

my_word = "PROGRESS?"

# this will be an array containing all our xs (we hold them in one array rather
# than doing loops, like in JavaScript, as Python loops are **slow**)
x_indices = None

# this is where we start on the
start_x = 0.0

# this is the speed at which we slide to the right (sensitive, already 0.1 is
# real fast)
x_speed = 0.01

# this is by how much we jump between each point on the Perlin curve: the
# bigger this number, and the closer we get to uniform noise (jagged rather
# than smooth)
step = 0.01

# this can never go below 1 (and higher numbers quickly start not making much
# of a difference unless you 'zoom in')
detail = 2


def setup():
    global x_indices
    create_canvas(600, 400)

    # create a range of numbers (same as `range`, but with a few additional
    # functionalities – for instance doing `range * x` multiplies all numbers
    # in `range` by `x`, without having to do a `for` loop)
    x_indices = np.arange(width)

    # define the noise detail (something like the `resolution` of the curve: a
    # higher number means more jaggedness when you zoom in, even as the overall
    # shape remains the same) – note that `detail` should be an int, and will
    # be clamped to 1 automatically if it's below that
    noise_detail(int(detail))


def draw():
    global start_x

    background(150)

    # our `x_indices` (from 0 to width), are spaced according to step (if
    # `step` is 2, then instead of 0,1,2,... we have 0,2,4,...), increasing the
    # randomness of the values we get, and we also shift by shifted right by
    # `start_x` (if it's 5, then `x_indices` will start from 5 instead of 0)
    x_offsets = start_x + x_indices * step

    # vectorized noise call: noise takes in a whole array, and returns another
    # array, of floats, within [0,1] (the same range as `random`)
    noise_array = noise(x_offsets)

    # we have values in [0,1], multipling by height gets us [0,height]
    y_values = noise_array * height

    # draw text at centre
    text_font("Times New Roman")
    text_size(54)
    text_align(CENTER, CENTER)
    no_stroke()
    fill(0)
    pos = width / 2

    # here we centre the word in x, but for y we use our shifting noise value
    # (make sure pos is an int when using it as an index)
    text(my_word, pos, y_values[int(pos)])

    if SHOW_SYSTEM:
        # use the values to draw the full curve
        stroke(255)
        no_fill()
        begin_shape()
        for i, y in enumerate(y_values):
            vertex(i, y)
        end_shape()

        # display our values on the screen
        push()
        text_size(14)
        text_align(LEFT)
        fill(1)
        stroke(1)
        text(f"start_x: {start_x}", 10, height - 55)
        text(f"noise detail: {int(detail)}", 10, height - 40)
        text(f"x_speed: {x_speed}", 10, height - 25)
        text(f"step: {step:}", 10, height - 10)
        pop()

    start_x += x_speed


run()

# IDEAS, to make it your own:
# - Change the word, and the appreance of the sketch.
# - What if you added more words at various xs across the width of the sketch.
#   Wouldn't that create a 'pursuit' effect? Could that be exploited
#   creatively?
# - This is fine, but what if you wanted to draw individual letters on that
#   curve instead of the whole word? The first step is to loop over your word
#   and call `text` on each letter. Then of course you need to adjust the x
#   coordinate of each letter, using an index, as we have seen in past labs. I
#   recommend using the following template:
#
#       push()
#       # translate to the middle of the width
#       translate(width/2, 0)
#       # TODO: there are more principled ways of doing this, but for now just pick a
#       # width (positive integer), and tweak it manually
#       letter_width = ...
#       for i, l in enumerate(my_word):
#           # TODO: this is where the magic happens: can you use i and letter_width
#           # to create a unique `letter_pos` for each letter? Can you think of
#           # how to get a centered effect?
#           letter_pos = ...
#           # TODO: this line will draw all letters at the same height, what
#           # should you change to display the letters on various heights?
#           text(l, letter_pos, y_values[int(pos)])
#       pop()
