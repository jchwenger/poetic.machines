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

run()
