import random


List = ['Rock', 'Paper', 'Scissors']

def RPS():
    Score_human = 0
    Score_PC = 0
    play = True
    
    while play:
        
    #print(choice, List[choice])
    
        if Score_human == 3:
            print('Gongratulation You Won')
            quit()
        elif Score_PC == 3:
            print('You Lost')
            quit()
        
        answer = input('Rock, Paper or Scissors? ')
        choice = random.randint(0,2)
            
        if answer == List[choice]:
            #print(answer, List[choice])        
            print('\n Draw !!!')
            print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
        
        elif answer == 'Rock' and List[choice] == 'Scissors':
            #print(answer, List[choice])       
            Score_human = Score_human + 1
            print('\n User win!')
            print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
            
        elif answer == 'Paper' and List[choice] == 'Rock':
            #print(answer, List[choice])        
            Score_human = Score_human + 1
            print('\n User win!')
            print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
            
        elif answer == 'Scissors' and List[choice] == 'Paper':
            #print(answer, List[choice])        
            Score_human = Score_human + 1
            print('\n User win!')
            print(' Human = ', Score_human, ' and PC = ', Score_PC, '\n')
            
        else:
            print(answer, List[choice])
            Score_PC += 1
            print('\n PC win!')
            print(' Human = ', Score_human, ' and PC = ', Score_PC )
            
    
    
        
print('This is a best of 5 Rock, Paper or Scissors game ')
playing = input('Do you want to play?  Y/n ') 
    
while True:
    
    if playing != 'Y':
        print('till next time')
        quit()
    
    else:
        RPS()        
        