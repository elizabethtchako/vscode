car = 'subaru'
print(car)
print(f"car == 'Subaru'? I predict False.")
print(car == 'Subaru', end='\n\n')

car = 'subaru'
print(car)
print(f"car != 'Subaru'? I predict True.")
print(car != 'Subaru', end='\n\n')

car = 'bmw'
print(car)
print(f"car.upper() == 'BMW'? I predict True")
print(car.upper() == 'BMW', end='\n\n')

car = 'toyota'
print(car)
print(f"car.title() == 'Toyota'? I predict True")
print(car.title() == 'Toyota', end='\n\n')

car = 'Honda'
print(car)
print(f"car.lower() == 'Honda'? I predict False")
print(car.lower() == 'Honda', end='\n\n')

car = 'Honda'
print(car)
print(f"car.lower() == 'honda'? I predict True")
print(car.lower() == 'honda', end='\n\n')


age = 1
print(age)
print (f'age > 5 or age == 1? I predict True')
print(age>5 or age==1, end='\n\n')

age = 10
print(age)
print (f'age < 20 or age == 15? I predict False')
print(age>20 and age==15, end='\n\n')

age = 10
print(age)
print (f'age < 20 and age >=10 ? I predict True')
print(age<20 and age>=10, end='\n\n')

age = 10
print(age)
print (f'age < 20 and age >10 ? I predict False')
print(age<20 and age>10, end='\n\n')


tasks = ['cook','clean','exercise']
print(tasks)
print (f"'sleep' in tasks? I predict False'")
print('sleep' in tasks, end='\n\n')

print(tasks)
print (f"'clean' in tasks? I predict True")
print('clean' in tasks, end='\n\n')

print(tasks)
print (f"'cook' not in tasks? I predict False'")
print('cook' not in tasks, end='\n\n')

print(tasks)
print (f"'eat' not in tasks? I predict True'")
print('eat' not in tasks, end='\n\n')