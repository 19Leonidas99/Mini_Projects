import random


List = ['Rock', 'Paper', 'Scissors']

def RPS():
    Score_human = 0
    Score_PC = 0
    play = True
    
    while play:
        
        #print(choice, List[choice])
        
        if Score_human == 3:
            print('Gongrats You Won')
            playing = input(' Wanna Play Again ? Y/n ')
            
            if playing == 'Y':
                Score_human, Score_PC = 0, 0
                
            else:
                print('BYE')
                quit()
                
        elif Score_PC == 3:
            print('I Won, You Lost')
            playing = input(' Rematch ? Y/n ')
            
            if playing == 'Y':
                Score_human, Score_PC = 0, 0
                
            else:
                print('BYE')
                quit()
        
        choice = random.randint(0,2)
        answer = input('Rock, Paper or Scissors? ')
        answer = answer.capitalize()
        print(answer, type(answer))        
        
        if answer != 'Rock' and answer != 'Paper' and answer != 'Scissors':
            print('\nInvalid input! \nThe Valid Choices Are:  ')
            answer = input('Rock, Paper or Scissors? ')
            answer = answer.capitalize()
        
        else:
            if answer == List[choice]:
                print(answer, List[choice])        
                print('\n Draw !!!')
                print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
            
            elif answer == 'Rock' and List[choice] == 'Scissors':
                print(answer, List[choice])       
                Score_human = Score_human + 1
                print('\n User win!')
                print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
                
            elif answer == 'Paper' and List[choice] == 'Rock':
                print(answer, List[choice])        
                Score_human = Score_human + 1
                print('\n User win!')
                print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
                
            elif answer == 'Scissors' and List[choice] == 'Paper':
                print(answer, List[choice])        
                Score_human = Score_human + 1
                print('\n User win!')
                print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
                
            else:
                print(answer, List[choice])
                Score_PC += 1
                print('\n PC win!')
                print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n' )
                 
print('\nThis is a best of 5 Rock, Paper or Scissors game ')
playing = input('Do you want to play?  Y/n ') 
    
while True:
    
    if playing == 'n':
        print('Till next time')
        quit()
    
    elif playing != 'Y':
        print('\nY - Yes or n - no')
        playing = input('Do you want to play?  Y/n ')
    
    else:
        RPS()        
        