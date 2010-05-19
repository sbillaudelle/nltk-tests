import cPickle as pickle

import nltk
import nltk.tag
import nltk.tokenize
import nltk.corpus

TRAIN_DATA = [
    [('do', 'ACTION_DO'), ('meeting', 'FOO')],
    [('add', 'ACTION_ADD'), ('meeting', 'DATE_TYPE')],
    ]

brown_train = nltk.corpus.brown.tagged_sents()

re_patterns = [('..:..', 'TIME')]
re_tagger = nltk.tag.RegexpTagger(re_patterns)

brown_tagger = nltk.tag.TrigramTagger(train=brown_train, backoff=re_tagger)

tagger = nltk.tag.TrigramTagger(train=TRAIN_DATA, backoff=brown_tagger)

pickle.dump(tagger, open('tagger.pickle', 'w'))
