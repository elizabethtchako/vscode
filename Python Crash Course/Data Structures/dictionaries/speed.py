alien = {}

alien['color'] = 'yellow'
alien['points'] = 5
alien['x-axis'] = 0
alien['y-axis'] = 25
alien['speed'] = 'slow'

print(alien)
print(f"Speed: {alien['speed'].title()}", end ='\n\n')
print(f"Original position: {alien['x-axis']}")


if alien['speed'] == 'slow':
    x_increment = 1

elif alien['speed'] == 'medium':
    x_increment = 2 

else:
    x_increment = 3

#the new postion is the old position plus the increment 
alien['x-axis'] = alien['x-axis'] + x_increment 
speed = alien['speed'] #hold in a variable for formatting 
space = alien['x-axis'] #hold in a variable for formatting  

print(f"New position: {space} ")