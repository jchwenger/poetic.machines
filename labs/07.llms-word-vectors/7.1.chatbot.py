import ollama

# https://ollama.com/library/gemma3
model_name = "gemma3:270m"

# TODO: customise the system prompt
system_prompt = """Only answer in Spanish."""

# create the system message separately for later reuse
system_message = {"role": "system", "content": system_prompt}

messages = [system_message]

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

# test if the model is downloaded, if not pull (download) from the server
if model_name not in [m.model for m in ollama.list().models]:
    print(f"model '{model_name}' not found, downloading...")
    ollama.pull(model_name)

msg = f"[initialising model: {model_name} with Ollama]"
print(msg)
print("-" * len(msg))

# -----------------------------------------------------------------------------

# Le chatbot
# ----------

# at its core, it's just a plain loop running forever... (ctrl+c to exit)

while True:

    # get user input
    user_input = input("> ")

    # TODO: add non-LLM functionalities here

    # create the current message object
    current_message = {"role": "user", "content": user_input}

    stream = ollama.chat(
        model=model_name,
        # trick: to make sure our model *really* follows the system message,
        # insert it right before the last (current) user message – this way,
        # the model should follow these instructions and not lose track of them
        # as the discussion grows
        messages=messages + [system_message, current_message],
        stream=True,
    )

    # we then add the current message to our history
    messages.append(current_message)

    response = ""

    # stream: we loop through all the chunks and print them one by one
    for chunk in stream:
        # if you want to debug things, you can print the response object
        # print(chunk)
        # breakpoint()

        # both syntaxes work
        # c = chunk["message"]["content"]
        c = chunk.message.content

        # we save the text as we go, to keep a history of our messages
        response += c
        print(c, end="", flush=True)

    # (try to) guarantee we add a '\n' only if we need to
    if not response.endswith("\n"):
        print()

    # save the bot response
    messages.append({"role": "assistant", "content": response})

    # print("--- debug ---")
    # print(messages)
    # print("--- debug ---")


# IDEAS, to make it your own:
# - The first, most direct way to change the behaviour of the bot is to change
#   the `system_prompt`. The bigger the model, the more reactive it can be to a
#   complex promt, and the more developed and detailed the prompt, including
#   even examples of the desired behaviour, the more likely the bot will act in
#   the way desired. There are some free short courses on this particular topic
#   here: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng,
#   https://learn.deeplearning.ai/courses/prompt-engineering-with-llama-2
#   Note: this is clunky!, especially for small models. Don't expect full
#   compliance : >.
# - If you wanted to add special, non-LLM-related functionalities, such
#   as '/quit' to exit, as ollama itself implements, what you would need to do
#   is add a check at the marked point, to see what the `user_input` looks like
#   (`if user_input == "/quit":`) (one good functionality could be to have a
#   '/reset' function, that clears all messages (including the system promt or
#   not?, your choice!), or that allows the user to change the system prompt,
#   or to get it printed, etc.
# - Note: we use the user input (as string) to trigger certain actions, but
#   nothing prevents us from doing the same thing on the LLM side? Maybe a
#   particular game could be to try and get the LLM to output exactly a certain
#   word, or a certain sentence, and then, again with the same check logic we
#   had before, we can test if the bot answer is that, and if it is, do
#   something (such as, say, call `exit()` and stop the program is the LLm says
#   "I am unhappy, I want to leave.").
