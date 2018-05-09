from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from nltk.corpus import brown

jar = './stanford-postagger/stanford-postagger.jar'
model = './stanford-postagger/models/english-bidirectional-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding= 'utf8')
text = brown.words(categories='humor')

print len(text)
tagged_text = pos_tagger.tag(text[:int(len(text)*0.5)])
tagged_text += pos_tagger.tag(text[int(len(text)*0.5):])
print tagged_text
