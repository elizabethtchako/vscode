favplaces={
    'tia':{
        'places':['new york city','las vegas']
    }, 
    'penny':{
        'places':['georgia','bali','houston']
    },
}

favplaces['george'] = {'places':['jamaica', 'ghana', 'algeria']}

print(favplaces)

for user, user_info in favplaces.items():
    print(f"\nUsers Name: {user.title()}")

    for places,location in user_info.items():
        print(f"{user.title()}'s Favorite {places.title()}:",end =' ')
        len_location = len(location)

        for values in location:
            if len_location == 1: 
                print(f"{values.title()}",end = '\n\n')
            else: 
                print(f"{values.title()}",end = ', ')

            len_location -= 1