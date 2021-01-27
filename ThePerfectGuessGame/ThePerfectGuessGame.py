import random ,os

num = random.randint(1,101)
noOfGuess = 0
u_num = None

while u_num != num:
    u_num = int(input('Enter ur number : '))
    noOfGuess +=1 
    if u_num>num:
        print(f'Number to guess is lower than {u_num}')
    elif u_num<num:
        print(f'Number to guess is higher than {u_num}')
    else:
        print(f'Bingo!! The number is {u_num} and you guessed in {noOfGuess} number of guesses')
        break

fileName = 'D:\\GITHUB\\GAMES\\ThePerfectGuessGame\\HighScore.txt'

isEmpty = False
with open(fileName,'r') as f:
    if os.stat(fileName).st_size == 0:
        isEmpty = True
        highScore = noOfGuess
    else:
        highScore = int(f.read())

if noOfGuess<highScore or isEmpty:
    if isEmpty: 
        print('New High Score!')
    else:
        print('You broke the High Score!')
    
    with open(fileName,'w') as f:
        f.write(str(noOfGuess))
