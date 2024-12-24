cities = {
    'chicago':{
        'country':'usa',
        'population': 2746388,
        'fact':"World's oldest surviving skyscrapper",
        },

    'nyc':{
        'country':'usa',
        'population':8258035 ,
        'fact':"The city's nickname, 'The Big Apple'"
        },

    'boston':{
        'country':'usa',
        'population':653833,
        'fact':'First public park',
        },

    }

for city,v in cities.items():
    if city == 'nyc':
        print(f"\nCity: {city.upper()}")
    else: 
        print(f"\nCity: {city.title()}")

    for subject,value in v.items():
        if value == 'usa':
            value = 'USA'

        if subject == ['fact']:
            print(f"\t{subject.title()}: {value}")
        elif subject == str:
            print(f"\t{subject.title()}: {value.title()}")
        else:
            print(f"\t{subject.title()}: {value}")