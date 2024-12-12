#Elizabeth Tchako
#07/02/2024
#Manipulate strings by stripping white space, title, captialized or lowercases string, more on formating strings 
#Learn about tab and new line 

print ("\tHi")
print("Languages:\nPython\nC\nJavaScript") # new line
print("Languages:\n\tPython\n\tC\n\tJavaScript") # tab the line 

#stripping white space from the right side 

fun = "python "
print(fun.rstrip()+"program") #checking if white space is still present 
print(f"{fun}program") #testing the format fucntion | print = python program 

#Question: can you print with the method and format
print(f"{fun.rstrip()}program") #print = pythonprogram

#it will sitll look the same unless you can strip it does not change the variable
print(f'{fun}program') #print = python program

#to remove permanetly yoy have to associate the stripped value with the varibale name
fun = fun.rstrip()
print(f"{fun}program") #print = pythonprogram


favorite_language = ' python '
print(f'\n\n\nthe{favorite_language}program')
favorite_language = favorite_language.rstrip() #remove the right side white space permanetly 
favorite_language = favorite_language.lstrip() #remove the left side white space permanetly 

once = ' python '
print(f'\n\n\nthe{once}program') # print = the python program
once = once.title() # practicing the title method
once = once.strip() # instead of two line that remove both sides it removes them at the same time 
print("the"+ once + "program") # print = thePythonprogram

name = '\n\thi\thow are you'
print(name)
name = name.strip()
print(name)
