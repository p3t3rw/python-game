import os

def game():
    while True:
        scrolls = 0
        mario_alive = True
        os.system('cls')
        start()
        scrolls, mario_alive = level1(scrolls)
        os.system('cls')
        if not mario_alive:
            continue
        scrolls, mario_alive = level2(scrolls)
        os.system('cls')
        if not mario_alive:
            continue
        scrolls, mario_alive = level3(scrolls)
        os.system('cls')
        if not mario_alive:
            continue
        if not end(scrolls):
            break
    print("Thanks for playing Mario's adventure!")

def start():
    print("MARIO'S MAGIC ADVENTURE")

def level1(scrolls):
    while True:
        lev1_opt = input("\nFork in the Road: Mario stops at a split in the road. He sees three different paths ahead: On the left, a foggy path leads into a dark forest. Strange sounds come from the mist, making Mario wonder what's hiding there. On the right, a bright, sunny path goes over green hills. It looks nice, with pretty flowers and shiny coins, but maybe it's too good to be true? In the middle, an odd path has old stones with weird marks on them. The air feels funny here, like there might be magic around. Each path looks interesting but could be dangerous too. Which way should Mario go? Into the spooky fog, along the sunny hills, or down the strange middle path?\n \nWHAT DOES MARIO DO NEXT?\n\n1. TAKE THE FOGGY PATH INTO THE DARK FOREST\n2. FOLLOW THE SUNNY PATH OVER THE GREEN HILLS\n3. CHOOSE THE MIDDLE PATH WITH THE STRANGE STONES\n")

        
        if lev1_opt == "1":
            print("Mario walks into the thick fog. He can't see where he's going and suddenly falls into a deep pit. Game Over!")
            print("***GAME OVER***")
            input("Press Enter to continue...")
            return scrolls, False
        elif lev1_opt == "2":
            print("Mario happily walks on the sunny path. He finds some helpful power-ups along the way and safely makes it to the next part of his journey. Mario continues his adventure!")
            input("Press Enter to continue...")
            return scrolls, True
        elif lev1_opt == "3":
            print("As Mario walks past the old stones, he notices something tucked behind one of them. It's an ancient scroll! Mario carefully takes the scroll and reads it, learning some useful info. Then he moves on to the next part of his quest.\n ----MAGIC SCROLL FOUND----\n")
            input("Press Enter to continue...")
            return scrolls + 1, True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")
            os.system('cls')


def level2(scrolls):
    while True:
        lev2_opt = input("\nMario has now reached the mysterious cave,\nthere is a large pit to his left with a  \ntunnel to safety on the other side. Mario \nenters the MYSTERIOUS CAVE. To his left \nthere is a pit, beyond that an exit to the \ndark forest. Straight ahead he is faced \nwith THE MIGHTY BOWSER, standing in front\nof a CHEST OF TREASURE and beyond that a tunnel \nthrough the mountain leading to the \nCASTLE. BOWSER turns and looks at MARIO, \nhead down, snorting, swiping his left foot behind \nhim. Suddenly BOWSER charges at Mario like a raging bull.\n\nWHAT DOES MARIO DO NEXT?\n\n1. JUMP OVER THE PIT TO SAFETY\n2. USE HIS MUSHROOM POWER TO CHARGE BACK AT BOWSER\n3. JUMP ON BOWSER'S HEAD\n")
        
        if lev2_opt == "1":
            print("MARIO makes it to the other side of the pit \nand then runs out into the dark forest \nthere he meets GLENDA the large forest spider, \nwho informs MARIO he will make a delicious meal \nfor her children.\n \n****GAME OVER****")
            input("Press Enter to continue...")
            return scrolls, False
        elif lev2_opt == "2":
            print("MARIO Charges back at bowser flashing every colour of the spectrum \ngetting faster with every step, Bowser continues to charge back at him, \nthe two clash with an almighty flash and a bang. Bowser is flung in to the \nair and comes back down with a bang, confused and wondering what hit him, \nhe gets up and runs out of the cave for safety. Mario opens the chest and \nfinds a Magic scroll. he then continues on looking for the magic castle\n ----MAGIC SCROLL FOUND----\n ")
            input("Press Enter to continue...")
            return scrolls + 1, True
        elif lev2_opt == "3":
            print("MARIO charges back at bowser the two of them staring each \nother down as they get closer and closer to each other. \nAs they near a few feet from one another MARIO jumps \nlanding perfectly on BOWSERS head and continues running \ndown the cave for safety bowser turns ad gives chase but is \ndazed and gives up.")
            input("Press Enter to continue...")
            return scrolls, True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")
            os.system('cls')

def level3(scrolls):
    while True:
        lev3_opt = input("\nMario sees a grand castle in the distance. Its tall towers reach into the clouds. He knows his adventure is nearing its end, but this last challenge looks tough. Mario has three ways to approach the castle:\n\nWHAT DOES MARIO DO NEXT?\n \n1. AVOID THE CASTLE\n2. APPOROCH THE CASTLE DIRECTLY \n3. ACT CAUTIOUSLY AND TRY TO FIND A DIFFERT WAY IN\n")
        
        if lev3_opt == "1":
            print("Mario decides to avoid the castle and look for another route. Unfortunately, this decision leads him away from his goal, and he fails to complete his quest.")
            print("***GAME OVER***")
            input("Press Enter to continue...")
            return scrolls, False
        elif lev3_opt == "2":
            print("Mario bravely walks up to the main gate and confronts Bowser directly. After a tough battle, Mario defeats Bowser and wins the game. Mario has successfully completed his quest!")
            input("Press Enter to continue...")
            return scrolls, True
        elif lev3_opt == "3":
            print("Mario carefully searches the castle's surroundings. His caution pays off! He discovers a hidden scroll tucked away in a secret alcove. The scroll contains valuable information about the castle's layout. Using this knowledge, Mario finds a secret entrance, confronts Bowser, and defeats him. Mario wins the game and completes his quest with the added bonus of finding the hidden scroll!\n ----MAGIC SCROLL FOUND----\n")
            input("Press Enter to continue...")
            return scrolls + 1, True
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            input("Press Enter to continue...")
            os.system('cls')

def end(scrolls):
    print(f"\nCongratulations! You've completed Mario's adventure with {scrolls} scroll(s)!")
    if scrolls == 3:
        print("Wow! Not only did you win, but you also found the secret scroll!\nYou're like the Indiana Jones of the Mushroom Kingdom. So fancy!\nMario's now equipped with knowledge beyond measure... not that he'll use it\nThe Princess is extra grateful this time, and so are we. For real\nEnjoy your scroll and your bragging rights. You're a true hero... until next time!\nThanks for playing! You've set a new bar... but don't get cocky.")
    elif scrolls > 0:
        print(f"You found {scrolls} scroll(s). Try to find all 3 for a secret ending!")
    else:
        print("You didn't find any scrolls this time. There are 3 hidden in the game. Can you find them all?")
    
    while True:
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again == "Y" or play_again == "N":
            return play_again == "Y"
        else:
            print("Invalid input. Please enter Y or N.")

# Run the game
game()