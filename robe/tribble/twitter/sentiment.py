import random, re
import csv
import nltk
from tribble.models import Words_Global, Words_India

with open('wordlist.txt','r') as f:
    wordlist = f.read().split('\n')

all_words = nltk.FreqDist(w.lower() for w in wordlist)
random.shuffle(all_words)
word_features = all_words.keys()[:2000]

def makeDocument(tweets):
    documents = []
    for (words, sentiment) in tweets:
        words_filtered = [e.lower() for e in words.split(' ')]
        documents.append((words_filtered, sentiment))
    return documents 

def trainClassifier(train_set,test_set):
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    print 'Accuracy :', nltk.classify.accuracy(classifier, test_set)
    return classifier

def documentFeatures(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def splitHashTag(hashTag):
    sent = ''
    s = []
    for wordSequence in re.findall('(?:' + wordlist + ')+', hashTag):
        s += re.findall(wordlist, wordSequence) 
    sent = " ".join(s)
    return sent

def getSenti():
    wg = Words_Global.objects.all()
    wi = Words_India.objects.all()
    output = {'global':[],'india':[]}

    with open('input/mtest.csv','r') as f:
        rdr = csv.reader(f)
        i = 0
        tweets = []
        for row in rdr:
            if i>1:
                words = row[5]
                sentiment = row[0]
                tweets += [(words, sentiment)]
            i+=1

    with open('input/mtrain.csv','r') as f:
        rdr = csv.reader(f)
        i = 0
        test_tweets = []
        for row in rdr:
            if i>1:
                words = row[5]
                sentiment = row[0]
                test_tweets += [(words, sentiment)]
            i+=1
            
    documents = makeDocument(tweets)
    test_tweets = makeDocument(test_tweets)
    random.shuffle(documents)

    featuresets = [(documentFeatures(d), c)  for (d,c) in documents[:500]]
    train_set = featuresets
    test_set = [(documentFeatures(d), c)  for (d,c) in test_tweets[:200]]
    classifier = trainClassifier(train_set,test_set)

    k=0
    for trend in wg:
        string = ''
        if trend.word_name[0] =='#': 
            for letter in trend.word_name:
                if ord(letter) >= 65 and ord(letter) <= 90:
                    string += ' '+letter 
                else:
                    string += letter
            string = splitHashTag(string.lower())[1:]
        else:
            string = trend.word_name
        k+=1
        print string, ':',classifier.classify(documentFeatures(string))
        edit = Words_Global.objects.get(id=trend.id)
        edit.sentiment = classifier.classify(documentFeatures(string))
        edit.save()
        train_set += [(documentFeatures(string),classifier.classify(documentFeatures(string)))]

    wg.save()
