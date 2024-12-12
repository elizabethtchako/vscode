colors = ['red','orange','yello','green','green','blue','purple']

colors[2] = 'yellow'
print(colors)

colors.remove('green')
print(colors)

colors.append('pink')
print(colors)

colors.insert(0,'white')
print(colors)

colors.append('black')
print(colors)

del colors[-1]
print(colors)

no_color = colors.pop(0)
print(colors)
print(no_color)



colors.reverse()
print(colors)

colors.reverse()
print(colors)

colors.sort()
print(colors)

print('\n')
colors.sort(reverse = True)
print(colors)

print(sorted(colors, reverse=True))

print(sorted(colors))
print(colors)

print(len(colors))

print(colors[6].title())










