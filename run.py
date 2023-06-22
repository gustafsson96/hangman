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
    word = random.choice(list_of_words)  # pick random word from list
    return word.upper()


 def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Lets play hangman!')
    print(tries)
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('you alreay guessed this letter!')
            elif guess not in word:
                print(guess, 'is not in word')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('good job', guess, 'is the word')
                guessed_letters.append(guess)
                print(guessed_letters)
                word_as_list = list(word_completion)
                indicies = [
                    i for i, letter in enumerate(word) if letter == guess]
                for index in indicies:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('you already guessed this word', guess)
            elif guess != word:
                print(guess, 'is not the word')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('not a valid guess')
        print(tries)
        print(word_completion)
        print('\n')
    if guessed:
        print('you guessed the word, you win!')
    else:
        print('sorry, you ran out of tries')


def main():
    word = get_word()
    play(word)
    while input('Play again? (Y/N) ').upper() == 'Y':
        word = get_word()
        play(word)


if __name__ == '__main__':
    main()