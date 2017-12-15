import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier
from nltk import classify

import csv
import re

nltk.data.path = ['Data/nltk_data']
sw = stopwords.words('english')
sw.extend(['ll', 've'])

def get_words_from_msg(message, stopwords=sw):
    
    msg_words = set(wordpunct_tokenize(message.lower()))
    msg_words = msg_words.difference(stopwords)
    msg_words = [w for w in msg_words 
            if re.search('[a-zA-Z]', w) and len(w) > 1]
    
    return msg_words

def feature_extractor(message):
    
    msg_words = get_words_from_msg(message)
    features = dict.fromkeys(msg_words, True)

    return features

def get_train_sets(raw_data_path):

    features_labes = []
    with open(raw_data_path, 'r') as f:
        csvf = csv.reader(f, delimiter=',')
        next(csvf)
        for msg, label in csvf:
            features = feature_extractor(msg)
            features_labes.append((features, label))

    return features_labes

def get_naive_bayes_classifier(train_file='Data/assignment1_data.csv'):
    
    train_set = get_train_sets('Data/assignment1_data.csv')
    classifier = NaiveBayesClassifier.train(train_set)


if __name__ == '__main__':
    train_set = get_train_sets('Data/assignment1_data.csv')
    classifier = NaiveBayesClassifier.train(train_set)