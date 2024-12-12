cars = []
cars.append('bmw')
cars.insert(0,'audi')
cars.append('subaru')
cars.insert(1,'toyota')

print(cars)

cars.sort()

print(cars)

cars.sort(reverse=True)
print(cars)

print(sorted(cars, reverse=True))

print(len(cars))
