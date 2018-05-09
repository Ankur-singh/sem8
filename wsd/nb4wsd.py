from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from nltk.corpus import brown, semcor
import os
import nltk
import pickle

'''
def sentsWithWord(word):
	return [sents for sents in semcor.sents() if word in sents],sense

def old_wsd_features(sentence, index):
	featureset = {}

	for i in range(max(0, index-3), index):
		featureset['left-context(%s)' % sentence[i]] = True
	for i in range(index, max(index+3, len(sentence))):
		featureset['right-context(%s)' % sentence[i]] = True
	return featureset
'''

jar = './stanford-postagger/stanford-postagger.jar'
model = './stanford-postagger/models/english-bidirectional-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding= 'utf8')

def senseExtractor(word):
	files_2 = os.listdir('/home/ankur/nltk_data/corpora/semcor/brown2/tagfiles/')
	files_1 = os.listdir('/home/ankur/nltk_data/corpora/semcor/brown1/tagfiles/')
	files_v = os.listdir('/home/ankur/nltk_data/corpora/semcor/brownv/tagfiles/')
	folder = {'brown1':files_1, 'brown2':files_2, 'brownv':files_v}
	result = []
	for path,files in folder.items():
		for fil in files:
			sents = semcor.xml(path+'/tagfiles/'+fil).findall('context/p/s')
			for sent in sents:
				sentence = []
				sense = ''
				#senseID = ''
				for wordform in sent.getchildren():
					sentence.append(wordform.text)
					if wordform.text == word:
						sense = wordform.get('lemma')
						#senseID = wordform.get('lexsn')
				if word in sentence:
					result.append((sentence,sense)) #,senseID))

	return result

def wsd_features(sentence, word):
	index = sentence.index(word)
	taggedSent = tagSent(sentence)
	featureset = {}

	featureset['word'] = word
	for i in range(max(0, index-3), index):
		featureset['left-context(%s)' % taggedSent[i][0]] = True
		featureset['%s' % taggedSent[i][0]] = taggedSent[i][1]
	for i in range(index, min(index+3, len(taggedSent))):
		featureset['right-context(%s)' % taggedSent[i][0]] = True
		featureset['%s' % taggedSent[i][0]] = taggedSent[i][1]
	return featureset

def tagSent(sentence):
	return pos_tagger.tag(sentence)

def printList(l):
	for t in l:
		print t

words = ['cut']#,'feet', 'passed']

sents=[]
featureset = []
for word in words:
	sents = senseExtractor(word)
	featureset += [(wsd_features(sent, word),sense) for sent,sense in sents]

a = len(featureset)
print a

trainningSet = featureset[:int(a*0.8)]
testingSet = featureset[int(a*0.8):]

classifier = nltk.NaiveBayesClassifier.train(trainningSet)
print(nltk.classify.accuracy(classifier, testingSet))

'''
f = open('nb_all.pickel','wb')
pickle.dump(classifier,f)
f.close()

f = open('nb_many.pickel','rb')
classifier = pickle.load(f)
f.close()
'''

print classifier.classify(wsd_features(['cut','his','feet','short','.'],'cut'))
#print wsd_features(['I','went','to','the', 'bank'], 'bank')
#print tagWord(['bank',])
#printList(featureset) 
