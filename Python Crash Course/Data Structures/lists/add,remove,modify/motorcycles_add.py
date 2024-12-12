#Elizabeth Tchako
#07/05/24
#learn how to modify, add to a list(at the end(APPEND), or wherever(INSERT))
#syntax for modifying an element is simlar to the syntax for accessing an element for lists and variable 

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)

#replace the first index / first item *You can change the value of any item
motorcycles[0] = 'ducati'
print(motorcycles)

#adding an item to the list is append, it willl go to the end of the list 
motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati') #append is a method for lists
print(motorcycles)# print = ['honda', 'yamaha', 'suzuki', 'ducati']

#You can even start with an EMPTY list and append from there
motorcycles = []
print (motorcycles)# print = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#you can add an elemeent to any postion of you list 
#do this by using th insert() methong and assign it an index and the value of the new item
#insert takes two arguments
#add takes one arguments

#open space at index one and store the value, shift every other value one postion right
motorcycles.insert(0,'ducati')
print(motorcycles)


 #removing an item takes two the index of a list, so you arent removing a specific value lists can contain duplicates)
motorcycles.insert(0,'ducati') #showing they can take duplicates 
print(motorcycles)# print = ['ducati', 'honda', 'yamaha', 'suzuki', 'ducati']

