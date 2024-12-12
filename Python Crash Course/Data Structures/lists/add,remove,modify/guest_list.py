#Elizabeth Tchako
#07/05/24
#project from book to reivew modifying, adding and removing from lists 

guests = ['George', 'Jessica']
guests.append('Adam')
guests.insert(1,'Ethan')
print(guests)

print(f"Hi, {guests[0]}, you're invivted to my party")
print(f"Hi, {guests[1]}, you're invivted to my party")
print(f"Hi, {guests[2]}, you're invivted to my party")
print(f"Hi, {guests[3]}, you're invivted to my party")

print (f"\n{guests[0]}, can't make it")
uninvited = guests.pop(0)
guests.append("Ella") # edn of the list 

new_guest = guests[-1] # give me the last peron that was added to the list, this is a form of modifying the data to set to a new variable 

print(f"The univited guests is {uninvited.upper()}, the replacement is {new_guest.upper()} ")

print(f"Hi, {guests[0]}, you're invivted to my party")
print(f"Hi, {guests[1]}, you're invivted to my party")
print(f"Hi, {guests[2]}, you're invivted to my party")
print(f"Hi, {guests[3]}, you're invivted to my party")

print(f"Hey {guests}, I found a larger table!")
guests.insert(0,'Bri') # nsert take 2 arguments 
guests.insert(3,'Carrie')
guests.append('Maria') # append goes tot eh end of the list 

print(f"Hi, {guests[0]}, you're invivted to my party")
print(f"Hi, {guests[1]}, you're invivted to my party")
print(f"Hi, {guests[2]}, you're invivted to my party")
print(f"Hi, {guests[3]}, you're invivted to my party")
print(f"Hi, {guests[4]}, you're invivted to my party")
print(f"Hi, {guests[5]}, you're invivted to my party")
print(f"Hi, {guests[6]}, you're invivted to my party")

print(f"\nMy table wont come in time I have to invivte only two people")

#assign pop to a new varaibel to store the value that you have removed from the list 
person1 = guests.pop(4)
person2 = guests.pop(2)

final=[] #creating a new list to add the popped values to 
final.append(person1)
final.append(person2)
print(f"I am inviting, {final[0].upper()} and {final[1].upper()}!")

print(len(final))




