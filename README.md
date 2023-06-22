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

After each guess, the letter will if correct replace a dash (or more if there are more than one of the letter in the word), and if incorrect, a message will be displayed telling the user that the guess was incorrect. 

After each turn, the previously guessed letter will be visible for the user in the form of a list. This makes it easy for the user to see what options they have left to guess. If the user still accidentally enters an already guessed letter, a message will tell the user what happened and ask for them to enter a different letter.

## Data Model

## Testing

### Bugs
#### Solved Bugs
#### Remaining Bugs

### Validator Testing

* PEP8
    * Test code using PEP8online.com

## Deployment

This project was deployed using Heroku.

* Steps used for deployment:
     * On the Heroku dashboard, click "Create new app".
     * Enter app name and region. Click "Create app".
     * Locate the "Settings" tab. Add Config Vars (key=PORT, value=8000). Add buildpacks Python and NodeJS (Python first, NodeJS second).
     * Locate the "Deploy" tab. Connect to GitHub and enter the repository name to link it to Heroku.
     * Make sure branch is set to "main".
     * Click on Deploy.

* This project was deployed manually before "Automatic Deploys" was enabled.

## Credits

[This YouTube video](https://www.youtube.com/watch?v=m4nEnsavl6w) by YouTube channel "Kite".

ASCII art from: 

Art by Horroroso

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
