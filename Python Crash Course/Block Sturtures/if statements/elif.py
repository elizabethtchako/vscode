age = 12
if age < 4:
    print(f"Because your age is {age}, your admission cost is $0" )
elif age < 18: 
    print(f" Because your age is {age}, your admission cost is $25")
else: 
    print(f"Because your age is {age}, your admission cost is $40")

#MORE CONCISE WAY 

age = 17 

if age <4:
    price = 0
elif age < 18:
    price = 25
elif age <65: #showing you can have more elif statements
    price = 40
else:
    price = 20

print(f"Because you are {age}, your admission cost is ${price}")
#more efficent becuase I would only need to change one print statment


#testing multiple condition (no if-elif-else chain)

requested_top = []
requested_top.append('cheese')
requested_top.insert(1,'chicken')
requested_top.append('veggies')
requested_top.insert(100, 'mushrooms')
print(requested_top)

del requested_top[-1]
requested_top.remove('veggies')
print(requested_top)

if 'mushrooms' in requested_top:
    print('Adding mushrooms!')

if 'veggies' in requested_top:
    print("Adding veggies")

if 'cheese' in requested_top:
    print("Adding cheese")

