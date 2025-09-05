from py5canvas import *

# eyeballed
row_height = 30
char_width = 16
char_height = 22
vertical_offset = 4

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

    current_colour = cursor_colours[blink_state]
    if sketch.frame_count % blink_every == 0:
        blink_state = (blink_state + 1) % 2

    fill(*current_colour)
    line_offset = row_height * (len(my_text) - 1)
    x_pos = 50 + char_width * len(my_text[-1])
    y_pos = 50 + line_offset - char_height + vertical_offset

    rectangle(x_pos, y_pos, char_width, char_height)

    fill(0, 255, 0)
    for i, t in enumerate(my_text):
        y_pos = 50 + i * row_height
        # instead of calculating the real width of characters,
        # print them one by one
        for j, char in enumerate(t):
            x_pos = 50 + char_width * j
            text(char, [x_pos, y_pos])


def key_pressed(key):
    global my_text

    if key == "BACKSPACE":
        # if the last line isn't emtpy
        if len(my_text[-1]) > 0:
            # remove the last character
            my_text[-1] = my_text[-1][:-1]
        elif len(my_text) > 1:
            my_text.pop()
            my_text[-1] = my_text[-1][:-1]
    elif key == "ENTER":
        # add a new line
        my_text.append("")
    else:
        # manual wrapping: if width is longer than
        # 21 chars (eyeballed it), continue on a new line
        if len(my_text[-1]) > 19:
            my_text.append(key)
        else:
            my_text[-1] += key
    print(f"key: {key} | text {my_text}")


run()

#

# TODO: handle control keys, here's a list:

# "ESCAPE", "ENTER", "TAB", "BACKSPACE", "INSERT", "DELETE", "RIGHT", "LEFT",
# "DOWN", "UP", "PAGE_UP", "PAGE_DOWN", "HOME", "END", "CAPS_LOCK",
# "SCROLL_LOCK", "NUM_LOCK", "PRINT_SCREEN", "PAUSE", "F1", "F2", "F3", "F4",
# "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15", "F16",
# "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24", "F25", "KP_0", "KP_1",
# "KP_2", "KP_3", "KP_4", "KP_5", "KP_6", "KP_7", "KP_8", "KP_9", "KP_DECIMAL",
# "KP_DIVIDE", "KP_MULTIPLY", "KP_SUBTRACT", "KP_ADD", "KP_ENTER", "KP_EQUAL",
# "LEFT_SHIFT", "LEFT_CONTROL", "LEFT_ALT", "LEFT_SUPER", "RIGHT_SHIFT",
# "RIGHT_CONTROL", "RIGHT_ALT", "RIGHT_SUPER"


# TODO: fun idea: how to add add "> " at the beginning of each line (and handle
#       the delete / wrap / new line logic)?

# TODO: ideally we'd need the behaviour of repeated key presses with one key
#       kept down
