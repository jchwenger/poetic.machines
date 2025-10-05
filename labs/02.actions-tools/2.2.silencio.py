from py5canvas import *


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    # text takes in:
    #   - the string to display
    #   - the x coordinate (horizontal)
    #   - the y coordinate (vertical – from the top down!)
    text("silencio silencio silencio", 60, 50)
    text("silencio silencio silencio", 60, 100)
    text("silencio          silencio", 60, 150)
    text("silencio silencio silencio", 60, 200)
    text("silencio silencio silencio", 60, 250)


run()

# IDEAS, to make it your own, (#BreakTheSilence!):
# - Change the colour of the words.
# - Change the placement of the words.
# - Change the typeface.
# - Change the words themselves.
# - At this stage it is encouraged to go wild: add/remove some of the lines,
#   experiment with superposing/mashing text, or even add some of the rotation
#   logic from `animation.py`?!
# - You could take screenshots along the way to document your destruction of
#   silencio!

# IMPORTANT NOTE: see?, here we have a static sketch with a draw. As it is, it
# could be rewritten by eliminating the `def draw():` and placing everything in
# `setup`. Of course, the capability of `draw` could be taken advantage of, and
# some animation could be introduced: can you make it move???