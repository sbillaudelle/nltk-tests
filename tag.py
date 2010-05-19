import cPickle as pickle

import nltk
import nltk.tag
import nltk.data
import nltk.tokenize
import nltk.corpus

tagger = nltk.data.load('file:tagger.pickle')

print tagger.tag(["add", "meeting", "at", "20:00"])
print tagger.tag(["do", "meeting"])
print tagger.tag(['The', 'dog', 'is', 'yellow'])
