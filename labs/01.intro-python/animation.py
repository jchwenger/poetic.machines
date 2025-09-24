from py5canvas import *


# The code inside `setup` runs only once.
# IMPORTANT PYTHON NOTE: indentation (leading spaces/tabs) matter!
# All the code inside `setup` or `draw` MUST be indented with one tab (4 spaces).
def setup():
    create_canvas(512, 512)
    frame_rate(60)
    background(0, 0, 0)


def draw():

    # Clear with alpha will create the "trail effect"
    background(0, 0, 0, 8)

    # Center of screen
    translate(width / 2, height / 2)
    
    # Rotating the canvas
    # (try changing the number, or adding `-` before)
    rotate(frame_count * 0.05)

    # Draw a circle
    fill(255, 0, 0)
    stroke(255)
    circle(0, 100, 80)

    # Something to try: uncomment the next lines by removing the leading '# '
    # (select them & cmd or ctrl + / )

    # text_align(CENTER)
    # text_size(200)
    # no_stroke()
    # fill(255)
    # text("?", 0, 0)

run()

