def life(age):
    if age < 2:
        print(f"At {age} years old, you are a baby")
    
    elif age < 4:
        print(f"At {age} years old, you are a toddler")
    
    elif age < 13:
        print(f"At {age} years old, you are a kid")

    elif age < 20:
        print(f"At {age} years old, you are a teenager")

    elif age < 65:
        print(f"At {age} years old, you are an adult")

    elif age >= 65:
        print(f"At {age} years old, you are an elder")
    
    else: 
        print(f"{age}, not valid.")
    

life(2)
life(4)
life(13)
life(20)
life(65)