users = {
    'mcurrie':{
    'first':'marie',
    'last':'currie',
    'location':'paris',
    }
}

users['aeinstien'] = {
    'first': 'albert',
    'last': 'einstien',
    'location':'princeton'
}



for name, values in users.items():
    print(f"\nUsername: {name}")
    print(f"Welcome {values['first'].title()}!")

    for k,v in users[name].items():
        print(f"\t{k.title()}: {v.title()}")
    







    for username, user_info in users.items():
        print(f"\nUsername: {username}")
        print(f"Full name: {user_info['first'].title()} {user_info['last'].title()}")
        print(f"Location: {user_info['location'].title()}")


