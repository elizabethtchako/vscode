#Elizabeth Tchako
#07/03/2024
#Manipulate strings by stripping white space, title, captialized or lowercases string, more on formating strings 
#STILL NEED TO IMPROVE THE TIE FOR THIS - improved with 
#try to manipulate these to have hard medium and easy levels 
#easy if CPU won the first time let them have another chance
#hard if player won do it again 

print("Hello World")

import random 
print("\n\n1) ✊\n2) ✋\n3) ✌️")
hand = int(input("\nPick a number: "))
com_hand = random.randint(1,3)


if hand == 1:
    print("\n\nYou chose: ✊")

elif hand == 2:
    print("\n\nYou chose: ✋")

elif hand == 3:
    print("\n\nYou chose: ✌️")

else: 
    print("\nerror with you")
    
if com_hand == 1:
    print("CPU chose: ✊")

elif com_hand == 2:
    print("CPU chose: ✋")

elif com_hand == 3:
    print("CPU chose: ✌️")

else: 
    print("error with CPU")

if com_hand == 1 and hand == 3:
    print("\nYou lost")

elif com_hand == 2 and hand ==1:
    print("\nYou lost") 

elif com_hand == 3 and hand == 2:
    print("\nYou lost")

#account for user error or computer use but make no one wins
elif hand > 3 or com_hand > 3: 
    print("\nNo game if both player did not throw hands :(")

elif hand == com_hand:
    print('\nDraw')

else:
    print("\nYou won!")


