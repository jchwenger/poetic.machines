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
