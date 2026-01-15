def run_fight():
    """Gives the user a choice to run away or fight a character"""
    path2 = input("Do you want to fight or run away?")
    if path2 == "fight":
        print("Sorry, you died")
    elif path2 == "run":
        print("You safely got away")

# The user approaches a point where the path breaks off into three paths
print("You see 3 paths ahead of you")
path = input("Which way would you like to go? Left, right, or straight?")
# ogre is on the left path
if path == "left":
    print("You see an ogre")
    run_fight()
# a dragon is on the right path
elif path == "right":
    print("You see a dragon")
    run_fight()
# straight ahead is a well
elif path == "straight":
    print("You see a water well")
# Add a statement if the user choices an invalid option
else:
    print("I didn't understand that")