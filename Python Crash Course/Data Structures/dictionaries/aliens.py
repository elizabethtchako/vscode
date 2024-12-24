#accessing, adding, modifying, removing 

#dictionary: 
#accessing (dicitionary['key'])
#accessing (dicitonary.get('key')) -- error message = None
#accessing2 (dicitonary.get('key','error message'))
#adding (dicitonary['key'] = value)
#modfiying (dictionary['key'] = new value)
#removing (del dictionary['key'])

#list: 
#accessing 
#adding 
#adding 
#

alien_0 = {'color': 'green','points':5}
#accessing key value pairs
#acessing by key 
print(alien_0['color'])
print(alien_0['points'])

#accesing a list - 
# accessing by index 
num = [1,2,3]
print(num[0])

newpoints = alien_0['points']
print(f"You just earned {newpoints} points!")

#adding to dictionary 
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

#adding to list
num.append(7)
num.insert(0,6)
num.sort()
print(num)


#working with an empty list 
numbers =[]
numbers.append('1')
numbers.insert(0,'2')
print(numbers)


#working with an empty dictionary 
alien_1 = {}

alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x axis'] = 0
alien_1['y axis'] = 25 

print(alien_1)


#modifying a list
numbers[1] = 6
print(numbers)

#modifying a dictionary 
color = alien_0['color']
print(f'The color of your alien is {color}')

#modifying value for key 'color'
alien_0['color'] = 'yellow'

color = alien_0['color']
print(f"The new color of your alien is {color}")

#removing in a  list
num = [1,2,3]
print()
print(num, end = '\n\n') 
del num[0]
num.remove(3)

print(f"remaining aftr 'del' and 'remove method': {num}")
nums = num.pop()

print(f"list after pop: {num}")
print(f"popped value: {nums}")

print()
#removing in a dictionary 
alien ={}
alien['color'] = 'yellow'
alien['points'] = 5

print(alien)
#del is permanately deleting 
del alien['points']

print(alien)



#.get() method
alien1 = {}
alien1['color'] = 'purple'
alien1['speed'] = 'slow'

print(alien1)

alien = alien1.get('color')
print(alien)

aliens = alien1.get('points', 'Does not exist')
print(aliens)

