from py5canvas import *
import numpy as np

brush_mode = 0


def brush(pos, delta, colour):
    average_delta = (abs(delta[0]) + abs(delta[1])) / 2
    # also possible: use numpy to compute the norm (length) of the vector
    # (https://numpy.org/doc/2.3/reference/generated/numpy.linalg.norm.html)
    # average_delta = np.linalg.norm(delta)
    # print(average_delta)

    push()
    stroke(0)
    fill(*colour)
    circle(pos, average_delta * 5)


def setup():
    create_canvas(800, 600)
    background(255)


def draw():
    background(255, 20)

    if dragging:
        brush(mouse_pos, mouse_delta, (255, 0))


def key_pressed(key):
    print(f"Key pressed: {key}")


def mouse_pressed():
    print("Mouse down")
    # a green circle when we click the mouse
    push()
    fill(0, 255, 0)
    circle(*mouse_pos, 30)
    pop()


def mouse_released():
    print("Mouse up")
    # a blue circle when we release the mouse
    push()
    fill(0, 0, 255)
    circle(*mouse_pos, 30)
    pop()


run()
