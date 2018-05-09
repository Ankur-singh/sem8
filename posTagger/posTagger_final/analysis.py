# analysis file
import nltk
from nltk.corpus import brown
import pickle
from tag_utils import *

tagged_sents = brown.tagged_sents(tagset='universal')
tagged_sents = tagged_sents[50000:]
gold = [tag for sent in tagged_sents for (word, tag) in sent]

############## CRF #################
'''
f = open('crf/crf_mapped.pickle', 'rb')
crf = pickle.load(f)
crf = tag_list(crf)

print "crf V/S brown_gold_tag"

cm = nltk.ConfusionMatrix(gold, crf)
print cm
'''

################# Brills ############3333333

f = open('brills/brill_mapped.pickle', 'rb')
brill = pickle.load(f)
brill = tag_list(brill)

print "Brills V/S brown_gold_tag"

cm = nltk.ConfusionMatrix(gold, brill)
print cm
