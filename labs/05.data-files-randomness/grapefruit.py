from py5canvas import *

row_height = 50

# load instructions from a text file, using Yoko Ono's Grapefruit (1964, extracts)
# https://en.wikipedia.org/wiki/Grapefruit_(book)
# (manually ported from the pdf source on Monoskop:
# https://monoskop.org/images/archive/6/64/20190320203953%21Ono_Yoko_Grapefruit_A_Book_of_Instructions_and_Drawings_2000.pdf)

with open("data/Ono.Grapefruit.extracts.txt", "r") as i:
    # first, split each poem by the separator ('***' added manually), remove
    # leading/trailing newlines, and split again by newlines
    instructions = [p.strip().split("\n") for p in i.read().split("***")]

new_instruction_length = random_int(1, 4)
print(new_instruction_length)


def setup():
    # we already know how tall our poem will be (since we don't wrap the text,
    # we can programmatically create our canvas, adding some margins as well
    # (1200 is done by hand, looking at the longest line)
    create_canvas(1200, 3 * row_height + row_height * new_instruction_length)

    text_font("Courier New")
    text_size(15)

    # title ----------------------------------------
    # get a random instruction, take the title (always first line)
    title = get_random_instruction()[0]
    text(title, row_height, row_height)

    # body -----------------------------------------
    # for as many lines as we decided above
    for i in range(new_instruction_length):
        # get a random instruction
        instr = get_random_instruction()
        # get any line which is not the first nor the last
        line_idx = int(random(1, len(instr) - 1))
        # write this line to the canvas
        text(instr[line_idx], row_height, row_height + (i + 1) * row_height)

    # date -----------------------------------------
    # get a random instruction, take the date (always last line)
    date = get_random_instruction()[-1]
    # i is still lying around, nifty!
    text(date, row_height, row_height + (i + 2) * row_height)


def get_random_instruction():
    idx = int(random(len(instructions)))
    return instructions[idx]


run()

# IDEAS, to make it your own:
# - Here the same principles of randomness apply as in the other sketches,
#   except that we use a plain text file structured in a certain way
#   (instructions separated by '***', always the same format). Working with
#   another text, and changing the way in which randomness is applied, will
#   modify the result a lot! This is very much the spirit of Alison Knowle's
#   *House of Dust*, and also Raymond Queneau's 1,00,000,000,000 poems!
