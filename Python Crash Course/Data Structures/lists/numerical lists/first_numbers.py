#Elizabeth
#07/10/24

#pythons rnage() function makes it easy to generate a series of number range(start,stop,[step])


for value in range(1,5): #is not inclusive of the number 5 
    print(value)
    #1
    #2
    #3
    #4

#starts at te first value you give it 
# to print 1-5 you must do for i inrange(1,6):

for value in range(1,6):
    print(value)

# you can also pass range only one argument and it wil start at 0 and would still be one off from the number you gave it 
for value in range(6):
    print(value)
    #0
    #1
    #2
    #3
    #4
    #5

numbers = list(range(1,6)) #makes range (1,6) 1-5 a list 
print(numbers)

# the thrid argument in the range function tells python to skip numbers ina given range, this is the step size 

