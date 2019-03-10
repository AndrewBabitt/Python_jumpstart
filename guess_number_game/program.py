import random

print('------------------------')
print(' GUESS THAT NUMBER GAME ')
print('------------------------')

the_number = random.randint(0,100)
guess_number = -1
name = input('Player what is your name? ')

while guess_number != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess_number = int(guess_text)
    if guess_number < the_number:
        print('Sorry {}, your guess of {} was too LOW'.format(name, guess_number))
    elif guess_number > the_number:
        print('Sorry {}, your guess of {} was too high'.format(name, guess_number))
    else:
        print('Excellent work {}. It was {}'.format(name, the_number))
