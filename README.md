# Alien-Attack
My first game developed using pygame.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


- This is a pygame about earth and aliens.
- The player controls a spaceship using mouse or keyboard. 
- Aliens are coming from opposite side. You can simply dodge them or hit them. 

## How to Download and Play

### Downloading the game
- You can download the game from [release section](https://github.com/vichitr/Alien-Attack/releases) or by cliking on `Alien Attack.zip` repository or from [here](https://github.com/vichitr/Alien-Attack/raw/master/Alien%20Attack.zip).
- After downloading unzip the downloaded folder i.e. `Alien Attack.zip`.
- Now run `AlienAttack.py` file and game window will appear. Start playing and have fun.

### Prerequisites to run the game
- Download and install `Python`(2.7.13 or higher version) and set environment variables. Link to download Python2.7.14 is [here](https://www.python.org/ftp/python/2.7.14/python-2.7.14.msi).
- Download any compiler or text editor to run python files. I use `Geany`. Link to download `Geany` is [here](http://download.geany.org/geany-1.31_setup.exe).
- Set environment variables for `Geany` to run .py files.
- Install `pygame` module for your version of `Python`. You can download latest version from [here](https://pypi.python.org/packages/61/06/3c25051549c252cc6fde01c8aeae90b96831370884504fe428a623316def/pygame-1.9.3.tar.gz#md5=ac744ea6952b68d5f2b6d02a6d8e836c).
- Make sure that `pygame` module is working for your current version of `Python` and your operating system.

### Playing the game
- After completing all above steps open `AlienAttack.py` file with your text editor i.e. `Geany` and Compile it.
- After succesful compilation Run the file. Game window will appear and you can start playing.
- All the commands and instructions to play the game are given in README.txt file.

### PS: Put all the files of zip folder in the same directory. Otherwise the game won't run.

### Instructions and Commands to play the game
1. Player is given 3 Lifes, 5 Superbullets and infinite spaceship bullets in the beginning of the game.   
2. Keyboard Controls-
- SPACE - To hit an alien
- LEFT TAB - To use super bullet
- KEY A or LEFT ARROW - Move left
- KEY D or RIGHT ARROW - Move right 
- KEY S or DOWN ARROW - Move Down
- KEY W or UP ARROW - Move Up
- KEY P - Pause the game
- ESCAPE - Exit the game
3. Mouse Controls-
- Use the mouse to move the spaceship
4. Difficulty Level-
- As the game progresses, difficulty level increases.
5. Powerups-
- Heart Sign Powerup - To increase the no of lifes(Max lifes = 3). 
- Energy Sign Powerup - To increase the no  of superbullets(Max = 9)
6. Aliens-  
- There are three types of aliens coming
- Alien: Hit once to destroy. Score - 10 per alien destroyed.
- Alien1: Hit once to destroy. Score - 15 per alien destroyed.
- Super Alien: Hit thrice to destroy. Score - 30 per alien destroyed.
7. Super Bullets-
- Max no of super bullets to store is 9.
- Super bullet doesn't get destroyed till it reaches the end of screen.
- It can destroy any type of alien with one hit.
- Also, player get more score if he/she destroys aliens with super bullets. 
- Score for different aliens is as following-  
  Alien - Score of 20, Alien1 - Score of 30 and Super Alien - Score of 60
