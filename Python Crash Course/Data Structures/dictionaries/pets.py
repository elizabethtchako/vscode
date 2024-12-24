pet1 = {'animal':'dog', 'owner': 'joe'}
pet2 = {'animal':'cat', 'owner': 'brian'}
pet3 = {'animal':'fish', 'owner': 'becky'}
pet4 = {'animal':'ferret', 'owner': 'gabe'}
pet5 = {'animal':'snake', 'owner': 'sarah'}
pet6 = {'animal':'turtle', 'owner': 'maria'}
pet7 = {'animal':'hamster', 'owner': 'stephen'}

pets = [pet1, pet2, pet3, pet4, pet5, pet6, pet7]

for pet in pets:
    print(f"\nPet:{pet['animal'].title()}\nOwner:{pet['owner'].title()}")
