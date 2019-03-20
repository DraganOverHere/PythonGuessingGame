from os import system, name 

from time import sleep

import random

from random import randint

def clear(): 
    
    if name == 'nt': 
        _ = system('cls') 
  
    else: 
        _ = system('clear')  

clear()

userinput= 0

easyguess=15

mediumguess=10

hardguess=5

easyrandom= randint(1,100)

mediumrandom= randint(1,300)

hardrandom= randint(1,500)

#------------------------------------------
def startmenu():
    print 30*"-", "[THE GUESSING GAME]", 30*"-"



    print  30*"-","[THE INSTRUCTIONS]", 31*"-"

    print "- Type down the mystery number."



    print "- Win by not running out of guesses."


    print  30*"-","[DIFFCULTY LEVELS]", 31*"-"



    print "1. EASY LEVEL: random integers from 1-100 and only have 15 guesses."
    print "2. MEDIUM LEVEL: random integers from 1-300 and only have 10 guesses."
    print "3. HARD LEVEL: random integers from 1-500 and give them 5 guesses."
    print 81*"-"

loop= True 






#---------------------------------------------------------------
while loop:
    startmenu()
    enterguesslevel= raw_input ("SELECT THE NUMBER DIFFCULTY: ")
    if enterguesslevel== "1":
        print ("EASY LEVEL SELECTED")
        sleep(2)
        clear()
        while True:
            try:
                if easyguess == 0:
                    print"You Lose"
                    break
                
                print 81*"-"
                print ("You have {0} guesses remaining".format(easyguess))
                guess = int(raw_input("Enter an integer from 1 to 100: "))
                if guess > 100:
                    print("Only integers within 1 to 100")
                    sleep(1)
                    clear()
                    
                elif guess < easyrandom:
                    easyguess=easyguess-1
                    print "Guess Higher"
                    sleep(1)
                    clear()
                    
                elif guess > easyrandom:
                    easyguess=easyguess-1
                    print "Guess Lower"
                    sleep(1)
                    clear()
                    
                else:
                    print "You guessed it!"
                    break
                
            except ValueError:
                print"Only integers"
                sleep(2)
                clear()
        break
    elif enterguesslevel== "2":
        print ("MEDIUM LEVEL SELECTED")
        sleep(2)
        clear()
        print 81*"-"
        while True:
            try:
                if mediumguess == 0:
                    print"You Lose"
                    break
                
                print 81*"-"
                guess = int(raw_input("Enter an integer from 1 to 300: "))
                if guess > 300:
                    print("Only integers within 1 to 300")
                    sleep(1)
                    clear()
                    
                elif guess < mediumrandom:
                    mediumguess=mediumguess-1
                    print "Guess Higher"
                    sleep(1)
                    clear()
                    
                    
                elif guess > mediumrandom:
                    mediumguess=mediumguess-1
                    print "Guess Lower"
                    sleep(1)
                    clear()

                    
                else:
                    print "You guessed it!"
                    break
            except ValueError:
                print"Only integers"
                sleep(2)
                clear()
        break
    
    elif enterguesslevel== "3":
        print ("HARD LEVEL SELECTED")
        sleep(2)
        clear()
        print 81*"-"
        while True:
            try:
                if hardguess == 0:
                    print"You Lose"
                    break
                
                print 81*"-"
                guess = int(raw_input("Enter an integer from 1 to 500: "))
                if guess > 500:
                    print("Only integers within 1 to 500")
                    sleep(1)
                    clear()
                    
                elif guess < hardrandom:
                    hardguess=hardguess-1
                    print "Guess Higher"
                    sleep(1)
                    clear()
                    print ("You have {0} guesses remaining".format(hardguess))
                    
                elif guess > hardrandom:
                    hardguess=hardguess-1
                    print "Guess Lower"
                    sleep(1)
                    clear()
                    print ("You have {0} guesses remaining".format(hardguess))
                    
                    
                else:
                    print "You guessed it!"
                    break
            except ValueError:
                print"Only integers"
                sleep(2)
                clear()
        break
    
    else:
        print "Error: PLEASE SELECT A PROPER LEVEL."
        sleep(1)
        clear()
        

# Sources https://docs.python.org/3/library/random.html
