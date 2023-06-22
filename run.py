import random

list_of_words = [
    'horse',
    'dog',
    'cat',
    'hamster',
    'apple',
    'orange',
    'pear',
    'strawberry',
    'banana',
    'pineapple',
    'carrot',
    'cucumber',
    'food',
    'student',
    'drink',
    'developer',
    'fish',
    'snake',
    'bubble',
    'wedding',
    'dress',
    'music',
    'book',
    'phone',
    'flower',
    'rose',
    'bag',
    'table',
    'chair',
    'mother',
    'father',
    'sister',
    'brother',
    'friend',
    'scarf',
    'house',
    'hand',
    'foot',
    'face',
    'heart',
    'elephant',
    'tornado',
    'thunder',
    'rain',
    'summer',
    'winter',
    'fall',
    'spring']

HANGMAN_ART = '''
*----
|   |
|   O
|  /|\ 
|  / \ 
|
'-------
'''


def welcome_message():
    '''
    Prints welcome message and hangman art
    '''

    print('Welcome to HANGMAN!' + HANGMAN_ART)


welcome_message()


lenstring = False

while not lenstring:  # Loop to ask for and validate user input
    username = input('Please enter your name: \n').capitalize()

    if len(username) >= 3:
        lenstring = True
    elif username.isdigit():
        print('Please enter letters only')
    else:
        print('Please enter a name that is at least three letters')

print(f'\nOkay, {username}, let\'s start guessing!\n')