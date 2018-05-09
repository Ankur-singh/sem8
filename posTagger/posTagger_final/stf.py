from nltk.tag import StanfordPOSTagger
from nltk import word_tokenize
from nltk.corpus import brown

jar = './stanford-postagger-2017-06-09/stanford-postagger.jar'
model = './stanford-postagger-2017-06-09/models/english-bidirectional-distsim.tagger'

pos_tagger = StanfordPOSTagger(model, jar, encoding='utf8')
#text = word_tokenize("what's the airspeed of and unladen swallon?")
text = brown.words(categories='humor')
print len(text)
tagged_text = pos_tagger.tag(text[:int(len(text)*0.7)])
tagged_text += pos_tagger.tag(text[int(len(text)*0.7):])
print tagged_text
