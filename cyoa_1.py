print("You see a path ahead of you")
path = input("Which way would you like to go? Left, right, or straight?")
if path == "left":
    print("You see an ogre")
    path2 = input("Do you want to fight or run away?")
    if path2 == "fight":
        print("Sorry, you died")
    elif path2 == "run":
        print("You safely got away")
elif path == "right":
    print("You see a dragon")
elif path == "straight":
    print("You see a water well")
else:
    print("I didn't understand that")