# Oliver Davis
# 4/15/2024
# Description:
#   A couple of varied functions that serve as a test of function knowledge
# Bugs:
#   I am not aware of any bugs currently
# Challenges:
#   - reverse
#   - tts
#   - initials
#   - is it a palindrome
#
# Instructions:
#   You will need to call these functions before this file does anything.


from os import remove # imports the remove function; this is used to delete files (in this case it is the mp3 file after it is played)
from  random import randint # just import the random integer thingy and leave the stuff I don't need

#   PYGAME SETUP
#--------------------
from pygame import mixer # import neccesary parts from the pygame library while leaving the others (because its a very big library)
mixer.init() # init mixer to allow its parts to be used (used to play sounds)

#   TTS SETUP
#----------------
from gtts import gTTS # import the neccesary parts from gtts (google's text to speach API)
language = 'en' # define the tts's language (it is set to 'en' short for english)



def output(text): # make a small output function so I dont need to give two print thingys
    print(text) # print it in the console
    #say(text) # say the output
    say = str(text) # sets input to a string (no need to have checks for failure because the user doesnt have full control over this function so in my code i wont input stuff that would give a failure)
    tts_output = gTTS(text=say, lang=language, slow=False) # create the audio file (i have no clue how this works, i just give the library what it asks for and I get back a fancy thing)
    
    tts_output.save("speaky.mp3") # save the fancy google magic in an mp3 file
    mixer.music.load('speaky.mp3') # open up the music file in pygame's mixer (it loads it in so it can now be printed)
    mixer.music.play() # play the loaded file
    while mixer.music.get_busy(): # while the file is playing run this loop that does nothing (a python way of doing 'wait unti'])
        pass # just tell the loop to do nothing
    mixer.music.unload() # unload the music
    remove("speaky.mp3") # delete the audio file


# note:
#   i use a function called output rather than printing so I can have it print as well as activate the tts with one function
#=============================
#       Main Assignment
#=============================
def song_chorus(): # define the function (yes, I am aware it sounds terrible but I though it fit)
    output( # seperate the lines used tripple quotes to make the print look better and make it easier to read
'''Daisy, Daisy, give me your answer do
I'm half crazy all for the love of you
It won't be a stylish marriage
I can't afford a carriage
But you'll look sweet upon the seat
Of a bicycle built for two''') # close quotes and output function
def print_list(input_list): # define function
    for word in input_list: output(word) # iterate through the list and print and say each item
def sum(num_1,num_2): output(num_1+num_2) # sets up function then print the sum of the two and says the sum of the two
def check_for_element(element,input_list): return element in input_list #define function  -- also isnt this useless because 'in' is already a thing?
def check_int(input_int): # define function
    try: return(int(input_int) == input_int) # if the thingy turned into an int is identical to it normally, return true, else return false
    except ValueError: return False # if it tries to turn something that cant become an int into an int, return false
def print_random(end_point_1,end_point_2): 
    if check_int(end_point_1) and check_int(end_point_2): output(randint(end_point_1,end_point_2)) # if bpth numbers are 
def swap_letters(controls,text): # 'controls' is intended to be a tuple/list for the string to replace and one that is being replaced.
    text = list(text) # turn the text into a list
    for index in range(len(text)):  # for the length of th text (uses range function to get an index number rather than a character)
        if text[index] == controls[0]: text[index] = controls[1] # if the selected thingy in the text is a equal to the control's first item (the letter to replace), that index becomes the second control, one to replace
    output(''.join(text)) # hi, i am a string method :)
    
#==========================
#       Challenges
#==========================

def reverse(string): return string[::-1] # defines funciton then uses collons (dont know if there is a fancy term for it) to use a -1 step, leaving the start and end vlaues blank (the first two collons), giving the word reversed which is then returned
def palindrome(string): return string == string[::-1] # # defines funciton then uses collons (dont know if there is a fancy term for it) to use a -1 step, leaving the start and end vlaues blank (the first two collons), giving the word reversed, one letter at a time iterating through it. while iterating, it compares to the unreversed version to ensure they are equal. if it succesfully iterates through it with all reversed being the same as normal it returns true
def initials(name): split_name = name.split(' '); output((split_name[0][0]+split_name[1][0]).upper()) # split name by the space to get both names seperatly then get the upper case version of the first letter of both names

#============================
# call variables here (makes it look better)
#============================
