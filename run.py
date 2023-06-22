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


def get_word():
    '''
    Gets and returns a random word from word list
    '''
    word = random.choice(list_of_words)  # pick random word from list
    return word.upper()  # Return the word uppercase 


def hangman(word):
    '''
    Main game function.

    Asks for and validates the users guesses.

    Keeps track of the users attempts and used letters.
    '''
    full_word = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print(f'{attempts} guesses left')
    print(full_word)
    print('\n')
    while not guessed and attempts > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('you alreay guessed this letter!')
            elif guess not in word:
                print(guess, 'is not in word')
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print('good job', guess, 'is the word')
                guessed_letters.append(guess)
                print(guessed_letters)
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
                print('you already guessed this word', guess)
            elif guess != word:
                print(guess, 'is not the word')
                attempts -= 1
                guessed_words.append(guess)
                print(guessed_letters)
            else:
                guessed = True
                full_word = word
        else:
            print('not a valid guess')
        print(attempts)
        print(full_word)
        print('\n')
    if guessed:
        print('you guessed the word, you win!')
    else:
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