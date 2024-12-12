party_name = input(f"What is your parties name? ")
guests = []
guest1 = input('What is the name of your first guest? ')
guest2 = input(f'What is the name of your second guest for your {party_name} Party? ')
guest3 = input(f"Complete your list by adding the last guest - ")

guests.insert(0,guest1)
guests.append(guest2)
guests.insert(2,guest3)

print(f"Would you like to come to dinner {guests[0].title()}?")
print(f"Would you like to come to dinner {guests[2].title()}?")
print(f"Would you like to come to dinner {guests[1].title()}?")

print(f"{guests[-1].upper()}, can't make it to dinner :(")
#guests[-1] = 'Sahyra'.upper()

print(f"Would you like to come to dinner {guests[0].title()}?")
print(f"Would you like to come to dinner {guests[2].title()}?")
print(f"Would you like to come to dinner {guests[1].title()}?\n")

guests.insert(0,"Mary")
guests.append("George")
guests.insert(2,"Stef")

print(f"Would you like to come to dinner {guests[0].title()}?")
print(f"Would you like to come to dinner {guests[1].title()}?")
print(f"Would you like to come to dinner {guests[2].title()}?")
print(f"Would you like to come to dinner {guests[3].title()}?")
print(f"Would you like to come to dinner {guests[4].title()}?")
print(f"Would you like to come to dinner {guests[5].title()}?")

print("\n Sorry everyone I can only bring two people like the orginal plan :(")
pop =[]
pop.append(guests.pop())
pop.append(guests.pop())
pop.append(guests.pop())
pop.append(guests.pop())
print(pop)


print(guests[0].upper())
print(guests[1].upper())

print(len(guests))

del guests[0]
del guests[0]
print(guests)



