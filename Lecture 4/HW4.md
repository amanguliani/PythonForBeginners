# Homework - Lecture 4

# Coding Problems 

NOTE:

Try and use functions in all problems and keep in mind that the code should work for other inputs similar to the examples in the problems.

1. Your program randomly select a number between 1 -1000.
Then take an input from the user to guess the number and give some clues.
- Print Higher if the number guessed is higher
- Lower otherwise
Give the user 20 chances to guess the number.

2. My bluetooth keyboard has a lag and sometimes repeats the last word i typed. Write a function to only remove the subsequent repeated word from a string. For Example.

For a string "Hey this is is a fun fun assignment is it not not "

Output should be "Hey this is a fun assigment is it not "

Note: How it keeps the 'is' later in the sentence in the example.

3. Calculate the word score

Write a function which takes a word of any length upto 10 and calculates its score adding the characters scores based on the dictionary given to you 

score = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}

Example: The score for "buzz" is 24 (3+1+10+10)

4. Word Cross.

Write a function that takes two words and prints how many places do the words cross each other like in a crossword

For ex:

word 1 : Homework
word 2 : Read


Words cross at 2 places  - R and e like this 

Homework
      e
      a
      d
   r
Homework
   a
   d


5. Cows and Bulls

Write a function that takes two words of same length and no repeated characters and prints how many characters in the two words are in the same place (Bulls) and how many characters are common but not in the same place.

For ex: 

word 1 = bird
word 2 = ride

Output should be 2 cow (for r and d) and 1 bull (for i)
