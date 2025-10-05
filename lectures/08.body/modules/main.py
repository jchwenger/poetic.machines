import printer as pr

pr.hello()

# Note: this no longer works since we aliased `printer` but it would work if you
# *also* add `import printer`above
# printer.hello()

print("\n".join(pr.messages))

print(f"(my script name is {__name__=})")
