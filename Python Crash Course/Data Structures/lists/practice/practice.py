fruits = ['bananas', 'kiwi', 'strawberries', 'raspberries', 'apple']
fruits.append('plum')
print(f'\n{fruits[0].title()}')
print(f'\n{fruits}')

fruits.insert(3, 'pineapple')
print(f'\n{fruits}')

fruits.pop() #print = ['bananas', 'kiwi', 'strawberries', 'pineapple', 'raspberries', 'apple'] removes 'plum'
print(fruits) 

nasty = fruits.pop(0)#remove bananas whihc is at index 0 
print(nasty) # pop can hold things that are removed for later 
del fruits[0] # removes kiwi (delete removes whichever index here i removed index 0 and so kiwiw is removed )
print(fruits)

fruits.remove('pineapple') # removing values 
print(fruits)

fruits.sort()
print(fruits)
print(len(fruits))
fruits.sort(reverse=True)
print(fruits)

print(sorted(fruits))
print(sorted(fruits, reverse=True))# sorting but not stored 
print(fruits) # shwoign its not sorted 

fruits = ['bananas', 'kiwi', 'strawberries', 'raspberries', 'apple']
fruits.reverse() # reverses the string without sorting 
print(f'\n{fruits}')

fruits[0] = 'fun' # you can modift indexes 
print(fruits)
print(fruits[0])
print(fruits[-1]) # always will ascess the last item in a list  wont work if the list is empty [] example below 

fruits =[]
print(fruits[-1])






