# Lab 8

In each lab, we encourage you to go over the lecture material (the Jupyter notebooks), run things for yourself, try and modify the examples given, think about how they work, and how you could modify them to make them more familiar or useful to you.

[py5canvas reference](https://github.com/colormotor/py5canvas/tree/main/docs) (and [p5.js](https://p5js.org/reference/))

## Analogue experiment: Poetic Scores

1. Look back at the score-based and poetic performance works we looked at in today’s lecture. Take a moment to recall the things you found surprising, enjoyable, or particularly evocative. Consider how instruction/process, performance, and interpretation functioned in those pieces.

2. Now, in groups of three, write your own poetic scores involving language for other group members to perform. Be mindful of the context in which they are to be performed (e.g., in this room, now). Think carefully about how the performer should interpret the score, what actions or gestures it might suggest, and how much freedom or specificity the instructions should contain.

3. Once your scores are written, playtest them in your groups. Each round, one person becomes the Writer, who chooses a score they have written and gives it to the Performer. A third person acts as the Observer, watching the performance closely and trying to guess what the original score might have been. After the performance, the Observer shares their guess.


## Programming practice

This week, we are using some pretrained models from [mediapipe](https://ai.google.dev/edge/mediapipe/solutions/guide) inside our sketches. The structure of each sketch is roughly similar, with the webcam frames being fed to a detection model that outputs **keypoints** (or **landmarks**: coordinates of various points in the detected body, either on the face, the hand, or the full body). Here are the three models:
- [face landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/face_landmarker)
- [hand landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [pose landmarker](https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker)

Each of these sketches will look for a model file (e.g. `hand_landmarker.task`) in the directory the script is run in, and download it if it's not present (just to let you know, if you run the script from a different directory, like so: `python labs/08.body/01.face_landmarks.py` and `cd labs/08.body/; python 01.face_landmarks.py`, then the model will be downloaded again (once in each directory).

Other note: I'm not sure where this bug comes from, but sometimes when pressing 'play' in VSCode, the activation of the environment is slow, and comes *after* the script is run (VSCode tries to do `python 01.face_landmarks.py` before the environment is activated). This will fail, but if you press play again and VSCode tries to run the script again in the same terminal, then that problem goes away, as this time the environment is loaded already...
