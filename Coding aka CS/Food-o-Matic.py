import random

options = [ # setup all the options (they are seperated by lines for readability, that isnt neccerary. It is seperated into the three categories it needs)
            [['A Plane ',7],['A Car ',2],['Roller Skates ',5],['A zipline ',1],['A Rocket ',6],['An unintentional submarine ',3],['An intentional submarine ',4]],
            [['Made of Wood ',3],['Made of Duct Tape ',2],['Made Mostly of hot glue ',5],['Made of LEGOs ',1],['Made of Garbage and Recycling ',6],['Made of Cylinders ',4],['Made of Stuff You Find Outside ',7]],
            [['Powered by the Wind.',6],['Powered by Water.',3],['That is Partially Edible.',1],['With Rockets Attached to it.',7],['Covered in Hot Glue.',2],['That is Very Dangerous.',5],['That Attacks My Brother.',4]]]

while True: # Setup to ask until the user puts in an input that succesfully converts into an integer
    try: # attempt to ask and get the input and make it an int, possibly epecting a ValueError
        user_input = int(input('How Many Stupid Invention Ideas do you want? '))
        break
    except ValueError: # if the line two above this doesnt work and returns ValueError (it tried to turn a string into an integer) then print that it isnt a number
        print('Not a number :/')
print('========================================')
for i in range(user_input): # repeat the number of times the user inputed
    choices = [random.choice(i) for i in options] # Using list comprehension, choose a random item from all lists from the array "options" and add it to a list in order
    print(choices[0][0]+choices[1][0]+choices[2][0]) #print out that list in a way that looks better (printing the list in general would work but it wouldn't look very good)
    allcosts = choices[0][1]+choices[1][1]+choices[2][1]
    #print(allcosts)
    print(f"Difficulty (percentage): {str(round((allcosts/21)*100))}%")
    print('-----------------------------------------')