from nltk.tag import brill, brill_trainer, DefaultTagger, UnigramTagger, BigramTagger, TrigramTagger
from nltk.corpus import brown
import pickle

def backoff_tagger(train_sents, tagger_classes, backoff=None):
	for cls in tagger_classes:
		backoff = cls(train_sents, backoff=backoff)
	return backoff

def train_brill_tagger(initial_tagger, train_sents, **kwargs):
	templates = [
		brill.Template(brill.Pos([-1])),
		brill.Template(brill.Pos([1])),
		brill.Template(brill.Pos([-2])),
		brill.Template(brill.Pos([2])),
		brill.Template(brill.Pos([-2, -1])),
		brill.Template(brill.Pos([1, 2])),
		brill.Template(brill.Pos([-3, -2, -1])),
		brill.Template(brill.Pos([1, 2, 3])),
		brill.Template(brill.Pos([-1]), brill.Pos([1])),
		brill.Template(brill.Word([-1])),
		brill.Template(brill.Word([1])),
		brill.Template(brill.Word([-2])),
		brill.Template(brill.Word([2])),
		brill.Template(brill.Word([-2, -1])),
		brill.Template(brill.Word([1, 2])),
		brill.Template(brill.Word([-3, -2, -1])),
		brill.Template(brill.Word([1, 2, 3])),
		brill.Template(brill.Word([-1]), brill.Word([1])),
	]

	#templates = nltkdemo18() # nltkdemo18plus() # fntbl37() # brill24()

	trainer = brill_trainer.BrillTaggerTrainer(initial_tagger, templates, deterministic=True, trace=True)

	return trainer.train(train_sents, **kwargs)

tagged_sents = brown.tagged_sents() # len(humor) = 1053, len(ALL) = 57340
train = tagged_sents[:50000]
test = tagged_sents[50000:]

"""
################ TRAIN ######################
default_tagger = DefaultTagger('NN')
initial_tagger = backoff_tagger(train, [UnigramTagger, BigramTagger, TrigramTagger], backoff=default_tagger)
print initial_tagger.evaluate(test) # 0.912180882644

brill_tagger = train_brill_tagger(initial_tagger, train)
print brill_tagger.evaluate(test) # 0.924566264265
 
'''
TBL train (fast) (seqs: 50000; tokens: 1039920; tpls: 18; min score: 2; min acc: None)
Finding initial useful rules...
    Found 254653 useful rules.
Selecting rules...
0.924566264265
'''

f = open('brill_brown_tagger.pickle', 'wb')
pickle.dump(brill_tagger, f)
f.close()
"""

############### TEST #####################
f = open('brill_brown_tagger.pickle', 'rb') 
brill_tagger = pickle.load(f)
tokens = []
for i in test:
	for j in i:
		tokens.append(j[0])

test_tagged = brill_tagger.tag(tokens)

#### save list object to file #####
f = open("test_tagged_obj.pickle", 'w')
pickle.dump(test_tagged, f)
f.close()

'''
temp = ""
for i in test_tagged:
	temp += str(i[0])+'\t\t'+str(i[1])+'\n'

f = open('brills_brown_tagged.txt', 'w')
f.write(temp)
f.close()

'''
