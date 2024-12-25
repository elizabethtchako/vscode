my_foods = ['bread','eggs','tbacon','chicken']
friend_foods = my_foods[:]

print(f"Here's my favorite foods:")
print(my_foods)

print(f"Here's my friend's favorite foods:")
print(friend_foods)

#prove they are different lists
friend_foods.append('spinach')
my_foods.insert(0,'pasta')

print(my_foods)
print(friend_foods)

#make them the same again
my_foods=friend_foods[:]
print(f"Here: {my_foods}")


print(f"The first three items in the list are {my_foods[:3]}")
print(f"Three items from the middle of the list are{my_foods[1:4]}")
print(f"The last three items in the list are: {my_foods[-3:]}")
