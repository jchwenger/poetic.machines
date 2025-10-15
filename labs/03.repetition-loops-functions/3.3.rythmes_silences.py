from py5canvas import *

margin = 50
row_height = 30

word1 = "rythmes"
word2 = "et"
word3 = "silence"

def setup():
    create_canvas(400, 520)
    background(255)
    frame_rate(60)


def draw():
    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    text("Read the TODOs", margin, margin)
    text("below (then delete", margin, margin + 50)
    text("me <3)", margin, margin + 100)

    # TODO: draw word1 using `draw_word_right_aligned`, place it at `margin`,
    # `margin`

    # TODO: draw word3 using `draw_word_left_aligned`, place it at `width -
    # margin`, `margin`

    # TODO: now that you have used existing functions it is time for you to define
    # your first function! Here's how you do it:
    # - first, use `text_align` to centre the text, then use `text` to write
    #  `word2` in the middle of the canvas, using `width` and `height`
    # - once you have this, go below `# functions`, and write, on a new line:
    #
    #       def draw_text_centred():
    #
    #   then cut the two lines you wrote earlier to display the text and paste
    #   them 'inside' this function (just below, with **one indentation** =
    #   tab/4 spaces); finally, call the function inside `draw`, where you had
    #   your two lines, like this:
    #
    #        draw_text_centred()
    #
    # - If you want to make this function more flexible, to allow it to display
    #   other kinds of texts, at various kinds of positions, what you need to do
    #   is:
    #   1) change it *definition* to:
    #
    #       def draw_text_centred(word, x, y):
    #
    #   2) change the body (code inside) so that what was "word2" is now
    #   "word", and the two coordinates of `text` are `x` and `y`;
    #   3) change the *call* inside `draw` to this (with ... replaced with the
    #   x and y you used earlier:
    #
    #       draw_text_centred(word2, ..., ...)


# functions ----------------------------------------------------------------------

# TODO: here you'll define your own `draw_text_centred` function

# NO NEED UNDERSTAND WHAT FOLLOWS IN DETAIL (we'll see more of this later)

def draw_word_right_aligned(word, x, y):
    text_align(RIGHT)

    # top bit
    for i in range(len(word)):
        txt = word[-(i + 1) :]
        x_adjusted = x + text_width(word)
        y_adjusted = y + row_height + i * row_height
        text(txt, x_adjusted, y_adjusted)

    # bottom bit
    for i in range(len(word)):
        txt = word[(i + 1) :]
        x_adjusted = x + text_width(word)
        # this is the same as top bit with also len(word) additional lines
        y_adjusted = y + row_height + i * row_height + len(word) * row_height
        text(txt, x_adjusted, y_adjusted)


def draw_word_left_aligned(word, x, y):
    text_align(LEFT)

    # top bit
    for i in range(len(word)):
        txt = word[: (i + 1)]
        x_adjusted = x - text_width(word)
        y_adjusted = y + row_height + i * row_height
        text(txt, x_adjusted, y_adjusted)

    # bottom bit
    for i in range(len(word)):
        txt = word[: len(word) - (i + 1)]
        x_adjusted = x - text_width(word)
        y_adjusted = y + row_height + len(word) * row_height + i * row_height
        text(txt, x_adjusted, y_adjusted)


# --------------------------------------------------------------------------------

run()


# IDEAS, to make it your own:
# - Experiment with different kinds of text (you can resize the canvas if the
#   shapes become too large). Using function allows you to do a lot very
#   concisely! Imagine, you could now write a loop that calls one of these
#   functions and draw a *lot* of text.
# - Given what you worked on snowball, you can even think about what you learnt
#   there to try and modify `draw_word_right_aligned` or
#   `draw_word_left_aligned`! 
