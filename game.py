scrolls=0
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
      
          

lev2intro= "\nyou have now reched MYSTERIOUS CAVE "
print(lev2intro)

lev2_opt=input("\nchallenge bowser\n or\ngo to next level")
if lev2_opt== "1":
    print ("Mario gets lost in the woods ")
    print("***GAME OVER***")
    quit()

elif lev2_opt== "2": 
      scrolls= +1
      print("STORY: FOUND HIDDEN SCROLL ")

elif lev2_opt== "3":
    
     print( "WIN: mario rests and regains his strength ")

lev3intro= "\nCHOICE3 castle in the distance "
print(lev2intro)

lev3_opt=input("\nchallenge bowser\n or\ngo to next level")
if "1.":
    print ("mario fails to compleate his quest ")
    print("***GAME OVER***")
    quit()

elif lev3_opt== "2":
      scrolls= +1 
      print("Story; Found hidden scroll ")

elif lev3_opt== "2.USE POWER UP":
     
     print( "WIN:Mario sucessfully enters the castle  ")

if scrolls == 3:
     print("SECRET ENDING: you have found all three scrolls an unlocked ")
else:
     print("goodbye try again statement")
     quit()