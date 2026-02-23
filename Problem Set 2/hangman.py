# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_letters = 0
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                matched_letters += 1
    if matched_letters >= len(secret_word):
        return True
    else:
        return False


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    string = []
    
    for i in secret_word:
        matched_letters = 0
        for j in letters_guessed:
            if i == j:
                matched_letters+=1
        if matched_letters == 0:
            string.append('*')
        else:
            string.append(i)
    return (''.join(string))


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in letters_guessed:
        if i in available_letters:
            available_letters.remove(i)
    return (''.join(sorted(available_letters)))

def provide_missing_letters(secret_word,available_letters):
    choose_from = []
    for i in available_letters:
        if i in list(secret_word):
            choose_from.append(i)
    new = random.randint (0, len(choose_from)-1)
    revealed_letter = choose_from [new]
    return revealed_letter

def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    vowels = ['a','e','i','o','u']
    letters_guessed = []
    guesses_left = 10
    user_guess = ''
    print ("Welcome to Hangman!")
    print (f'I am thinking of a word that is {len(secret_word)} letters long')

    while guesses_left > 0 and get_word_progress(secret_word, letters_guessed) != secret_word:
        print ("------------")
        if guesses_left == 1:
            print (f'You have {guesses_left} guess left.')
        else:
            print (f'You have {guesses_left} guesses left.')
        print(f'Available letters: {get_available_letters (letters_guessed)}')
        user_guess = (input ("Please guess a letter: ")).lower()
        if user_guess.isalpha() == True:
            if user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
                if user_guess in list(secret_word):
                    print (f'Good guess: {get_word_progress(secret_word,letters_guessed)}')
                else:
                    if user_guess not in vowels:
                        guesses_left-=1
                        print (f'Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}')
                    else:
                        if guesses_left == 1:
                            print (f'Game over!')
                            break
                        else:
                            guesses_left-=2
                            print (f'Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}')
            else:
                print (f"Oops! You've already guessed that letter: {get_word_progress(secret_word,letters_guessed)}")
        elif with_help and  user_guess =="!":
            if guesses_left >= 3:
                revealed_letter = provide_missing_letters(secret_word,get_available_letters (letters_guessed))
                letters_guessed.append(revealed_letter)
                print(f'Letter revealed: {revealed_letter}')
                print (f'{get_word_progress(secret_word,letters_guessed)}')
                guesses_left-=3
            else:
                print (f'Oops! Not enough guesses left: {get_word_progress(secret_word,letters_guessed)}')
        else:
            print (f'Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word,letters_guessed)}')

    if guesses_left == 0:
            print ('------------------')
            print (f'Sorry, you ran out of guesses. The word was {secret_word}.')
    else:
        print ('------------------')
        print (f'Congratulations, You won!')
        total_score = (guesses_left + 4 * len(set(secret_word)) + (3 * len(secret_word)))
        print (f'Your total score was {total_score}')





# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    with open ('words.txt') as f:
        secret_word = random.choice(f.read().split())
    secret_word = 'hi'
    with_help = True
    hangman(secret_word, with_help)

