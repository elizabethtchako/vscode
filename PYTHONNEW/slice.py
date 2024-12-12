players = []

players.append('eli')
players.insert(1,'martina')
players.append('florence')
players.append('micheal')
players.insert(0,'charles')

print(players)

print(players[:4])
print(players[1:3])
print(players[1:])
print(players[-3:])

#mena the same thing 
print(players[::2])
print(players[:5:2])
print(players[0::2])

print(f"Here are my first three players:")

for player in players[:3]:
    print(player.title())

