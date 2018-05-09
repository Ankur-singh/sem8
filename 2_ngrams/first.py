from nltk.tokenize import word_tokenize
import csv

def vocab(text):
	tokens = word_tokenize(text)
	#print tokens
	vocab = list(set(tokens))
	#print vocab
	vocab.sort()
	return vocab	

def prob(a, b):
	global sample_text
	#print b+' '+a
	#print text.count(b+' '+a)
	#print text.count(b)
	p = sample_text.count(' '+b+' '+a+' ')/float(sample_text.count(' '+b+' '))
	return p

def n_gram(sample_text):
	matrix = []
	vocabulary = vocab(sample_text)
	print vocabulary
	matrix.append([' ']+vocabulary)
	for i in vocabulary:
		row = []
		if vocabulary.index(i) != 0:
			row.append(i)
		for j in vocabulary:
			row.append(prob(j,i))
		matrix.append(row)
	return matrix

def predict(a, matirx, vocabulary):	
	try:
		row = matrix[vocabulary.index(a)+1]
		del(row[0])
		max_index = row.index(max(row))
		return vocabulary[max_index]
	except:
		return 'word not in corpus .. SORRY!'

def write_to_csv(matrix):
	f = open('output.csv', 'w')
	with f:
		writer = csv.writer(f)
		#matrix
		writer.writerows(matrix)
	print 'completed'


sample_text = 'i had been expecting more of this movie than the less than thrilling twister . \
twister was good but had no real plot and no one to simpithize with . \
but twister had amazing effects and i was hoping so would volcano \
volcano starts with tommy lee jones at emo . \
he worrys about a small earthquake enough to leave his daughter at home with a baby sitter . \
there is one small quake then another quake . \
then a geologist points out to tommy that its takes a geologic event to heat millions of gallons of water in 12 hours .'

'''
a few hours later large amount of ash start to fall . \
then . . . . it \
starts . \
the volcanic eruption . . . .  \
i liked this movie . . . but \
it was not as great as i hoped . \
i was still good none the less . \
it had excellent special effects . \
the best view . . . the \
helecopters flying over the streets of volcanos . \
also . . . there were interesting side stories that made the plot more interesting . \
so . . . it was good ! ! '''

matrix = n_gram(sample_text)
write_to_csv(matrix)
vocabulary = vocab(sample_text)
while True:
	word = raw_input("enter a word, I'll predict the next ;)")
	if word == 'quit':
		break
	print predict(word, matrix, vocabulary)
	
