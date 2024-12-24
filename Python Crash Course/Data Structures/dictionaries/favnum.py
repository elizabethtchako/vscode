fav_num = {
    'rina' : [5],
    'elizabeth' : [72,13],
    'stevie' : [3],
    'joey' : [52],
}

print(fav_num)

for user, numbers in fav_num.items():
    if len(numbers) == 1:
        print(f"\n{user.title()}'s favorite number is:")
    else: 
        print(f"\n{user.title()}'s favorite numbers are:")
        
    num_len = len(numbers)

    for num in numbers:
        if num_len == 1:
            print(f"{num}")
        else: 
            print(f"{num}")
