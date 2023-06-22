import random
import os

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

ASCII_ART_WIN = '''
         _,----.
      ,-'     __`.
     /    .  /--\`)
    /  .  )\/_,--\ 
   /  ,'\/,-'    _\_
  |  /  ,' ,---'  __\ 
 ,' / ,:     _,-\'_,(
  (/ /  \ \,'   |'  _)         ,. ,.,.
   \/   |          '  \        \ ,. \ )
    \, ,-              \       /,' )//
     ; \'`      _____,-'      _|`  ,'
      \ `"\    (_,'_)     _,-'    ,'
       \   \       \  _,-'       ,'
       |, , )       `'       _,-'
       /`/ Y    ,    \   _,-'
          :    /      \-'
          |     `--.__\___
          |._           __)
-hrr-     |  `--.___    _)
          |         `----'
         /                \ 
        '                . )

'''

ASCII_ART_LOST = '''

                   _ ,___,-'",-=-.
       __,-- _ _,-'_)_  (""`'-._\ `.
    _,'  __ |,' ,-' __)  ,-     /. |
  ,'_,--'   |     -'  _)/         `\ 
,','      ,'       ,-'_,`           :
,'     ,-'       ,(,-(              :
     ,'       ,-' ,    _            ;
    /        ,-._/`---'            /
   /        (____)(----. )       ,'
  /         (      `.__,     /\ /,
 :           ;-.___         /__\/|
 |         ,'      `--.      -,\ |
 :        /            \    .__/
  \      (__            \    |_
   \       ,`-, *       /   _|,\ 
    \    ,'   `-.     ,'_,-'    \ 
   (_\,-'    ,'\")--,'-'       __\ 
    \       /  // ,'|      ,--'  `-.
     `-.    `-/ \'  |   _,'         `.
        `-._ /      `--'/             \ 
-hrr-      ,'           |              \ 
          /             |               \ 
       ,-'              |               /
      /                 |             -'
'''


def welcome_message():
    '''
    Prints welcome message and hangman art
    '''

    print('Welcome to HANGMAN!' + HANGMAN_ART)


welcome_message()


lenstring = False

# Asks for and validates user input
while not lenstring:
    username = input('Please enter your name: \n').capitalize()

    if len(username) >= 3:
        lenstring = True
    elif username.isdigit():
        print('Please enter letters only')
    else:
        print('Please enter a name that is at least three letters')

print(f'\nOkay, {username}, let\'s start the game!\n')


def get_word():
    '''
    Gets and returns a random word from word list
    '''
    word = random.choice(list_of_words)  # pick random word from list
    return word.upper()  # Return the word uppercase 


# Code inspired by https://www.youtube.com/watch?v=m4nEnsavl6w&t=7s.
# The code has been modified to fit my project.
def hangman(word):
    '''
    Main game function.

    Asks for and validates the users guesses.

    Keeps track of the users attempts and used letters.
    '''
    full_word = '_' * len(word)
    guessed = False
    guessed_letters = []  # Empty list for guessed letters
    guessed_words = []  # Empty list for guessed words
    attempts = 7 # To track user attempts
    print(f'You have {attempts} guesses.')
    print(full_word)
    print('\n')
    while not guessed and attempts > 0:
        guess = input('Please enter a letter or word: \n').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You alreay guessed this letter!\n')
                print('\nGuessed letters: ', *guessed_letters, sep=' ')
            elif guess not in word:
                print(f'{guess} is not in word')
                attempts -= 1
                guessed_letters.append(guess)
                print('\nGuessed letters: ', *guessed_letters, sep=' ')
            else:
                print(f'Nice, {guess} is the word!\n')
                guessed_letters.append(guess)
                print('\nGuessed letters: ', *guessed_letters, sep=' ')
                word_as_list = list(full_word)
                indicies = [
                    i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                full_word = ''.join(word_as_list)
                if '_' not in full_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f'You already guessed {guess}, please try again')
            elif guess != word:
                attempts -= 1
                guessed_words.append(guess)
                print('\nGuessed letters: ', *guessed_letters, sep=' ')
                print('Guessed words: ', *guessed_words, sep=' ')
                print(f'Sorry, {guess} is not the word')
            else:
                guessed = True
                full_word = word
        else:
            print('Not a valid guess. Please try again.')
        print('\n')
        print(f'{attempts} tries left.\n')
        print(full_word)
    if guessed:
        print(ASCII_ART_WIN)
        print(f'{word} is correct, you win!')
    else:
        print(ASCII_ART_LOST)
        print('Sorry, no more guesses left!\n')
        print(f'The word was {word}\n')
        

def main():
    '''
    Asks if user wants to play again and asks for input Y/N.
    '''
    word = get_word()
    hangman(word)
    while input('Play again? (Y/N) ').upper() == 'Y':
        word = get_word()
        hangman(word)


if __name__ == '__main__':
    main()