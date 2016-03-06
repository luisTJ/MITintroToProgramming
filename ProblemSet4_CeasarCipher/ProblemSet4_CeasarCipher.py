# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random
import sys
import itertools

WORDLIST_FILENAME = "ps4/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def load_words():
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable

def printDict(dict):
    keys = dict.keys()
    keys.sort()
    for key in keys :
        sys.stdout.write(key)
    sys.stdout.write("\n")
    for key in keys :
        sys.stdout.write(dict[key])
    sys.stdout.write("\n")

# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    #convert negative to comparable positive
    if(shift < 0):
        shift = (27 - abs(shift)%27)%27
    elif(shift > 0):
        shift = shift % 27
    result = {}
    a = ord('a')
    for i in range(0,26):
        key = chr(a + i)
        tmp = i+shift
        
        val = chr(a + (tmp % 27))

        if(val == '{'): #{ comes after z
            val = ' '

        result[key] = val
        result[key.upper()] = val.upper()

    if(shift > 0):
        result[' '] = chr(a+shift-1)
    else:
        result[' '] = ' '

    printDict(result)
    return result


def build_encoder(shift):
    return build_coder(shift)

def build_decoder(shift):
    return build_coder(-shift)


def apply_coder(text, coder):
    result = ""
    i = 0
    size = len(text)
    while i < size:
        try:
            result += coder[text[i]]
        except:
            result += text[i]
        i += 1
    return result
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    return apply_coder(text,build_encoder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    for i in range(28):
        decoder = build_decoder(i)
        original_text = apply_coder(text,decoder)
        words = original_text.split(' ')
        count = 0
        for word in words:
            if(not is_word(wordlist,word)):
                break;
            else:
                count +=1
        if(count == len(words)):
            return i
   
#
# Problem 3: Multi-level encryption.
#
def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text: A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    if(type(shifts) is int):
        shift = [shifts]

    result = text;
    for item in shifts:
        item_type = type(item)
        if(item_type is tuple):
            start_pos = item[0]
            if(start_pos < 0):
                start_pos = 0
            result = result[0:item[0]] + apply_coder(result[item[0]:],build_encoder(item[1]))
        elif(item_type is int):
            result = apply_coder(text,build_encoder(shift))
        #maybe do list version too?
    return result

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """

    shifts = list(find_best_shifts_rec(wordlist,text,0))
    return shifts if shifts.count > 0 else None


def find_best_shifts_rec(wordlist, text, start):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text: scambled text to try to find the words for
    start: where to start looking at shifts
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    """
    if start > len(text)-1 :
        return []

    shifts = []

    for i in xrange(28):
        encoder = build_encoder(i)
        may_contains_plain_text = apply_coder(text,encoder)
        portion = may_contains_plain_text[start:]
        words = portion.split(' ')
        plain_text_recovered_len = 0
        count = 0
        for word in words:
            if(is_word(wordlist,word)):
               plain_text_recovered_len += len(word)+1
               count += 1
            else:
                break
        
        if(count > 0):
            shifts.append((start,i))
            shifts = itertools.chain(shifts,find_best_shifts_rec(wordlist,may_contains_plain_text,start+plain_text_recovered_len))
            #below works but less efficient 
            #shifts += find_best_shifts_rec(wordlist,may_contains_plain_text,start+plain_text_recovered_len)
            return shifts
    else:
        return []

    return shifts


def decrypt_fable():
     """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    ### TODO.


#cipher = apply_shift('This is a test.', 8)
#shift = find_best_shift(wordlist,cipher)
#print apply_coder(cipher,build_decoder(shift))

cipher = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
shifts = find_best_shifts(wordlist, cipher)
print apply_shifts(cipher,shifts)

    
#What is the moral of the story?
#
#
#
#
#

