from py5canvas import *
import ollama

# TODO change the system prompt & hard-coded message (one could imagine
# implementing a chatbot logic, like in the other sketch)

system_prompt = """
You are a helpful assistant, and in self your current role you are particularly
verbose, and try to answer queries with as much detail as you possibly can.
"""

hard_coded_message = """
Hello there, how are you?
"""

# global variables: our stream, the speed of response, and a boolean flip
# preventing multiple text requests at the same time
stream = None
chunk_every = 5
message_requested = False

# ollama ----------------------------------------------------------------------

# `try / except` allows you to catch an error without your program failing
try:
    # this just tests the connection to the server
    ollama.ps()
except ConnectionError as ce:
    print("-" * 80)
    print(ce)
    print("**")
    print("This means:")
    print(
        "The Ollama server not running, open a terminal and run `ollama serve`! (Obviously Ollama needs to be installed...)"
    )
    print("-" * 80)
    exit()

# https://ollama.com/library/gemma3
model_name = "gemma3:270m"

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": hard_coded_message},
]

current_tokens = []

# test if the model is downloaded, if not pull from the server
if model_name not in [m.model for m in ollama.list().models]:
    print(f"model '{model_name}' not found, downloading...")
    ollama.pull(model_name)

msg = f"[initialising model: {model_name} with Ollama]"
print(msg)
print("-" * len(msg))

# -----------------------------------------------------------------------------

# text chunk ------------------------------------------------------------------

# logic derived from Dan Shiffman's Nature of Code
# https://natureofcode.com/particles/
# https://editor.p5js.org/natureofcode/sketches/-xTbGZMim


class Token:
    def __init__(self, chunk, pos):
        self.chunk = chunk
        self.acceleration = create_vector(0, 0.05)
        self.velocity = create_vector(
            random(-1, 1),
            random(-1, 0),
        )
        self.position = pos
        self.lifespan = 255

    # print(f"Initialisation: {self.chunk=}, {self.position=}")

    def run(self):
        self.update()
        self.display()

    # method to update position
    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.lifespan -= 2

    # method to display
    def display(self):
        push()
        no_stroke()
        text_align(CENTER, CENTER)
        text_size(36)
        fill(0, self.lifespan)
        text(self.chunk, self.position)
        pop()

    # is the particle still useful?
    def is_dead(self):
        if self.lifespan < 0.0:
            return True
        else:
            return False


# -----------------------------------------------------------------------------


def setup():
    create_canvas(800, 600)
    background(255)
    frame_rate(60)

    text_font("Helvetica")
    text_size(25)
    no_stroke()
    fill(0)


def draw():
    global current_tokens
    global message_requested
    global stream

    background(255)

    # 1) We get tokens from the stream: only if there's been a request, and
    # only every `chunk_every` frame (slowing things down)
    if message_requested and frame_count % chunk_every == 0:

        # get the next chunk
        next_token = next(stream)

        # this prints to the terminal, for debugging
        print(next_token.message.content, end="", flush=True)

        # TODO: here we could also loop over content and have one Token per char!
        # TODO: we could imagine using something other than the mouse position

        # create a new `Token` object with the content
        tok = Token(next_token.message.content, [mouse_x, mouse_y])
        current_tokens.append(tok)

        # once the LLM is done writing, we allow new requests again
        if next_token.done:
            message_requested = False

    for chunk in current_tokens:
        # print(f"printing chunk: {chunk.chunk}")
        chunk.run()
        if chunk.is_dead():
            # print("dead chunk, removing")
            current_tokens.remove(chunk)
            # print(current_tokens)


def mouse_pressed():
    global stream
    global message_requested

    # a switch: if the LLM is not writing, flip the switch (that will prevent
    # any more requests), and continue; if it is, return (don't request text)
    if not message_requested:
        message_requested = True
    else:
        return

    print("-" * 40)
    msg = "requesting message"
    print(msg)
    print("-" * len(msg))

    # we also use the stream, but simply update the global variable `stream`,
    # and deal with the chunks in draw
    stream = ollama.chat(
        model=model_name,
        messages=messages,
        stream=True,
    )


run()

# IDEAS, to make it your own:
# - As you can see, here the interaction with the bot is not the usual one:
#   instead of a 'dialogue', we just use it almost like a tap, i.e. a 'word
#   dispenser', with the mouse click opening the tap to get some text, and the
#   system prompt and first message being hard coded. All these elements can be
#   changed: of course the system prompt & initial message, but perhaps more
#   importantly the interaction and the use of text after:
#       - Can you think of other ways of interacting with the LLM text stream
#         (even if you can't implement this right now)?
#       - Can you think of ways in which that text stream can be used? Simple
#         example: what if you `lowercase`-d all the text, and then defined one
#         particular action or animation for every letter (simpler idea: one
#         action for vowels, one for consonants, one for punctuation & spaces):
#         then the 'textual' answer is translated into something visual!
# - I highly recommend digging into Dan Shiffman's Nature of Code, that has so
#   many interesting examples of how to construct various systems and
#   animations (in p5.js, but by now you can start seeing how it might be
#   possible to port these to Python, even using ChatGPT to help you). I don't
#   believe a single one of these sketches cannot be transformed to integrate
#   some form of textuality, and now you know how to use a tool that can
#   potentially produce (semi-)meaningful text for you, and that can be
#   integrated into these. One next step here, for instance, would be to
#   research Physics Engines, so that you can get these tokens to bump into
#   each other, and e.g. pile up on the 'floor' of the sketch, like physical
#   balls.
