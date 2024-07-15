def game():
    while True:
        scrolls = 0
        mario_alive = True
        start()
        scrolls, mario_alive = level1(scrolls, mario_alive)
        if not mario_alive:
            continue
        scrolls, mario_alive = level2(scrolls, mario_alive)
        if not mario_alive:
            continue
        scrolls, mario_alive = level3(scrolls, mario_alive)
        if not mario_alive:
            continue
        if not end(scrolls):
            break
    print("Thanks for playing Mario's adventure!")

def start():
    print("\nYOU ARE MARIO STORY 12345")

def level1(scrolls, mario_alive):
    lev1_opt = input("Fork in the Road: Mario stops at a split in the road. He sees three different paths ahead: On the left, a foggy path leads into a dark forest. Strange sounds come from the mist, making Mario wonder what's hiding there. On the right, a bright, sunny path goes over green hills. It looks nice, with pretty flowers and shiny coins, but maybe it's too good to be true? In the middle, an odd path has old stones with weird marks on them. The air feels funny here, like there might be magic around. Each path looks interesting but could be dangerous too. Which way should Mario go? Into the spooky fog, along the sunny hills, or down the strange middle path?\n1.Take the foggy path into the dark forest\n2.Follow the sunny path over the green hills\n3.Choose the middle path with the strange stones\n")

    if lev1_opt == "1":
        print("Mario walks into the thick fog. He can't see where he's going and suddenly falls into a deep pit. Game Over!")
        print("***GAME OVER***")
        return scrolls, False
    elif lev1_opt == "2":
        print("Mario happily walks on the sunny path. He finds some helpful power-ups along the way and safely makes it to the next part of his journey. Mario continues his adventure!")
        return scrolls, True
    elif lev1_opt == "3":
        print("As Mario walks past the old stones, he notices something tucked behind one of them. It's an ancient scroll! Mario carefully takes the scroll and reads it, learning some useful info. Then he moves on to the next part of his quest.")
        return scrolls + 1, True
    else:
        print("Invalid choice. Game Over.")
        return scrolls, False

def level2(scrolls, mario_alive):
    lev2intro = "\nMario has now reached the mysterious cave,\nthere is a large pit to his left with a  \ntunnel  to safety on the other side, Mario \nenters the MYSTERIOUS CAVE TO HIS his left \nthere is a pit, beyond that an exit to the \ndark forest. straight ahead he is faced is \nwith THE MIGHTY BOWSER. standing in front \nof a CHEST OF TREASURE and beyond that a tunnel \nthrough the mountain to the leading to the \nCASTLE.BOWSER turns and looks at MARIO \nhead down snorting swiping his left foot behind \nhim suddenly BOWSER charges at Mario like a raging bull \n \nWHAT DOES MARIO DO NEXT?\nANSWER 1,2 OR 3 "
    
    print(lev2intro)
    lev2_opt = input("\n***1.JUMP OVER THE PIT TO SAFETY*** \n\n***2.USE HIS MUSHROOM POWER TO CHARGE BACK AT BOWSER***\n\n***3.JUMP ON BOWSERS HEAD***\n")
    if lev2_opt == "1":
        print("MARIO makes it to the other side of the pit \nand then runs out into the dark forest \nthere he meets GLENDA the large forest spider, \nwho informs MARIO he will make a delicious meal \nfor her children.\n \n****GAME OVER****")
        return scrolls, False
    elif lev2_opt == "2":
        print("MARIO Charges back at bowser flashing every colour of the spectrum \ngetting faster with every step, Bowser continues to charge back at him, \nthe two clash with an almighty flash and a bang. Bowser is flung in to the \nair and comes back down with a bang, confused and wondering what hit him, \nhe gets up and runs out of the cave for safety. Mario opens the chest and \nfinds a Magic scroll. he then continues on looking for the magic castle\n ----MAGIC SCROLL FOUND----\n ")
        return scrolls + 1, True
    elif lev2_opt == "3":
        print("MARIO charges back at bowser the two of them staring each \nother down as they get closer and closer to each other. \nAs they near a few feet from one another MARIO jumps \nlanding perfectly on BOWSERS head and continues running \ndown the cave for safety bowser turns ad gives chase but is \ndazed and gives up.\n \n----MARIO CONTINUES HIS JOURNY---- ")
        return scrolls, True
    else:
        print("Invalid input. Game over.")
        return scrolls, False

def level3(scrolls, mario_alive):
    print("\nCHOICE3 castle in the distance ")
    lev3_opt = input("\n1. Challenge bowser\n2. Go to next level\n3. Enter the castle\n")
    if lev3_opt == "1":
        print("Mario fails to complete his quest ")
        print("***GAME OVER***")
        return scrolls, False
    elif lev3_opt == "2":
        print("Story: Found hidden scroll ")
        return scrolls + 1, True
    elif lev3_opt == "3":
        print("WIN: Mario successfully enters the castle")
        return scrolls, True
    else:
        print("Invalid input. Game over.")
        return scrolls, False

def end(scrolls):
    print(f"Congratulations! You've completed Mario's adventure with {scrolls} scroll(s)!")
    if scrolls == 3:
        print("SECRET ENDING: You've collected all three scrolls and unlocked the secret ending!")
    elif scrolls > 0:
        print(f"You found {scrolls} scroll(s). Try to find all 3 for a secret ending!")
    else:
        print("You didn't find any scrolls this time. There are 3 hidden in the game. Can you find them all?")
    
    play_again = input("Do you want to play again? (Y/N): ")
    return play_again.upper() == "Y"

# Run the game
game()