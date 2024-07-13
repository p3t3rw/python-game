scrolls=0
restart_game=True
introduction= " \nYOU ARE MARIO STORY"
print(introduction)
lev1_opt=input("CHOICE 1 FORK IN THE ROAD please answer 1,2 or 3")

if lev1_opt== "1":
    print ("Mario fell into a pit ")
    print("***GAME OVER***")
    quit()

elif lev1_opt== "2":
      scrolls= +1 
      print("story: found hidden scroll ")

elif lev1_opt== "3":
     
     print( "WIN Mario continues his journey ")
      
          

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