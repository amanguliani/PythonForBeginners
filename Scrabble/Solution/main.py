import random, math, replit

vowels = ["a", "e", "i", "o", "u"]

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def is_valid_dictionary_word(word):
  return word in load_words()

def get_random_letters(total = 7):
  random.shuffle(vowels)
  random.shuffle(consonants)

  v = math.ceil((2 * total)/ 7)
  c = total - v 
  return vowels[0:v] + consonants[0:c]

def refill_random_letters(random_letter_list, last_word):  
  for char in last_word:
    if char in random_letter_list:
      random_letter_list.remove(char)
  
  return random_letter_list + get_random_letters(len(last_word))

def calc_score(word):
    score_dict = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 5 , "l": 1 ,
         "m": 3 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 10, "r": 1 , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 4 , "x": 8 ,
         "y": 4 , "z": 10}
    score = 0
    for c in word.lower(): 
        if c in score_dict: # if character exists in dict
            score += score_dict.get(c) 
    return score

def new_word(letter_list):
  nw = input (" Whats your word ? ")
  if (not is_valid_dictionary_word(nw.lower())):
    return "Error: Your word is not a valid dictionary word, Try again !"
  
  letter_list_new = letter_list[:]
  for w in nw:
    if w not in letter_list_new:
      return "Error: Word is not compromised of the letters in your hand , Try again !"
    else:
      letter_list_new.remove(w)
  
  return nw

def append(word_list, letter_list):
  aw = input (" Whats the word you want to add to: ")
  
  if aw not in word_list:
    return "Error: Word is not on the board, Try again !", ""
  
  ac = input (" What letter do you want to add to the word: ")

  lln = letter_list[:]
  for c in ac:
    if c not in lln:
      return "Error: Letters being added is not in assigned letters , Try again !", ""
    else:
      lln.remove(c)
  
  naw = aw+ac
  if (not is_valid_dictionary_word(naw.lower())):
    return "Error: Your word is not a valid dictionary word, Try again !", ""
  
  return aw, ac

# This is the main function, start here
def main():
  print ("Welcome to Simple Scrabble")
  play_choice = input("Would you like to play ? Press Y for Yes.    ")
  if (play_choice != "Y"):
    print ("\n No problem ! Good Bye !")
    return

  print ("\n\nGood choice, before we get started, let me tell you the rules")
  print ("- You will randomly get you 7 letters to make words")
  print ("- You can make a new valid word or add to an existing word")
  print ("- Each word you make has points")
  print ("- To win you need 30 points")
  print ("- As you use the letters in your hand, you will get more letters")
  print ("- Not happy with the letters in your hand ? You can change them")
  print ("\nPhew ! That was a lot !")
  name = input(" \n Who do i have a pleasure to play with ? ")
  print ("\n\n Lets play simple scrabble {} !!!".format(name.capitalize()))

  letters_for_player = get_random_letters()
  score = 0 
  list_of_words = []
  error_message = ""
  while (score < 30):
    replit.clear()
    print ("\n\nYour letters {} ".format(letters_for_player))
    print ("Current Score {} ".format(score))
    print ("List of words on board {} ".format(list_of_words))
    print ("\n\nWhat would you like to do ? ")
    print ("1. (N)ew - Make a new words ")
    print ("2. (A)ppend - Append to an exsiting word ")
    print ("3. (R)eshuffle - Reshuffle your deck ")
    print ("4. (Q)uit - Quit the game :( ")
    print ("\n\n{}".format(error_message))
    option = input("Choice >>   ")
    option = option.lower()
    error_message = ""
    word = ""
    if (option == "q" or option == "quit"):
      print ("Sad to see you go , your were {} points away from winning ".format(30-score))
      is_quit = True
      break
    elif (option == "r" or option == "reshuffle"):
      letters_for_player = get_random_letters()
    elif (option == "n" or option == "new"):
      word = new_word(letters_for_player)
      if ("Error:" not in word):
        letters_for_player = refill_random_letters(letters_for_player, word)
        score += calc_score(word)
        list_of_words.append(word)
      else:
        error_message = word;
    elif (option == "a" or option == "append"):
      word, char = append(list_of_words, letters_for_player)
      if ("Error:" not in word):
        letters_for_player = refill_random_letters(letters_for_player, char)
        list_of_words[list_of_words.index(word)] = word+char
        score += calc_score(word+char)
      else:
        error_message = word;

  if score >= 30:
    print ("!!! You reached the score of {} !!! Thanks for playing ..".format(score))

# DO NOT EDIT THIS
if __name__ == "__main__":
  main()