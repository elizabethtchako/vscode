bicycles = ["trek", 'cannondale', 'redline', 'specialized']
print(bicycles)

print(bicycles[1])

print(f"{bicycles[0]}, Nice Choice!")
print (f"{bicycles[0].title()}")

del bicycles[0]
print(bicycles)

pop_bike = bicycles.pop()

print(pop_bike)
print(f"The last bike I owned was a {pop_bike.title()}")
print(bicycles)

expensive = 'cannondale'
bicycles.remove(expensive)
print(bicycles[0].title())
print(f"{expensive.title()} was removed because it was expensive")