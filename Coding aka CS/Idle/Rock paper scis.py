import random
import time


def printpaper():
    print ("+-----------------------------+")
    print ("|                             |")
    print ("|    |||||||||||||||||||      |")
    print ("|    ||||||||||||||||||||     |")
    print ("|     |||||||||||||||||||     |")
    print ("|     |||||||||||||||||||     |")
    print ("|      |||||||||||||||||||    |")
    print ("|      |||||||||||||||||||    |")
    print ("|      |||||||||||||||||||    |")
    print ("|     |||||||||||||||||||     |")
    print ("|     |||||||||||||||||||     |")
    print ("|     ||||||||||||||||||||    |")
    print ("|      |||||||||||||||||||    |")
    print ("|        ||||||||||||||||     |")
    print ("|                             |")
    print ("+-----------------------------+")
def printrock():
    print ("+-----------------------------+")
    print ("|                             |")
    print ("|                             |")
    print ("|           __                |")
    print ("|         /||||\              |")
    print ("|       /|||||||\             |")
    print ("|      |||||||||||\           |")
    print ("|      |||||||||||||-         |")
    print ("|     ||||||||||||||||        |")
    print ("|    /||||||||||||||||\       |")
    print ("|   |||||||||||||||||||---    |")
    print ("|  /||||||||||||||||||||||\   |")
    print ("|  ------------------------   |")
    print ("|                             |")
    print ("|                             |")
    print ("+-----------------------------+")
def printscissor():
    print ("+-----------------------------+")
    print ("|                             |") 
    print ("|                             |")
    print ("|     /---\            -==-   |")
    print ("|    ||||||--      -=======-  |")
    print ("|    \|    |\  -===========-  |")
    print ("|     \|    ||| -=======-     |")
    print ("|      \||||||||-==-          |")
    print ("|      /|||||| |-==-          |")
    print ("|     /|    ||| -=======-     |")
    print ("|    /|    |/  -===========-  |")
    print ("|    ||||||--      -=======-  |")
    print ("|     \---/            -==-   |")
    print ("|                             |")
    print ("|                             |")
    print ("+-----------------------------+")

answer = input ("Rock, paper, or scissors? ")
answer = answer.lower()

if answer == 'rock' or answer == 'paper' or answer == 'scissors':
    if answer == "rock":
        time.sleep(0.3)
        print ('rock..')
        time.sleep(0.3)
        print ('paper..')
        time.sleep(0.3)
        print ('scissors..')
        time.sleep(0.3)
        print ('SHOOT!')
        printpaper()
        print ('HA! Paper! YOU LOSE!')
    if answer == "paper":
        time.sleep(0.3)
        print ('rock..')
        time.sleep(0.3)
        print ('paper..')
        time.sleep(0.3)
        print ('scissors..')
        time.sleep(0.3)
        print ('SHOOT!')
        printscissor()
        print ('HA! Scissors! YOU LOSE!')
    if answer == "scissors":
        time.sleep(0.3)
        print ('rock..')
        time.sleep(0.3)
        print ('paper..')
        time.sleep(0.3)
        print ('scissors..')
        time.sleep(0.3)
        print ('SHOOT!')
        printrock()
        print ('HA! Rock! YOU LOSE!')
    #if answer == "scissors":

#if answer == "paper":
        
else:
    print ("bye")

#play2an
#p2nmb
























##print ("+-----------------------------+")
##print ("|                             |")
##print ("|    |||||||||||||||||||      |")
##print ("|    ||||||||||||||||||||     |")
##print ("|     |||||||||||||||||||     |")
##print ("|     |||||||||||||||||||     |")
##print ("|      |||||||||||||||||||    |")
##print ("|      |||||||||||||||||||    |")
##print ("|      |||||||||||||||||||    |")
##print ("|     |||||||||||||||||||     |")
##print ("|     |||||||||||||||||||     |")
##print ("|     ||||||||||||||||||||    |")
##print ("|      |||||||||||||||||||    |")
##print ("|        ||||||||||||||||     |")
##print ("|                             |")
##print ("+-----------------------------+")
##
##print ("+-----------------------------+")
##print ("|                             |")
##print ("|                             |")
##print ("|           __                |")
##print ("|         /||||\              |")
##print ("|       /|||||||\             |")
##print ("|      |||||||||||\           |")
##print ("|      |||||||||||||-         |")
##print ("|     ||||||||||||||||        |")
##print ("|    /||||||||||||||||\       |")
##print ("|   |||||||||||||||||||---    |")
##print ("|  /||||||||||||||||||||||\   |")
##print ("|  ------------------------   |")
##print ("|                             |")
##print ("|                             |")
##print ("+-----------------------------+")
##
##
##
##
##
##       
##
##print ("+-----------------------------+")
##print ("|                             |") 
##print ("|                             |")
##print ("|     /---\            -==-   |")
##print ("|    ||||||--      -=======-  |")
##print ("|    \|    |\  -===========-  |")
##print ("|     \|    ||| -=======-     |")
##print ("|      \||||||||-==-          |")
##print ("|      /|||||| |-==-          |")
##print ("|     /|    ||| -=======-     |")
##print ("|    /|    |/  -===========-  |")
##print ("|    ||||||--      -=======-  |")
##print ("|     \---/            -==-   |")
##print ("|                             |")
##print ("|                             |")
##print ("+-----------------------------+")
