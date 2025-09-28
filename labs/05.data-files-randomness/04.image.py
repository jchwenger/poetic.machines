# Edwin Morgan, ‘Computer's first Code Poem’, 1965. Source
# https://www.researchgate.net/figure/Edwin-Morgan-Computers-first-Code-Poem-1965_fig7_328480411

from py5canvas import *

img = load_image("data/Edwin-Morgan.The-Computer-s-First-Code-Poem.1965.png")

def setup():
    create_canvas(*img.size)

def draw():
    background(0)

    # place the image on the canvas
    image(img, 0, 0)

    # the last two arguments allow you to resize the video
    # image(img, 0, 0, width/2, height/2)

run()

