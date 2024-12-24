rivers = {}
rivers['nile'] = 'Egypt'
rivers['mississippi'] = 'USA' 
rivers['amazon'] = 'brazil'
rivers['congo'] = 'angola'
rivers['danube'] = 'germany'


for river, location in rivers.items():
    print(f"The {river.title()} river runs through {location.title()}")

print()

for river, location in rivers.items():
    print(f"\n\nRiver: {river.title()}")
    print(f"Location: {location.title()}")

print()
print()

for river in rivers:
    print(f"River: {river.title()}")
print()

for location in rivers.values():
    print(f"Location: {location.title()}")