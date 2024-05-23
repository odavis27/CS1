# Oliver Davis
# 3/29/2024
# Description:
#   more of a joke project than anything else, this is a little thing that will randomly generate an idea for you to create,
#   then it will add some modifiers to make it more interesting.
# Bugs:
#   - The only real bug I am aware of is if you were to input: "1please" it would not count it as there is no space
#
#   - the other thing was while creating it, I was running into issues with the main for loop in the FINAL OUTPUT LOGIC section
#   with it believing the user input was a string despite me using an int() function a few lines above it. I put a quick
#   patch on it by using a second int() function in the loop
# Challenges: (note, I am not aware of what is considered a challenging but I will just say some stuff I had some fun doing)
#   - three lines on the vertical axis rather than two
#   - usage of dictionarys
#   - difficulty reader and averaging it out
#   - covering the user from putting in wrong inputs
#   - making the user say please
#   - the usage of list comprehension
# Instructions:
#   Run the file and input a number of inventions you want. Just make sure to be kind :)

#===================
#   SCRIPT SETUP
#===================
import random #import librarys

# sets up the ideas into a parralel array of dictionarys with each "invention modifier" being the value with its difficulty to make as the key
invention = {7:'A Plane ',2:'A Car ',5:'Roller Skates ',1:'A zipline ',6:'A Rocket ',3:'An unintentional submarine ',4:'An intentional submarine '} # the "base"
what_made_of = {3:'Made of Wood ',2:'Made of Duct Tape ',5:'Made Mostly of hot glue ',1:'Made of LEGOs ',6:'Made of Garbage and Recycling ',4:'Made of Cylinders ',7:'Made of Stuff You Find Outside '} # how the invention is made
modifier = {6:'Powered by the Wind.',3:'Powered by Water.',1:'That is Partially Edible.',7:'With Rockets Attached to it.',2:'Covered in Hot Glue.',5:'That is Very Dangerous.',4:'That Attacks My Brother.'} # a modifier to the invention to make it more interesting

#==========================
#   USER INPUT SEQUENCE
#==========================
while True: # a while true loop to run until user inputs a legal response, in which case it will break the loop
    user_input = input('How many terrible inventions would you like? ').lower() # prompts the user for an input while also removing uppercase characters and replacing them with lowercase ones to remove possible errors
    if user_input.endswith(' please'): # checks if the user's message ends with please (includes a space so that later it can remove possible cases where the space is left in with the number and it cannot be turned into an integer)
        user_input = user_input.removesuffix(' please') # removes the ' please' from the end of the string to leave just the numbers so it cant properly be turned into an integer
        try: #try to run the code, expecting a specific error
            int(user_input) # turn the user's input into an iteger
            print('=============================================================') # just print a line to make the final output of the script look nicer
            break # end the while loop, 
        except ValueError: print('Hey, thats not a number!') #if the expected error (in this case it is ValueError meaning the string could not be turned into an integer) does occur, tell the user that they did not imput a number
    else: # if the users input did not include please in it
        print('''What's the magic word? ''') # tripple quotes were used here as I wanted the proper punctuation in What's and the quotation mark would have ended the string if I did not use tripple quotes

#=========================
#   FINAL OUTPUT LOGIC
#=========================
for i in range(int(user_input)): # uses the range class to return a list with the length of the user input to make the for loop repeat the user's desired ammount of times
    random_items = [random.randint(1,7) for i in range(0,3)] # uses List Comprehension, iterates three times, each time picking a random number 1-7 (including end points) and adding it to a list (these numbers will be used as the keys to accese the values in the dictionarys as well as the difficulties)
    print(invention[random_items[0]]+what_made_of[random_items[1]]+modifier[random_items[2]]) # accesses the values (the invention modifiers) from all three dictionary's using their coresponding difficulty in the previously created list
    print(f'''Oliver's Difficulty-To-Build-O-Meter Score:  {round((sum(random_items)/21)*100)}%''') # uses something called f-strings to make it look better; adds together all items in the difficulties list and averages them into a percentage then rounds to remove decimals
    print('-------------------------------------------------------------') # just print a line to make the final output of the script look nicer