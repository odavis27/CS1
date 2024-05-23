print ("give me money:(")

import random
import time

computer = random.choice(["heads", "tails"])
guess = input("heads or tails? ")
guess = guess.lower()

if guess == "tails" or guess == "heads":
    print ("Flipping coin!")
    time.sleep(2)
    print(computer)
    if guess == "tails" and computer == "tails":
        print ("You were RIGHT!")
    else:    
        if guess == "heads" and computer == "heads":
            print ("You were RIGHT!")
        else:
            print ("you were WRONG!")

else:
    print("WHY YOU NO PUT REAL ANSWER")

#print (x)
    print ("Flipping coin!")
    time.sleep(2)
    print ("NO IM NOT!!!! YOU TRIED CHEATING  >:( !")

