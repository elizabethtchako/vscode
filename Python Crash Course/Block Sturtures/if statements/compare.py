car = 'bmw'
car == 'bmw'
#True

car = 'bmw'
car == 'BMW'
#False

car = 'Audi'
car.lower() == 'audi'
#True
print(car) # still Audi


requested_top = 'mushrooms'

if requested_top != 'anchovies':
    print(f'Hold the anchovies! They want {requested_top}.')

age = 19
age < 21
#True

age <= 21
#True

age > 21
#False

age >= 21
#False

age1 =12
age2 = 10


age1 >= 10 and age2>=10 #both for same or it could be different comparisons 
#True

(age1>=10) and (age2>=10)#improve readibility 


age1 >= 10 or age2>=10