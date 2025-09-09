from py5canvas import *


def setup():
    create_canvas(512, 512)
    background(255)
    frame_rate(60)


def draw():
    background(255)
    no_stroke()

    fill(0)
    text_font("Times New Roman")
    # text_style("normal")
    text_size(35)
    text("hello", [30, 50])

    fill(255, 0, 0)
    text_font("Courier New")
    text_style("italic")
    text_size(65)
    text("world!", [80, 100])

    fill(0, 255, 0)
    text_font("Helvetica")
    text_style("bold")
    text_size(65)
    text("goodbye", [140, 300])

    fill(0, 0, 255)
    text_font("Brush Script MT")
    text_style("bolditalic")
    text_size(75)
    text("universe!", [60, 400])


run()
