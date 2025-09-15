from py5canvas import *


def setup():
    create_canvas(512, 512)
    frame_rate(60)
    background(0, 0, 0)


def draw():
    # Clear with alpha will create the "trail effect"
    background(0, 0, 0, 8)

    push()
    # Center of screen
    translate(width / 2, height / 2)
    # Draw rotating circle
    fill(255, 0, 0)
    stroke(255)
    rotate(frame_count * 0.05)
    circle(100, 0, 20)
    pop()

    # push()
    ## Move somewhere to the bottom right
    # translate(width - 80, height - 80)
    ## No fill, draw in blue
    # no_fill()
    # stroke(0, 0, 255)
    # rotate(-frame_count * 0.1)
    # rectangle(0, 0, 40, 40)
    # pop()


run()
