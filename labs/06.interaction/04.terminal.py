from py5canvas import *

# all of these numbers are eyeballed, depend on the font and taste!
row_height = 30
char_width = 16
char_height = 22
vertical_offset = 4

# every 25 frames, our cursor will switch from green to black
blink_every = 25
cursor_colours = [(0, 255, 0), (0, 0, 0)]
blink_state = 0

my_text = [""]


def setup():
    global char_width
    global char_height

    background(0)
    create_canvas(400, 600)
    text_font("Courier New")
    text_size(25)
    no_stroke()


def draw():
    global my_text
    global blink_state

    background(0)

    # cursor ------------------------------------------------------------------

    # at a regular rythm, `blink_every`, flip the blink state
    if sketch.frame_count % blink_every == 0:
        blink_state = (blink_state + 1) % 2

    # update the colour and 
    current_colour = cursor_colours[blink_state]
    fill(*current_colour)

    # width and height at which our cursor (after the text)
    x_pos = 50 + char_width * len(my_text[-1])
    line_offset = row_height * (len(my_text) - 1)
    y_pos = 50 + line_offset - char_height + vertical_offset

    # draw the cursor
    rectangle(x_pos, y_pos, char_width, char_height)

    # text --------------------------------------------------------------------

    fill(0, 255, 0)
    for i, t in enumerate(my_text):
        # y is easy, just move down one line
        y_pos = 50 + i * row_height

        # instead of calculating the real width of characters,
        # print them one by one
        for j, char in enumerate(t):
            x_pos = 50 + char_width * j
            text(char, [x_pos, y_pos])


def key_pressed(key):
    global my_text

    print(f"key: {key}")

    # many control keys, we don't really need them (KP: keypad), but it's good
    # to have a reference (see here:
    # https://github.com/colormotor/py5canvas/blob/405ce311a941032d9b6c6e8fab557bd3f59cd355/py5canvas/run_sketch.py#L1864)
    # TODO: implement DELETE (remove forward), arrow keys to move cursor, etc...

    # (the following is an instruction for the formatter, ruff)
    # fmt: off
    if key in [
        "ESCAPE", "TAB", "INSERT", "DELETE",
        "RIGHT", "LEFT", "DOWN", "UP", "PAGE_UP", "PAGE_DOWN", "HOME", "END",
        "CAPS_LOCK", "SCROLL_LOCK", "NUM_LOCK", "PRINT_SCREEN", "PAUSE",
        "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11",
        "F12", "F13", "F14", "F15", "F16", "F17", "F18", "F19", "F20", "F21",
        "F22", "F23", "F24", "F25",
        "KP_0", "KP_1", "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8",
        "KP_9", "KP_DECIMAL", "KP_DIVIDE", "KP_MULTIPLY", "KP_SUBTRACT",
        "KP_ADD", "KP_ENTER", "KP_EQUAL",
        "LEFT_SHIFT", "LEFT_CONTROL", "LEFT_ALT", "LEFT_SUPER", "RIGHT_SHIFT",
        "RIGHT_CONTROL", "RIGHT_ALT", "RIGHT_SUPER",
    ]: return
    # fmt: on

    if key == "BACKSPACE":
        # if the last row isn't emtpy
        if len(my_text[-1]) > 0:
            # remove the last character
            my_text[-1] = my_text[-1][:-1]
        # if the last row is empty and we have more than one line
        elif len(my_text) > 1:
            # remove it
            my_text.pop()
            # and remove the last char of the previous line
            my_text[-1] = my_text[-1][:-1]

    elif key == "ENTER":
        # add a new row
        my_text.append("")
    else:
        # manual wrapping: if width is longer than
        # 19 chars (eyeballed it), continue on a new row
        if len(my_text[-1]) > 19:
            my_text.append(key)
        else:
            my_text[-1] += key

    print(f"           | text {my_text}")


run()

# IDEAS, to make it your own:
# - In some sense, this is just a 'technical' sketch, referring to early
#   computer aesthetic as already played with in pop-culture films like The
#   Matrix. Exploring the feel of this small interface this can already change
#   the overall experience quite significantly (an interesting concept here is
#   the one of 'skeuomorph', https://en.wikipedia.org/wiki/Skeuomorph, an
#   artifact that deliberately hints at a former technology that it has
#   replaced – like a digital 'notebook' integrating, as part of its design,
#   fake metal rings that remind people of paper notebooks...)
# - One fun alleyway of exploration, that has interesting implications
#   especially if your language does not follow the left-to-right direction
#   that Western languages have, would be to modify the sketch to write from
#   right to left, or top to bottom.
# - One could imagine other kinds of ways in which the seemingly simple act of
#   typing could be made weirder: what if letter you type is displayed
#   somehwere, randomly? What if the user only sees one letter at a time, the
#   last one that was typed?
# - Technical challenge: how would you go about adding a "> " at the beginning
#   of each line (and handle the delete / wrap / new line logic)?
