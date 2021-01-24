import random
from words_list import *

def complexCheck(word):
    if "!" in word:
        return False
    elif "@" in word:
        return False
    else:
        return True

def complicate_child(word):
    toChange = ["B","e","o","a","i"]
    changeTo = ["8","e","0","@","!"]
    Word = False
    for i in range(0,len(toChange)):
        if toChange[i] in word and Word==False:
            Word = word.replace(toChange[i],changeTo[i])
        else:
            Word = False
    return Word



def getWord(type,complicated=False):
    while complicated==False:
        num1 = random.randint(0, len(child_words[type]))
        word = child_words[type][num1]
        word = complicate_child(word)
        print(word)
        complicated=word
    return complicated.capitalize()


for i in range(0,100):
    noun = getWord(0)
    adj = getWord(1)
    printme = "Combo "+str(i)+".)  "+adj + " " + noun
    print(printme)
