from py5canvas import *


def setup():
    create_canvas(512, 512)
    frame_rate(60)
    background(0, 0, 0)


def draw():

    # try adding an alpha parameter...
    background(0, 0, 0)

    push() # 1

    # center of canvas and do a first rotation
    translate(width / 2, height / 2)
    rotate(frame_count * 0.01)

    push() # 2

    # move to where our white ! is going to be
    translate(100, 0)

    # draw a piece of text
    text_align(CENTER, CENTER)
    text_size(80)
    no_stroke()
    fill(255)
    text("!", 0, 0)

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
    # here we're back before we rotate the last time

    pop() # 2
    # here we're back before we translate to our !, so the center

    pop() # 1
    # here we're back before the first rotation and translation
    # (here we're )back in the top left corner)

run()
