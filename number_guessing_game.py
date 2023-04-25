import random

def guess_the_nunber():
    guessing_number = random.randint(0, 100)
    number_of_guesses = 0
    print(guessing_number)
    
    print('Guess The Number Game!\nGuess the random number between 0-100,\nlesser guesses better. Simple right?!')
    guess = int(input('Guess: '))
    
    if guess == guessing_number:
        print('Gongrats!!! You Won')
        quit()
    
    elif guess < guessing_number:
        print('It is a higher number')
        number_of_guesses += 1
    
    else:
        print('Lower')
        number_of_guesses += 1
        
 
guess_the_nunber()