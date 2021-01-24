import random

user_score = 0
comp_score = 0

while user_score != 5 and comp_score != 5 :
    
    option_user = input('Enter your Option Snake/Water/Gun : ').lower()
    option_list = ['snake','water','gun']
    

    if option_user in option_list:

        option_comp = random.choice(option_list)
        print('Computer  Option : ', option_comp.capitalize())
        print()

        if (option_user == 'snake' and option_comp == 'water') or \
            (option_user == 'water' and option_comp == 'gun') or \
            (option_user == 'gun' and option_comp == 'snake'):

            user_score +=1

        if (option_comp == 'snake' and option_user == 'water') or \
            (option_comp == 'water' and option_user == 'gun') or\
            (option_comp == 'gun' and option_user == 'snake'):
            comp_score +=1
            
        print('User Score : ',user_score)
        print('Computer Score : ',comp_score)
        print('-'*40,'\n\n')
        print("Enter 'Exit'  to leave the game\n")
        print()


    elif option_user.lower() == 'exit':
        print('User Score : ',user_score)
        print('Computer Score : ',comp_score)
        print('-'*40)
        print('\n','*'*40,sep='')
        print('Thank you for Playing'.upper())
        print('*'*40)
        break
    else:
        print('\n','*'*40,sep='')
        print('Enter valid option (Snake/Water/Gun) only'.upper())
        print('*'*40,'\n\n')

        

print('SCORE : ')
print('User Score : ', user_score)
print('Computer Score : ', comp_score)
print('\n\n\n\n')
if user_score ==5 :
    print('You Won'.center(20,'*').upper() )
elif user_score == comp_score:
    print('Draw'.center(20,'*').upper())
else:
    print('You Lost'.center(20,'*').upper())