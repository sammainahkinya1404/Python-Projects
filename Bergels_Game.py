import random

NUM_DIGITS=3
MAX_GUESSES=10

def main():
    print('''
          Bagels, a deductive logic game.
          By Samson Kinyanjui

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:  That means:
Pico         One digit is correct but in the wrong position.
Fermi        One digit is correct and in the right position.
Bagels       No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))
    # Main game loop
    while True:
        # variable to store the secret number the player needs
        secretNum=getSecretNum()
        print('I have thought of up a number')
        print('you have {} guesses to get it'.format(MAX_GUESSES))
        
        numGuesses=1
        while numGuesses <= MAX_GUESSES:
            guess=''
            # keep looping until you enter a valid guess
            while len(guess) !=NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess=input('>')
            
            
            clues=getClues(guess, secretNum)
            print(clues)
            numGuesses +=1
            
            if guess == secretNum:
                # They're correct so break out of this loop
                
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses')
                print('The answer was {}.'.format(secretNum))
        # Ask player if they want to play again
        print("Do you want to play again ?(yes or no)")
        if not input('>').lower().startswith('y'):
            break
        print('Thanks for playing!')
def getSecretNum():
    # create a list of digits 0-9
    numbers= list('0123456789')
    # shuffle them into random order
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum += numbers[i]
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got ir!'
    
    clues=[]
    for i in range(len(guess)): 
        if guess[i] == secretNum[i]:
            # A correct digit is in correct place
            clues.append('Fermi')
        elif guess[i] in  secretNum:
            # A correct digit is in the wrong place
            clues.append('Pico')
    if len(clues) == 0:
        # There are no correct digits at all
        clues.append('Bagels')
        
    else:
        clues.sort()
        # Make a single string from  the list of strings clues
        return ''.join(clues)

main()
    
    
    