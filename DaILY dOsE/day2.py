names = []
name = input('What is your name?')
print(f"{name} you left some space maybe?")
name = name.strip()
names.append(name)

names.insert(0,'stevie')
names.insert(1, 'joey'.title())
names.append('marina'.title())

print(names)


name