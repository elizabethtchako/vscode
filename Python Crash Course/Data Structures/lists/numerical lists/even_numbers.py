#Elizabeth Tchako
#07/10/24


# the thrid argument in the range function tells python to skip numbers ina given range, this is the step size 
#using the range of numbers and converting it to a list() with the list() function 
#combine loops and list to manipulate the numbers and print out a list of numbers

even_numbers = list(range(2,11,2)) # starts with 2, add to the value 2 until it reaches 11 which it does not print
print(even_numbers)

squared = [] # start with an empty list

for value in range(1,11): # take the values from the range 1-10
    square = (value**2) # create a varible called square that will store the value 
    squared.append(square) # append that value 

print(squared)

# trying it again how I wouldve approached 
soup = list(range(11))
soups = []
for i in soup:
    souped = i**2
    soups.append(souped)
print(soups)

# more conscise
squares = []
for i in range(1,11):
    squares.append(i**2)
print(f'\n{squares}')

# all methods work but the first is easier to read, the second is long, the thrid is conciss





