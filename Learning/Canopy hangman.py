# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print len(wordlist), "words loaded."
    print ('Welcome to the game, Hangman!')
    
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
    

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    a=''
    c=0
    q=0
    s=[]
    for k in lettersGuessed:
        if k not in s:
            s.append(k)


    lettersGuessed=s[:]
    if lettersGuessed == []:
        return False
    for x in lettersGuessed:
        for y in secretWord:
            if x == y:
                a+=x
                break
    for z in a:
        for w in secretWord:
            if z == w:
                c+=1
    q = len(secretWord)
    if c==q:
        return True
    else:
        return False
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    c=0
    q=0
    s=[]
    k=1
    q = len(secretWord)
    t=[]
    l=''
    for h in range (0,q):
        t+='_'

    for k in lettersGuessed:
        if k not in s:
            s.append(k)

    lettersGuessed=s[:]
    for x in lettersGuessed:
        k=0
        for y in secretWord:
            if x == y:

                t[k]=secretWord[k]
            k+=1
    for o in t:
        l+=o

    return( " ".join(l))
    



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a='abcdefghijklmnopqrstuvwxyz'
    b=a[:]
    c=len(a)
    d=[]

    for q in range(0,c):
        d+=a[q]

    for x in lettersGuessed:
        k=0
        for y in d:
            if x==y:
                
                del d[k]
            k+=1
    return( " ".join(d))



    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    
"k=getAvailableLetters(a)"

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    raw = 'd'
    """a = len(secretWord)
    print ('I am thinking of a word that is %d letters long.' %a)
    print ('_ _ _ _ _ _ _ _ _ _ _ _ _')
    for x in range(a,0,-1):
        print ('You have %d guesses left'%x)"""
    k =  getAvailableLetters(raw)
    print ("The Available is  %s "%k)
    lettersGu = raw_input('Please Guess a letter: ')
    print lettersGu
#getGuessedWord(secretWord, lettersGu)











# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
#secretWord='apple'
hangman(secretWord)
