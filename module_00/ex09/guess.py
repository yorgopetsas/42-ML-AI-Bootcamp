import sys
from random import randint


text = 'This is an interactive guessing game!\n'\
        'You have to enter a number between 1 and 99 to find out'\
        'the secret number.\nType \'exit\' to end the game.\nGood Luck!\n'
print(text)
down_limit = 1
up_limit = 99
intentos = 0
ranum = randint(down_limit, up_limit)


def check_choice(choice):
    if choice < 1 or choice > 99:
        print("Please provide a number between 1 and 99 including.")
        return (1)


state = 1
while state == 1:
    choice = input('What\'s your guess between 1 and 99?\n')
    intentos = intentos + 1
    if choice == 'exit':
        print('Goodbye!')
        break
    choice = int(choice)
    if check_choice(choice) == 1:
        continue

    elif choice == 42 and intentos == 1:
        text42 = 'The answer to the ultimate question of life,'\
            'the universe and everything is 42.\nCongratulations! '\
            'You got it on your first try!'
        print(text42)
        break

    elif choice == 42:
        text42 = 'The answer to the ultimate question of life,'\
            'the universe and everything is 42.'
        print(text42)
        print(f"Congratulations,you've got it!You won in {intentos} attempts!")
        break

    elif int(choice) == ranum and intentos == 1:
        print('Congratulations! You got it on your first try!')
        break

    elif int(choice) == ranum:
        print(f"Congratulations,you've got it!You won in {intentos} attempts!")
        state = 0
        break

    elif int(choice) > ranum:
        print('Too High')

    else:
        print('Too Low')
