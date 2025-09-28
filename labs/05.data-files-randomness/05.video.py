# Unrolling Event (1965) Director: Paul Sharits. Source:
# https://www.gartenbergmedia.com/dvd-distribution-and-sales/experimental-narratives-avant-garde-shorts/fluxfilm-anthology

from py5canvas import *

video = VideoInput(
    # if you do not give a file name, your webcam is used instead
    "data/fluxus-instructions.low.mp4",
    # the next arguments allow you to filp the video horizontally or vertically
    # flipped=True,
    # vertical_flipped=True
)

def setup():
    # print(f"video size {video.size}")
    create_canvas(*video.size)

def draw():
    background(0)

    # extract the next frame
    frame = video.read()

    # place the frame on the canvas
    image(frame, 0, 0)

    # the last two arguments allow you to resize the video
    # image(frame, 0, 0, width/2, height/2)

run()
