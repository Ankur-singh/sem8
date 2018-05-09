import sys
from nltk.corpus import wordnet 
from nltk.tokenize import word_tokenize

wordsNotRequired = ['about', 'across', 'against', 'along', 'around', 'at', 'is', 'behind', 'beside', 'besides', 'by', 'despite', 'down', 'during', 'for', 'from', 'in', 'inside', 'into', 'near', 'of', 'off', 'on', 'onto', 'over', 'through', 'to', 'toward', 'with', 'within', 'without', 'anything', 'everything', 'anyone', 'everyone', 'ones', 'such', 'it', 'itself', 'something', 'nothing', 'someone', 'the', 'some', 'this', 'that', 'every', 'all', 'both', 'one', 'first', 'other', 'next', 'many', 'much', 'more', 'most', 'several', 'no', 'a', 'an', 'any', 'each', 'no', 'half', 'twice', 'two', 'second', 'another', 'last', 'few', 'little', 'less', 'least', 'own', 'and', 'but', 'after', 'when', 'as', 'because', 'if', 'what', 'where', 'which', 'how', 'than', 'or', 'so', 'before', 'since', 'while', 'although', 'though', 'who', 'whose', 'can', 'may', 'will', 'shall', 'could', 'be', 'do', 'have', 'might', 'would', 'should', 'must', 'here', 'there', 'now', 'then', 'always', 'never', 'sometimes', 'usually', 'often', 'therefore', 'however', 'besides', 'moreover', 'though', 'otherwise', 'else', 'instead', 'anyway', 'incidentally', 'meanwhile']

def calculateOverlap(synset, sentence):
    gloss = set(word_tokenize(synset.definition()))
    for i in synset.examples():
         gloss.union(i)
    gloss = gloss.difference(wordsNotRequired)
    
    sentence = set(sentence.split(" "))
    sentence = sentence.difference(wordsNotRequired)
    
    return len(gloss.intersection(sentence))

def lesk(word1, sentence):
    bestsense = None
    maxoverlap = 0
    word=wordnet.morphy(word1)
  
    for sense in wordnet.synsets(word):
        overlap = calculateOverlap(sense,sentence)
        if overlap > maxoverlap:
                maxoverlap = overlap
                bestsense = sense
    return bestsense

sentence = raw_input("Enter the Sentence:")
word = raw_input("Enter the word to disambiguate:")

if word in sentence:
    synset = lesk(word,sentence)
    print '\n'
    print synset
    
    if synset is not None:
        print synset.definition()
else:
    print "word not in sentence."
