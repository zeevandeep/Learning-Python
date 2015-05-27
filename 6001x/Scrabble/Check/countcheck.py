


SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
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
    
   

"""
def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if searchFor in v:
                return k
    return None

#Checking if string 'Mary' exists in dictionary value
print search(myDict, 'Mary') #prints firstName

"""
getWordScore('qi',7)
