favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'rust',
    'phil':'python',
    }

print(favorite_languages)

voters = ['sarah','edward','joe','mike']

for name in voters: 
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll {name.title()}!")
    else: 
        print(f"Please take the poll {name.title()}")

language = favorite_languages['sarah']
print(f"Sarah's favorite lanuage is {language.title()}")