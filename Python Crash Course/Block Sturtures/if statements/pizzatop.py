toppings = []

toppings.append('pepperoni')
toppings.insert(0, 'extra cheese')
toppings.append('chicken')
toppings.append('veggie')
toppings.insert(0, 'anchovies')



print(toppings, end='\n\n')

toppings = []

if toppings:
    for top in toppings:
        if top in toppings:
            print(f"Adding {top.title()}!")

else: 
    print(f"Are you sure you want a plain pizza?")



toppings = []

toppings.append('pepperoni')
toppings.insert(0, 'extra cheese')
toppings.append('chicken')
toppings.append('veggie')
toppings.insert(0, 'anchovies')

available = ('anchovies', 'extra cheese', 'pepperoni', 'chicken', 'veggie')


request = ['mushrooms', 'olives', 'french fries']
request.append('pepperoni')
request.insert(0, 'veggie')


for top in request: 
    if top in available: 
        print(f"Adding {top}")
    else: 
        print(f"{top.title()}, not avaible")