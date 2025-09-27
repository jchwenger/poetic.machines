from py5canvas import *
import numpy as np


def setup():
    create_canvas(512, 512)
    frame_rate(60)
    background(0, 0, 0)


def draw():

    # try adding an alpha parameter...
    background(0, 0, 0)

    # TODO 1: draw something here

    push() # 1

    # center of canvas and do a first rotation
    translate(width / 2, height / 2)
    rotate(frame_count * 0.01)

    # TODO 2: draw something here

    push() # 2

    # move to where our white ! is going to be
    translate(100, 0)

    # draw a piece of text
    text_align(CENTER, CENTER)
    text_size(80)
    no_stroke()
    fill(255)
    text("!", 0, 0)

    # TODO 3: draw something here

    push() # 3


    # now start a new rotation
    rotate(frame_count * .08)

    # here we could translate again, but instead
    # I draw text 
    text_size(20)
    no_stroke()
    fill(255, 0, 0)
    text("?", 70, 0)

    pop() # 3
    # here we're back before we rotated the last time
    # TODO 3: draw something here, it should be at the same spot as before # 3

    pop() # 2
    # here we're back before we translated to our !, so the center
    # TODO 2: draw something here, it should be at the same spot as before # 2

    pop() # 1

    # here we're back before the first rotation and translation
    # (here we're )back in the top left corner)
    # TODO 1: draw something here, it should be at the same spot as before # 1


run()


# IDEAS, to make it your own:
# - Change the characters: can you think of ways of creating a piece using only
#   punctuation marks?
# - As before, use the tools you know to change the look, feel and meaning
#   (colours/typeface/placement) of your sketch.
# - Experiment with the rotation speeds and directions.
# - Either add a second main orbit, or a second orbiting object around '!'!
# - If you expand your canvas size, and increase the orbit of '!', and its
#   statellites , can you now make something orbit around '?'?
# - Extras: the orbit of planets is, famously, not circular, but elliptic. This
#   is where maths becomes useful in a very direct way. If you do some
#   research, you can find that there is a so-called "parametric" way of
#   defining an ellipse (https://www.mathopenref.com/coordparamellipse.html),
#   that you can implement in code (my recommendation is to comment out all the
#   code you have, then just translate to the middle of the canvas, then play
#   with this piece of code, changing various parameters to see what they do):
#
#       # t will be the coordinate around the ellipse
#       t = frame_count * .08
#       # a & b are the two radii
#       a = 150
#       b = 60
#       x = a * cos(t)
#       y = b * sin(t)
#       text_size(20)
#       text("O", x, y)
