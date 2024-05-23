#----------------------#
#-----DOCUMENTATION----#
#----------------------#


# Oliver Davis
# 11/5/2023
# Description:
#   A fun little storline where you have to make it through an imaginary morning routine with an annoying alarm clock at your side trying to ruin it
# Bugs:
#   Ideally, there would be no bugs. I have ran through all possible outcomes and have not found any, but there is almost certainly atleast one that I have missed
# Challenges:
#   To be fully honest, im not quite certain of what counts as a challenge so I have just put things that I think count:
#       - str.lower -
#           makes all inputs put in lowercase. for example, if I were to use it for an input, the user could put in "GoOd DaY" and it would be changed into "good day"
#       - function loop -
#           uses functions to form a loop that repeats until stopped. For example, I was able to use this so that when you put "sleep in" in the first answer, it will wait a few seconds and then restart the code
#       - time.sleep() -
#           uses a module named 'time' to add delay. I don't know what else to add here, i can just say time.sleep() and put a parameter inside of the parenthesis to make it wait for an ammount of time I want in seconds. for example, if I were to do time.sleep(1), it would wait for 1 second then continue on
#       - while i in range loops
#           these allow me to use loops to repeat code a specified ammount of times. For example, I would do 'while i in range(5):', then whatever in indented after it will repeat until i is no longer in range 5. to only make it repeat 5 times, i would do i+1 in the loop
#       - Correct answer detection -
#           if you insert an answer that is not one of the ones that I have coded it to detect on that specific question (for example if it asks a or b and you put in c). if you dont put in one of the answers, it will just restart
#
# Instructions:
#   run the module, then answer with one of the options given. it is not cap-sensitive as it will always make it lowercase. then, it will reply to you with another question



#----------------------#
#------CODE START------#
#----------------------#



import time  # imports the module 'time' allowing me to use special things in it. one if these things allows me to add a delay to my code

def morningtime():  # defines the function 'morningtime'. this means that all code idented under this is under this function. all that code can then be ran by running the function
    print('''Annoying Alarm Clock:)
      Hey stupid, wake up. Its Morning time
    -----------------------------------------
    Will u wake up? (A) for yes, (B) for no:''')  # says everything inside of the '''
    x = str.lower(input())  # stores the next thing the user types on the variable x and makes all uppercase letters lowercase  

    if x == 'b':  # if x is 'b', do this stuff ('this stuff' means the stuff tabbed below this)
        print('''-----------------------------------------
        You:
          no u

        ''')  # says everything inside of the '''
        time.sleep(1) #wait 1 second
        print('''Alarm Clock:
          fine you can have 5 seconds''')  # says everything inside of the '''
        time.sleep(1) #wait 1 second
        i = 0  # Sets the variable i to 0 to prepare for the upcoming loop
        while i in range(5):
            print("  ...")  # says everything inside of the "
            time.sleep(1) #wait 1 second
            i += 1
        print('''  Okay, times up.
        ''')  # says everything inside of the '''
        morningtime()  # runs the previously defined function 'morningtime' with no paramaters (because there werent supposed to be any)
        #----------------------#
        #-------RE-START-------#
        #----------------------#
    elif x == 'a':  # if the user's input was not 'b', then if the input was 'a', do this
        print('''-----------------------------------------
        You:
          Ok

        ''')  # says everything inside of the '''
        time.sleep(1) #wait half a second
        print("You get ready for school and are about to leave")  # says everything inside of the "
        time.sleep(1) #wait half a second
        print("")  # says everything inside of the "
        print('''Annoying Alarm Clock:
          Arent you gonna eat breakfast?
        
        -----------------------------------------
        Will you say: (A) for: I already did, or (B) for just shut up stupid:''')  # says everything inside of the '''
        x = str.lower(input())  # stores the next thing the user types on the variable x and makes all uppercase letters lowercase
        
        if x == 'b':
            print('''-----------------------------------------
            You through the alarm clock out the window.
            You can hear the low, angry beepin.g
            The next night, it appears in your room again and wakes you up 10 seconds early''')  # says everything inside of the '''

            #----------------------#
            #-----END CONDITION----#
            #----------------------#
            
        elif x == 'a':  # if the user's input was not 'b', then if the input was 'a', do this
            print('''-----------------------------------------
            You:
              UGH! I ALREADY DID!
              YOU LITTERALY WATCHED ME!!!
              I HATE YOU!
              YOU MAKE MY MORNINGS EVEN MORE MISSERALE THEN THEY ALREADY ARE!!!!!!1!!1111!

            Annoying Alarm Clock:
            
            ''')  # says everything inside of the '''
            i = 0  # Sets the variable i to 0 to prepare for the upcoming loop
            while i in range(5):
                print("  ...")  # says everything inside of the "
                time.sleep(1) #wait 1 second
                i += 1
            print('''Can I come to school with u?)

            ''')  # says everything inside of the '''
            time.sleep(1) #wait 1 second
            print("")  # says everything inside of the "
            time.sleep(1) #wait 1 second
            print("")  # says everything inside of the "
            time.sleep(1) #wait 1 second
            print('''-----------------------------------------
            Will you: (A) for: Throw it int your fireplace, (B) for: just walk away, or (C) for: saying 'Sure.' ''')  # says everything inside of the '''
            x = str.lower(input())  # stores the next thing the user types on the variable x and makes all uppercase letters lowercase

            if x == 'a':  # if the user's input was 'a', do this
                print('''-----------------------------------------
                you throw your alarm clock into the fireplace
                you then miss the next 3 weeks of school because you slept too much''')  # says everything inside of the '''

                #----------------------#
                #-----END CONDITION----#
                #----------------------#
                
            elif x == 'b':   # if the previous thing was not true, then if x = 'b' do this stuff
                print('''-----------------------------------------
                You stare at the alarm clock for a while before walking to the door, opening it, walking through it, and locking it from the outside
                -----------------------------------------
                Will you: (A) for: Walk to school, or (B) for: Take the bus''')  # says everything inside of the '''
                x = str.lower(input())  # stores the next thing the user types on the variable x and makes all uppercase letters lowercase

                if x == 'a':  # if the user's input was 'a', do this
                    print("-----------------------------------------")  # says everything inside of the "
                    print('''you step in a puddle on your way to school
                    your socks were soggy the whole day. Now your sad''')  # says everything inside of the '''

                    #----------------------#
                    #-----END CONDITION----#
                    #----------------------#
                    
                elif x == 'b':   # if the previous thing was not true, then if x = 'b' do this stuff
                    print("-----------------------------------------")  # says everything inside of the "
                    print('''You wait for the bus. Once it arrives, you hop on and see your friends
                    they all find the story about your alarm clock very funny''')  # says everything inside of the '''

                    #----------------------#
                    #-----END CONDITION----#
                    #----------------------#
                    
                else:  # If no other inputs are true, do this stuff
                    print('''Annoying Alarm Clock:)
                    (  dude''')  # says everything inside of the '''
                    time.sleep(1) #wait 1 second
                    print('  not cool')
                    time.sleep(1) #wait 1 second
                    print('''  like just put a real answer
                    -----------------------------------------''')  # says everything inside of the '''
                
            elif x == 'c':  # if the previous thing was not true, then if x = 'c' do this stuff
                print('''-----------------------------------------
                You stare at the alarm clock for a while before walking to it, and shoving it in your bag. You then walk out the door, ready for school
                -----------------------------------------
                Will you: (A) for: Walk to school, or (B) for: Take the bus''')  # says everything inside of the '''
                x = str.lower(input())  # stores the next thing the user types on the variable x and makes all uppercase letters lowercase

                if x == 'a':  # if the user's input was 'a', do this
                    print("-----------------------------------------")  # says everything inside of the "
                    print('You walk to school. Your feet kinda hurt from the walk')

                    #----------------------#
                    #-----END CONDITION----#
                    #----------------------#
                    
                elif x == 'b':   # if the previous thing was not true, then if x = 'b' do this stuff
                    print('''-----------------------------------------
                    You wait for the bus.
                    once it arrives, you hop on and sit near your friends.
                    then, your alarm clock starts to talk. They hear it, and start to bully you about it
                    you then relize you need new friends''')  # says everything inside of the '''

                    #----------------------#
                    #-----END CONDITION----#
                    #----------------------#
                    
                else:  # If no other inputs are true, do this stuff
                    print('''Annoying Alarm Clock:)
                    (  dude''')  # says everything inside of the '''
                    time.sleep(1) #wait 1 second
                    print('  not cool')
                    time.sleep(1) #wait 1 second
                    print("  like just put a real answer")  # says everything inside of the "
                    print("-----------------------------------------")  # says everything inside of the "
            else:  # If no other inputs are true, do this stuff
                print('''Annoying Alarm Clock:)
                (  dude''')  # says everything inside of the '''
                time.sleep(1) #wait 1 second
                print('  not cool')
                time.sleep(1) #wait 1 second
                print("  like just put a real answer")  # says everything inside of the "
                print("-----------------------------------------")  # says everything inside of the "

            
        else:  # If no other inputs are true, do this stuff
            print("Annoying Alarm Clock:")  # says everything inside of the "
            print("  dude")  # says everything inside of the "
            time.sleep(1) #wait 1 second
            print("  not cool")  # says everything inside of the "
            time.sleep(1) #wait 1 second
            print("  like just put a real answer")  # says everything inside of the "
            print("-----------------------------------------")  # says everything inside of the "
            morningtime()  # runs the previously defined function 'morningtime' with no paramaters (because there werent supposed to be any)

            #----------------------#
            #-------RE-START-------#
            #----------------------#
            
    else:  # If no other inputs are true, do this stuff
        print("Annoying Alarm Clock:")  # says everything inside of the "
        print("  dude")  # says everything inside of the "
        time.sleep(1) #wait 1 second
        print("  not cool")  # says everything inside of the "
        time.sleep(1) #wait 1 second
        print("  like just put a real answer")  # says everything inside of the "
        print("-----------------------------------------")  # says everything inside of the "
        morningtime()  # runs the previously defined function 'morningtime' with no paramaters (because there werent supposed to be any)

        #----------------------#
        #-------RE-START-------#
        #----------------------#
        
morningtime()  # runs the previously defined function 'morningtime' with no paramaters (because there werent supposed to be any)
