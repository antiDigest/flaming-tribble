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

taggedtext = getTaggedWords()
word_features = getWords(taggedtext)

def makeDocument(tweets): # seems correct
    documents = []
    for (words, sentiment) in tweets:
        words_filtered = [e.lower() for e in words]
        documents.append((words_filtered, sentiment))
    return documents 

def documentFeatures(document): # seems correct
    document_words = set(document)
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

def getSenti(stmt):
    # print stopwords.words('english'
    # test_tweets = makeDocumenst(test_tweets)
    random.shuffle(taggedtext)

    featureset = nltk.classify.apply_features(documentFeatures, taggedtext)
    training_set = featureset[300:]
    test_set = featureset[:300]
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    print 'Accuracy :', nltk.classify.accuracy(classifier, test_set)

    count_neg =0
    count_pos =0
    count_neutral = 0
    for s in stmt:
        s = s.lower()
        s = s.split()
        out = classifier.classify(documentFeatures(s))
        if out < -0.4:
            count_neg += 1
        elif out > 0.4:
            count_pos += 1
        else:
            count_neutral += 1
        # print out

    return getMax(count_neutral, count_neg, count_pos)