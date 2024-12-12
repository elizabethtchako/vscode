toppings = []
toppings.append('cheese')
toppings.insert(0, 'pepperoni')
toppings.insert(-1, 'veggie')
toppings.append('anchovies')

print(toppings)

'mushrooms' in toppings
#False

'mushrooms' not in toppings 
#True

requested_top = 'mushrooms'

if requested_top not in toppings:
    print(f"{requested_top.title()}, is not on the menu.")


print(len(toppings))
toppings.insert(0,'chicken')
print(toppings)