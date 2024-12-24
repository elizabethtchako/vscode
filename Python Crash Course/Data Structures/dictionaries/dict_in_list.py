#3ways to create a list 

#empty list
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

#multiple lined
alien_1 = {
    'color':'yellow',
    'points': 15,
    }

#default list 
alien_2 = {'color':'red', 'points': 10}

#DICTIONARY IN A LIST 
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


alienss = []

for alien in range(30):
    new_alien = {'color':'purple','speed':'fast'}
    alienss.append(new_alien)

for i in alienss[:3]: 
    i['color'] = 'yellow'
    i['speed'] = 'medium'
    print(i)

for i in alienss:
    if i['color'] == 'purple':
        i['color'] = 'red'
        i['points'] = 15

    elif i['color'] == 'yellow':
        i['points'] = 10
    
print()
for i in alienss:
    print(i)


print(f'The total length of the aliens in {len(alienss)}')





