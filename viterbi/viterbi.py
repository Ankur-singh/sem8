from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from collections import Counter
import pickle

'''
def pl(b,a):
	global lexical
	return lexical[a][b]


def pb(b,a):
	global bigram
	return bigram[a][b]
'''

def print_matrix(mat):
	for i in mat:
		print i
	print ''


def print_dic(dic):
	for i in dic.keys():
		print "{} : {}".format(i, dic[i])
	print ''


def back_track(i,t, backPointer):
	global tagset
	ptags = []
	ptags.append(tagset[i])
	for j in range(t-1,0,-1):
		i = backPointer[i][j]
		ptags.append(tagset[i]) 

	ptags.reverse()
	return ptags


def create_bigram():
	tagged_sents = brown.tagged_sents(tagset='universal')
	tags = [tag for sents in tagged_sents for word, tag in sents]
	
	#tags = ['noun', 'verb', 'part', 'verb', "noun"]
	tag_set = Counter(tags)
	print tag_set

	bigram = {}
	for b in tag_set.keys(): 
		bigram[b] = {}
		for a in tag_set.keys():
			count = 0
			
			for k in xrange(len(tags)-1):
				if tags[k] == a and tags[k+1] == b:
					count += 1
			bigram[b][a] = float(count)/tag_set[a]

	f = open('bigram_matrix.pickle', 'wb')
	pickle.dump(bigram, f)
	f.close()

	print "done"
	print_dic(bigram)


def load_bigram():
	f = open('bigram_matrix.pickle', 'rb')
	bigram = pickle.load(f)
	f.close()
	return bigram	


def create_lexical(words):
	tagged_sents = brown.tagged_sents(tagset='universal')
	tags = [tag for sents in tagged_sents for word, tag in sents]
	tuples = [(word.lower(), tag) for sents in tagged_sents for word, tag in sents]

	word_set = list(set(words))
	tag_set = Counter(tags)

	lexical = {}
	for word in word_set:
		lexical[word] = {}
		for tag in tag_set:
			count = 0
			for tup in tuples:
				if tup[0] == word and tup[1] == tag:
					count += 1
			lexical[word][tag] = float(count)/tag_set[tag]

	return lexical


def viterbi(words, tag_set):
	global bigram, lexical
	
	t = len(words)
	n = len(tag_set)
	
	vit_matrix = []
	backPointer = []
	
	for i in xrange(n):
		vit_matrix.append([None for i in range(t)])
		backPointer.append([None for i in range(t)])

	for i in xrange(0,n):
		vit_matrix[i][0] = float(bigram[str(tag_set[i])][str(tag_set[0])]*lexical[str(words[0])][str(tag_set[i])])
		backPointer[i][0] = -1
	
	for i in xrange(1,t):
		for j in xrange(0,n):
			#print [(vit_matrix[s][i-1], bigram(s+1,j)) for s in xrange(0,n)]
			v = [(vit_matrix[s][i-1]*bigram[str(tag_set[j])][str(tag_set[s])]) for s in xrange(0,n)]
			#print "({},{}) ".format(i,j)+str(max(v))
			vit_matrix[j][i] = max(v)*lexical[str(words[i])][str(tag_set[j])]
			#print v
			#print max(v) ,v.index(max(v))
			backPointer[j][i] = v.index(max(v))

	

	v = [vit_matrix[s][t-1] for s in xrange(0,t)]
	#vit_matrix[j][i] = max(v)*pb(tokens[t],tags[j])
	#backPointer[j][i] = v.index(max(v))
	print "\nBack Pointer"
	#print_matrix(vit_matrix)

	print_matrix(backPointer)
	print v.index(max(v))  
	print back_track(v.index(max(v)), t,backPointer)

'''
bigram = [[0.29,0.71,0.0001,0.0001],
		  [0.13,0.0001,0.43,0.44],
		  [1,0.0001,0.0001,0.0001],
		  [0.35,0.65,0.0001,0.0001],
		  [0.26,0.74,0.0001,0.0001]]

lexical = [[0.063,0.076,0.01, 0.076],
			[0.0001,0.0001,0.0001,0.0001],
			[0.05,0.05,0.1,0.05],
			[0.0001,0.0001,0.068,0.0001]]
'''
text = raw_input('enter the text to be tagged !')
words = word_tokenize(text)
words = [word.lower() for word in words]

tagged_sents = brown.tagged_sents(tagset='universal')
tags = [tag for sents in tagged_sents for word, tag in sents]
	
#tags = ['noun', 'verb', 'part', 'verb', "noun"]
tag_count = Counter(tags)
tagset = [x for x in tag_count.keys()]
print tagset

bigram = load_bigram()
#print_dic(bigram)

lexical = create_lexical(words)
#print_dic(lexical)

viterbi(words, tagset)
print words
