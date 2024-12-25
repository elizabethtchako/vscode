message = input("tell me something and I will repeat it back to you: ")
print(message)

prompt = f"We are personalizing a message for you!"
prompt += f"\nWhat is your name? "

name = input(prompt)

print(f"Hello, {name.title()}!")
