#Elizabeth Tcako

#learn about methods [.sort() can take the argument reverse=True -- .sort permenant change] and [.reverse() permenant change]
#learn about functions [sorted() - can take two argument, the value and then reverse= True] and len() length is not by index but by items 
#store the list alpabetically, or in order in which you please or the kenght of the list 
# le

cars = ['bmw','audi','toyota','subaru']
cars.sort() # changes the order prementaly 
print(cars) # print = ['audi', 'bmw', 'subaru', 'toyota']

#You can also sort in reverse alphabetical order by passing the argument reverse=True to the sort methos 
cars.sort(reverse=True) # again the list is permentaly changed 
print(cars) # print = ['toyota', 'subaru', 'bmw', 'audi']


#  to maintain the order but stil present it in the sorted form you can use the sorted  FUNCTION
cars = ['bmw','audi','toyota','subaru']
print (f'Here is the orginal list {cars}')
print (f'Here is the new list {sorted(cars)}') # sorted() fuction takes the arguemnt (cars) 
print (f'Here is the new list reverse and sorted {sorted(cars, reverse = True )}') # sorted and reversed but no permentant ( takes 2 arguments )
print (f'Here is the orginal list again {cars}') # showing its not permenant 

#NOTE - sorting when not eveerything is lowercase makes thign complicted becuase there are several ways to interept captial letters 

#reverign the order of the list without sorting-
#maybe you want to sort becuase thi sis the order you recived the cars and you want to the ist in chronological order 
print('\n\n\n\n\n\n')
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse() # simply reverses the list 
print(cars) # changes the list permenantly print = ['subaru', 'toyota', 'audi', 'bmw']

#len is a function
len(cars)
print(len(cars)) # 4 not off by one error )