people = {
    'mike':{
        'first':'michael',
        'last':'jordan',
        'age':'42',
        'city':'chicago',
    },
    'mary':{
        'first':'mary-ann',
        'last':'jones',
        'age':'18',
        'city':'miami',
    }

}

people['eliza'] = {
        'first':'elizabeth',
        'last':'taylor',
        'age':'30',
        'city':'boston',
}


people['joe'] = {
    'first':'joseph',
    'last':'brown',
    'age':'22',
    'city':'brooklyn',
    }

for person,user_info in sorted(people.items()):
    print(f"\nWelcome: {person.title()}")
    for subject, info in user_info.items():
        print(f"\t{subject.title()}: {info.title()}")
