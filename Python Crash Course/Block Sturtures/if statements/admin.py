usernames = []
usernames_fix = []

usernames.append('Mike')
usernames.insert(3,'georgE')
usernames.append('Elizabeth')
usernames.insert(1,'JOHN')
usernames.insert(0,'MileY')

for name in usernames: 
    usernames_fix.append(name.lower()) #ensuring all usernames are lower case 

print(usernames)
print(usernames_fix, end='\n\n')

usernames = usernames_fix[:] #copying a list 
usernames.sort() #alphabetical order
print(usernames)

usernames.insert(0,'admin')
print(usernames)

usernames.clear()

if usernames: 
    for name in usernames: 
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?", end='\n\n')
        else: 
            print(f"Hello {name.title()}, thank you for logging in again.", end='\n\n')

else: 
    print("We need some users!")

currentusers = usernames_fix [:]
new_users = ['Elizabeth', 'george', 'johnny', 'micheal', 'brianna']

print(currentusers)
print(new_users)


for name in new_users: 
    if name.lower() in currentusers:
        print(f'"{name.lower()}", is not valid enter a new username') 
    else: 
       print(f'"{name.lower()}" valid!')