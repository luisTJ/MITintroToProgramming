# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
import urllib
import json
from bs4 import BeautifulSoup

WORDLIST_FILENAME = "words.txt"
API_KEY_FILENAME = "key.json"

key = None

def load_keys():

    global key
    with open('key.json') as key_file:    
        key  = json.load(key_file)


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
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

def takeInput(available):

    while(True):
        user_input = raw_input("Please guess a letter: ")[0].lower()
        if(user_input in available):
            return user_input
        else:
            print user_input + " is already used"
            tmp = list(available)
            tmp.sort()
            print "Available letters: "+ "".join(tmp)

def printline(num = 10):
    try:
        num = int(num)
    except:
        num = 10
    print "-"*num

def printDefinition(word):
    try:
        success = queryAonaware(word)
        if(not success):
            queryMariamWebSter(word)
    except Exception as e:
        pass

def queryAonaware(word):
    try:
        query = urllib.urlencode({'query':word})
        url = 'http://services.aonaware.com/DictService/Default.aspx?action=define&dict=wn&%s' % query
        search_response = urllib.urlopen(url)
        html = search_response.read()
        definition = parseHtml(html)
        printline()
        soup = BeautifulSoup(html,"html.parser")
        header = soup.span.text
        meaning = soup.pre.get_text()
        text = header+"\r\n\r\n"+meaning
        print definition
        return True
    except Exception:
        return False

def queryMariamWebSter(word):
    try:
        with open('key.json') as key_file:    
            key  = json.load(key_file)
            url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{0}?key={1}".format(word, key["dict_key"])
            search_response = urllib.urlopen(url)
            html = search_response.read()
            soup = BeautifulSoup(html,"xml.parser")
            #header = word + soup.
            return True
    except Exception:
        return False

def getHtml(word):

    global key
    url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{0}?key={1}".format(word, key["dict_key"])
    #url = 'http://services.aonaware.com/DictService/Default.aspx?action=define&dict=wn&%s' % query
    search_response = urllib.urlopen(url)
    html = search_response.read()
    return html

def parseHtml(html):
    soup = BeautifulSoup(html,"html.parser")
    #header = soup.span.text
    #meaning = soup.pre.get_text()
    #text = header+"\r\n\r\n"+meaning

    return text


def hangman(tries = 6):
    
    try:
        tries = int(tries)
    except:
        tries = 6

    print "Welcome to the game, Hangman!"
    answer = choose_word(wordlist)
    available = set('abcdefghijklmnopqrstuvwxyz')
    game = []
    for i in range(len(answer)):
        game.append('_')

    print "I am thinking of a word that is "+ str(len(answer))+" letters long."
    printline()

    while(tries > 0):
        print "You have "+ str(tries) +" guess"+ ("es" if tries > 1 else "") + " left"
        tmp = list(available)
        tmp.sort()
        print "Available letters: "+ "".join(tmp)
        input = takeInput(available)
        available.remove(input)
        matched = False
        for i in range(len(answer)):
            if(input == answer[i]):
                game[i] = input
                matched = True

        if(matched):
            print "%-45s%-20s" % ("Good Guess: ", " ".join(game))
        else:
            print "%-45s%-20s" % ("Oops! That letter is not in my word: ", " ".join(game))
            tries -= 1

        printline()
        if(''.join(game) == answer):
            break;
        

    if(tries <= 0):
        print "You're dead"
        print "The answer is "+ answer
    else:
        print "Congratulations, you won!"
    
    printDefinition(answer)

load_keys();
printDefinition("renitent")
#hangman(8)

#http://www.merriam-webster.com/dictionary/renitent