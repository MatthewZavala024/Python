print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
cave = input("The tunnel slits into 2 different directions. "
             "Which do you pick right or left? ").lower()


if cave == "right":
    lake = (input('A lake has appeared!! Do you wait for a "boat" to go across'
                  ' or try to "swim"?')).lower()
    if lake == "boat":
        three_doors = input('You have reached the other side. '
                            'Three doors appear in front of you'
                            '"Red", "Yellow", and "Blue". Which do you pick?').lower()
        if three_doors == "red":
            print("This door leads to fire. You have been burned alive. Game Over.")
        elif three_doors == "blue":
            print("This door leads to ice monsters. You have been killed. Game Over.")
        elif three_doors == "yellow":
            print("You have found the treasure. You WIN!!!!")
        else:
            print("This door does not exists. You took to long.. "
                  "The kraken came from the lake and took you. Game Over.")

    elif lake == "swim":
        print("Sharks have appeared and eaten you. Game Over.")


else:
    print("You ran into a ogre and have been eaten!! Game Over..")