import random 
num = random.randint(1,101)

u_num = 0
while u_num != num:
    u_num = int(input('Enter ur number : '))
    if u_num>num:
        print(f'Number to guess is lower than {u_num}')
    elif u_num<num:
        print(f'Number to guess is higher than {u_num}')
    else:
        print(f'Bingo!! The number is {u_num}')
        break