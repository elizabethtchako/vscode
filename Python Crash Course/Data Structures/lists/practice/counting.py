#Elizabeth Tchako
#07/10/24
# practice what you learned using numbers and ranges with lists 

twenty = [value for value in range(1,21)]

print(twenty)

million = [value for value in range(1,1_000_001)]
#print(million)

print(min(million))
print(max(million))
print(sum(million))


odd_num = [value for value in range(1,20,2)]
print(odd_num)

threes = [value for value in range(3,30)]
mod=[]
for i in threes:
    if i%3==0:
        mod.append(i)
print(mod)

three = [value**3 for value in range(3,30)]
print(three)


cubed =[]
for i in range(1,11):
    cubed.append(i**3)
print(cubed)


cubes = [value**3 for value in range(1,11)]
print(cubes)
