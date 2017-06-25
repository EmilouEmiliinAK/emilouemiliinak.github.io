# Emily DaLuz Guess the Number Game
from __future__ import print_function

import random

#game function

def guess_num_game():
    
    guessesMade = 0 # setting the guesses to zero at start of game
    
    print('Player Name:')
    playerName = raw_input()
    
    number = random.randint(1,20)
    print('Hi', playerName, ', I am thinking of a whole number between 1 and 20. Can you guess what it is?')
    
    while guessesMade < 5:
        print('Make a guess.')
        guess= input()
        guess=int(guess)
        
        guessesMade = guessesMade + 1
        
        if guess < number:
            print('Too low. Try again.')
        
        if guess > number:
            print('Too high. Try again.')
    
        if guess == number:
            break
        
    if guess == number:
        guessesMade = str(guessesMade)
        print('Nice job, ' + playerName +'! You guessed my number in ' + guessesMade + ' guesses!')
        
    if guess != number:
        number = str(number)
        print('Sorry, the number I was thinking of was ' + number + '.')
        

