from nltk.tokenize import word_tokenize

def vocab(text):
	global tokens
	#print tokens
	vocab = list(set(tokens))
	#print vocab
	vocab.sort()
	return vocab

def prob(a, b):
	global tokens
	p = my_count(a, b)/float(tokens.count(a))	
	return p

def my_count(a, b):
	global tokens
	count = 0
	for i in xrange(len(tokens)-1):
		if tokens[i] == a and tokens[i+1] == b:
			count += 1
	return count

def predict(a):
	d = {}
	for i in vocabulary:
		d[i] = prob(a,i)
	d = sorted(d.iteritems(), key=lambda (k,v): (v,k))
	#print d
	for i in xrange(len(d)):
		if d[-1*i][1] > 0:
			print d[-1*i][0]+'('+str(d[-1*i][1])+')',
	print ''

def prob_sentence(a):
	l = a.split(' ')
	prob3 = 1
	for i in xrange(len(l)-1):
		#print prob(l[i], l[i+1])
		prob3 = prob3*prob(l[i], l[i+1])
	#print 'final '+str(prob3)
	return prob3, l[-1]		
	
def n_gram(a):
	global sample_text, vocabulary
	d = {}
	prob2, last_word = prob_sentence(a)
	try:
		for i in vocabulary:
			d[i] = prob2*prob(last_word, i)
		d = sorted(d.iteritems(), key=lambda (k,v): (v,k))
		#print d
		for i in xrange(len(d)):
			if d[-1*i][1] > 0:
				print d[-1*i][0]+'('+str(d[-1*i][1])+')',
		print ''
	except:
		print 'word not found in corpus OR mispelled'


sample_text = 'i had been expecting more of this movie than the less than thrilling twister . \
twister was good but had no real plot and no one to simpithize with . \
but twister had amazing effects and i was hoping so would volcano \
volcano starts with tommy lee jones at emo . \
he worrys about a small earthquake enough to leave his daughter at home with a baby sitter . \
there is one small quake then another quake . \
then a geologist points out to tommy that its takes a geologic event to heat millions of gallons of water in 12 hours . \
a few hours later large amount of ash start to fall . \
then . . . . it \
starts . \
the volcanic eruption . . . .  \
i liked this movie . . . but \
it was not as great as i hoped . \
i was still good none the less . \
i was still good none the less . \
i was still good none the less . \
it had excellent special effects . \
the best view . . . the \
helecopters flying over the streets of volcanos . \
also . . . there were interesting side stories that made the plot more interesting . \
so . . . it was good ! ! '

tokens = word_tokenize(sample_text)
vocabulary = vocab(sample_text)

while True:
	word = raw_input("enter a word, I'll predict the next ;) ")
	if word == 'quit':
		break	
	#predict(word)
	n_gram(word)
