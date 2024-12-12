numbers =['3','5']
x,y,z = '6','7','8'
numbers.append('1')
numbers.insert(1,'2')
numbers.append('4')
numbers.append(x)
numbers.append(y)
numbers.insert(0,z)

print(numbers)
for num in numbers:
    print(num)

numbers.sort()

print(numbers)
for num in numbers:
    print(num)


print('\n')
magicians=[]
magicians.append('carolina')
magicians.insert(0,'alice')
magicians.append('david')


for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I am looking forward to your next trick, {magician.title()}. \n")

print(f"Thank you, everyone. That was a great magic show!")
#Good way to summarize texts 
print(magician)
#the last magician is stored in that variable and can be used again
# 
#nums = list(range(1))
nums = range(0,11)

#showing the multiple way tou can work with loops outside of the formal way 
numbers = [value for value in range(11)]
print(numbers)
numbers1 = [value**3 for value in list(nums)]
numbers2 = [value**2 for value in list(range(1,10))]

#the mixed list

names = []
names.insert(0,'elizabeth')
names.append('lizzie')
names.append('liz')

double_list = [number+2 for number in numbers ]+[f"Hi my name is: {name}" for name in names]
print(double_list)

print(f"Here are the cubed numbers: {numbers}")
print(f"Here are the squared numbers: {numbers2}")
