pizzas =[]

pizzas.append('cheese')
pizzas.insert(0,'buffalo')
pizzas.insert(2,'veggie')


for pizza in pizzas:
    print(f"I like {pizza} pizza")

print(f"I really like pizza")

pizzas.append('balsamic')
fpizza = pizzas[:]

fpizza.insert(0,'pepperoni')
pizzas.insert(3,'garlic')


print(f"My friends favorite pizzas are {fpizza}")

print(f"\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    

print(f"\nMy friends favorite pizzas are:")
for pizza in fpizza:
    print(pizza)





pets = []
pets.append('dog')
pets.append('cat')
pets.insert(0,'fish')

for pet in pets:
    print(f"A {pet} would make a great pet.")

print(f"Any of thee animals would make a great pet!")
    