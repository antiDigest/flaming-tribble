import random, re
import string
import csv
import nltk
from nltk.corpus import stopwords
from stemming.porter2 import stem
import math
import sys
import os
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

punct = string.punctuation
parenthesis = [')','(', ']','[','{','}','*','&','\\','!','$','^',';','<','>','?','_','=','+','RT']

def getTaggedWords():
    #Load positive tweets into a list
    p = open('positive.txt', 'r')
    postxt = p.read().split('\n')

    #Load negative tweets into a list
    n = open('negative.txt', 'r')
    negtxt = n.read().split('\n')

    neglist = []
    poslist = []

    #Create a list of 'negatives' with the exact length of our negative tweet list.
    for i in range(0,len(negtxt)):
        neglist.append(-1)

    #Likewise for positive.
    for i in range(0,len(postxt)):
        poslist.append(1)

    #Creates a list of tuples, with sentiment tagged.
    postagged = zip(postxt, poslist)
    negtagged = zip(negtxt, neglist)

    # print postagged
    #Combines all of the tagged tweets to one large list.
    taggedtext = postagged + negtagged

    # print len(taggedtext)
    return taggedtext

def getAllWords(tweets):
    allwords = []
    for (words, sentiment) in tweets:
        allwords.extend(words)
    return allwords

#Order a list of tweets by their frequency.
def getWordFeatures(listoftweets):
    #Print out wordfreq if you want to have a look at the individual counts of words.
    wordfreq = nltk.FreqDist(listoftweets)
    words = wordfreq.keys()
    return words


def getWords(taggedtext): # seems correct
    # print wordlist

    tweets = []
    customstopwords = ['band', 'they', 'them']

    for (word, sentiment) in taggedtext:
        word_filter = [i.lower() for i in word.split()]
        tweets.append((word_filter, sentiment))

    wordlist = getWordFeatures(getAllWords(tweets))
    wordlist = [i for i in wordlist if not i in stopwords.words('english')]
    wordlist = [i for i in wordlist if not i in customstopwords]

    return wordlist

def textCleaner(value):
    # print value
    
    for i in parenthesis:
        value = value.replace(i, '')
    # print value
    for word in value.split(' '):
        if '#' in word:
            if word[0] == '#':
                value = re.sub(word,"",value)
        if '@' in word:
            value = re.sub(word,"",value)
            # print word
        if 'http://' in word or 'http' in word or '.com' in word:
            value = re.sub(word,"",value)
            # print word
    for i in string.punctuation:
        value = value.replace(i, '')
    return value

def textClean(s):
    remove = ['\t','\n','  ']
    # s = s.replace(i, Noneunct)
    for i in remove:
        s = re.sub(i,'',s)
    s = s.lower()
    s = s.split()
    return s

def makeDocument(tweets): # seems correct
    documents = []
    for (words, sentiment) in tweets:
        words_filtered = [e.lower() for e in words]
        documents.append((words_filtered, sentiment))
    return documents 

def documentFeatures(taggedtext): # seems correct
    # print taggedtext
    document_words = set(taggedtext)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def getMax(a,b,c):
    if a>b:
        if a>c:
            return a, 0
        else:
            return c, 1
    else:
        if b>c:
            return b, -1
        else:
            return c, 1

taggedtext = getTaggedWords()
word_features = getWords(taggedtext)

def trainClassifier():
    
    random.shuffle(taggedtext)

    # print taggedtext
    featureset = nltk.classify.apply_features(documentFeatures, taggedtext)
    # print len(featureset)
    training_set = featureset[100:]
    test_set = featureset[:100]
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print 'Accuracy :', nltk.classify.accuracy(classifier, test_set)
    classifier.show_most_informative_features(30)
    return classifier

def getSenti(stmt, classifier):
    print 'Getting Sentiment ... '
    # print stmt
    count_neg =0
    count_pos =0
    count_neutral = 0
    for s in stmt:
        # print s
        s = textClean(s)
        if s!=' ':
            out = classifier.classify(documentFeatures(s))
            if out < -0.4:
                count_neg += 1
            elif out > 0.4:
                count_pos += 1
            else:
                count_neutral += 1
            # print s, out

    return count_neutral, count_neg, count_pos, len(stmt)

# word disambigustiojn