# mediapipe model ----------------------------------------------------------------

# Pose landmarks with:
# https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker

import pathlib
import urllib.request
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.core import base_options as base_options_module

# Path to the model file
model_path = pathlib.Path("pose_landmarker.task")

# Check if the model file exists, if not, download it
if not model_path.exists():
    url = "https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_heavy/float16/latest/pose_landmarker_heavy.task"
    print()
    print(f"Downloading model from {url}...")
    with urllib.request.urlopen(url) as r, model_path.open("wb") as o:
        while chunk := r.read(1024):
            o.write(chunk)
    print(f"Model downloaded and saved as {model_path}")

# Initialize MediaPipe HandLandmarker
base_options = base_options_module.BaseOptions(model_asset_path=model_path)
options = vision.PoseLandmarkerOptions(
    base_options=base_options, output_segmentation_masks=True
)
model = vision.PoseLandmarker.create_from_options(options)

# --------------------------------------------------------------------------------

from py5canvas import *
import numpy as np

video_size = 512
video = VideoInput(size=(video_size, video_size))


def setup():
    create_canvas(video_size, video_size)


def draw():
    background(0)

    # Video frame
    frame = video.read()
    frame = np.array(frame)  # uint8 (SRGB)

    push()
    scale(width / video_size)
    image(frame)

    # Detect pose landmarks
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    result = model.detect(mp_image)

    # Draw each detected person
    if result and result.pose_landmarks:
        # Canonical pose connections from the Solutions API
        POSE_CONNECTIONS = mp.solutions.pose.POSE_CONNECTIONS

        for lms in result.pose_landmarks:
            pts = landmarks_to_px(lms)

            # 1) Connections (white)
            no_fill()
            stroke(255)
            stroke_weight(2.0)
            draw_connections(pts, POSE_CONNECTIONS)

            # 2) Joints (cyan dots)
            no_stroke()
            fill(0, 200, 255)
            for x, y in pts:
                circle((x, y), 4.0)

    pop()  # close the push() done before drawing the frame


# helpers ------------------------------------------------------------------------


def landmarks_to_px(lms):
    """Convert one pose's landmarks to pixel coordinates in the video space."""
    return np.array([[lm.x * video_size, lm.y * video_size] for lm in lms], dtype=float)


def draw_connections(pts, connections):
    for a, b in connections:
        line(pts[a], pts[b])


run()


# IDEAS, to make it your own:
# - There is no obligation to display the video, and you could for instance
#   imagine a blank canvas where a few points from the body are used to control
#   the position, or other parameters (the size?) of text that is displayed on
#   the screen, like in the Google and Bill T. Jones collaboration here:
#   https://experiments.withgoogle.com/billtjonesai
# - You could instead use the distance between, say, the nose and one wrist,
#   that would allow a user to control the size of a figure!, or to make
#   something happen if they touch their noses! In this project, this idea is
#   used to allow users to scream silently!
#   https://x.com/JordanneChan/status/1483988494032805895
# - Going further with this, you have no obligation to work with the entire
#   skeleton, and perhaps you might want to use only the two wrists, or the two
#   knees, or less obvious combinations (eye and hip?, wrist and knee?)
