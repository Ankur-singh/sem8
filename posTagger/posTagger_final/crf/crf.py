from nltk.tag import CRFTagger
from nltk.corpus import brown
import pickle
#from tag_utils import *

tagged_sents = brown.tagged_sents()
train = tagged_sents[:50000]
test = tagged_sents[50000:]
crf = CRFTagger()

'''
############# Train #############
crf.train(train, 'crf_brown.tagger')
print crf.evaluate(test) # 0.954383534534
'''

############# Test #############
crf.set_model_file('crf_brown.tagger')
tokens = []
for i in test:
	for j in i:
		tokens.append(j[0])
 
test_tagged = crf.tag(tokens)

'''
f = open("test_tagged_obj.pickle", 'w')
pickle.dump(test_tagged, f)
f.close()
'''

#print test_tagged
temp = ""
for i in test_tagged:
	temp += str(i[0])+'\t\t'+str(i[1])+'\n'

f = open('crf_brown_tagged.txt', 'w')
f.write(temp)
f.close()

