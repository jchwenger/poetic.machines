from py5canvas import *

to_be_snowballed = "the relief of the simplicity of it"

def setup():
    create_canvas(400, 700)

def draw():
    background(255)

    text_font("Courier New")
    text_size(14)
    no_stroke()
    fill(0)

    for i in range(len(to_be_snowballed) + 1):
        text(to_be_snowballed[:i], 10,  10 + i * 20)

run()