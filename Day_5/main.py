name = input("Enter your name: ")

print(f"You are Welcome {name} to this adventure!")

answer = input("You are on a dirt road,it has come to an end and you can go left or right.\nwhich way you wanna go?  ").lower()

if answer == "left":
    answer = input("You come to a river.You can walk around it or you can swim accross.\nType 'walk' to walk and type 'swim' to swim").lower()
    if answer == "swim":
        print("You swan accorss and were eaten by alligator.You lost the game.")
    elif answer == "walk":
        print("You walk for many miles,ran out of water and lost the game.")
    else:
        print("Invalid option.You loss!")     
           
elif answer == "right":
    answer = input("You come to a bridge.It looks mysterious.Do You to want to cross it,or head back ? \nType 'cross' to cross and type 'back' to head back. ").lower()
    if answer == "back":
        print("You go back and lose! ")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger.Do you want to talk them (yes/no) ?").lower()
        if answer == "yes":
            print("Stranger was a seriall killer and you are dead.")
        elif answer == "no":
            print("You are save now.Stranger was a serial killer.You won!.")    
    else:
        print("Invalid option.You loss!")     
else:
    print("Not a valid option! ")        