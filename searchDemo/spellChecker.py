from nltk.corpus import brown
from minDistance import *
import pickle


f = open('brown_dict.pickle', 'rb')
words = pickle.load(f)
f.close()

sample = raw_input("enter a word !")
possible_words = mindistance(sample, words)
print possible_words