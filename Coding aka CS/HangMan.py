import random   #Imports the random module so that I can generate pseudo-random numbers

images = ['img1','img2','img3','img4']  #Sets up where the images are - there is just text there currently but you can add a text image if youd like
words = ['hello']   # This sets where the possible words it can choice for you to guess
hidden = [] # Makes an empty list where the line of guesses can show
wordchoice = random.choice(words)   #Choses the word the computer will use for you to guess
wordchoice2 = list(wordchoice)  #Makes a worse looking version the variable above that is used for checking if your guess is correct

for letters in wordchoice:
    if letters == ' ':
        hidden.append('  ')
    else: hidden.append("_ ")


guesses = 0
running = True

tries = 3

print(images[guesses])
print(''.join(hidden))

while guesses < len(images) and "_ " in hidden:
    letterguess = input('Letter guess: ')
    if letterguess not in list('qwertyuioplkjhgfdsazxcvbnm '):
        print('put in a letter')
    print('---------------------------------')
    if letterguess in wordchoice2:
        for index in range(len(wordchoice2)):
            if letterguess == wordchoice2[index]:
                hidden[index] = letterguess+' '
    guesses+=1
    if guesses > len(images): print(images[guesses])
    print(''.join(hidden))

if guesses == tries:
    print('u lose')
    running = False
if "_ " not in hidden:
    print('u win')
    running = False