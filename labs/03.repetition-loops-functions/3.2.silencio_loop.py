from py5canvas import *


# This is more of a 'plumbing' sketch: we're still looking at Gomringer's
# *silencio*, and seeing how we can 'refactor' (change/reconfigure) the code to
# achieve the same effect but experimenting with various techniques.

def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    # define my two types of lines
    line = "silencio silencio silencio"
    line_gap = "silencio          silencio"

    text("Use `line` and `line_gap` to", 60, 50)
    text("recreate the original poem.", 60, 100)
    text("(then look at the TODO...)", 60, 150)

run()

# TODO:
#   - Create a list containing the variables `line` and `line_gap` like so:
#
#       poem = [ ... ]
#
#     Then use a `for` loop with enumerate to display the lines:
#
#       for i, l in enumerate(poem):
#           text( ... )
#
#     We use `enumerate` to have an index that tells us the current line. You
#     can use that to increment the y position you use in text, so that you
#     don't draw all the lines at the same height! 
#
#   - We will now do the same thing, but with a different method.
#     We have our lines defined already, but we can also define all the
#     positions for each line (beware: both `poem` and `line` **must** have the
#     same number of elements!):
#
#       positions = [[60, 50],[...], ... ]

#     With both `poem` and `positions`, we can use a `for` loop with `zip` to
#     print the line at the position (the first `p` below is `[60, 50]`):
#
#       for l,p in zip(poem, positions):
#           text(l, p)
#
#   - Notice how we use this `60` all the time for x? Create a variable called
#     `margin` that holds this 60 that we use all the time for the x position.
#     Replace all instances of the 60, then see how you can change `margin`
#     *once* to control all lines.
#   - Extra: you could even automate things further and use a *comprehension*
#     for the creation of your positions, something like (replacing ... with
#     the same increment logic that we had with enumerate:
#
#       positions = [[60, ... ] for i in range(len(poem))]

# IDEAS, to make it your own:
# - Here, apart from changing the words as well as look and feel of the text,
#   the main thing we are working towards is the construction of a *system*: we
#   start with the original, but gradually we construct a machine, or process,
#   that *produces* that same original, if certain parameters are given (say,
#   the number of times our loop runs, or the line height, etc.). As we keep
#   building, it is possible for us to change the parameters, and let *the
#   system* itself guide the process of creation, opening new possibilities for
#   us.
