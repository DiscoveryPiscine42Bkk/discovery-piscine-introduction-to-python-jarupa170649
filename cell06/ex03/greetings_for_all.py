def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

# Test calls as requested
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)