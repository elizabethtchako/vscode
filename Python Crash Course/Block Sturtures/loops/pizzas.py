pizzas = ['veggies']
pizzas.append('buffalo chicken')
pizzas.insert(0,'cheese')

for i in pizzas:
    print(f'I like {i}, pizza')

print("I really like pizza!")

animals =[]
animals.append('dog')
animals.insert(0, 'cat')
animals.insert(1,'parrot')
del animals[-1]

animals.append('monkey')

for i in animals:
    print(f'A {i} would make a great pet!')