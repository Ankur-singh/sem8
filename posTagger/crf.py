from nltk.tag import CRFTagger
from nltk.corpus import brown

tagged_sents = brown.tagged_sents()
train = tagged_sents[:50000]
test = tagged_sents[50000:]

crf = CRFTagger()
crf.train(train, 'crf_tagger.model')
a = crf.evaluate(test)
print a
