numbers =[]

for value in range(1,21):
    numbers.append(value)

print(numbers)

for value in range(1,21):
    print(value)


millions = list(range(1,1_000_001))

print(min(millions))
print(max(millions))
print(sum(millions))


odd_num= [value for value in range(1,21,2)]
print(odd_num)

multhree = [value*3 for value in range(0,31)]
print(multhree)




#list comprehension 
cubes = [value**3 for value in range(1,11)]
print(cubes)

#using empty list 
cubed = []
for value in range(1,11):
    cubed.append(value**3)
print(cubed)

#using list function
cubese = list(range(1,11))
for value in cubese:
    print(value**3)
