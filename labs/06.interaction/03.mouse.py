from py5canvas import *
import numpy as np

brush_mode = 0


def brush(pos, delta, colour):
    # delta is a common name for 'difference' or 'gap' (it's also a Greek
    # letter name): here we add x and y, divide by two, then the absolute value
    # (so our number is positive, we can use it as the radius of a circle)
    average_delta = abs((delta[0] + delta[1]) / 2)
    # also possible: use numpy to compute the norm (length) of the vector
    # (https://numpy.org/doc/2.3/reference/generated/numpy.linalg.norm.html)
    # average_delta = np.linalg.norm(delta)
    # print(average_delta)

    push()
    stroke(0)
    fill(colour)
    # use the delta as the radius of a circle
    circle(pos, average_delta * 5)
    pop()


def setup():
    create_canvas(800, 600)
    background(255)


def draw():
    background(255, 20)

    if dragging:
        # py5canvas conveniently keeps a global variable `mouse_delta` for you,
        # constantly tracking the difference of the current mouse position and
        # the previous one (it is a NumPy array with two elements, for x & y)
        # Note: you could also compute it manually by keeping separate
        # variables, `past_mouse_x`, `past_mouse_y`, and in `draw` do something
        # like:
        #   delta = mouse_x - past_mouse_x
        #   past_mouse_x = mouse_x
        brush(mouse_pos, mouse_delta, (255, 0))


def mouse_pressed():
    # print("Mouse down")

    push()

    # background flash
    background(0)

    # a green circle when we click the mouse
    fill(0, 255, 0)
    circle(*mouse_pos, 30)

    # and some text
    fill(255)
    text_size(130)
    text_align(CENTER, CENTER)
    text("CLICKED", center)
    pop()


def mouse_released():
    print("Mouse up")

    push()

    # background flash
    background(0)

    fill(0, 0, 255)
    # a blue circle when we release the mouse
    circle(*mouse_pos, 30)

    # and some text
    fill(255)
    text_size(130)
    text_align(CENTER, CENTER)
    text("RELEASED", center)
    pop()


run()

# IDEAS, to make it your own:
# - Two key elements of interaction are present here: the `delta`, namely the
#   difference in position, which allows us to measure the speed of the mouse
#   movement (and as you can see, the delta can be used to modify any
#   animation, here simply the size of a circle drawn at the location of the
#   mouse); and actions such as the pressing (or clicking) or the mouse, the
#   dragging, and its final release. Here those are associated with relatively
#   simple events (drawing some shapes & text), but nothing prevents you to
#   think about more complicated processes.
# - Add random letters instead of circles? Think about how this distance
#   measure, the `delta`, could be used creatively: at the end of the day, it
#   just gives you one number, small when the mouse doesn't move much, big when
#   it does, that can be used to control anything you want!

