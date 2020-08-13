# Scrabble

Your assignment is to build a simple version of scrabble to play against.
A Player should be able to play against your program. 

## Time
You have 2 weeks to finish this assigment. Try and divide the code into several functions so you can build it iteratively.

## Logistics
You can use either repl.it or your own python interpretor to write the full python code. DO NOT use  notebook for this project. It can be done but is not practical. You are encourages to try parts of the code in a notebook to try them out quickly.

## Word checking 
To make it easier to check if a word exist in dictionary you can use code and file in  https://repl.it/@AmandeepGuliani/scrabble which loads the dictionary word in a list.

## Game Play

### Setup
Explain the rules in the begginning to the player so they know what they need to play and win.
To start the game, you will ask the players name if they want to play.
If yes randomly assign the player 7 alphabets, to make it fair, give the player 5 consonants and at least 2 vowel.

### Playing the game 
Once the alphabets are distributed , you ll ask the player what they want to do. The following choices are valid:

1. Quit 
The player wants to quit the game. 
On selecting this option, give the players final score and quit.

2. New
The players wants to make a new word on the board.
On selecting this option, ask the word from the player.
Once entered check the following:
* Word is valid
* Word is not already on the board
* Word is made from given alphabets assigned to the player.

After the word is successful taken. Update the following:
* List of words on the board
* Players score
* Players assigned alphabets.

3. Append
The players wants to append to an existing word.
On selecting this option, ask which word to they want to add to and what.
Once entered check the following.

* Word being add to is on the board.
* Alphabet chosen is assigned to the player 
* Word and alphabet appended is a valid dictionary word.

After a successfull appen, update the following
* List of words on the board
* Players score
* Players assigned alphabets.

4. Flush 
The players wants to flush existing assigned alphabets and wants a new set of alphabets.
On selecting this option , your program will discard all left alphabets and give the player fresh 7 alphabets.

### Winning
The player will win the game if their score reaches 30. Every word added or appended, gives the player a score based on the following dictionary: 
score = {"a": 1 , "b": 3 , "c": 3 , "d": 2,  "e": 1 , "f": 4 , "g": 2 , "h": 4 ,"i": 1 , "j": 8 , "k": 5 , "l": 1 , "m": 3 , "n": 1 , "o": 1 , "p": 3 ,"q": 10, "r": 1 , "s": 1 , "t": 1 , "u": 1 , "v": 4 , "w": 4 , "x": 8 ,"y": 4 , "z": 10}

### Misc
Make the game as user friendly as possible. If you feel adding something will make the game more fun, absolutely do. 
