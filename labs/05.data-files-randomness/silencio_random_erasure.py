from py5canvas import *
import numpy as np

step_every = 20

n_line = 5
n_col = 3

random_line = np.random.randint(0, n_line - 1)
random_col = np.random.randint(0, n_col - 1)


def setup():
    create_canvas(512, 300)
    background(255)
    frame_rate(60)


def draw():
    global random_line
    global random_col

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    # text_style("normal")
    text_size(25)

    word = "silencio"

    sleep_time = 0.2

    # here we have the same logic as last week,
    # with only one big difference: our conditional
    # is now 
    for i in range(n_line):
        line = ""
        for j in range(n_col):
            if i == random_line and j == random_col:
                line += " " * (len(word) + 1)
            else:
                line += word + " "
        text(line, [60, 50 + 50 * i])

    if sketch.frame_count % step_every == 0:
        # create a random number in [0,1], multiply it by the number we want,
        # then turn that to an int (this works because `random` never actually
        # outputs 1, so we never ever reach `n_line` or `n_col`, always a bit
        # below, and the decimal part gets chopped off by int() (it's a *floor*
        # rather than a *ceiling* operation)
        random_line = int(random() * n_line)
        random_col = int(random() * n_col)

        # for sanity you can always check
        # print(random_line, random_col)


run()

# IDEAS, to make it your own:
# - You might start feeling slightly sick of this silentious example, and this,
#   I assure you, is a sign of sanity! Rest assured, however: just like with
#   the stages of grief, acceptance is coming soon, I promise (after reading
#   week, to be precise, when we see this **for the last time** :}). For this
#   one, the important thing is that you understand what the random generation
#   does, and what it gives you. Once you understand that you can get random
#   numbers between [0,1] (never reaching one), and that you can scale those
#   numbers with multiplication, and potentially turn those floats into ints,
#   then you have the tools you need to apply randomness to any parameter you
#   like! Fun thing to try:
#   - Change the word (lol, but yes, do that).
#   - If you implemented a version where you draw each word separately, then
#     instead of replacing that word with blanks, you could do a translate with
#     a random destination, or a rotate with a random angle!
#   - Remember how we #BrokeTheSilence using colours and such? Now you can use
#     random numbers to select the integer in your RGBA values, or the size of
#     the text, or even the font, if you define a list of font names at the
#     start of the sketch!
#   - Also, you could inject randomness in `step_every`, by picking a new
#     random `step_every` in the same spot where we currently select
#     `random_line` and `random_col`, creating a very different kind of
#     movement in the piece!
