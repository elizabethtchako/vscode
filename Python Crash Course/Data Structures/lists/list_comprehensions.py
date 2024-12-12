#Elizabeth Tchako
#07/10/24
#write a list of list comprhensions 

#HOW TO WRITE?????
# - statrt with a list name 
# - open the bracket
# - define the expression for the value you want to store in the new list (what would go under the for loop)
# - last write  for loop to genreate the number you want to feed into the expression
# - close the bracket 

#Let's practice!

#square numbers
square = [value**2 for value in range(1,11)]
print(square)

#even numbers
even_num = [value for value in range(0,11,2)]
print(even_num)

odd_num = [value for value in range(1,10,2)]
print(odd_num)

# AS FOR NOW CANT DO MULTIPLE IN THE LIST COMPREHENSION 
multiple = [value **2 for value in range(1,10)]
print(multiple)

