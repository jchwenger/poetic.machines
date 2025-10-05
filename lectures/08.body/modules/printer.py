def hello():
    print("Hello from `printer.py`")

messages = ["One message from `printer.py`", "Another message from `printer.py`"]

print(f"(my script name is {__name__=})")

if __name__ == "__main__":
    print("Hi there, I am `printer.py`, and I have just been invoked as a standalone script.")
