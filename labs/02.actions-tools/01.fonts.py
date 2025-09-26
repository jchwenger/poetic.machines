from py5canvas import *


def setup():
    create_canvas(512, 512)
    background(255)
    frame_rate(60)

    # everything from here could go into a draw function
    background(255)

    # `no_stroke` disables stroke/outline around shapes/text
    # see below for how to add a stroke colour
    no_stroke()

    # `fill` with one parameter is a shade of grey: 0 for black, 255 for white
    # (the opposite is `no_stroke`)
    fill(0)
    text_font("Times New Roman")
    # text_style("normal")
    text_size(35)
    text("hello", 30, 50)

    # `fill` with one parameter is (Grey, Alpha)
    # Alpha is transparency, also a number [0 (opaque) - 255 (transparent)]
    # try changing the alpha value (and the colour)
    fill(0, 100)
    text_font("Courier New")
    text_style("italic")
    text_size(65)
    text("world!", 80, 100)

    # `fill` with three parameters is (Red, Green, Blue): https://rgbcolorpicker.com/
    # try changing this to 1) pure Green (0, 255, 0); 2) pure Blue (0, 0, 255)
    fill(255, 0, 0)
    text_font("Helvetica")
    text_style("bold")
    text_size(65)
    text("goodbye", 140, 300)

    # `fill` with four parameters is (Red, Green, Blue, Alpha)
    # Alpha is transparency, also a number [0 (opaque) - 255 (transparent)]
    # try changing the alpha value (and the colour)
    fill(9, 240, 70, 200)

    # the colour format for `stroke` works the same as with `fill`
    stroke(238, 0, 255)
    # defines the thickness in pixels
    stroke_weight(2)

    text_font("Brush Script MT")
    text_style("bolditalic")
    text_size(95)
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
# - Add or subtract words (the number of time you invoke `text`).
# - Bonus: Note that nothing is stopping you from writing words *on top of one
#   another*. That actually creates a very different aesthetic (both in terms
#   of the colour combination but also the overal effect: cramming, packing,
#   blurring the meanings of the words you use).

# IMPORTANT NOTE: notice that in this sketch we only have `setup` and no
# `draw`? This this means that this sketch will draw things **only once** (no
# animation): `setup` runs once, but `draw` keeps running forever, redrawing
# the canvas many times per second. We need this for animation, but for static
# sketches like this one, it isn't needed. Go have a look at `animation.py` in
# the first lab: it has both `def setup():` and `def draw():`, because we need
# animation. You could test that you understand these concepts by taking the
# entire contents of `draw` in `animation.py`, and putting it in `setup`, see
# what happens; or vice versa, add `def draw():` here, with no indent, and
# adding all the code from the marked line down (not `run()`, leave that at the
# bottom) into it. Make sure the indent remains the same!
