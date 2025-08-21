def greet(name):
    return f"Hello, {name}"

print(greet("How are you?"))


def message(greet):
    if "how are you" in greet.lower():
        return "I'm fine, thank you! How are you?"
    elif "hello" in greet.lower():
        return "Hello there, Nice to meet you!"
    elif "bye" in greet.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure, how to respond to that, but I'm learning"
    
print(message("How are you?"))
print(message("Hello"))
print(message("Okay, bye"))
print(message("come"))
