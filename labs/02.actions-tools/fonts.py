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
    text("hello", 30, 50)

    fill(255, 0, 0)
    text_font("Courier New")
    text_style("italic")
    text_size(65)
    text("world!", 80, 100)

    fill(0, 255, 0)
    text_font("Helvetica")
    text_style("bold")
    text_size(65)
    text("goodbye", 140, 300)

    fill(0, 0, 255)
    text_font("Brush Script MT")
    text_style("bolditalic")
    text_size(75)
    text("universe!", 60, 400)


run()

# IDEAS, to make it your own:
# - Change the words.
# - Change the placement of those words.
# - Change the colour of the words.
# - Change the typefaces of the words (the only requirements to pick a typeface
#   is that it is installed in your system, but you can download them here:
#   https://www.dafont.com/, https://www.1001freefonts.com/). It might also be
#   possible to play with the the *name* of the fonts as well.
# - Add or subtract words.
# - Bonus: Note that nothing is stopping you from writing words *on top of one
#   another*. That actually creates a very different aesthetic (both in terms
#   of the colour combination but also the overal effect: cramming, packing,
#   blurring the meanings of the words you use).
