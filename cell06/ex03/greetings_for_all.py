def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings('Kylian')
greetings('Mbappe')
greetings()
greetings(42)