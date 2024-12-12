cars = []
cars.append('bmw')
cars.append('audi')
cars.insert(1,'chevy')
cars.insert(-1,'toyota')

for car in cars:

    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())




