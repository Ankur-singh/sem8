'''
import nltk
from nltk.corpus import brown

tagged_brown = nltk.pos_tag(brown.words(categories='humor'), tagset='universal')
#fd = nltk.FreqDist(tag for (word, tag) in tagged_brown)

#print fd.most_common()

gold_tags = [tag for (word, tag) in brown.tagged_words(categories='humor', tagset='universal')]
#print gold_tags
print nltk.ConfusionMatrix(gold_tags, tagged_brown)
'''
from nltk.corpus import brown
from nltk.tag import StanfordPOSTagger #from nltk.tag.corenlp.CoreNLPPOSTagger import StanfordPOSTagger
import nltk

stan_tagger = StanfordPOSTagger('stanford-postagger-2017-06-09/models/english-bidirectional-distsim.tagger','stanford-postagger-2017-06-09/stanford-postagger.jar')
words = brown.words(categories='humor')
test_tag = stan_tagger.tag(words)
gold_tag = [tag for (word, tag) in words]

print test_tag.evaluate(gold_tag)

