scrolls=0
restart_game=True
introduction= " \nYOU ARE MARIO STORY"
print(introduction)
lev1_opt=input("Fork in the Road:Mario stops at a split in the road. He sees three different paths ahead: On the left, a foggy path leads into a dark forest. Strange sounds come from the mist, making Mario wonder what's hiding there.On the right, a bright, sunny path goes over green hills. It looks nice, with pretty flowers and shiny coins, but maybe it's too good to be true?In the middle, an odd path has old stones with weird marks on them. The air feels funny here, like there might be magic around.Each path looks interesting but could be dangerous too. Which way should Mario go? Into the spooky fog, along the sunny hills, or down the strange middle path?\n1.Take the foggy path into the dark forest\n2.Follow the sunny path over the green hills\n3.Choose the middle path with the strange stones")

if lev1_opt== "1":
    print ("Mario walks into the thick fog. He can't see where he's going and suddenly falls into a deep pit. Game Over!")
    print("***GAME OVER***")
    quit()

elif lev1_opt== "2":
      scrolls= +1 
      print("Mario happily walks on the sunny path. He finds some helpful power-ups along the way and safely makes it to the next part of his journey. Mario continues his adventure!")

elif lev1_opt== "3":
     
     print( "As Mario walks past the old stones, he notices something tucked behind one of them. It's an ancient scroll! Mario carefully takes the scroll and reads it, learning some useful info. Then he moves on to the next part of his quest.")
      
          

lev2intro= "\nMario has now reached the mysterious cave,\nthere is a large pit to his left with a  \ntunnel  to safety on the other side, Mario \nenters the MYSTERIOUS CAVE TO HIS his left \nthere is a pit, beyond that an exit to the \ndark forest. straight ahead he is faced is \nwith THE MIGHTY BOWSER. standing in front \nof a CHEST OF TREASURE and beyond that a tunnel \nthrough the mountain to the leading to the \nCASTLE.BOWSER turns and looks at MARIO \nhead down snorting swiping his left foot behind \nhim suddenly BOWSER charges at Mario like a raging bull \n \nWHAT DOES MARIO DO NEXT?\nANSWER 1,2 OR 3 "

while restart_game:
    print(lev2intro)

    lev2_opt=input("\n***1.JUMP OVER THE PIT TO SAFETY*** \n\n***2.USE HIS MUSHROOM POWER TO CHARGE BACK AT BOWSER***\n\n***3.JUMP ON BOWSERS HEAD***\n")
    if lev2_opt == "1":
        game_start=input("MARIO makes it to the other side of the of pit \nand the runs out to in to the dark forest \nthere he meets GLENDA the large forest spider, \nwho informs MARIO he will make a delicious meal \nfor her children.\n \n****GAME OVER****\n\n**DO YOU WANT TO TRY AGAIN?** \nY for YES \nN for NO \n")
        if game_start == "Y":
            continue

        else:
            print("**ThANKS FOR PLAYING**")
            restart_game=False
            quit()

        

    elif lev2_opt == "2": 
        print("MARIO Charges back at bowser flashing every colour of the spectrum \ngetting faster with every step, Bowser continues to charge back at him, \nthe two clash with an almighty flash and a bang. Bowser is flung in to the \nair and comes back down with a bang, confused and wondering what hit him, \nhe gets up and runs out of the cave for safety. Mario opens the chest and \nfins a Magic scroll. he then continues on looking for the magic castle\n ----MAGIC SCROLL FOUND----\n ")
        scrolls= +1
        print("**YOU NOW HAVE  " + str(scrolls) + "  MAGIC SCROLL**")
        break      
    elif lev2_opt=="3":
        print( "MARIO charges back at bowser the two of them staring each \nother down as they get closer and closer to each other. \nAs they near a few feet from one another MARIO jumps \nlanding perfectly on BOWSERS head and continues running \ndown the cave for safety bowser turns ad gives chase but is \ndazed and gives up.\n \n----MARIO CONTINUES HIS JOURNY---- ")
        break
    else:
        print("game over")

lev3intro= "\nCHOICE3 castle in the distance "
print(lev3intro)

lev3_opt=input("\nchallenge bowser\n or\ngo to next level")
if "1":
    print ("mario fails to compleate his quest ")
    print("***GAME OVER***")
    quit()

elif lev3_opt== "2":
      scrolls= +1 
      print("Story; Found hidden scroll ")

elif lev3_opt== "3":
     
     print( "WIN:Mario sucessfully enters the castle  ")

if scrolls == 3:
     print("SECRET ENDING: you have found all three scrolls an unlocked ")
else:
     print("goodbye try again statement")
     quit()