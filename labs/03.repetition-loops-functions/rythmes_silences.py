from py5canvas import *

margin = 50
row_height = 30

def setup():
    create_canvas(600, 520)
    background(255)
    frame_rate(60)


def draw():

    background(255)
    no_stroke()

    fill(0)
    text_font("Courier New")
    text_size(25)

    word1 = "rythmes"
    word2 = "et"
    word3 = "silence"
    gap   = " " * 4

    for i in range(len(word1)):
        if i == len(word1) - 1:
            txt = " " * (len(word1) - i - 1) + word1[-(i+1):] + gap + word2 + gap + word3[:(i+1)]
        else:
            txt = " " * (len(word1) - i - 1) + word1[-(i+1):] + gap + " " * len(word2) + gap + word3[:(i+1)]
        text(txt, [margin + 60, margin + row_height + i * row_height])

    for i in range(len(word1)):
        txt = " " * (i + 1) + word1[(i+1):] + gap + " " * len(word2) + gap + word3[:len(word3) - (i+1)]
        text(txt, [margin + 60, margin + row_height + len(word1) * row_height + i * row_height])

run()
