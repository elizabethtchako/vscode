pizza = {
    'crust': 'thick',
    'toppings': ['cheese','chicken']
}

print(f"You order a {pizza['crust']} crust pizza" 
    " with these toppings:")
for i in pizza['toppings']:
    print(i.title())



fav_lang = {
    'jen':['python','rust'],
    'phil':['c'],
    'edward':['rust','go'],
    'sarah':['python','haskell'],
}

fav_lang['elizabeth'] = ['python','java']

print()

for name, language in fav_lang.items():
    if len(language)<2:
        print(f"\n{name.title()}'s favorite language is", end =' ')

    else:
        print(f"\n{name.title()}'s favorite languages are:")
    
    for lang in language: 
        print(lang.title())


for name, language in fav_lang.items():
    print(f"{name.title()} has a favorite language")
    
    #for lang in language: 
       # print(lang.title())