#Elizabeth Tchako
#7/04/2024
# Laarn about Integers, Floats, What's a Multiple Assignment? and What are Constants? 

#for addition 
print(2+3)# = 5

#for subtraction
print(3-2)# = 1

#for multiplying 
print(2*3)# = 6

#for division
print (3/2)# =1.5

#for exponents
print(3**2)# = 6
print(3**3)# = 27
print(10**6)# = 1000000

#python support PEMDAS
print(2+3*4)# = 14 Math: 3*4 =12 +2 =14
print((2+3)*4)# = 20 Math 2+3 =5 *4 =20

#any number with a decimal point is a float 
print(0.1+0.1)
print(0.2+0.2)
#float over power what happens to the result of a combination of numbers 
print(2*0.1)
print(2*0.2)

#python wants to represent the number as precise as possible so maybe you will get an arbitrary number 
print(0.2+0.1) # = .30000000000000004

#when you diide any two number even if they are integers the result will send a float 
print(4/2) # = 2.0
print(2*3.0)# = 6.0
print(3.0**2)# = 9.0

#when writing long numbers you can group digits 
print(14_000_000_000) # 10_00 and 1_000 are both 1000

#multiple assignment 
x,y,z = "hio", 0, 0 # checking to see if you can mix differnt data types
print(x,y,z) #it will keep the alst value that is stored within the variable
x,y,x = "hio", 0, 0 
print(x,y,x) #it will keep the alst value that is stored within the variable 
#use all caps to label something as constant 
HELLO = 0
print(HELLO)

print(2+6)
print(10-2)
print(2*4)
print(16/2)

fav_num = 72
print(f'My favorite number is {fav_num}')