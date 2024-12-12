name = 'Elizabeth'

age = input(f"What is your age, {name}?")
print(f"you entered {age}")

age = age.lstrip()

print(f"Here is the cleaned up {age}")

print(f"Here is your age modified {age.removesuffix('1')} cleaned kinda")
age = age.rstrip()
print(f"Here is your age modified again {age.removeprefix('2')} cleaned")

print(f"all caps \n\t{name.upper()}")
print(f"lowercase \n\t{name.lower()}")
print(f"Captialize 1 {name.title()}")



