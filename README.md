# Hangman Game

This Hangman game was created using Python and it runs in the terminal. 

The user can enter letters, one by one, until they either figure out what word the computer is asking for or until they run out of turns. 

The live game can be found here: [HANGMAN](https://hangman-1dbsvtdt9g-ac6d00bf4158.herokuapp.com/)

![Screenshot of AMIRESPONSIVE](/documentation/amiresponsive.png)

## Game Rules
Hangman is a classic game. It was originally played using pen and paper (many may remember it being played on a black/whiteboard in a classroom), but today there are many different version available online as well. 

In this Hangman game, the user is first asked to put in their name. 

The computer then generates a random word for the user to guess. The word is first displayed as a row of dashes, where the each dash represents a letter. 

By guessing letters, one by one, the user has 6 attempts to get the word right.

## Features

### Existing Features

* The user is first asked to input their name (at least three characters and letters only). When that is done, a random word is generated from a list of words for the user to guess.

![Screenshot of "welcome to game"](/documentation/welcome_screenshot1.png)

* If the user guesses a letter correctly, a message is displayed and the letters replace the dashes where they belong in the word. For both correct and incorrect guesses, the already used letters are displayed as a list. 

![Screenshot of correctly guessed letter](/documentation/correct_letter_sh.png)

* If the guessed letter is incorrect, a message is displayed and the attempts left to guess is updated. For both correct and incorrect guesses, the already used letters are displayed as a list. 

![Screenshot of incorrectly guess letter](/documentation/incorrect_letter_sh.png)

* If the user guesses a word that is incorrect, the word will be added and displayed as "guessed words".

![Screenshot of incorrectly guessed word](/documentation/word_counter_screenshot6.png)

* If the user runs out of attempts, the correct word is displayed together with ASCII art in the shape of a character from "The Simpsons".

![Screenshot of game lost](/documentation/lose_screenshot4.png)

* If the user guesses the word correctly, a "you win!" message is displayed together with ASCII art in the shape of a character from "The Simpsons" (different from the one if the user loses).

![Screenshot of game won](/documentation/win_screenshot.png)

* The user is then asked if they want to play again. 
    * Accepts user input. 
    * If 'y' (yes), a new random word will be generated and the user can play again. 


### Features Left to Implement

* In the deployed version, the dashes representing each letter of the word to guess looks like one line. I would like there to be space between the dashes, to make it clear for the user how many letters are in the word. I did not have enough time or knowledge to fix this without breaking the code.

## Testing

The manual tests done to ensure the projects functionality are:
* Run final code through [CI Python Linter](https://pep8ci.herokuapp.com/) and made sure there were no errors to report.
* Run the project in both the Codeanywhere terminal and the deployed version in Code Institute's mock terminal on Heroku.
* Enter invalid user inputs to ensure this is not possible.

### Bugs

#### Solved Bugs
* When I first ran the code through the [CI Python Linter](https://pep8ci.herokuapp.com/), it returned several errors regarding "invalid escape sequence" and "trailing whitespace" between line 54 and 120 where the ASCII art is stored. I found the first error was because the ASCII art used single backslashes. I solved this by adding double backslashes instead. To fix the second error I made sure there were no trailing whitespace.

#### Remaining Bugs
* No remaining bugs to report.

### Validator Testing

* PEP8
    * The final code was tested using the [CI Python Linter](https://pep8ci.herokuapp.com/). No errors were found.
   

## Deployment

This project was deployed using Heroku.

* Steps used for deployment:
     * On the Heroku dashboard, click "Create new app".
     * Enter app name and region. Click "Create app".
     * Locate the "Settings" tab. Add Config Vars and add buildpacks Python and NodeJS (Python first, NodeJS second).
     * Locate the "Deploy" tab. Connect to GitHub and enter the repository name to link it to Heroku.
     * Make sure branch is set to "main".
     * Click on Deploy.

* This project was deployed manually before "Automatic Deploys" was enabled.

## Credits

* [This YouTube video](https://www.youtube.com/watch?v=m4nEnsavl6w) by YouTube channel "Kite" was used as a guide to create the code for the functionality of the game. The code has been modified for my project.  
* [This YouTube video](https://www.youtube.com/watch?v=cJJTnI22IF8&t=512s) by YouTube channel "Kylie Ying" as also used as inspiration.
* ASCII art from [ASCII Art Archive](https://www.asciiart.eu/) (art by "Horroroso")