#Elizabeth Tchako
#07/03/2024
#Manipulate strings by stripping white space, title, captialized or lowercases string, more on formating strings 

name = "elizabeth tchako"
print(name.title()) #title refers to a method 
#"." tells python to make an action on that variable

print(name.upper())
print(name.lower())

print (name.title())

first_name = "elizabeth"
last_name = "tchako"

full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#or make the final print call much simpler
message = f"Hello, {full_name.title()}!"
print(message)


first_name = "Lizzie"
last_name = "Tchako"

name = f"First Name: {first_name}\nLast Name: {last_name}"
print(name)

