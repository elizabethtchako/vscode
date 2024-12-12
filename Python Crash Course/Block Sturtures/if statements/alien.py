def alien(alien_color):
    points = 0
    if alien_color.lower() == 'green':
        points +=5
        print(f"You now have {points} points!")
    
    elif alien_color.lower() == 'yellow':
        points +=10
        print(f"You now have {points} points!")

    elif alien_color.lower() == 'red':
        points +=15
        print(f"You now have {points} points!")

    else: 
        print(f"You still have {points} points.")

alien('Green')
alien('yellow')
alien('RED')
alien('pink')
