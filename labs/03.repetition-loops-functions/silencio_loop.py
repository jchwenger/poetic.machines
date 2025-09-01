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

    # define my two types of lines
    line = "silencio silencio silencio"
    line_gap = "silencio          silencio"

    # gather the lines into a poem & define all the positions
    # beware: both must have the same number of elements!
    poem = [line, line, line_gap, line, line]
    positions = [[60, 50],[60, 100],[60, 150],[60, 200],[60, 250]]

    # use a for loop to print the line at the position!
    for l,p in zip(poem, positions):
        text(l, p)

run()
