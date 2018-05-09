from minDistance import *
import subprocess


def grep(a):
	try:
		path = 'papers'  #change papers to whatevere path you want!
		output = subprocess.check_output('find {} -name \*.pdf | grep -i -E "{}"'.format(path,a), shell=True)
		output = output.split('\n')
		for i in output:	
			print i
	except:
		print 'keyword not found!!....trying spell correction'
		output = subprocess.check_output('find papers -name \*.pdf', shell = True)
		output = output.split('\n')
		vocab = []		
		for i in output:
			j = i.split('/')
			for k in j:
				vocab.append(k)
		extras = ['nawp','ass']  #possible keyword that can be spelled incorrect and can give output for grep command.
		vocab = vocab+extras
		vocab = list(set(vocab))
		vocab.remove('papers')
		vocab.remove('')
		print vocab
		print a
		new_word = mindistance(a, vocab)
		print 'new word: '+new_word
		grep(new_word)		

key = raw_input('enter word to search: ')
grep(key)
