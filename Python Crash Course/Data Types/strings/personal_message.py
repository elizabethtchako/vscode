#Elizabeth Tchako
#07/03/2024
#Pratice for the name.py

name = input("What is your name?\n ")
name = name.strip()
print(f"Hello {name.title()}, would you like to learn some Python today? ")

name_up = name.upper()
print(name_up)

name_low = name_up.lower()
print(name_low)

name_title = name_low.title()
print(name_title)

author = 'Albert Einstein'
quote = 'A person who never made a mistake never tried anything new'

print(f'{author.title()} once said, "{quote}."') #quote and add quotations 









name = 'elizabeth'
print(f"Hello {name.title()}, would you like to learn some Python")

print(name.upper())
print(name.lower())


famous_person = 'micheal jackson'
print(famous_person.title())
print(famous_person.upper())
print(famous_person.lower())
fun = ' \telizabeth\n'
print(fun)

print(fun.lstrip())
print(fun.rstrip())
print(fun.strip())

value = 'python_notes.txt'
print(value.removesuffix('.txt'))