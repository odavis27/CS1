# Oliver Davis
# 11/14/2023
# Description:
#   A cool little rock paper scissors game with custom images and sound. Animated using PYGAME
# Bugs:
#   there are two bugs that im aware of, neither of which I know how to solve.
#   1. it wont work for you
#       - this was an issue with the file locations but its fixed!
#   2. Closing the program
#       - pygame on certain things you can run coe works differently. basicly all that means is that if you
#         click the X to close the window on one of these programs, it wont shut and the game will freeze
#         (I used Visual Studio and it works well if your wondering)
# Challenges:
#  The visual game
#     - the drawing of the UI and the images for the moves you make
#  The audio - sounds for winng, losing, and for ties
#  score counter + the fact that its visual
#  The visual text printing
#  The visual shaking
#  Main gameplay loop
#
# Instructions:
#   Run, then just do what it says
#===========================================================
#===========================================================

#   make modules exist in me code
import random
import pygame
pygame.init()

#   time data setup
#===================================
clock = pygame.time.Clock()
time = clock.get_time()
clock.tick(40)  # Makes the game run at 40 ticks per second - the main gameplay loop runs 40 times per second at a maximum - can be less

#===================================
# Sounds
#===================================
pygame.mixer.set_num_channels(999)

screen = pygame.display.set_mode((480,340))

screen.fill((255,255,255))
pygame.display.set_caption('rock, paper, siccsor, say, YES')
pygame.display.update()
#===================================
#===================================


#===================================
# Image Data
#===================================
#--img--
paper = pygame.image.load(r".\PyGame Sprite Art\Paper.png").convert_alpha() # tells the code where the image is
paperect = paper.get_rect()
paperect.topleft = (40,40)
#--------------------------------
#--img--
rock = pygame.image.load(r".\PyGame Sprite Art\New Piskel.png").convert_alpha() # tells the code where the image is
rockrect = rock.get_rect()
rockrect.topleft = (40,40)
#--------------------------------
#--img--
scissors = pygame.image.load(r".\PyGame Sprite Art\Scoisners.png").convert_alpha() # tells the code where the image is
scissorsrect = scissors.get_rect()
scissorsrect.topleft = (40,40)
#===================================
#===================================


#===================================
#   FUNCTION SETUP
#===================================

# sets up a function for me to easily print the images up on the screen
def setpos(img,imgrect,img2,imgrect2,clear=False):
    #if the parameter clear is used, run this stuff to clear the board
    if clear:
        #moves the location of the image to a location
        imgrect.topleft = (40,40)
        # Fills the rect object from above with plain white to simulate clearing an area
        pygame.draw.rect(screen, (255,255,255), imgrect)
        #moves the location of the image to a location
        imgrect2.topleft = (280,40)
        # Fills the rect object from above with plain white to simulate clearing an area
        pygame.draw.rect(screen, (255,255,255), imgrect)
    else:
        #moves a rect object to a location 1
        imgrect.topleft = (40,40)
        # attaches an image to the rect object then prints it on the screen
        screen.blit(img,imgrect)
        #moves a rect object to a location 2
        imgrect2.topleft = (280,40)
        # attaches an image to the rect object then prints it on the screen
        screen.blit(img2,imgrect2)

# sets up a function for me to easily print text
def printtext(tosay,x,y,size=20,printdelay=0,bold=False): 
    font = pygame.font.Font('C:\Windows\Fonts\Arial.ttf', size)  # defines the font that I will use for the text
    if bold:  #make the text bold if a parameter is added
        font.set_bold(6)  # changes the tickness of the text making it bold
        font.set_underline(15)  # Gives the text an underline
    textbox =  font.render(tosay, True, (0,0,0)) # renders the font and puts it in a variable
    #moves it to the correct spot
    rect = textbox.get_rect()
    rect.center = (x,y)
    #prints the text on screen
    pygame.draw.rect(screen, (255,255,255), rect)
    screen.blit(textbox, rect)
    pygame.display.flip()  # Updates the displau
    #adds a delay if one is needed
    if printdelay>0:
        pygame.time.delay(printdelay)

# sets up function to print constant map ellements - the white backround, and black lines
def mapdraw(clear = True):
    # if told to, clear the map
    if clear:
        screen.fill((255,255,255))
    pygame.draw.rect(screen, (0,0,0), (0,220,480,10))
    pygame.draw.rect(screen, (0,0,0), (230,230,10,150))
    scores()

# sets up function to print the score
def scores():
    #prints the computer and player score
    printtext(str(pscore),115,285,50)
    printtext(str(compscore),360,285,50)
#===================================
#===================================
    
# sets up a giant list with all the possible ways to win and the things to draw on the screen if that chosen thing happenes
wincons = [[['rock','scissors'],['rock','paper'],['paper','rock'],['paper','scissors'],['scissors','paper'],['scissors','rock']],[rock,rockrect,scissors,scissorsrect],[rock,rockrect,paper,paperect],[paper,paperect,rock,rockrect],[paper,paperect,scissors,scissorsrect],[scissors,scissorsrect,paper,paperect],[scissors,scissorsrect,rock,rockrect],['rock',rock,rockrect],['paper',paper,paperect],['scissors',scissors,scissorsrect]]


#   Some gameplay-based variable setup
#---------------------------------
run = True
inpt = 'em' #Sets the user input to em - short for empty - so the game doesnt play automaticly
compscore = 0
pscore = 0
timer = 0 # sets up a variable for keeping track of time

#   Quick final visual touches 
#---------------------------------------
mapdraw() # prints all ui elements - the score, lines and stuff
printtext('''Oliver's Rock Paper Scissors''',240,85,32,bold=True) # Title screen
printtext('V for rock, B for paper, and N for Scissors',240,120,22) # Makes title screen instructions
pygame.display.flip()  # Updates the display


while run: #Main gameplay loop

    timer += 1 # moves the timer up by one to keep track of time
#======================================
#   EVENT HANDLER
#======================================
    #checks if event used is quit. if it is, end the gameplay loop ending the game and allowing the windows to close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #create a key variable to handle events
    keys = pygame.key.get_pressed()
    #ckecks if a set key is pressed and sets the user input to that keys corresponding thing
    if keys[pygame.K_v]:
        inpt = 'rock'
    if keys[pygame.K_b]:
        inpt = 'paper'
    if keys[pygame.K_n]:
        inpt = 'scissors'
#======================================
#======================================

    #if the players input is not 'em' for empty, allow the game to run
    if inpt != 'em':
        mapdraw() # Draws the map
        # Randomizes the computer's action
        compinpt = random.choice(['rock','paper','scissors'])

        # in the first item (where the ways to win are) in the wincons list, it checks if the users input and the computer input are in it. if they arent in it, it is a tie
        if wincons[0].count([inpt,compinpt]) == 0:
            #Visual
            printtext('Its a tie!',240,20,40) # Print that its a tie
            pygame.mixer.Channel(1).play(pygame.mixer.Sound(r".\StupidSoundsForPY\ItsATie.mp3"))  # Playes an audio file in the first sound channel - in these cases the audio played is  Nikhil saying the outcome of the match

            # Repeats 3 times
            for i in range(0,3):
                # starting at the 7th item where the tie conditions are, it goes through until it find the list where the correct tie condition is. once it finds it, it prints out the images using the data in that list.
                if wincons[7+i][0] == inpt:
                    setpos(wincons[7+i][1],wincons[7+i][2],wincons[7+i][1],wincons[7+i][2])
        # if it isn't a tie, check to see who wins
        else:
            # repeats for the number of items in wincones[0] AKA, for the ammount of possible win conditions
            # once it breaks, it gets the position of where that item is
            setpos((wincons[(wincons[0].index([inpt,compinpt]))+1])[0],(wincons[(wincons[0].index([inpt,compinpt]))+1])[1],(wincons[(wincons[0].index([inpt,compinpt]))+1])[2],(wincons[(wincons[0].index([inpt,compinpt]))+1])[3])
            
            if (wincons[0].index([inpt,compinpt])) % 2 == 0:
                pscore+=1
                printtext('You win!',240,20,40) # Print that you won
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(r".\StupidSoundsForPY\YouWon.mp3"))  # Playes an audio file in the first sound channel - in these cases the audio played is  Nikhil saying the outcome of the match
            else:
                compscore+=1
                printtext('aw, you lose!',240,20,40) # Print that you lost
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(r".\StupidSoundsForPY\YouLost.mp3"))  # Playes an audio file in the first sound channel - in these cases the audio played is  Nikhil saying the outcome of the match
        inpt = 'em' # Since the match is over, set the user input to empty so it doesnt play again untill another input is made
    scores() # Prints the scores
    pygame.display.flip()  # Updates the display
