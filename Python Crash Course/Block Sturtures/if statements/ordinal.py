ordinal = list(range(1,10))

for num in ordinal:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    else: 
        print(f"{num}th")