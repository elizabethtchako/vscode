#Elizabeth Tchako
#07/05/24
#Learn how to remove items from a list, removing from an index using (DEL - function : [index] ), or remove from list and to store for later using (.pop() for end value leave blank- or index, value), or removing by value using .remove(value)- one argument
#if you want to delete an item from a list and not use the item again use del
#if you want to use an item as you remove it, use the pop() method

motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles) 
del motorcycles[0]#removes the first index                                                                                                            
print(motorcycles) # print = ['yamaha', 'suzuki']

#you can remove from any position 
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1] #removes the second index   
print(motorcycles)#print = ['honda', 'suzuki']


#reminder when you del you cannot access these values anymore
#with pop you can access again 

motorcycles = ['honda', 'yamaha', 'suzuki'] #reset
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)# print['honda', 'suzuki']
print(popped_motorcycles) #print = suzuki (prove that we still have access to the item)


motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f'The last motorcyle I owned was a {last_owned.title()}')

#although not sending the method pop an argument will remove the last index, you can pop from any index when you add an argumen to the parenthese
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#sometimes you wont know a postion of a value you want to remove from a list 
#use the remove method which recives an argument of the value you are looking to remove 
#let's say you want to remove anyting in your list that is ducati

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
print(motorcycles)

#remove method only eremoves te first occurence of the value you specifil, if it appears more than one you need a loop
remove = motorcycles.remove('ducati') # remove one ducati
remove = motorcycles.remove('ducati') # remove second ducati (only one ducati)
too_expensive = 'ducati' # remove second ducati
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'The {too_expensive.title()} is too expensive')







