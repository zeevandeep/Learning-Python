import random
import string
 
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
def isValidWord(word, hand, wordList):
    a=''
    c=0
    k=0
    for x in word:
        for y in hand:      
            if x==y:
                if hand[y]==0:
                    break
                else:
                    hand[y]-=1
                    a+=x
                
    if a in wordList or a =='':
        return True
    else:
        return False
def calculateHandlen(hand):
    
    a=0
    for y in hand:
        if hand[y]!=0:
            a+=hand[y]
    return a
def getWordScore(word, n):
    a= len(word)
    o=0
    for q in word:
        for w in SCRABBLE_LETTER_VALUES:
            
            if w == q:
                o+= SCRABBLE_LETTER_VALUES[w]
    g=o*a
    if a == n:
        return g+50
    else:
        return g    
def isValidWord(word,hand,wordList):
	a=''
	c=0
	k=0
	for x in word:
		for y in hand:		
			if x==y:
				if hand[y]==0:
					break
			else:
				hand[y]-=1
				a+=x
				
	if a in hand or a =='':
		return True
	else:
		return False 

def playHand(hand, wordList, n):
	a=False
	t=0
	r=0
	
	while not a:
		for x in hand:
			print x
		s=raw_input('Enter word, or a "." to indicate that you are finished: ')
		if s == '.':
			a=True
			break
		else:
			m= isValidWord(word,hand,wordList);
			if m == False:
				print ('Invalid word, please try again.')
			else:
				u=calculateHandlen(hand);
				if u==0:
					a=True
					break
				else:

					t=getWordScore(word,n)
					r+=t
					print('%s'%word+'has earned him %d '%t + 'points.')
					print ('Total: %d '%r+ 'points')
					updateHand(hand, word);


