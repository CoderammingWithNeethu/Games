import random 
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