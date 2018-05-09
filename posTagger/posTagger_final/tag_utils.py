import nltk
import pickle
from nltk.tag import mapping

def list_to_file_readable(l, outputfile):
	temp = ""
	for i in l:
		temp += str(i[0])+'\t\t'+str(i[1])+'\n'

	f = open(outputfile, 'w')
	f.write(temp)
	f.close()

def list_to_file_object(l, outputfile):
	f = open(outputfile, 'w')
	pickle.dump(l, f)
	f.close()
	

def tag_freq(l, outputfile):
	tag_fd = nltk.FreqDist(tag for (word,tag) in l)
	l1 = tag_fd.most_common()
	list_to_file_readable(l1, outputfile)

def tag_list(tokens):
	l = [tag for (word,tag) in tokens]
	return l

def mapped_tag(tokens):  # [(word, tag), (word, tag)....]
	return [(i[0], mapping('brown', 'universal', i[1])) for i in tokens]
	

		