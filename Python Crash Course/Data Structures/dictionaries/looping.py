user_0 = {
    'username':'gliz',
    'First':'elizabeth',
    'Last' : 'tchako',
}

for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print()
favorite_languages = {}
favorite_languages['sarah'] = 'c'
favorite_languages['jen'] = 'python'
favorite_languages['edward'] = 'rust'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(f"{name.title()}'favorite language is {language.title()}")

print()
friends = []
friends.append('sarah')
friends.insert(0,'edward')

for name in sorted(favorite_languages.keys()): # dont need sorted, it is just there to show ohy hhyrganizing a dictionary
    print(f"Hi {name.title()}.")
    language = favorite_languages[name]
    if name in friends: 
        print(f"\t{name.title()}, I see you like {language.title()}")

#keys method is not only for looping, returns a sequence of all the keys 
if 'erin' not in favorite_languages.keys(): 
    print('Erin, please take our poll')

print(sorted(favorite_languages.keys())) # not permenant
print(favorite_languages.keys())

