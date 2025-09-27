from py5canvas import *

erase_row = 0
erase_col = 0
step_every = 20


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    # we need global variables here since we are modifying them
    global erase_row
    global erase_col

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    # this time
    word = "silencio"
    n_row = 5
    n_col = 3

    # loop 1: for each row
    for i in range(n_row):
        line = ""
        # loop 2: for each column
        for j in range(n_col):

            # conditionals!
            if i == erase_row and j == erase_col:
                # if i (row) and j (col) correspond to the row/col to erase,
                # instead of adding the word like below, we add as many spaces
                # as there are characters in the word!
                line += " " * (len(word) + 1)
            else:
                # otherwise, at all other i and j, add the word
                line += word + " "
        text(line, [60, 50 + 50 * i])

    # we are in `draw`, which is run many times per second: try change
    # `step_every` to 1 and see how fast the change occurs (we use the modulo
    # logic to make sure that the code is only executed at certain frames (with
    # `step_every = 20`, it will be when `frame_count` is 0, 20, 40, ...)
    if sketch.frame_count > 0 and sketch.frame_count % step_every == 0:

        # linear logic: we update the column, but if we reach the max, we go
        # back to zero
        erase_col = (erase_col + 1) % n_col

        # then, if our column is at zero, it means we should update our row
        # (move down by one), so we use the same logic
        if erase_col == 0:
            erase_row = (erase_row + 2) % n_row

run()

# IDEAS, to make it your own:
# - What we built here is twofold: we have a system where we have just one
#   word, and then parameters we can easily control (rows, columns, and the
#   location – row, col – of erasure). What is more, we can use the modulo to
#   create various patterns, here are a few ideas:
#   - Can you change the system so that you erase an entire row, or column,
#     instead of just one slot? (Huh oh, the speed seems to change, why is
#     that?)
#   - Can you make the erasure happen every two cols, or two rows, instead of
#     every single one? (Note that the synchronisation between rows and columns
#     might get trickier than what we have here, don't worry about it for now.)
#   - For fun, can you test (and try to understand) what happens if you change
#     the logical operator `and` for `or`? This changes when this entire
#     line (the two expressions `i == erase_row`, `j == erase_col` combined)
#     is `True` or `False`!
#   - Can you reverse the direction of the flow (erase the last slot, then
#     next-to-last, etc.)?
#   - Change the poem to a square (same n_row/n_col): can you erase only the
#     word in one diagonal?
# - Extra: Notice how in the logic above we still build a text line for each
#   row, then display it? Another way of proceeding would be to just use `text`
#   inside the conditional, and just draw the full poem word by word. For this,
#   one additional thing is needed: `text_width`. Knowing the display width of
#   the word (given font & size) will allow you to update your indices
#   correctly.
