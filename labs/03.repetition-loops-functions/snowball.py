from py5canvas import *


# we define a variable called `to_be_snowballed`, containing
# the text we want; later on, we pass that to `text` to display
# its contents
to_be_snowballed = "the relief of the simplicity of it"

def setup():
    create_canvas(400, 700)

    background(255)

    text_font("Courier New")
    text_size(14)
    no_stroke()
    fill(0)

    # i here is a variable that changes at each iteration of the loop:
    # it starts with zero, then 1, then 2, etc.. (use `print` to see it in the
    # console)
    for i in range(len(to_be_snowballed) + 1):
        text(to_be_snowballed[:i], 10,  i * 20)

run()

# IDEAS, to make it your own:
# - Where does the snowball magic happen? It's when we combine the loop logic
#   with the slicing `[:i]`. Currently the text grows from left to right, can
#   you reverse that, and make it gradually go from complete text to one letter
#   (using the index)?
# - Notice that `+ 1` after `len(to_be_snowballed)`? What happens if you remove
#   it? Can you add the `+ 1` in the slicing brackets instead, to see the
#   difference? These subtle changes (and problems that come with it) are very
#   common in programming, and having familiarity with them is essential not to
#   stumble on weird unexpected problems later down the line : ).
# - How about using `text_align` to centre the text? Can you see the whole
#   text? How do you make sure the full text is visible on the canvas? Can you
#   use `width` so that the text remains centred even if you change the size of
#   the canvas?
# - Build a new work: can you think of a different text that could be used with this
#   effect to create an interesting overall meaning? As before, it can be
#   useful to think about colour, size, font, etc.
# - You are not limited to only one increasing/decreasing text: can you add
#   another loop (and potentially another text) and experiment with placement?
# - In the examples given by Ilse Garnier, you can see that she works with two
#   movements, increase to full text, then decrease. This could be an
#   interesting challenge!
# - Like before, you could move everything from `background` downwards into a
#   `def draw():` function – respecting the indent! – if you wanted to add some
#   animation later down the line.
